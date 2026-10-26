"""Servicio de reproduccion y grabacion simultanea.

Milestone 1: Generacion de senales.

``sounddevice`` se importa **dentro** de la funcion (import perezoso): asi el
resto de la API, los tests y el CI funcionan en maquinas sin placa de audio.
"""

import numpy as np

PRE_ROLL_S = 0.5  # silencio inicial en segundos (latencia del driver de audio)


def play_and_record(signal: np.ndarray, fs: int, record_duration: float) -> np.ndarray:
    """Reproduce una senal y graba simultaneamente (``sounddevice.playrec``).

    Consideraciones:

    - ``record_duration`` debe ser mayor o igual a la duracion de la senal
      para capturar la cola de reverberacion del recinto.
    - Aceptar senales mono (array 1D) y estereo (array 2D ``(muestras, canales)``)
      sin asumir la forma.
    - Se recomienda un silencio inicial (pre-roll) de 0.5-1 s para compensar la
      latencia del sistema de audio.
    - Documentar en el README la configuracion usada (dispositivo, canales, fs,
      buffer size).

    Parameters
    ----------
    signal : np.ndarray
        Senal a reproducir (1D mono o 2D ``(muestras, canales)``).
    fs : int
        Frecuencia de muestreo en Hz.
    record_duration : float
        Duracion total de la grabacion en segundos.

    Returns
    -------
    np.ndarray
        Senal grabada, con ``int(record_duration * fs)`` muestras.

    Raises
    ------
    RuntimeError
        Si no hay un dispositivo de audio disponible (con un mensaje informativo).
    ValueError
        Si record_duration no alcanza para el silencio inicial mas la senal.
    """
    import sounddevice as sd

    senal = np.asarray(signal, dtype=np.float32)
    es_mono = senal.ndim == 1
    if es_mono:
        senal = senal[:, np.newaxis]  # (N,) -> (N, 1)

    n_total = int(record_duration * fs)
    n_pre_roll = int(PRE_ROLL_S * fs)
    n_senal, canales = senal.shape
    if n_pre_roll + n_senal > n_total:
        raise ValueError(
            "record_duration es demasiado corta: no alcanza para el silencio "
            "inicial mas la senal"
        )

    a_reproducir = np.zeros((n_total, canales), dtype=np.float32)
    a_reproducir[n_pre_roll : n_pre_roll + n_senal] = senal

    try:
        grabacion = sd.playrec(
            a_reproducir, samplerate=fs, channels=canales, blocking=True
        )
    except sd.PortAudioError as exc:
        raise RuntimeError(
            "No se pudo usar el dispositivo de audio. Verifica que haya un "
            "microfono y un parlante conectados y disponibles."
        ) from exc

    return grabacion[:, 0] if es_mono else grabacion
