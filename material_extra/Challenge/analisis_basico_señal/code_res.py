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

def calcular_energia(señal):
    """
    Calcula la energía de una señal (suma de los cuadrados de sus valores).
    
    Parámetros:
    - señal: Array de numpy con la señal
    
    Retorna:
    - La energía total de la señal
    """
    # La energía es la suma de los cuadrados de la señal
    energia = np.sum(señal**2)
    return energia

def generar_señal_compuesta(duracion, fs):
    """
    Genera una señal compuesta por la suma de dos señales sinusoidales.
    
    Parámetros:
    - duracion: Duración en segundos
    - fs: Frecuencia de muestreo en Hz
    
    Retorna:
    - t: Vector de tiempo
    - señal_compuesta: Señal compuesta resultante
    """
    # Crear vector de tiempo
    t = np.arange(0, duracion, 1/fs)
    
    # Parámetros para la primera señal
    frecuencia1 = 5  # Hz
    amplitud1 = 2.0
    
    # Parámetros para la segunda señal
    frecuencia2 = 15  # Hz (frecuencia más alta)
    amplitud2 = 0.5   # Amplitud menor
    
    # Generar ambas señales
    señal1 = amplitud1 * np.sin(2 * np.pi * frecuencia1 * t)
    señal2 = amplitud2 * np.sin(2 * np.pi * frecuencia2 * t)
    
    # Sumar las señales para crear la señal compuesta
    señal_compuesta = señal1 + señal2
    
    return t, señal_compuesta

# Parámetros de la señal (¡puedes modificarlos!)
frecuencia = 5  # Hz
amplitud = 2.0
duracion = 1.0  # segundos
fs = 1000  # frecuencia de muestreo en Hz

# Generar la señal
t, señal = generar_senoidal(frecuencia, amplitud, duracion, fs)
#t, señal = generar_señal_compuesta(1.0, 1000)

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