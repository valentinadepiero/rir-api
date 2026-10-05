import numpy as np

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