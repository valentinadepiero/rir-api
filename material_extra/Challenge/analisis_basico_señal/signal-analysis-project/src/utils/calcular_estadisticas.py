def calcular_estadisticas(señal):
    """
    Calcula estadísticas básicas de la señal.
    
    Parámetros:
    - señal: Array de numpy con la señal
    
    Retorna:
    - Un diccionario con las estadísticas calculadas
    """
    import numpy as np
    
    estadisticas = {
        "valor_maximo": np.max(señal),
        "valor_minimo": np.min(señal),
        "valor_medio": np.mean(señal),
        "desviacion_estandar": np.std(señal)
    }
    return estadisticas