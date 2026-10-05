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
    # Clase 3: Ejercicios Practicos
    ## Construir con Funciones

    En estos ejercicios vas a crear funciones completas con docstrings, type hints, y (en algunos casos) tests.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: midi_a_hz

    Escribi una funcion `midi_a_hz(nota_midi)` que convierta un numero de nota MIDI a frecuencia en Hz.

    **Requisitos:**
    - Formula: `f = 440 * 2**((midi - 69) / 12)`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `nota_midi` no esta entre 0 y 127, lanzar `ValueError`

    Proba con MIDI 60, 69, 72, y 48.
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
    ### Ejercicio 2: hz_a_midi

    Escribi la funcion inversa: `hz_a_midi(frecuencia)` que convierta una frecuencia en Hz al numero de nota MIDI mas cercano.

    **Requisitos:**
    - Formula: `midi = round(69 + 12 * log2(freq / 440))`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `frecuencia <= 0`, lanzar `ValueError`
    - Necesitas `import math` y usar `math.log2()`

    Proba con 440 Hz, 261.63 Hz, 880 Hz.
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
    ### Ejercicio 3: aplicar_fade

    Escribi una funcion `aplicar_fade(signal, tipo="in", duracion_ms=100, fs=44100)` que aplique un fade lineal a una senal.

    **Requisitos:**
    - `tipo` puede ser `"in"` (fade in) o `"out"` (fade out)
    - El fade es **lineal**: multiplica las muestras por un factor que va de 0 a 1 (fade in) o de 1 a 0 (fade out)
    - `duracion_ms` indica cuantos milisegundos dura el fade
    - La funcion retorna una **nueva lista** (no modifica la original)
    - Docstring y type hints

    **Ejemplo de fade in de 4 muestras sobre 8 muestras:**
    ```
    Original: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    Factores: [0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    Resultado:[0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    ```
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
    ### Ejercicio 4: mezclar_senales

    Escribi una funcion `mezclar_senales(*signals, pesos=None)` que mezcle multiples senales.

    **Requisitos:**
    - Recibe un numero variable de senales (listas de floats) via `*signals`
    - Si `pesos` es `None`, todas las senales tienen el mismo peso (1/N)
    - Si `pesos` es una lista, cada senal se multiplica por su peso correspondiente
    - Todas las senales deben tener la misma longitud
    - Retorna la mezcla como una nueva lista
    - Docstring y type hints

    **Ejemplo:**
    ```python
    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]
    mezclar_senales(a, b)                  # -> [0.5, 0.75, -0.25]
    mezclar_senales(a, b, pesos=[0.8, 0.2]) # -> [0.8, 0.6, -0.4]
    ```
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
    ### Ejercicio 5: info_audio

    Escribi una funcion `info_audio(nombre, sr=44100, **kwargs)` que retorne un string formateado con informacion del archivo de audio.

    **Requisitos:**
    - Siempre muestra nombre y sample rate
    - Cualquier parametro adicional (**kwargs) tambien se muestra
    - Retorna un string (no imprime directamente)
    - Docstring y type hints

    **Ejemplo de uso:**
    ```python
    info_audio("cancion.wav", sr=48000, bits=24, canales=2, artista="Queen")
    ```
    **Resultado:**
    ```
    === cancion.wav ===
    Sample Rate: 48,000 Hz
    bits: 24
    canales: 2
    artista: Queen
    ```
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
    ### Ejercicio 6: Crear un modulo

    Este ejercicio es para hacer **fuera del notebook**, en un archivo separado.

    Crea un archivo llamado `mis_funciones.py` que contenga:

    1. `midi_a_hz(nota_midi)` - del ejercicio 1
    2. `hz_a_midi(frecuencia)` - del ejercicio 2
    3. `calcular_rms(signal)` - calcula el RMS de una lista de muestras

    Cada funcion debe tener docstring y type hints.

    Agrega un bloque `if __name__ == "__main__":` que demuestre el uso de cada funcion.

    Despues de crearlo, verifica que funciona:
    ```bash
    python mis_funciones.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    (Este ejercicio se resuelve creando el archivo. En la celda siguiente, simula la importacion.)
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Simula aca las funciones que pondrias en el modulo
    # y mostra que funcionan
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Tests para midi_a_hz

    Escribi **3 funciones de test** para la funcion `midi_a_hz` del ejercicio 1.

    Los tests deben seguir el formato de pytest (funciones que empiezan con `test_`):

    1. `test_midi_a_hz_a4()` - verifica que MIDI 69 retorna 440.0
    2. `test_midi_a_hz_octavas()` - verifica que subir 12 semitonos duplica la frecuencia
    3. `test_midi_a_hz_rango_invalido()` - verifica que MIDI -1 o 128 lanza ValueError

    Para el test 3, usa un bloque `try/except`:
    ```python
    try:
        midi_a_hz(-1)
        assert False, "Deberia haber lanzado ValueError"
    except ValueError:
        pass  # OK, se espera el error
    ```

    Ejecuta todos los tests y muestra los resultados.
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
    ### Ejercicio 8: normalizar con tests

    Escribi una funcion `normalizar(signal)` que normalice una senal al rango [-1, 1].

    **Requisitos:**
    - Encuentra el valor absoluto maximo de la senal
    - Divide todas las muestras por ese valor
    - Si la senal es toda ceros, retorna la senal sin cambios
    - Docstring, type hints

    Ademas, escribi **3 tests**:
    1. `test_normalizar_basico()` - una senal con pico en 0.5 debe tener pico en 1.0
    2. `test_normalizar_ya_normalizada()` - una senal con pico en 1.0 no cambia
    3. `test_normalizar_silencio()` - una senal de ceros retorna ceros

    Ejecuta los tests y muestra resultados.
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca
    return


if __name__ == "__main__":
    app.run()
