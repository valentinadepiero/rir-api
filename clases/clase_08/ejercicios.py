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
    # Clase 8: Ejercicios Practicos
    ## Convolucion + Entrega 1

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
    ### Ejercicio 1: Convolucion manual

    Calcula **a mano** la convolucion de $x = [1, 2, 3]$ con $h = [1, 0, -1]$.

    Escribe el calculo paso a paso para cada valor de $n$ (de 0 a 4).
    Luego verifica tu resultado con `np.convolve`.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    # Calcula a mano y luego verifica:
    # y[0] = ...
    # y[1] = ...
    # y[2] = ...
    # y[3] = ...
    # y[4] = ...
    #
    # Verificar:
    # y = np.convolve([1, 2, 3], [1, 0, -1])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Convolucion desde cero

    Implementa la convolucion discreta **usando loops** (sin usar `np.convolve`):

    ```python
    def mi_convolucion(x, h):
        # Tu implementacion
        ...
        return y
    ```

    Verifica que tu resultado coincida con `np.convolve` para al menos 3 pares de senales diferentes.
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    # def mi_convolucion(x, h):
    #     ...
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Propiedad de identidad

    Verifica la propiedad de identidad de la convolucion:

    $$x[n] * \delta[n] = x[n]$$

    1. Crea una senal $x$ arbitraria (ej: `np.array([1, -2, 3, 0, 5, -1])`)
    2. Crea un impulso unitario $\delta$ = `np.array([1.0])`
    3. Convoluciona y verifica que el resultado es igual a $x$
    4. Ahora prueba con un impulso desplazado: $\delta[n-3]$ = `np.array([0, 0, 0, 1.0])`
    5. Que obtenes? Que significa esto fisicamente?
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
    ### Ejercicio 4: Convolucion de pulsos rectangulares

    1. Crea un pulso rectangular de 10 muestras: $x_1[n] = 1$ para $0 \leq n \leq 9$, 0 en otro caso
    2. Crea otro pulso rectangular de 5 muestras: $x_2[n] = 1$ para $0 \leq n \leq 4$
    3. Convoluciona $x_1 * x_2$
    4. Grafica las tres senales
    5. Que forma tiene el resultado? Por que?
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
    ### Ejercicio 5: Efecto de eco por convolucion

    Crea un efecto de eco usando convolucion. La respuesta al impulso del eco es:

    $$h[n] = \delta[n] + 0.5 \cdot \delta[n - D]$$

    donde $D$ es el retardo en muestras.

    1. Calcula $D$ para un retardo de **0.3 segundos** a 44100 Hz
    2. Construye $h[n]$ como un array con el impulso y su eco
    3. Genera una senal de prueba (un click corto o un tono de 0.1 s)
    4. Aplica el eco por convolucion: `y = np.convolve(senal, h)`
    5. Grafica la senal original y la senal con eco
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
    ### Ejercicio 6: Comparacion de rendimiento

    Compara el tiempo de ejecucion de:
    - `np.convolve(x, h)`
    - `scipy.signal.fftconvolve(x, h)`

    Para senales de **44100 muestras** cada una (1 segundo de audio a 44100 Hz).

    1. Genera dos senales aleatorias de 44100 muestras
    2. Mide el tiempo de cada metodo (usa `time.perf_counter()`)
    3. Verifica que los resultados sean iguales (o casi iguales)
    4. Calcula el speedup (cuantas veces mas rapido es fftconvolve)
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca
    # import time
    # from scipy.signal import fftconvolve
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: IR sintetica de sala

    Genera una respuesta al impulso sintetica de una sala:
    1. **Sonido directo**: impulso en $n=0$ con amplitud 1.0
    2. **Reflexiones tempranas**: 5 impulsos a tiempos aleatorios entre 10-80 ms, con amplitudes decrecientes
    3. **Cola reverberante**: ruido blanco multiplicado por una envolvente exponencial con $T_{60} = 1.0$ s

    Convoluciona esta IR con un click y grafica:
    - La IR
    - El click original
    - El click convolucionado (debe sonar como un click con reverb)
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
    ### Ejercicio 8: Deconvolucion basica

    Dadas dos senales conocidas $x$ y $h$:
    1. Calcula $y = x * h$ (convolucion)
    2. Recupera $h$ a partir de $y$ y $x$ usando deconvolucion por FFT:

    $$H[k] = \frac{Y[k]}{X[k]}$$
    $$h_{\text{recuperada}}[n] = \text{IFFT}(H[k])$$

    3. Compara $h$ original con $h$ recuperada
    4. Calcula el error

    Usa estas senales de prueba:
    - $x$: barrido de senos corto (0.1 s)
    - $h$: `[1, 0.5, -0.3, 0.1]`

    **Pista**: agrega un pequeno $\epsilon$ al denominador para evitar division por cero:
    `H = Y / (X + epsilon)`
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
