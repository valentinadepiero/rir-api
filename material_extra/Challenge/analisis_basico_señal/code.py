# Ejercicio: Análisis Básico de una Señal Sinusoidal
# ----------------------------------------------
# Este programa genera y analiza una señal sinusoidal simple.
# Conceptos: variables, funciones, bibliotecas, gráficos y cálculos básicos.
#
# Consigna:
# 1. Ejecuta este código y observa la salida
# 2. Modifica la frecuencia y la amplitud y observa cómo cambia la señal
# 3. Agrega una función para calcular la energía de la señal (suma de cuadrados)
# 4. Opcional: Genera una segunda señal y súmala a la primera para crear una señal compuesta

import numpy as np
import matplotlib.pyplot as plt

def generar_senoidal(frecuencia, amplitud, duracion, fs):
    """
    Genera una señal sinusoidal con parámetros específicos.
    
    Parámetros:
    - frecuencia: Frecuencia de la señal en Hz
    - amplitud: Amplitud de la señal
    - duracion: Duración en segundos
    - fs: Frecuencia de muestreo en Hz
    
    Retorna:
    - t: Vector de tiempo
    - señal: Señal sinusoidal generada
    """
    # Crear vector de tiempo
    t = np.arange(0, duracion, 1/fs)
    
    # Generar la señal
    señal = amplitud * np.sin(2 * np.pi * frecuencia * t)
    
    return t, señal

def calcular_estadisticas(señal):
    """
    Calcula estadísticas básicas de la señal.
    
    Parámetros:
    - señal: Array de numpy con la señal
    
    Retorna:
    - Un diccionario con las estadísticas calculadas
    """
    estadisticas = {
        "valor_maximo": np.max(señal),
        "valor_minimo": np.min(señal),
        "valor_medio": np.mean(señal),
        "desviacion_estandar": np.std(señal)
    }
    return estadisticas

# Parámetros de la señal (¡puedes modificarlos!)
frecuencia = 5  # Hz
amplitud = 2.0
duracion = 1.0  # segundos
fs = 1000  # frecuencia de muestreo en Hz

# Generar la señal
t, señal = generar_senoidal(frecuencia, amplitud, duracion, fs)

# Calcular estadísticas
stats = calcular_estadisticas(señal)

# Mostrar resultados
print("Análisis de la Señal Sinusoidal:")
print(f"Frecuencia: {frecuencia} Hz")
print(f"Amplitud: {amplitud}")
print(f"Duración: {duracion} segundos")
print(f"Frecuencia de muestreo: {fs} Hz")
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