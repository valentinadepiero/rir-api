import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Configuración de parámetros (usando listas de tuplas)
# =============================================================================
# Cada señal es una tupla con: (frecuencia, amplitud, color, nombre)
señales = [
    (500, 10.0, 'blue', 'Señal 500 Hz'),
    (5000, 3.0, 'red', 'Señal 5 kHz'),
    (1000, 5.0, 'green', 'Señal 1 kHz')
]

# Parámetros generales
duracion = 0.01  # Duración en segundos
fs = 100000       # Frecuencia de muestreo (100 kHz)

# =============================================================================
# Función para generar señales
# =============================================================================
def generar_senoidal(frecuencia, amplitud, duracion, fs):
    """Genera una señal senoidal usando NumPy"""
    t = np.arange(0, duracion, 1/fs)  # Vector de tiempo
    return t, amplitud * np.sin(2 * np.pi * frecuencia * t)

# =============================================================================
# Procesamiento principal
# =============================================================================
# Lista para almacenar todas las señales y sus tiempos
todas_señales = []
tiempos = []

# Generar las señales
for params in señales:
    frecuencia, amplitud, color, nombre = params
    t, señal = generar_senoidal(frecuencia, amplitud, duracion, fs)
    todas_señales.append(señal)
    tiempos.append(t)

# Crear señal combinada
señal_combinada = np.sum(todas_señales, axis=0)

# =============================================================================
# Análisis de señales
# =============================================================================
print("="*60)
print("ANÁLISIS DE SEÑALES")
print("="*60)


# =============================================================================
#Para el siguiente bucle for, se generan y recorren las listas con las tuplas
#para cada señal y sus parámetros.

#todas_señales: Lista de arrays NumPy con las señales generadas
#[array_señal1, array_señal2, array_señal3]

#señales: Lista de tuplas con parámetros de configuración
#[(50, 10.0, 'blue', 'Señal 50 Hz'), 
# (3000, 3.0, 'red', 'Señal 3 kHz'),
# (1000, 5.0, 'green', 'Señal 1 kHz')]

# Combinación con zip()

#zip(todas_señales, señales)
#Crea un iterador que empareja elementos correspondientes de ambas listas:

#[
#    (array_señal1, (50, 10.0, 'blue', 'Señal 50 Hz')),
#    (array_señal2, (3000, 3.0, 'red', 'Señal 3 kHz')),
#    (array_señal3, (1000, 5.0, 'green', 'Señal 1 kHz'))
#]

#La funcion enumerate() añade un índice a cada par de elementos, comenzando desde 1.
#[
#    (1, (array_señal1, (50, 10.0, 'blue', 'Señal 50 Hz'))),
#    (2, (array_señal2, (3000, 3.0, 'red', 'Señal 3 kHz'))),
#    (3, (array_señal3, (1000, 5.0, 'green', 'Señal 1 kHz')))
#]

# Desempaquetado de Tuplas

#i, (señal, params)
#Descompone cada elemento en:

#i: Número de iteración (1, 2, 3)
#señal: Array NumPy con los datos de la señal
#params: Tupla con parámetros (frecuencia, amplitud, color, nombre)

# =============================================================================
for i, (señal, params) in enumerate(zip(todas_señales, señales), 1):
    frecuencia, amplitud, color, nombre = params
    
    # Cálculos con NumPy
    maximo = np.max(señal)
    minimo = np.min(señal)
    media = np.mean(señal)
    desviacion = np.std(señal)
    energia = np.sum(señal**2) * (1/fs)
    energia_teorica = (amplitud**2 * duracion)/2
    
    print(f"\nSeñal {i}: {nombre}")
    print(f"• Frecuencia: {frecuencia} Hz")
    print(f"• Amplitud: {amplitud}")
    print(f"• Máximo: {maximo:.2f}")
    print(f"• Mínimo: {minimo:.2f}")
    print(f"• Valor medio: {media:.2f}")
    print(f"• Desviación estándar: {desviacion:.2f}")
    print(f"• Energía calculada: {energia:.2f}")
    print(f"• Energía teórica: {energia_teorica:.2f}")



 # Análisis para señal combinada
print("\n" + "="*60)
print("ANÁLISIS DE SEÑAL COMBINADA")
print("="*60)

# Calculamos la energía teórica como la suma de energías individuales
energia_teorica_combinada = sum((params[1]**2 * duracion)/2 for params in señales)

# Realizamos los cálculos para la señal combinada
maximo_comb = np.max(señal_combinada)
minimo_comb = np.min(señal_combinada)
media_comb = np.mean(señal_combinada)
desviacion_comb = np.std(señal_combinada)
energia_comb = np.sum(señal_combinada**2) * (1/fs)

print(f"\nSeñal resultante de la combinación:")
print(f"• Máximo: {maximo_comb:.2f}")
print(f"• Mínimo: {minimo_comb:.2f}")
print(f"• Valor medio: {media_comb:.2f}")
print(f"• Desviación estándar: {desviacion_comb:.2f}")
print(f"• Energía calculada: {energia_comb:.2f}")
print(f"• Energía teórica (suma individuales): {energia_teorica_combinada:.2f}")
print(f"• Relación energía calculada/teórica: {energia_comb/energia_teorica_combinada:.2f}")   

# =============================================================================
# Visualización con Matplotlib
# =============================================================================
plt.figure(figsize=(12, 10))

# Gráfico individual de cada señal
for i in range(3):
    plt.subplot(4, 1, i+1)
    plt.plot(tiempos[i], todas_señales[i], color=señales[i][2])
    plt.title(señales[i][3])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)

# Gráfico combinado
plt.subplot(4, 1, 4)
for i, señal in enumerate(todas_señales):
    plt.plot(tiempos[i], señal, color=señales[i][2], alpha=0.5, label=señales[i][3])
plt.plot(tiempos[0], señal_combinada, 'black', label='Señal Combinada', linewidth=2)
plt.title('Composición de Señales')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()