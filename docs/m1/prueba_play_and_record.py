"""Prueba real de play_and_record con parlante y microfono (M1)."""

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

from app.services.audio_io import PRE_ROLL_S, play_and_record

FS = 48000  # frecuencia de muestreo (Hz)
FRECUENCIA_HZ = 1000.0  # frecuencia del tono de prueba
DURACION_TONO_S = 2.0
AMPLITUD = 0.2  # baja, para no saturar ni exigir al parlante
RECORD_DURATION_S = 4.0

# BEHRINGER UMC 202HD (MME): entrada 1, salida 5 (numeros de sd.query_devices())
sd.default.device = (1, 5)
print("Entrada:", sd.query_devices(1)["name"])
print("Salida: ", sd.query_devices(5)["name"])


def rms(x: np.ndarray) -> float:
    """Valor eficaz (RMS) de una senal."""
    return float(np.sqrt(np.mean(x**2)))


t = np.arange(int(DURACION_TONO_S * FS)) / FS
tono = AMPLITUD * np.sin(2 * np.pi * FRECUENCIA_HZ * t)

grabacion = play_and_record(tono, FS, RECORD_DURATION_S)

esperadas = int(RECORD_DURATION_S * FS)
print(f"Muestras grabadas: {grabacion.shape[0]} (esperadas: {esperadas})")

# Tramo de silencio (antes de que empiece el tono) y tramo central del tono
silencio = grabacion[int(0.2 * PRE_ROLL_S * FS) : int(0.8 * PRE_ROLL_S * FS)]
centro = grabacion[int((PRE_ROLL_S + 0.5) * FS) : int((PRE_ROLL_S + 1.5) * FS)]

relacion_db = 20 * np.log10(rms(centro) / max(rms(silencio), 1e-12))

espectro = np.abs(np.fft.rfft(centro * np.hanning(len(centro))))
frecuencias = np.fft.rfftfreq(len(centro), d=1 / FS)
f_dominante = frecuencias[np.argmax(espectro)]

print(f"RMS silencio: {rms(silencio):.5f}")
print(f"RMS tono:     {rms(centro):.5f}")
print(f"Relacion tono/silencio: {relacion_db:.1f} dB")
print(f"Frecuencia dominante: {f_dominante:.1f} Hz (esperada: {FRECUENCIA_HZ:.0f} Hz)")
print(f"Pico de la grabacion: {np.max(np.abs(grabacion)):.3f}")
t_grabacion = np.arange(grabacion.shape[0]) / FS
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))

ax1.plot(t_grabacion, grabacion, linewidth=0.5)
ax1.axvline(PRE_ROLL_S, color="r", linestyle="--", label="inicio del tono")
ax1.axvline(PRE_ROLL_S + DURACION_TONO_S, color="r", linestyle="--", label="fin del tono")
ax1.set_xlabel("Tiempo [s]")
ax1.set_ylabel("Amplitud")
ax1.set_title(f"Grabacion (tono/silencio = {relacion_db:.1f} dB)")
ax1.legend()

ax2.plot(frecuencias, 20 * np.log10(espectro + 1e-12))
ax2.set_xlim(0, 5000)
ax2.set_xlabel("Frecuencia [Hz]")
ax2.set_ylabel("Nivel relativo [dB]")
ax2.set_title(f"Espectro del tramo central (pico en {f_dominante:.0f} Hz)")

fig.tight_layout()
fig.savefig("docs/m1/prueba_play_and_record.png", dpi=150)
print("Grafico guardado en docs/m1/prueba_play_and_record.png")
