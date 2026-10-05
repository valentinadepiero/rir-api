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
    # Clase 2: Ejercicios Practicos
    ## Hablar en Python

    Resuelve cada ejercicio en la celda indicada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Clasificar frecuencias

    Escribi un condicional que clasifique una frecuencia en las siguientes categorias:

    | Rango (Hz) | Categoria |
    |-----------|-----------|
    | 20 - 60 | Sub-bass |
    | 60 - 250 | Bass |
    | 250 - 4000 | Mid |
    | 4000 - 12000 | Treble |
    | 12000 - 20000 | Ultra-treble |

    Proba con `freq = 880` y con `freq = 35`. Imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    # freq = 880
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Primeros 10 armonicos

    Dado un `fundamental = 220` Hz (A3), crea un bucle `for` que genere e imprima los primeros **10 armonicos**.

    Recordatorio: el armonico N tiene frecuencia = fundamental * N.

    Formato de salida: `"Armonico 1: 220 Hz"`
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
    ### Ejercicio 3: Amplitudes a dB (list comprehension)

    Dada la lista `amplitudes = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]`, crea una list comprehension que convierta cada valor a dB usando la formula:

    $$dB = 20 \times \log_{10}(amplitud)$$

    Necesitas importar `math` y usar `math.log10()`.

    Imprimi cada par (lineal, dB) con formato.
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    # import math
    # amplitudes = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Diccionario de bandas de octava

    Crea un diccionario que mapee las frecuencias centrales de las bandas de octava estandar a su **ancho de banda**. El ancho de banda de una banda de octava es: `bw = fc * (sqrt(2) - 1/sqrt(2))` donde `fc` es la frecuencia central.

    Frecuencias centrales: `[125, 250, 500, 1000, 2000, 4000, 8000]`

    Imprimi el diccionario con formato: `"125 Hz: BW = XX.X Hz"`
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
    ### Ejercicio 5: Filtrar archivos de audio por metadata

    Dada la siguiente lista de diccionarios:

    ```python
    archivos = [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]
    ```

    Usando list comprehension, filtra los archivos que tengan `sr >= 44100`.
    Imprimi los nombres de los archivos que pasan el filtro.
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
    ### Ejercicio 6: Tabla frecuencia x armonico

    Usando bucles anidados, crea una tabla donde:
    - Las filas son frecuencias fundamentales: `[100, 200, 440]`
    - Las columnas son numeros de armonico: `[1, 2, 3, 4, 5]`
    - Cada celda muestra `fundamental * armonico`

    Formato de salida (con alineacion):
    ```
         |     x1     x2     x3     x4     x5
    -----|------------------------------------
     100 |    100    200    300    400    500
     200 |    200    400    600    800   1000
     440 |    440    880   1320   1760   2200
    ```
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
    ### Ejercicio 7: Track listing con enumerate

    Dada la lista:
    ```python
    album = ["Speak to Me", "Breathe", "On the Run", "Time",
             "The Great Gig in the Sky", "Money", "Us and Them",
             "Any Colour You Like", "Brain Damage", "Eclipse"]
    ```

    Usa `enumerate` para imprimir un listado numerado empezando en 1:
    ```
    01. Speak to Me
    02. Breathe
    ...
    ```
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
    ### Ejercicio 8: Stereo pairs con zip

    Dadas las muestras del canal izquierdo y derecho:
    ```python
    left =  [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]
    ```

    Usa `zip` para:
    1. Crear una lista de tuplas `stereo_pairs` con los pares (L, R)
    2. Calcular la senal mono (promedio de L y R) para cada muestra
    3. Imprimi cada muestra: `"Muestra 0: L=+0.50, R=+0.30, Mono=+0.40"`
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
    ### Ejercicio 9: Operaciones con sets

    Dados los sample rates soportados por dos interfaces de audio:
    ```python
    interface_a = {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b = {44100, 48000, 96000}
    ```

    Calcula e imprimi:
    1. Sample rates soportados por **ambas** interfaces
    2. Sample rates soportados por **al menos una** interfaz
    3. Sample rates que tiene la interfaz A pero **no** la B
    4. Si los SR de la interfaz B son un **subconjunto** de los de la A
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
    ### Ejercicio 10: Dict comprehension - Notas y frecuencias

    Crea un diccionario usando **dictionary comprehension** que mapee los nombres de las notas de A3 a A5 a sus frecuencias.

    Datos de entrada:
    ```python
    nombres_notas = ["A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]
    ```

    Formula MIDI a Hz: `f = 440 * 2**((midi - 69) / 12)`

    El diccionario debe ser: `{"A3": 220.0, "B3": 246.94, ...}`
    """)
    return


@app.cell
def _():
    # EJERCICIO 10: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
