import numpy as np
import matplotlib.pyplot as plt

from utils.generar_senoidal import generar_senoidal
from utils.calcular_estadisticas import calcular_estadisticas
from utils.calcular_energia import calcular_energia
from utils.generar_señal_compuesta import generar_señal_compuesta

# Parámetros de la señal (¡puedes modificarlos!)
frecuencia = 5  # Hz
amplitud = 2.0
duracion = 1.0  # segundos
fs = 1000  # frecuencia de muestreo en Hz

# Generar la señal
t, señal = generar_senoidal(frecuencia, amplitud, duracion, fs)

# Calcular estadísticas
stats = calcular_estadisticas(señal)

# Calcular energía
energia_señal = calcular_energia(señal)

# Mostrar resultados
print("Análisis de la Señal Sinusoidal:")
print(f"Frecuencia: {frecuencia} Hz")
print(f"Amplitud: {amplitud}")
print(f"Duración: {duracion} segundos")
print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Energía de la señal: {energia_señal}")
print("\nEstadísticas:")

for key, value in stats.items():
    print(f"- {key}: {value:.4f}")

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, señal)
plt.title(f"Señal Sinusoidal de {frecuencia} Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Para mostrar la gráfica:
plt.show()