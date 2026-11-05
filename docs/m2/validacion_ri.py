from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from app.services.filter import filter_single_band
from app.services.signal_utils import load_audio, logarithmic_scale_conversion

BANDAS = [125, 250, 500, 1000, 2000, 4000]
SALIDA = Path("docs/m2")


def curva_decaimiento_db(h):
    """Curva de Schroeder en dB (0 dB al inicio)."""
    energia = np.cumsum(h[::-1] ** 2)[::-1]
    # el servicio 5 espera amplitud, y la energía es amplitud al cuadrado
    return logarithmic_scale_conversion(np.sqrt(energia))


def t60_desde_curva(curva_db, t):
    mascara = (curva_db <= -5) & (curva_db >= -25)
    if mascara.sum() < 2:
        return None
    pendiente, _ = np.polyfit(t[mascara], curva_db[mascara], 1)
    return -60 / pendiente


def analizar(ruta, nombre):
    h, fs = load_audio(ruta)
    t = np.arange(len(h)) / fs

    fig, ejes = plt.subplots(3, 1, figsize=(9, 11))

    ejes[0].plot(t, h)
    ejes[0].set(title=f"{nombre} - forma de onda", xlabel="Tiempo [s]", ylabel="Amplitud")

    f = np.fft.rfftfreq(len(h), 1 / fs)
    espectro_db = logarithmic_scale_conversion(np.abs(np.fft.rfft(h)))
    ejes[1].semilogx(f[1:], espectro_db[1:])
    ejes[1].set(
        title="Espectro",
        xlabel="Frecuencia [Hz]",
        ylabel="Magnitud [dB]",
        ylim=(-100, 5),
    )

    for fc in BANDAS:
        hb = filter_single_band(h, fs, fc)
        curva = curva_decaimiento_db(hb)
        t60 = t60_desde_curva(curva, t)
        etiqueta = f"{fc} Hz" + (f" (T60≈{t60:.2f} s)" if t60 else "")
        ejes[2].plot(t, curva, label=etiqueta)
        print(f"{nombre} {fc} Hz: T60 = {t60}")
    ejes[2].set(
        title="Decaimiento por banda",
        xlabel="Tiempo [s]",
        ylabel="Nivel [dB]",
        ylim=(-70, 5),
    )
    ejes[2].legend()

    fig.tight_layout()
    fig.savefig(SALIDA / f"{nombre}.png", dpi=150)


analizar("docs/m2/ri_corta_real.wav", "ri_corta_real")
analizar("docs/m2/ri_larga_real.wav", "ri_larga_real")
