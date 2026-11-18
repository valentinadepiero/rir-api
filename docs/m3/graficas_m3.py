"""Graficas 1 y 2 de M3 con los servicios de la propia API.

Uso, desde la raiz del repositorio (PowerShell):
    $env:PYTHONPATH = "."
    uv run python docs/m3/graficas_m3.py

Genera en docs/m3/:
  schroeder_regresiones.png  (grafica 1: curva de Schroeder + rectas de EDT, T20 y T30)
  filtros_octava.png         (grafica 2: filtros de octava y RI real filtrada por banda)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from app.services.acoustic_parameters import (
    apply_schroeder_integral,
    apply_smoothing,
    linear_regression,
)
from app.services.filter import filter_single_band
from app.services.signal_utils import load_audio

BASE = Path("docs/m3")
BANDAS = [125, 250, 500, 1000, 2000, 4000]
BANDA_GRAFICA_1 = 1000
CASOS = [
    ("RI sintética (T60 = 2 s)", BASE / "ri_sintetica.wav"),
    ("RI real (con 5 ms de ceros al inicio)", BASE / "ri_larga_real_pad.wav"),
]
# Tramos de cada parametro: (nivel inicial, nivel final) en dB
TRAMOS = {"EDT": (0, -10), "T20": (-5, -25), "T30": (-5, -35)}
COLORES = {"EDT": "#2ca02c", "T20": "#ff7f0e", "T30": "#d62728"}


def grafica_schroeder() -> None:
    fig, ejes = plt.subplots(1, len(CASOS), figsize=(11, 4.4), sharey=True)
    for ax, (titulo, ruta) in zip(ejes, CASOS):
        ir, fs = load_audio(ruta)
        banda = filter_single_band(ir, fs, BANDA_GRAFICA_1)
        edc = apply_schroeder_integral(banda)
        t = np.arange(len(edc)) / fs
        ax.plot(t, edc, color="#1f4e79", lw=1.6, label="Curva de Schroeder")
        for nombre, (inicio, fin) in TRAMOS.items():
            tramo = (edc <= inicio) & (edc >= fin)
            m, b, r2 = linear_regression(t[tramo], edc[tramo])
            t_60 = -60 / m
            x = np.array([t[tramo][0], (-60 - b) / m])
            ax.plot(
                t[tramo],
                m * t[tramo] + b,
                color=COLORES[nombre],
                lw=2.4,
                label=f"{nombre} = {t_60:.2f} s (R² = {r2:.3f})",
            )
            ax.plot(x, m * x + b, color=COLORES[nombre], lw=1, ls="--")
        ax.axhline(-60, color="gray", lw=0.8, ls=":")
        ax.set_ylim(-75, 3)
        bajo = np.where(edc < -75)[0]
        ax.set_xlim(0, min(t[-1], 1.1 * t[bajo[0]]) if len(bajo) else t[-1])
        ax.set_title(f"{titulo} · banda de {BANDA_GRAFICA_1} Hz")
        ax.set_xlabel("Tiempo (s)")
        ax.grid(alpha=0.3)
        ax.legend(loc="upper right", fontsize=8)
    ejes[0].set_ylabel("Nivel respecto de la energía total (dB)")
    fig.suptitle("Curva de decaimiento (integral de Schroeder) y regresiones lineales")
    fig.tight_layout()
    salida = BASE / "schroeder_regresiones.png"
    fig.savefig(salida, dpi=150)
    print(f"Guardado: {salida}")


def respuesta_filtros(fs: int = 48000, n: int = 2**16) -> None:
    """Mide la respuesta en frecuencia de cada filtro pasandole un impulso."""
    impulso = np.zeros(n)
    impulso[n // 2] = 1.0
    freqs = np.fft.rfftfreq(n, 1 / fs)
    for fc in BANDAS:
        h = np.fft.rfft(filter_single_band(impulso, fs, fc))
        db = 20 * np.log10(np.abs(h) + 1e-12)
        plt.gca().semilogx(freqs[1:], db[1:], label=f"{fc} Hz")


def grafica_filtros() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))

    plt.sca(ax1)
    respuesta_filtros()
    ax1.axhline(-3, color="gray", lw=0.8, ls=":")
    ax1.set_xlim(40, 20000)
    ax1.set_ylim(-60, 5)
    ax1.set_xlabel("Frecuencia (Hz)")
    ax1.set_ylabel("Ganancia (dB)")
    ax1.set_title("Respuesta de los filtros de octava (fs = 48 kHz)")
    ax1.grid(alpha=0.3, which="both")
    ax1.legend(fontsize=8, ncol=2, loc="lower center")

    ir, fs = load_audio(CASOS[1][1])
    for fc in BANDAS:
        banda = filter_single_band(ir, fs, fc)
        env = apply_smoothing(banda, fs, method="moving_average", window_ms=10)
        env_db = 20 * np.log10(env / env.max() + 1e-12)
        ax2.plot(np.arange(len(env_db)) / fs, env_db, lw=1.3, label=f"{fc} Hz")
    ax2.set_ylim(-70, 3)
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Envolvente RMS (dB, normalizada por banda)")
    ax2.set_title("RI real filtrada por banda (envolvente RMS, 10 ms)")
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=8, ncol=2)

    fig.tight_layout()
    salida = BASE / "filtros_octava.png"
    fig.savefig(salida, dpi=150)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    grafica_schroeder()
    grafica_filtros()
