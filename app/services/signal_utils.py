"""Utilidades de procesamiento de senales.

Milestone 2: Procesamiento de la respuesta al impulso.
"""

import os
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal as sps

from app.services.filter import filter_single_band


def load_audio(path: str | Path) -> tuple[np.ndarray, int]:
    """Carga un archivo de audio (al menos WAV y FLAC) y retorna señal y fs.

    La señal se devuelve en mono: si el archivo es estéreo (o multicanal),
    se promedian los canales. Se convierte a float64 utilizando la escala
    de amplitud proporcionada por soundfile, sin normalización adicional.

    Parameters
    ----------
    path : str | Path
        Ruta al archivo de audio a cargar.

    Returns
    -------
    signal : np.ndarray
        Señal de audio mono como array 1D float64.
    fs : int
        Frecuencia de muestreo del archivo en Hz.

    Raises
    ------
    FileNotFoundError
        Si el archivo especificado no existe.
    ValueError
        Si el archivo no es un audio válido o el formato no es soportado
        (con un mensaje claro que indique el archivo y el motivo).
    """

    path = Path(path)

    if os.path.splitext(path)[1].lower() not in (".wav", ".flac"):
        raise ValueError("Formato no soportado. Sólo se aceptan archivos de audio WAV o FLAC.")

    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo no se encuentra en {path}.")

    try:
        signal, fs = sf.read(path, dtype="float64")

    except Exception as e:
        raise ValueError(f"El archivo no es un audio valido: {path}. Motivo: {e}") from e

    signal = np.asarray(signal, dtype=np.float64)

    if signal.ndim not in (1, 2):
        raise ValueError("Numero de canales invalido.")

    if signal.ndim == 2:  # por si el array es estereo
        signal = signal.mean(axis=1)  # si es estéreo, promedia ambos canales para obtener mono

    if signal.size == 0:
        raise ValueError("El archivo de audio está vacío.")

    return signal, int(fs)


def generate_synthetic_ir(duration: float, t60_values: dict[float, float], fs: int) -> np.ndarray:
    """Sintetiza una respuesta al impulso con valores de T60 conocidos por banda.

    Modelo: ``h(t) = n(t) * exp(-alpha * t)`` con ``alpha = 3 * ln(10) / T60``,
    donde ``n(t)`` es ruido blanco filtrado en la banda de octava. Se suman las
    componentes de todas las bandas y se normaliza.

    Parameters
    ----------
    duration : float
        Duracion de la respuesta al impulso en segundos.
    t60_values : dict[float, float]
        Diccionario ``{frecuencia_central_Hz: T60_segundos}``.
        Ejemplo: ``{125: 2.0, 250: 1.8, 500: 1.5, 1000: 1.2, 2000: 1.0, 4000: 0.8}``.
    fs : int
        Frecuencia de muestreo en Hz.

    Returns
    -------
    np.ndarray
        Respuesta al impulso sintetizada (array 1D de ``int(duration * fs)`` muestras).
    """

    if len(t60_values) == 0:
        raise ValueError("El T60 por banda no puede estar vacío.")

    if fs <= 0:
        raise ValueError("La frecuencia debe ser positiva.")

    n_samples = int(np.ceil(duration * fs))
    t = np.arange(n_samples, dtype=np.float64) / fs
    ri_sintetizada = np.zeros(n_samples, dtype=np.float64)

    for fc, t60 in t60_values.items():
        fc = float(fc)
        t60 = float(t60)

        if fc <= 0:
            raise ValueError(f"Frecuencia inválida: {fc}")

        if t60 <= 0:
            raise ValueError(f"T60 inválido: {t60}")

        noise = np.random.normal(loc=0.0, scale=1.0, size=n_samples)

        filtrado = filter_single_band(noise, fs, fc)

        rms = np.sqrt(np.mean(filtrado**2))
        if rms > 0:
            filtrado /= rms

        alfa = np.log(1000.0) / t60
        envolv = np.exp(-alfa * t)
        banda = filtrado * envolv

        ri_sintetizada += banda

    max_abs = np.max(np.abs(ri_sintetizada))
    if max_abs > 0:
        ri_sintetizada /= max_abs

    return ri_sintetizada


# Margen antes del pico: unas 256 muestras (~5 ms a 48 kHz). Evita que el filtrado
# por bandas de M3 deforme el comienzo de la respuesta al impulso.
PRE_PICO_MUESTRAS = 256


def get_impulse_response(recording: np.ndarray, inverse_filter: np.ndarray) -> np.ndarray:
    """Obtiene la respuesta al impulso mediante deconvolucion de un sine sweep.

    ``h(t) = y(t) * x_inv(t)``, con ``y = recording`` y ``x_inv = inverse_filter``;
    usar ``scipy.signal.fftconvolve`` (``mode='full'``), recortar para que la RI
    comience en el pico (o ligeramente antes) y normalizar respecto del pico.

    Parameters
    ----------
    recording : np.ndarray
        Senal grabada que contiene la respuesta de la sala al sweep.
    inverse_filter : np.ndarray
        Filtro inverso del sweep utilizado.

    Returns
    -------
    np.ndarray
        Respuesta al impulso estimada, normalizada.
     Raises
    ------
    ValueError
        Si las entradas no son arrays 1D no vacios o la grabacion no tiene senal.
    """
    y = np.asarray(recording, dtype=np.float64)
    x_inv = np.asarray(inverse_filter, dtype=np.float64)
    if y.ndim != 1 or x_inv.ndim != 1 or y.size == 0 or x_inv.size == 0:
        raise ValueError("recording e inverse_filter deben ser arrays 1D no vacios")

    h = sps.fftconvolve(y, x_inv, mode="full")

    i_pico = int(np.argmax(np.abs(h)))
    pico = np.abs(h[i_pico])
    if pico == 0:
        raise ValueError("La grabacion no contiene senal")

    inicio = max(i_pico - PRE_PICO_MUESTRAS, 0)
    return h[inicio:] / pico


def logarithmic_scale_conversion(signal: np.ndarray) -> np.ndarray:
    """Convierte una senal a escala logaritmica (dB) normalizada.

    ``L = 20 * log10(|x| / max(|x|))``. Evitar ``log(0)`` (usar un ``eps`` o
    un piso, por ejemplo -120 dB).

    Parameters
    ----------
    signal : np.ndarray
        Senal de entrada (valores lineales, array 1D).

    Returns
    -------
    np.ndarray
        Senal en dB, normalizada a 0 dB en el maximo.
    """
    amplitud = np.abs(signal)
    maximo = np.max(amplitud)

    piso_db = -120.0

    if maximo == 0:
        return np.full_like(amplitud, piso_db, dtype=float)

    amplitud_normalizada = amplitud / maximo
    amplitud_normalizada = np.maximum(amplitud_normalizada, 10 ** (piso_db / 20))

    return 20 * np.log10(amplitud_normalizada)
