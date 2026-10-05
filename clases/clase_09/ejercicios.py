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
    # Clase 9: Ejercicios Practicos
    ## Frecuencia y Filtros

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import signal
    from scipy.fft import rfft, rfftfreq
    return np, plt, signal, rfft, rfftfreq


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: FFT de un tono de 440 Hz

    Genera un tono puro de **440 Hz** (1 segundo, fs=44100).
    Calcula la FFT y grafica el espectro de **magnitud en dB** (solo frecuencias positivas).

    Usa `rfft` y la formula: $\text{dB} = 20 \log_{10}(|X|)$

    Verifica que el pico este en 440 Hz.
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
    ### Ejercicio 2: FFT de senal con 3 frecuencias

    Genera una senal que sea la suma de 3 sinusoides:
    - 200 Hz con amplitud 1.0
    - 500 Hz con amplitud 0.5
    - 1200 Hz con amplitud 0.3

    Duracion 1s, fs=44100. Calcula la FFT e identifica los 3 picos.
    Grafica el espectro de magnitud y marca los picos con lineas verticales.
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
    ### Ejercicio 3: Fuga espectral

    Genera un tono de **100.5 Hz** (frecuencia que no encaja en la grilla FFT para 1 segundo).

    Compara la FFT **sin ventana** vs **con ventana Hanning**.

    Grafica ambos espectros superpuestos (zoom en 50-150 Hz) y explica la diferencia.
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
    ### Ejercicio 4: Espectro del ruido rosa

    Genera **ruido rosa** de 2 segundos (puedes partir de ruido blanco y filtrar con $1/\sqrt{f}$).

    Calcula el espectro y verifica que la pendiente es **-3 dB/octava**.

    **Pista**: grafica en escala log-log y ajusta una recta con `np.polyfit` sobre las frecuencias en escala log.
    Verifica que la pendiente es cercana a -3 dB/octava (o -10 dB/decada).
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
    ### Ejercicio 5: Filtro pasa-bajos Butterworth

    Disena un filtro **Butterworth pasa-bajos** de orden 6 con frecuencia de corte **1 kHz** (fs=44100).

    1. Genera ruido blanco de 2 segundos
    2. Aplica el filtro con `sosfilt`
    3. Grafica los espectros del ruido original y filtrado superpuestos
    4. Grafica la respuesta en frecuencia del filtro con `sosfreqz`
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
    ### Ejercicio 6: Filtro pasa-banda para 1 kHz

    Disena un filtro pasa-banda centrado en **1 kHz** con ancho de una octava:
    - $f_{low} = 1000 / \sqrt{2} \approx 707$ Hz
    - $f_{high} = 1000 \cdot \sqrt{2} \approx 1414$ Hz

    Orden 4, fs=44100.

    1. Grafica la respuesta en frecuencia
    2. Aplica a ruido blanco y grafica el espectro resultante
    3. Verifica que el ancho de banda a -3 dB sea correcto
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
    ### Ejercicio 7: Banco de filtros de octava completo

    Implementa un banco de filtros de octava para las frecuencias centrales de **125 Hz a 8000 Hz**:
    [125, 250, 500, 1000, 2000, 4000, 8000]

    1. Crea una funcion `banco_octavas(x, fs)` que retorne un diccionario `{fc: senal_filtrada}`
    2. Grafica todas las respuestas en frecuencia superpuestas
    3. Aplica a ruido blanco y grafica la energia (RMS en dB) por banda
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
    ### Ejercicio 8: Espectrograma de sine sweep

    Genera un **sine sweep logaritmico** de 20 Hz a 20 kHz de 5 segundos (fs=44100).

    Usa `scipy.signal.chirp` con `method='logarithmic'`.

    Calcula y grafica el espectrograma. Deberia verse una linea diagonal.

    Experimenta con distintos valores de `nperseg` (256, 1024, 4096) y observa como cambia la resolucion.
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Energia por banda de ruido rosa

    Genera ruido rosa de 5 segundos. Filtra por bandas de octava (125-8000 Hz).

    Calcula la **energia RMS en dB** por banda y grafica un grafico de barras.

    Para ruido rosa, la energia por banda de octava deberia ser **aproximadamente constante** (cada banda tiene el mismo ancho relativo y el ruido rosa compensa con -3 dB/oct).

    Compara con el resultado para ruido blanco (ejercicio 7).
    """)
    return


@app.cell
def _():
    # EJERCICIO 9: Tu codigo aca
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Analizador de frecuencia interactivo

    Crea un analizador interactivo con dos sliders:
    - **Frecuencia 1** (100-5000 Hz)
    - **Frecuencia 2** (100-5000 Hz)

    La senal es la suma de dos sinusoides con esas frecuencias.

    Muestra lado a lado:
    1. La senal en el tiempo (primeros 20 ms)
    2. El espectro de magnitud

    **Pista**: usa `mo.ui.slider` para crear los controles.
    """)
    return


@app.cell
def _():
    # EJERCICIO 10: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
