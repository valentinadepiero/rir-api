"""Prueba real de play_and_record con el sine sweep (M1).

Cadena: generate_sine_sweep_pair -> play_and_record -> convolucion con el filtro
inverso. Si la medicion funciona, la convolucion da la respuesta al impulso del
sistema (parlante + sala + microfono).
"""

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy import signal as sps

from app.services.audio_io import PRE_ROLL_S, play_and_record
from app.services.sine_sweep import generate_sine_sweep_pair

FS = 48000  # frecuencia de muestreo (Hz)
F1, F2 = 20.0, 20000.0  # rango del sweep (Hz)
DURACION_SWEEP_S = 5.0
AMPLITUD = 0.2  # escala del sweep, para no exigir al parlante
RECORD_DURATION_S = 8.0  # pre-roll + sweep + latencia + cola de reverberacion

# BEHRINGER UMC 202HD (MME): entrada 1, salida 5 (numeros de sd.query_devices())
sd.default.device = (1, 5)
print("Entrada:", sd.query_devices(1)["name"])
print("Salida: ", sd.query_devices(5)["name"])


def rms(x: np.ndarray) -> float:
    """Valor eficaz (RMS) de una senal."""
    return float(np.sqrt(np.mean(x**2)))


# 1) Generar el sweep y su filtro inverso (servicio 2)
sweep, inverso = generate_sine_sweep_pair(DURACION_SWEEP_S, F1, F2, FS)

# 2) Reproducir y grabar al mismo tiempo (servicio 3)
grabacion = play_and_record(AMPLITUD * sweep, FS, RECORD_DURATION_S)
esperadas = int(RECORD_DURATION_S * FS)
print(f"Muestras grabadas: {grabacion.shape[0]} (esperadas: {esperadas})")

# 3) Respuesta al impulso: convolucion de la grabacion con el filtro inverso
rir = sps.fftconvolve(grabacion, inverso)
i_pico = int(np.argmax(np.abs(rir)))

# Posicion del pico al convolucionar el sweep original con su inverso (referencia
# sin latencia): la diferencia entre ambos es el retardo del sistema.
i_ref = int(np.argmax(np.abs(sps.fftconvolve(sweep, inverso))))
retardo_s = (i_pico - i_ref) / FS - PRE_ROLL_S

# Pico contra el ruido justo antes de la llegada del sonido directo
ruido = rir[i_pico - int(0.1 * FS) : i_pico - int(0.02 * FS)]
relacion_db = 20 * np.log10(np.abs(rir[i_pico]) / rms(ruido))

print(f"Pico de la grabacion: {np.max(np.abs(grabacion)):.3f}")
print(f"Retardo del sistema: {retardo_s * 1000:.0f} ms")
print(f"Pico de la respuesta al impulso / ruido: {relacion_db:.1f} dB")

# 4) Graficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 10))

t = np.arange(grabacion.shape[0]) / FS
ax1.plot(t, grabacion, linewidth=0.5)
ax1.set_xlabel("Tiempo [s]")
ax1.set_ylabel("Amplitud")
ax1.set_title("Grabacion del sweep")

# En el espectrograma el sweep tiene que verse como una linea que sube en frecuencia
f, tt, sxx = sps.spectrogram(grabacion, fs=FS, nperseg=4096, noverlap=2048)
nivel_db = 10 * np.log10(sxx[1:] + 1e-20)
vmax = nivel_db.max()
ax2.pcolormesh(tt, f[1:], nivel_db, shading="auto", vmin=vmax - 80, vmax=vmax)
ax2.set_yscale("log")
ax2.set_ylim(F1, F2)
ax2.set_xlabel("Tiempo [s]")
ax2.set_ylabel("Frecuencia [Hz]")
ax2.set_title("Espectrograma de la grabacion")

pre, post = int(0.1 * FS), int(1.5 * FS)
tramo = np.abs(rir[i_pico - pre : i_pico + post])
t_rir = (np.arange(tramo.size) - pre) / FS
ax3.plot(t_rir, 20 * np.log10(tramo / tramo.max() + 1e-12))
ax3.set_ylim(-100, 5)
ax3.set_xlabel("Tiempo respecto del pico [s]")
ax3.set_ylabel("Nivel [dB]")
ax3.set_title(f"Respuesta al impulso (pico/ruido = {relacion_db:.1f} dB)")

fig.tight_layout()
fig.savefig("docs/m1/prueba_real_sweep.png", dpi=150)
print("Grafico guardado en docs/m1/prueba_real_sweep.png")
