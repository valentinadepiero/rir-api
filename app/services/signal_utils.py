"""Utilidades de procesamiento de senales.

Milestone 2: Procesamiento de la respuesta al impulso.
"""

from pathlib import Path

import numpy as np
import soundfile as sf


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

    if path.suffix.lower() not in (".wav", ".flac"):
        raise ValueError(f"Formato no soportado: {path}")

    if not path.exists():
        raise FileNotFoundError(f"El archivo no se encuentra en {path}.")

    try:
        signal, fs = sf.read(path, dtype="float64")
    except sf.LibsndfileError as e:
        raise ValueError(f"No se pudo leer el archivo de audio {path}: {e}") from e

    signal = np.asarray(signal, dtype=np.float64)

    if signal.ndim not in (1, 2):
        raise ValueError("Numero de canales invalido.")

    if signal.ndim == 2:
        signal = signal.mean(axis=1)

    if signal.size == 0:
        raise ValueError("El archivo de audio esta vacio.")

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
    raise NotImplementedError("Implementar en Milestone 2")


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
    """
    raise NotImplementedError("Implementar en Milestone 2")


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
    raise NotImplementedError("Implementar en Milestone 2")
