import numpy as np

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
    import numpy as np
    
    # Crear vector de tiempo
    t = np.arange(0, duracion, 1/fs)
    
    # Generar la señal
    señal = amplitud * np.sin(2 * np.pi * frecuencia * t)
    
    return t, señal