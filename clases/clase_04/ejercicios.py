import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 4: Ejercicios practicos
    ## El Universo NumPy y las Senales

    Completa cada ejercicio en la celda indicada. Todos los ejercicios requieren NumPy y Matplotlib.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Eje temporal

    Crea un eje temporal para una senal de **2 segundos** muestreada a **48000 Hz**.

    - Usa `np.arange`
    - Verifica que el numero de muestras sea correcto (debe ser 96000)
    - Verifica que la ultima muestra sea menor que 2.0 segundos
    - Imprime: numero de muestras, primera muestra, ultima muestra, duracion total
    """)
    return


@app.cell
def _(np):
    # === EJERCICIO 1: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Senoidal de 440 Hz

    Genera una senoidal de **440 Hz** con amplitud 1, muestreada a **44100 Hz**.

    - Calcula cuantas muestras corresponden a exactamente **5 periodos**
    - Genera la senal solo para esos 5 periodos
    - Graficala con `plt.plot()`, incluyendo titulo, labels y grid
    - El eje x debe estar en milisegundos
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 2: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Suma de senoidales

    Genera dos senoidales:
    - **Fundamental**: 440 Hz, amplitud 1.0
    - **Armonico**: 880 Hz, amplitud 0.5

    Ambas a 44100 Hz durante 10 ms. Graficalas en **3 subplots** verticales:
    1. Fundamental sola
    2. Armonico solo
    3. Suma de ambas

    Usa la misma escala en Y para los tres graficos (`set_ylim(-1.6, 1.6)`).
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 3: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Impulso unitario con stem

    Crea un array de **1000 muestras** de ceros y coloca un impulso unitario en la **muestra 100**.

    - Graficalo con `plt.stem()` mostrando solo las muestras 80 a 120 (para que se vea bien)
    - Titulo: "Impulso unitario en n=100"
    - Labels apropiados
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 4: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Exponencial decreciente en dB

    Genera una exponencial decreciente que modela una reverberacion con **T60 = 2 segundos**.

    - Frecuencia de muestreo: 44100 Hz
    - Duracion: 3 segundos
    - $\alpha = 6.908 / T_{60}$
    - Grafica en **2 subplots**: escala lineal y escala en dB
    - En el grafico dB, marca con una linea horizontal el nivel -60 dB
    - Marca con una linea vertical el instante T60

    Tip: para convertir a dB usa $20 \log_{10}(|x|)$ y evita el $\log$ de cero con `np.maximum(x, 1e-10)`.
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 5: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Envolvente ADSR

    Crea un array que represente una envolvente **ADSR** (Attack-Decay-Sustain-Release) con los siguientes parametros:

    - **Attack**: 10 ms, de 0 a 1.0 (lineal)
    - **Decay**: 20 ms, de 1.0 a 0.7 (lineal)
    - **Sustain**: 200 ms, nivel constante 0.7
    - **Release**: 50 ms, de 0.7 a 0 (lineal)
    - Frecuencia de muestreo: 44100 Hz

    Graficala con `plt.plot()`. Marca con lineas verticales punteadas las transiciones entre cada fase.

    Tip: usa `np.linspace` para cada segmento y `np.concatenate` para unirlos.
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 6: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Broadcasting - Matriz de senoidales

    Usa broadcasting para crear una **matriz** donde cada fila contiene una senoidal de diferente frecuencia.

    - Frecuencias: [100, 200, 400, 800, 1600] Hz
    - Frecuencia de muestreo: 44100 Hz
    - Duracion: 20 ms
    - La matriz debe tener shape `(5, N)` donde N es el numero de muestras

    **Sin usar loops**. Pista: crea un vector columna de frecuencias `(5, 1)` y un vector fila de tiempo `(1, N)`, y multiplica.

    Grafica las 5 senoidales en subplots verticales.
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 7: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Comparacion de rendimiento

    Genera **1 millon** de muestras de una senoidal de 440 Hz a 44100 Hz, de dos formas:

    1. Con un **loop for** de Python (usando `math.sin`)
    2. Con **NumPy vectorizado** (usando `np.sin`)

    Usa `time.perf_counter()` para medir el tiempo de cada metodo. Imprime:
    - Tiempo de cada metodo en milisegundos
    - Factor de speedup (cuantas veces mas rapido es NumPy)
    - Verificacion de que ambos resultados son iguales (`np.allclose`)
    """)
    return


@app.cell
def _(np):
    import time
    import math
    # === EJERCICIO 8: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Senoidal interactiva

    Crea una senoidal interactiva usando sliders de Marimo:

    - `mo.ui.slider` para **frecuencia** (100 a 2000 Hz, paso 10)
    - `mo.ui.slider` para **amplitud** (0.1 a 1.0, paso 0.1)

    La senal debe mostrarse con `plt.plot()`, siempre mostrando exactamente **5 periodos**.
    El titulo del grafico debe mostrar los valores actuales de frecuencia y amplitud.
    """)
    return


@app.cell
def _(mo):
    # === EJERCICIO 9: Crea los sliders aqui ===
    pass
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 9: Grafica reactiva aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Analisis de una senal

    Dado el siguiente array que simula una senal de audio (ya proporcionado), calcula e imprime:

    1. **Duracion** en segundos (asumiendo fs = 44100)
    2. **Amplitud pico** (valor absoluto maximo)
    3. **Valor RMS** (Root Mean Square): $\text{RMS} = \sqrt{\frac{1}{N} \sum_{n=0}^{N-1} |x[n]|^2}$
    4. **RMS en dBFS** (dB Full Scale, referencia = 1.0): $\text{dBFS} = 20 \log_{10}(\text{RMS})$
    5. **Factor de cresta** (Peak / RMS)

    Usa la senal generada en la celda de abajo.
    """)
    return


@app.cell
def _(np):
    # Senal de ejemplo: mezcla de senoidales con ruido
    np.random.seed(42)
    fs_ej10 = 44100
    duracion_ej10 = 2.0
    t_ej10 = np.arange(int(fs_ej10 * duracion_ej10)) / fs_ej10
    audio_ej10 = (0.5 * np.sin(2 * np.pi * 440 * t_ej10) +
                  0.3 * np.sin(2 * np.pi * 880 * t_ej10) +
                  0.05 * np.random.randn(len(t_ej10)))
    return audio_ej10, fs_ej10


@app.cell
def _(audio_ej10, fs_ej10, np):
    # === EJERCICIO 10: Tu codigo aqui ===
    # Usa audio_ej10 y fs_ej10
    pass
    return


if __name__ == "__main__":
    app.run()
