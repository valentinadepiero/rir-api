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
    # Clase 7: Ejercicios Practicos
    ## Sistemas y Clasificacion

    Resuelve cada ejercicio en la celda indicada.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Clasificacion de sistemas

    Clasifica los siguientes sistemas segun **todas** sus propiedades (lineal, TI, causal, estable, con memoria). Justifica cada respuesta en comentarios.

    - (a) $y[n] = x[n-5]$ (retardo puro)
    - (b) $y[n] = x[n]^2$ (cuadrador)
    - (c) $y[n] = x[n] + 3$ (offset)
    - (d) $y[n] = x[-n]$ (inversion temporal)

    Completa la tabla en el codigo.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    # Completa la tabla:
    # Sistema          | Lineal | TI  | Causal | Estable | Memoria
    # (a) y[n]=x[n-5]  |  ?     |  ?  |   ?    |    ?    |    ?
    # (b) y[n]=x[n]^2   |  ?     |  ?  |   ?    |    ?    |    ?
    # (c) y[n]=x[n]+3   |  ?     |  ?  |   ?    |    ?    |    ?
    # (d) y[n]=x[-n]    |  ?     |  ?  |   ?    |    ?    |    ?
    #
    # Justifica cada respuesta
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Test numerico de linealidad

    Implementa una funcion `test_linealidad(sistema, x1, x2, a, b)` que:
    1. Calcule $T\{a \cdot x_1 + b \cdot x_2\}$
    2. Calcule $a \cdot T\{x_1\} + b \cdot T\{x_2\}$
    3. Compare ambos resultados
    4. Retorne `True` si el error maximo es menor a $10^{-10}$

    Prueba con estos sistemas:
    - `lambda x: 3 * x` (ganancia)
    - `lambda x: x ** 2` (cuadrador)
    - `lambda x: np.clip(x, -0.5, 0.5)` (clipper)
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    # def test_linealidad(sistema, x1, x2, a, b):
    #     ...
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Test numerico de invarianza temporal

    Implementa una funcion `test_invarianza_temporal(sistema, x, k)` que:
    1. Calcule $y[n] = T\{x[n]\}$
    2. Desplace la entrada: $x_d[n] = x[n-k]$
    3. Calcule $y_d[n] = T\{x_d[n]\}$
    4. Desplace la salida original: $y[n-k]$
    5. Compare $y_d[n]$ con $y[n-k]$
    6. Retorne `True` si son iguales (error < $10^{-10}$)

    Prueba con:
    - Un filtro FIR: `y[n] = x[n] + 0.5*x[n-1]`
    - Un sistema TV: `y[n] = n * x[n]`
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    # def test_invarianza_temporal(sistema, x, k):
    #     ...
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Media movil de 2 muestras

    Dado el sistema **media movil de 2 muestras**:

    $$y[n] = 0.5 \cdot x[n] + 0.5 \cdot x[n-1]$$

    1. Implementa el sistema como funcion
    2. Testa linealidad con tu funcion del Ejercicio 2
    3. Testa invarianza temporal con tu funcion del Ejercicio 3
    4. Encuentra su **respuesta al impulso** (aplica $\delta[n]$ como entrada)
    5. Grafica la respuesta al impulso
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
    ### Ejercicio 5: Sistema de eco

    Implementa un sistema de eco:

    $$y[n] = x[n] + 0.6 \cdot x[n - D]$$

    donde $D$ es el retardo en muestras.

    1. Implementa la funcion `eco(x, D)` para un retardo de 0.3 segundos a 44100 Hz
    2. Clasifica sus propiedades: lineal? TI? causal? estable? con memoria?
    3. Genera un click y aplica el eco. Grafica el resultado.
    4. Calcula la respuesta al impulso y graficala.
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
    ### Ejercicio 6: Hard clipper

    Implementa un **hard clipper** (limitador duro):

    $$y[n] = \begin{cases} T & \text{si } x[n] > T \\ x[n] & \text{si } -T \leq x[n] \leq T \\ -T & \text{si } x[n] < -T \end{cases}$$

    1. Implementa `hard_clipper(x, T)` con umbral $T = 0.5$
    2. Es lineal? Demuestra con codigo usando tu test del Ejercicio 2
    3. Grafica la **curva de transferencia** (entrada vs salida) para ver la no-linealidad
    4. Aplica a una senoidal de amplitud 1.0 y grafica antes/despues
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
    ### Ejercicio 7: Respuesta al impulso de la derivada discreta

    Dado el sistema **derivada discreta**:

    $$y[n] = x[n] - x[n-1]$$

    1. Encuentra su respuesta al impulso $h[n]$ (aplica $\delta[n]$)
    2. Graficala
    3. Cuantas muestras tiene $h[n]$ (antes de que sea cero para siempre)?
    4. Es un sistema FIR o IIR?
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
    ### Ejercicio 8: T60 y decaimiento exponencial

    La respuesta al impulso de una sala se puede modelar como un decaimiento exponencial:

    $$h[n] = e^{-\alpha n / f_s}$$

    donde $\alpha$ es la tasa de decaimiento y $f_s$ es el sample rate.

    El **T60** es el tiempo en que la senal decae 60 dB. Esto significa:

    $$20 \cdot \log_{10}(e^{-\alpha \cdot T_{60}}) = -60 \text{ dB}$$

    1. Despeja $\alpha$ en funcion de $T_{60}$
    2. Calcula $\alpha$ para $T_{60} = 1.5$ segundos
    3. Genera $h[n]$ para $f_s = 44100$ Hz con ese $\alpha$
    4. Grafica $h[n]$ en dB y verifica que decae 60 dB en 1.5 s
    5. Multiplica $h[n]$ por ruido blanco para simular una IR mas realista
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    # Pista: de la ecuacion, alpha = 6.908 / T60
    # (porque -60 dB = 20*log10(e^(-alpha*T60)) -> alpha*T60 = 60/(20*log10(e)) = 6.908)
    return


if __name__ == "__main__":
    app.run()
