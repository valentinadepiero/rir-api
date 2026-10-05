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
    # Clase 5: Ejercicios practicos
    ## Operaciones con Senales

    Completa cada ejercicio en la celda indicada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Desplazamiento temporal

    Dada la senal $x[n] = [1, 2, 3, 4, 5]$ definida para $n = 0, 1, 2, 3, 4$:

    1. Computa $x[n - 2]$ (desplazamiento a la derecha por 2)
    2. Grafica ambas senales con `stem` en un mismo grafico, usando diferentes colores
    3. El eje $n$ debe ir de -2 a 8 para que se vean ambas
    4. Agrega una leyenda

    **Tip**: para $x[n-2]$, la senal original que empieza en $n=0$ ahora empieza en $n=2$.
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 1: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Inversion temporal

    Genera una senoidal de **440 Hz** durante **1 segundo** a 44100 Hz.

    1. Crea la senal invertida $x[-n]$ usando slicing de NumPy (`x[::-1]`)
    2. Grafica ambas en 2 subplots verticales (muestra solo los primeros 5 ms)
    3. Describi en un comentario: si reprodujeras la senal invertida, que escucharias?
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
    ### Ejercicio 3: Mezcla de senoidales (tercera mayor)

    Genera dos senoidales:
    - 440 Hz (La4) con amplitud 0.5
    - 554.37 Hz (Do#5, tercera mayor) con amplitud 0.5

    Ambas a 44100 Hz, duracion 20 ms.

    1. Suma ambas senales
    2. Grafica las dos originales y la suma en 3 subplots
    3. En un comentario, explica que se escucharia al reproducir la suma (un acorde consonante)
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
    ### Ejercicio 4: Modulacion AM (tremolo)

    Implementa un efecto de **tremolo**:

    1. Genera una portadora de 440 Hz, duracion 500 ms, fs = 44100
    2. Genera una moduladora de 5 Hz: $m[n] = 0.5 + 0.5 \sin(2\pi \cdot 5 \cdot n/f_s)$ (rango 0 a 1)
    3. Multiplica portadora por moduladora
    4. Grafica el resultado completo y la envolvente (moduladora) superpuesta
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
    ### Ejercicio 5: Interferencia constructiva y destructiva

    Crea dos senoidales de **1000 Hz** a 44100 Hz, duracion 5 ms.

    1. Grafica la suma para tres valores de fase: $\phi = 0$, $\phi = \pi/2$, $\phi = \pi$
    2. Usa 3 subplots
    3. Calcula y muestra la amplitud pico de la suma en cada caso
    4. Titulo de cada subplot: indica el tipo de interferencia

    Recordatorio: $x_1 = \sin(2\pi f t)$, $x_2 = \sin(2\pi f t + \phi)$
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
    ### Ejercicio 6: Periodicidad

    Determina si las siguientes frecuencias son **exactamente periodicas** a $f_s = 44100$ Hz:

    - 441 Hz
    - 440 Hz
    - 1000 Hz
    - 882 Hz

    Para cada una:
    1. Calcula $f_0 / f_s$ como fraccion irreducible (usa `fractions.Fraction`)
    2. Determina el periodo fundamental $N$ (denominador de la fraccion)
    3. Indica si el periodo es "practico" (< 1000 muestras) o "muy largo"
    4. Imprime los resultados en una tabla formateada
    """)
    return


@app.cell
def _(np):
    # === EJERCICIO 6: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Energia y potencia

    Calcula la energia y potencia de las siguientes senales (todas a 44100 Hz):

    - (a) Impulso unitario $\delta[n]$ (1000 muestras, impulso en $n=0$)
    - (b) Senoidal de 440 Hz, amplitud 1.0, duracion 1 segundo
    - (c) Silencio: 1 segundo de ceros

    Imprime una tabla con: Energia, Potencia, RMS, RMS en dBFS.

    Formulas:
    - $E = \sum |x[n]|^2$
    - $P = \frac{1}{N} \sum |x[n]|^2$
    - $\text{RMS} = \sqrt{P}$
    - $\text{dBFS} = 20 \log_{10}(\text{RMS})$
    """)
    return


@app.cell
def _(np):
    # === EJERCICIO 7: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Conversion a dBFS

    Dada la senal $x[n] = 0.5 \sin(2\pi \cdot 440 \cdot n / f_s)$ con $f_s = 44100$, duracion 1 segundo:

    1. Calcula el valor RMS
    2. Convierte a dBFS (referencia = 1.0)
    3. Verifica analitica: para una senoidal de amplitud $A$, $\text{RMS} = A / \sqrt{2}$
    4. Verifica: $\text{dBFS} = 20 \log_{10}(A/\sqrt{2})$
    5. Imprime el resultado numerico y la verificacion analitica
    """)
    return


@app.cell
def _(np):
    # === EJERCICIO 8: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Fade-in lineal

    Crea un efecto de **fade-in** (aparicion gradual):

    1. Genera un tono de 440 Hz, duracion 2 segundos, amplitud 0.8, fs = 44100
    2. Crea una envolvente de fade-in: va de 0 a 1 linealmente durante los primeros 500 ms, luego se mantiene en 1
    3. Multiplica el tono por la envolvente
    4. Grafica: el tono original, la envolvente, y el resultado, en 3 subplots
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 9: Tu codigo aqui ===
    pass
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Crossfade entre dos senales

    Implementa un **crossfade** (transicion suave) entre dos senales:

    - Senal A: tono de 440 Hz, duracion 1 segundo
    - Senal B: tono de 660 Hz, duracion 1 segundo
    - Crossfade: 100 ms de transicion

    El crossfade funciona asi:
    1. Durante la zona de crossfade, la Senal A se atenua linealmente de 1 a 0
    2. Simultaneamente, la Senal B se atenua linealmente de 0 a 1
    3. La salida es la suma de ambas senales atenuadas

    La senal total debe durar: `duracion_A + duracion_B - duracion_crossfade`

    Grafica la senal resultante completa. Marca la zona de crossfade con un fondo sombreado.
    """)
    return


@app.cell
def _(np, plt):
    # === EJERCICIO 10: Tu codigo aqui ===
    pass
    return


if __name__ == "__main__":
    app.run()
