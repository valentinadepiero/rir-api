"""Servicio de generacion de sine sweep logaritmico.

Milestone 1: Generacion de senales.
"""

import numpy as np
import math as ma


def generate_sine_sweep_pair(
    duracion: float, f1: float, f2: float, fs: int
) -> tuple[np.ndarray, np.ndarray]:
    """Genera un barrido senoidal logaritmico (sine sweep) y su filtro inverso.

    El sweep es ``x(t) = sin[2*pi*f1*T / ln(f2/f1) * (exp(t*ln(f2/f1)/T) - 1)]``
    y el filtro inverso es el sweep invertido en el tiempo con correccion de
    amplitud ``A(t) = exp(-t*ln(f2/f1)/T)`` (tecnica de Farina, 2000). La
    convolucion ``sweep * inverse_filter`` debe aproximar un impulso.

    Parameters
    ----------
    duration : float
        Duracion del barrido en segundos.
    f1 : float
        Frecuencia inicial del barrido en Hz (tipicamente 20 Hz).
    f2 : float
        Frecuencia final del barrido en Hz (tipicamente 20000 Hz).
    fs : int
        Frecuencia de muestreo en Hz.

    Returns
    -------
    sweep : np.ndarray
        Senal del barrido senoidal, normalizada, de longitud ``int(duration * fs)``.
    inverse_filter : np.ndarray
        Filtro inverso correspondiente, normalizado, de la misma longitud.

    References
    ----------
    .. [1] Farina, A. (2000). "Simultaneous measurement of impulse response
       and distortion with a swept-sine technique." 108th AES Convention.
    """

    # SINE SWEEP ------------------------------------------
    # para generar el array de muestras: entre 0 y duración 
    # ubico una cantidad de muestras (duracion * frecuencia de sampleo) 
    # separados por intervalos iguales.
    t = np.linspace(0, duracion, int(duracion * fs))

    # para cada una de las muestras, aplico la formula de sine sweep logaritmico
    sine_sweep = np.array(
        [ma.sin(
            (2 * ma.pi * f1 * duracion) *
            (ma.exp(n * (ma.log(f2 / f1) / duracion)) - 1) /
            ma.log(f2 / f1)
            ) 
        for n in t]
    )

    # FILTRO INVERSO ---------------------------------------
    # para cada una de las muestras, aplico la formula de envolvente
    envolvente = np.array(
        [ma.exp(-n * ma.log(f2 / f1) / duracion)
        for n in t]
    )
    filt_inv = sine_sweep[::-1] * envolvente   # multiplica muestra a muestra el sine sweep invertido con la envolvente

    # NORMALIZAR --------------------------------------------
    # divide la señal por la amplitud máxima de la señal
    sine_sweep_normalizada = sine_sweep / np.max(       # max devuelve "the maximum of an array or maximum along an axis."
        np.abs(sine_sweep))                             # abs devuelve "An ndarray containing the absolute value of each element in x"
                         

    filt_inv_normalizado = filt_inv / np.max(       
        np.abs(filt_inv))    

    return sine_sweep_normalizada, filt_inv_normalizado
