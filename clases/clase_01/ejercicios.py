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
    # Clase 1: Ejercicios Practicos
    ## El Punto de Partida

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Total de muestras

    Calcula el **numero total de muestras** para un audio de **3 segundos** grabado a **48000 Hz**.
    Guarda el resultado en una variable llamada `total_muestras` e imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    # duracion = ...
    # sample_rate = ...
    # total_muestras = ...
    # print(...)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Tamano de archivo WAV

    Calcula el **tamano en MB** de un archivo WAV con las siguientes caracteristicas:
    - Estereo (2 canales)
    - Bit depth: 16 bits
    - Sample rate: 44100 Hz
    - Duracion: 5 segundos

    Formula: `tamano_bytes = sample_rate * duracion * canales * (bit_depth / 8)`

    Guarda el resultado en `tamano_mb` e imprimi con 2 decimales.
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
    ### Ejercicio 3: Convertir segundos a mm:ss

    Dada una duracion en segundos (`duracion_seg = 197`), convertila al formato **mm:ss** usando los operadores `//` y `%`.

    El resultado debe ser un string como `"3:17"`.
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    # duracion_seg = 197
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Extraer extension de archivo

    Dado el nombre de archivo `nombre = "mi_cancion_final_v2.wav"`, extraer:
    1. La **extension** (sin el punto): `"wav"`
    2. El **nombre sin extension**: `"mi_cancion_final_v2"`

    Usa metodos de strings (`.split()`, slicing, etc.).
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca
    # nombre = "mi_cancion_final_v2.wav"
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Frecuencia de una nota MIDI

    La formula para convertir un numero de nota MIDI a frecuencia en Hz es:

    $$f = 440 \times 2^{(midi - 69) / 12}$$

    Calcula la frecuencia de las siguientes notas MIDI:
    - **60** (Do central / Middle C)
    - **69** (La 440 / A4)
    - **72** (Do una octava arriba / C5)

    Imprimi cada resultado con 2 decimales.
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
    ### Ejercicio 6: f-string descriptivo

    Crea las siguientes variables:
    - `titulo = "Bohemian Rhapsody"`
    - `artista = "Queen"`
    - `duracion_seg = 354`
    - `sample_rate = 44100`
    - `bit_depth = 24`

    Usando f-strings, crea un string `info` que muestre:
    ```
    Pista: Bohemian Rhapsody - Queen
    Duracion: 5:54
    Formato: 44,100 Hz / 24 bits
    Total muestras: 15,609,400
    ```
    Imprimi el resultado.
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
    ### Ejercicio 7: Logica booleana para calidad de audio

    Crea las variables:
    - `sr = 48000` (sample rate)
    - `bits = 24` (bit depth)
    - `canales = 2` (numero de canales)

    Determina (como booleanos):
    1. `es_profesional`: el sample rate es >= 44100 **Y** el bit depth es >= 16
    2. `es_hd`: el sample rate es >= 96000 **O** el bit depth es >= 24
    3. `es_surround`: el numero de canales es > 2
    4. `calidad_ok`: es profesional **Y NO** es surround (estereo profesional)

    Imprimi cada resultado.
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
    ### Ejercicio 8: Frecuencia de Nyquist

    La **frecuencia de Nyquist** es la maxima frecuencia que se puede representar con un sample rate dado.
    Se calcula como: `f_nyquist = sample_rate / 2`

    Para los siguientes sample rates, calcula e imprimi la frecuencia de Nyquist:
    - 22050 Hz
    - 44100 Hz
    - 48000 Hz
    - 96000 Hz
    - 192000 Hz

    Imprimi en formato: `"SR: 44100 Hz -> Nyquist: 22050.0 Hz"`
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
    ### Ejercicio BONUS: Calculadora de latencia

    La **latencia** de un buffer de audio se calcula como:

    $$latencia_{ms} = \frac{buffer\_size}{sample\_rate} \times 1000$$

    Calcula la latencia para las siguientes combinaciones:
    - Buffer: 64, SR: 44100
    - Buffer: 128, SR: 44100
    - Buffer: 256, SR: 48000
    - Buffer: 512, SR: 96000

    Imprimi cada resultado con 2 decimales en formato:
    `"Buffer: 64 @ 44100 Hz -> Latencia: X.XX ms"`
    """)
    return


@app.cell
def _():
    # EJERCICIO BONUS: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
