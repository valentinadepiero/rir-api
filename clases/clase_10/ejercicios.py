import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 10: Ejercicios Practicos
    ## Procesamiento de la Respuesta al Impulso

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import signal
    return np, plt, signal


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Envolvente con Hilbert

    Genera una sinusoide de **1000 Hz** que decae exponencialmente con $\tau = 0.2$ s.
    Duracion 1 segundo, fs=44100.

    1. Calcula la envolvente usando `scipy.signal.hilbert`
    2. Grafica la senal y la envolvente superpuestas
    3. Grafica la envolvente en dB

    **Pista**: la envolvente es `np.abs(signal.hilbert(x))`
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Promedio movil sobre ruido

    Genera una senal que sea una **sinusoide de 5 Hz** sumada con **ruido gaussiano**.

    1. Aplica promedio movil con ventanas de M = 10, 50, 100 y 200 muestras
    2. Grafica todos los resultados superpuestos
    3. Comenta: cual M es mejor para recuperar la sinusoide?

    fs = 1000 Hz, duracion = 2 s, amplitud sinusoide = 1.0, amplitud ruido = 0.5
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Integral de Schroeder

    Genera una RI sintetica con **T60 = 2 segundos**:
    ```
    tau = T60 / (6 * np.log(10))
    h = np.random.randn(N) * np.exp(-t / tau)
    ```

    1. Calcula la integral de Schroeder (EDC)
    2. Normaliza y convierte a dB
    3. Grafica la RI y la EDC en dB
    4. Marca con una linea horizontal el nivel de -60 dB

    fs = 44100, duracion = 3 s
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: T30 y T60 con regresion lineal

    Usando la RI del ejercicio 3 (T60 real = 2 s):

    1. Calcula la EDC en dB
    2. Selecciona el rango de -5 a -35 dB
    3. Ajusta una recta con `np.polyfit`
    4. Calcula T30 = -60 / pendiente
    5. Grafica la EDC con la recta de regresion superpuesta
    6. Compara T30 con el T60 real

    **Pista**: primero encontra los indices donde la EDC esta entre -5 y -35 dB.
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: EDT (Early Decay Time)

    Usando la misma RI:

    1. Calcula el EDT usando el rango de **0 a -10 dB** de la EDC
    2. Ajusta una recta y calcula EDT = -60 / pendiente
    3. Compara EDT con T30

    En una sala real, EDT < T60 indica que la energia decae rapido al principio
    (reflexiones tempranas fuertes). Si EDT ≈ T60, el campo es mas difuso.
    """)
    return


@app.cell
def _():
    # EJERCICIO 5: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Efecto del piso de ruido

    Genera una RI con T60 = 2 s y agrega un **piso de ruido** constante:
    ```
    h = h_limpia + nivel_ruido * np.random.randn(N)
    ```

    Prueba con niveles de ruido: 0.001, 0.01, 0.05

    1. Calcula la EDC para cada caso
    2. Grafica las EDCs superpuestas
    3. Calcula T30 para cada caso
    4. Observa como el piso de ruido **distorsiona** la curva de decaimiento

    Este problema motiva el uso del **metodo de Lundeby** (que veremos mas adelante).
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: T60 por banda de octava

    Genera una RI sintetica con T60 = 1.5 s (broadband).

    1. Filtra la RI en bandas de octava: 125, 250, 500, 1000, 2000, 4000 Hz
       (usa filtros Butterworth de la clase 9)
    2. Calcula T30 para cada banda
    3. Grafica T30 vs frecuencia (grafico de barras)

    **Nota**: para una RI sintetica con decaimiento uniforme, T30 deberia ser similar en todas las bandas. En salas reales, T60 varia con la frecuencia (generalmente mayor en bajas frecuencias).
    """)
    return


@app.cell
def _():
    # EJERCICIO 7: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Funcion completa de analisis

    Implementa una funcion `analizar_ri(h, fs)` que reciba una RI y su fs, y retorne un diccionario con:

    ```python
    {
        'broadband': {'EDT': ..., 'T20': ..., 'T30': ...},
        125: {'EDT': ..., 'T20': ..., 'T30': ...},
        250: {'EDT': ..., 'T20': ..., 'T30': ...},
        ...
    }
    ```

    Prueba con una RI sintetica de T60 = 1.8 s y muestra los resultados en una tabla.

    **Pista**: combina los filtros de octava, Schroeder, y regresion de los ejercicios anteriores.
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
