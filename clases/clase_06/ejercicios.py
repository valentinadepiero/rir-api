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
    # Clase 6: Ejercicios Practicos
    ## Audio en Python + Generacion de Senales

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
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
    ### Ejercicio 1: Tono puro

    Genera un tono puro (senoidal) de **440 Hz** con las siguientes caracteristicas:
    - Duracion: **1 segundo**
    - Sample rate: **44100 Hz**
    - Amplitud: **0.5**

    Guardalo como archivo WAV en `/tmp/ej1_tono_440.wav` usando `soundfile`.
    Grafica los primeros **10 ms** de la senal.
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
    ### Ejercicio 2: Audio estereo

    Genera un archivo WAV **estereo** de **2 segundos** a 44100 Hz:
    - **Canal izquierdo**: senoidal de 440 Hz
    - **Canal derecho**: senoidal de 880 Hz

    Amplitud de 0.5 en ambos canales. Guardalo en `/tmp/ej2_estereo.wav`.

    **Pista**: un array estereo tiene shape `(n_muestras, 2)`. Usa `np.column_stack()`.
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
    ### Ejercicio 3: Ruido blanco normalizado

    Genera **3 segundos** de ruido blanco a 44100 Hz:
    1. Usa `np.random.randn()` para generar las muestras
    2. **Normaliza** para que el pico maximo sea exactamente **0.8**
    3. Guarda como `/tmp/ej3_ruido.wav`
    4. Imprime: valor pico, valor RMS, y crea un histograma de la distribucion

    **Nota**: RMS = $\sqrt{\frac{1}{N}\sum_{n=0}^{N-1} x[n]^2}$
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
    ### Ejercicio 4: Tonos DTMF

    Los tonos **DTMF** (*Dual-Tone Multi-Frequency*) son los que genera un telefono al marcar.
    Cada digito es la suma de dos frecuencias:

    |       | 1209 Hz | 1336 Hz | 1477 Hz |
    |-------|---------|---------|---------|
    | **697 Hz** | 1 | 2 | 3 |
    | **770 Hz** | 4 | 5 | 6 |
    | **852 Hz** | 7 | 8 | 9 |
    | **941 Hz** | * | 0 | # |

    Genera una secuencia de tonos DTMF para los digitos **1 a 9**:
    - Cada tono dura **0.2 segundos**
    - Silencio de **0.1 segundos** entre tonos
    - Sample rate: 44100 Hz
    - Amplitud: 0.3 por cada frecuencia

    Concatena todo y guarda como `/tmp/ej4_dtmf.wav`.
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca
    # Pista: crea un diccionario con las frecuencias de cada digito
    # dtmf = {
    #     '1': (697, 1209),
    #     '2': (697, 1336),
    #     ...
    # }
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Analisis de archivo WAV

    Lee el archivo `/tmp/ej4_dtmf.wav` (o genera uno nuevo si no existe) y calcula:
    1. **Duracion** en segundos
    2. **Cantidad de canales**
    3. **Sample rate**
    4. **Tipo de datos** (dtype)
    5. **Nivel pico en dBFS**: $\text{dBFS} = 20 \cdot \log_{10}(\text{pico})$

    Imprime toda la informacion en un formato legible.
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
    ### Ejercicio 6: Control de volumen

    Implementa una funcion `control_volumen(senal, ganancia_db)` que:
    1. Convierte la ganancia de dB a lineal: $g = 10^{ganancia_{dB}/20}$
    2. Multiplica la senal por la ganancia
    3. Aplica **clipping** para que los valores queden en $[-1.0, 1.0]$
    4. Retorna la senal procesada

    Prueba con un tono de 440 Hz y ganancias de: -6 dB, 0 dB, +6 dB, +20 dB.
    Grafica todas las versiones superpuestas (primeros 5 ms).
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca
    # def control_volumen(senal, ganancia_db):
    #     ...
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Barrido de senos (sine sweep)

    Genera un **barrido de senos logaritmico** de 5 segundos:
    - Frecuencia inicial: **20 Hz**
    - Frecuencia final: **20000 Hz**
    - Sample rate: 44100 Hz

    La formula para un barrido logaritmico es:

    $$x(t) = \sin\left(2\pi f_1 \frac{T}{\ln(f_2/f_1)} \left(e^{t \ln(f_2/f_1)/T} - 1\right)\right)$$

    donde $T$ es la duracion total, $f_1$ y $f_2$ las frecuencias inicial y final.

    Guarda como `/tmp/ej7_sweep.wav` y grafica 3 zooms: inicio, medio, y final.
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
    ### Ejercicio 8: Reproduccion y grabacion simultanea (concepto)

    Este ejercicio es **conceptual** (no requiere hardware de audio).

    Usando `sounddevice`, explica y escribe el codigo (comentado) para:
    1. Generar un barrido de senos de 3 segundos
    2. Reproducirlo por los parlantes y grabar simultaneamente con el microfono usando `sd.playrec()`
    3. Guardar tanto la senal emitida como la grabada

    Responde estas preguntas en comentarios:
    - Que pasa si el sample rate del `playrec` no coincide con el del dispositivo?
    - Que efecto tiene el `blocksize` (tamano del buffer) en la latencia?
    - Por que es importante usar `sd.playrec()` en vez de `sd.play()` + `sd.rec()` por separado?
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca (puede estar comentado)
    return


if __name__ == "__main__":
    app.run()
