import numpy as np

def calcular_energia(señal):
    """
    Calcula la energía de una señal (suma de los cuadrados de sus valores).
    
    Parámetros:
    - señal: Array de numpy con la señal
    
    Retorna:
    - La energía total de la señal
    """
    energia = np.sum(señal**2)
    return energia