"""Servicio de filtrado por bandas de octava.

Milestone 2: Procesamiento de la respuesta al impulso.
"""

import numpy as np
from scipy import signal as sps


def filter_single_band(
    signal: np.ndarray, fs: int, center_freq: float, order: int = 4
) -> np.ndarray:
    """Aplica un filtro pasabanda de una octava centrado en ``center_freq`` (IEC 61260).

    Filtro Butterworth pasabanda (``scipy.signal.butter`` con ``output='sos'``)
    con frecuencias de corte:

    - inferior: ``center_freq / sqrt(2)``
    - superior: ``center_freq * sqrt(2)``

    Aplicarlo con ``scipy.signal.sosfiltfilt`` (fase cero), importante para no
    distorsionar EDT y T60. La forma ``(b, a)`` con ``filtfilt`` es inestable en
    las bandas graves.

    Parameters
    ----------
    signal : np.ndarray
        Senal de entrada (array 1D).
    fs : int
        Frecuencia de muestreo en Hz.
    center_freq : float
        Frecuencia central de la banda de octava en Hz.
    order : int, optional
        Orden del filtro Butterworth (por defecto 4).

    Returns
    -------
    np.ndarray
        Senal filtrada (array 1D, misma longitud que ``signal``).

    Raises
    ------
    ValueError
        Si el borde superior de la banda alcanza la frecuencia de Nyquist
        (``fs / 2``), por ejemplo la banda de 16 kHz con ``fs = 44100``.
    """
    f_inf = center_freq / np.sqrt(2)
    f_sup = center_freq * np.sqrt(2)

    if f_sup >= fs / 2:
        raise ValueError(
            f"La banda de {center_freq:g} Hz no entra con fs = {fs} Hz: "
            f"su borde superior ({f_sup:.1f} Hz) llega a Nyquist ({fs / 2:g} Hz)."
        )

    sos = sps.butter(order, [f_inf, f_sup], btype="bandpass", fs=fs, output="sos")
    return sps.sosfiltfilt(sos, signal)
