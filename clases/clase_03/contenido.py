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
    # Senales y Sistemas - Practica 2026
    ## Clase 3: Construir con Funciones

    Hoy vamos a aprender a **organizar** nuestro codigo en funciones reutilizables, documentarlas correctamente, y dar los primeros pasos en **testing**.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Funciones: fundamentos

    Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.

    ```python
    def nombre_funcion(parametros):
        # cuerpo de la funcion
        return resultado
    ```
    """)
    return


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(math):
    # Funcion basica: generar muestras de una senoidal
    def generar_senoidal(frecuencia, duracion, amplitud=1.0, fs=44100):
        """Genera muestras de una senal senoidal."""
        n_muestras = int(fs * duracion)
        muestras = []
        for i in range(n_muestras):
            t = i / fs
            muestra = amplitud * math.sin(2 * math.pi * frecuencia * t)
            muestras.append(muestra)
        return muestras

    # Usar la funcion
    senal = generar_senoidal(440, 0.01)  # 440 Hz, 10 ms
    print(f"Generamos {len(senal)} muestras de una senoidal de 440 Hz")
    print(f"Primeras 10 muestras: {[f'{m:.4f}' for m in senal[:10]]}")
    return (generar_senoidal,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Parametros posicionales, keyword y por defecto

    - **Posicionales**: se pasan en orden
    - **Keyword**: se pasan por nombre
    - **Por defecto**: tienen un valor predefinido si no se pasan
    """)
    return


@app.cell
def _(generar_senoidal):
    # Diferentes formas de llamar a la funcion
    s1 = generar_senoidal(440, 0.001)                       # posicional
    s2 = generar_senoidal(440, 0.001, amplitud=0.5)         # keyword
    s3 = generar_senoidal(frecuencia=880, duracion=0.001)   # todo keyword
    s4 = generar_senoidal(440, 0.001, 0.5, 48000)           # todo posicional

    print(f"s1: {len(s1)} muestras (440 Hz, amp=1.0, fs=44100)")
    print(f"s2: {len(s2)} muestras (440 Hz, amp=0.5, fs=44100)")
    print(f"s3: {len(s3)} muestras (880 Hz, amp=1.0, fs=44100)")
    print(f"s4: {len(s4)} muestras (440 Hz, amp=0.5, fs=48000)")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### *args: numero variable de argumentos posicionales

    Cuando no sabemos cuantos argumentos va a recibir una funcion, usamos `*args`. Los argumentos se reciben como una tupla.
    """)
    return


@app.cell
def _():
    # *args: mezclar multiples senales
    def mezclar(*senales):
        """Mezcla multiples senales sumandolas muestra a muestra.

        Todas las senales deben tener la misma longitud.
        """
        if not senales:
            return []

        longitud = len(senales[0])
        mezcla = [0.0] * longitud

        for senal in senales:
            for i in range(longitud):
                mezcla[i] += senal[i]

        # Normalizar para evitar clipping
        n_senales = len(senales)
        mezcla = [m / n_senales for m in mezcla]
        return mezcla

    # Ejemplo
    s_a = [0.5, 0.3, -0.2, 0.8]
    s_b = [0.1, -0.4, 0.6, -0.3]
    s_c = [0.3, 0.2, 0.1, 0.0]

    resultado = mezclar(s_a, s_b, s_c)
    print(f"Senal A: {s_a}")
    print(f"Senal B: {s_b}")
    print(f"Senal C: {s_c}")
    print(f"Mezcla:  {[f'{m:.3f}' for m in resultado]}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### **kwargs: argumentos keyword variables

    Con `**kwargs` recibimos argumentos con nombre como un diccionario. Util para funciones con muchas opciones configurables.
    """)
    return


@app.cell
def _():
    # **kwargs: configuracion flexible de audio
    def crear_configuracion(nombre, sr=44100, **kwargs):
        """Crea un diccionario de configuracion de audio.

        Parameters
        ----------
        nombre : str
            Nombre de la configuracion.
        sr : int
            Sample rate (default 44100).
        **kwargs
            Opciones adicionales (bit_depth, canales, formato, etc.)
        """
        config = {
            "nombre": nombre,
            "sample_rate": sr,
        }
        # Agregar todas las opciones extra
        config.update(kwargs)
        return config

    # Uso con diferentes niveles de detalle
    config_basica = crear_configuracion("Grabacion simple")
    config_completa = crear_configuracion(
        "Master final",
        sr=96000,
        bit_depth=32,
        canales=2,
        formato="WAV",
        dither=True,
        normalizacion=-0.3,
    )

    print("Config basica:")
    for k, v in config_basica.items():
        print(f"  {k}: {v}")

    print("\nConfig completa:")
    for k, v in config_completa.items():
        print(f"  {k}: {v}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Docstrings (estilo NumPy)

    Los **docstrings** documentan que hace una funcion, que parametros recibe, y que retorna. Usamos el estilo **NumPy** porque es muy legible y es el estandar en ciencia e ingenieria.
    """)
    return


@app.cell
def _(math):
    def calcular_rms(signal):
        """Calcula el valor RMS (Root Mean Square) de una senal.

        El valor RMS es una medida de la "potencia" promedio de una senal.
        Se calcula como la raiz cuadrada del promedio de los cuadrados
        de las muestras.

        Parameters
        ----------
        signal : list[float]
            Senal de entrada como lista de muestras.

        Returns
        -------
        float
            Valor RMS de la senal.

        Examples
        --------
        >>> calcular_rms([1.0, -1.0, 1.0, -1.0])
        1.0
        >>> calcular_rms([0.0, 0.0, 0.0])
        0.0
        """
        if not signal:
            return 0.0
        suma_cuadrados = sum(m ** 2 for m in signal)
        return math.sqrt(suma_cuadrados / len(signal))

    # Ejemplo de uso
    senal_ejemplo = [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4, -0.1]
    rms = calcular_rms(senal_ejemplo)
    rms_db = 20 * math.log10(rms) if rms > 0 else float('-inf')

    print(f"Senal: {senal_ejemplo}")
    print(f"RMS: {rms:.4f} ({rms_db:.1f} dB)")

    # Ver el docstring
    print(f"\nDocstring de la funcion:\n{calcular_rms.__doc__}")
    return (calcular_rms,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Type Hints

    Los **type hints** indican que tipo de datos espera y retorna una funcion. No son obligatorios en Python, pero mejoran la legibilidad y permiten que herramientas detecten errores.
    """)
    return


@app.cell
def _(math):
    def generar_senoidal_tipada(
        frecuencia: float,
        duracion: float,
        amplitud: float = 1.0,
        fs: int = 44100,
    ) -> list[float]:
        """Genera muestras de una senal senoidal.

        Parameters
        ----------
        frecuencia : float
            Frecuencia de la senoidal en Hz.
        duracion : float
            Duracion de la senal en segundos.
        amplitud : float, optional
            Amplitud pico (default 1.0).
        fs : int, optional
            Frecuencia de muestreo en Hz (default 44100).

        Returns
        -------
        list[float]
            Lista de muestras de la senoidal.
        """
        n_muestras = int(fs * duracion)
        return [
            amplitud * math.sin(2 * math.pi * frecuencia * (i / fs))
            for i in range(n_muestras)
        ]

    # Con type hints, es muy claro que tipo de datos espera
    senal_tipada = generar_senoidal_tipada(440.0, 0.005, amplitud=0.8)
    print(f"Generamos {len(senal_tipada)} muestras con type hints")
    return


@app.cell
def _(mo):
    mo.md(r"""
    Algunos type hints comunes:

    ```python
    def funcion_a(x: int) -> str:              # recibe int, retorna str
    def funcion_b(datos: list[float]) -> float: # recibe lista de floats
    def funcion_c(config: dict[str, int]):      # recibe dict str->int
    def funcion_d(nombre: str | None = None):   # str o None (opcional)
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Scope: variables locales vs globales

    El **scope** (alcance) determina donde se puede acceder a una variable.
    """)
    return


@app.cell
def _():
    # Variable global
    SR_GLOBAL = 44100  # Por convencion, constantes en MAYUSCULAS

    def procesar_muestra(muestra):
        # Variable local: solo existe dentro de la funcion
        ganancia = 0.5
        resultado = muestra * ganancia
        # Podemos LEER la variable global
        print(f"  (procesando a {SR_GLOBAL} Hz)")
        return resultado

    valor = procesar_muestra(0.8)
    print(f"Resultado: {valor}")

    # ganancia NO existe fuera de la funcion
    # print(ganancia)  # Esto daria NameError!
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Por que evitar variables globales mutables?

    Las variables globales hacen que el codigo sea dificil de entender y debuggear. Si una funcion depende de un valor externo que puede cambiar, el resultado se vuelve impredecible.

    **Regla de oro**: las funciones deben recibir todo lo que necesitan como parametros y retornar sus resultados. No deben modificar estado externo.

    ```python
    # MAL: depende de estado global
    nivel = 0.5
    def aplicar_ganancia(senal):
        return [m * nivel for m in senal]  # Que valor tiene 'nivel'?

    # BIEN: todo explicito
    def aplicar_ganancia(senal, nivel):
        return [m * nivel for m in senal]  # Claro y predecible
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Modulos

    Un **modulo** es simplemente un archivo `.py` que contiene funciones y variables. Podemos importar funciones de un modulo en otro archivo.

    ### Crear un modulo

    Imagina que creamos un archivo llamado `audio_utils.py`:

    ```python
    # audio_utils.py
    import math

    def midi_a_hz(nota_midi: int) -> float:
        '''Convierte nota MIDI a frecuencia en Hz.'''
        return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))

    def hz_a_midi(frecuencia: float) -> int:
        '''Convierte frecuencia en Hz a nota MIDI mas cercana.'''
        return round(69 + 12 * math.log2(frecuencia / 440.0))

    def calcular_rms(signal: list[float]) -> float:
        '''Calcula el valor RMS de una senal.'''
        if not signal:
            return 0.0
        return math.sqrt(sum(m ** 2 for m in signal) / len(signal))

    if __name__ == "__main__":
        # Esto solo se ejecuta si corremos el archivo directamente
        # NO se ejecuta si lo importamos como modulo
        print(f"A4 = {midi_a_hz(69)} Hz")
        print(f"440 Hz = MIDI {hz_a_midi(440)}")
    ```

    ### Importar el modulo

    ```python
    # En otro archivo:
    import audio_utils
    freq = audio_utils.midi_a_hz(60)

    # O importar funciones especificas:
    from audio_utils import midi_a_hz, hz_a_midi
    freq = midi_a_hz(60)
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### El patron `if __name__ == "__main__"`

    Cuando Python ejecuta un archivo, le asigna el nombre `"__main__"` al modulo principal. Si el archivo se importa, su nombre es el nombre del modulo.

    Esto permite tener codigo que solo se ejecuta cuando el archivo se corre directamente (no cuando se importa):

    ```python
    # utils.py
    def mi_funcion():
        return 42

    if __name__ == "__main__":
        # Esto solo corre si hacemos: python utils.py
        print(mi_funcion())
        # NO corre si hacemos: from utils import mi_funcion
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplo practico: simular un modulo dentro del notebook
    """)
    return


@app.cell
def _(math):
    # Simulamos las funciones que pondriamos en audio_utils.py

    def midi_a_hz(nota_midi: int) -> float:
        """Convierte un numero de nota MIDI a frecuencia en Hz.

        Parameters
        ----------
        nota_midi : int
            Numero de nota MIDI (0-127).

        Returns
        -------
        float
            Frecuencia en Hz.
        """
        return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))

    def hz_a_midi(frecuencia: float) -> int:
        """Convierte una frecuencia en Hz al numero de nota MIDI mas cercano.

        Parameters
        ----------
        frecuencia : float
            Frecuencia en Hz (debe ser positiva).

        Returns
        -------
        int
            Numero de nota MIDI mas cercano.
        """
        if frecuencia <= 0:
            raise ValueError("La frecuencia debe ser positiva")
        return round(69 + 12 * math.log2(frecuencia / 440.0))

    def amplitud_a_db(amplitud: float) -> float:
        """Convierte amplitud lineal a decibeles.

        Parameters
        ----------
        amplitud : float
            Amplitud lineal (debe ser positiva).

        Returns
        -------
        float
            Valor en decibeles.
        """
        if amplitud <= 0:
            return float('-inf')
        return 20 * math.log10(amplitud)

    # Demostrar uso
    print("Funciones del modulo audio_utils:")
    print(f"  midi_a_hz(69)    = {midi_a_hz(69):.2f} Hz")
    print(f"  midi_a_hz(60)    = {midi_a_hz(60):.2f} Hz")
    print(f"  hz_a_midi(440)   = {hz_a_midi(440)}")
    print(f"  hz_a_midi(261.6) = {hz_a_midi(261.6)}")
    print(f"  amplitud_a_db(1.0) = {amplitud_a_db(1.0):.1f} dB")
    print(f"  amplitud_a_db(0.5) = {amplitud_a_db(0.5):.1f} dB")
    return amplitud_a_db, hz_a_midi, midi_a_hz


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Testing con pytest

    ### Por que testear?

    > **"Si no esta testeado, esta roto."**

    Los tests automaticos verifican que nuestro codigo funciona correctamente. Sin tests, cada cambio que hacemos puede romper algo sin que nos demos cuenta.

    ### assert: la base del testing

    `assert` verifica que una condicion es verdadera. Si es falsa, lanza un `AssertionError`.
    """)
    return


@app.cell
def _(midi_a_hz):
    # assert basico
    assert midi_a_hz(69) == 440.0, "A4 debe ser 440 Hz"
    assert midi_a_hz(81) == 880.0, "A5 debe ser 880 Hz"
    assert midi_a_hz(57) == 220.0, "A3 debe ser 220 Hz"

    # Para floats, usamos una tolerancia
    resultado = midi_a_hz(60)
    esperado = 261.6255653005986
    assert abs(resultado - esperado) < 0.001, f"C4 debe ser ~261.63, got {resultado}"

    print("Todos los asserts pasaron correctamente!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Escribir tests con pytest

    Con **pytest**, cada test es una funcion que empieza con `test_`:

    ```python
    # test_audio_utils.py
    from audio_utils import midi_a_hz, hz_a_midi, calcular_rms

    def test_midi_a_hz_a4():
        '''A4 (MIDI 69) debe ser 440 Hz.'''
        assert midi_a_hz(69) == 440.0

    def test_midi_a_hz_octava_arriba():
        '''Una octava arriba debe duplicar la frecuencia.'''
        assert midi_a_hz(81) == 880.0  # A5

    def test_midi_a_hz_octava_abajo():
        '''Una octava abajo debe ser la mitad de la frecuencia.'''
        assert midi_a_hz(57) == 220.0  # A3

    def test_hz_a_midi_roundtrip():
        '''Convertir MIDI->Hz->MIDI debe dar el mismo valor.'''
        for nota in [48, 60, 69, 72, 84]:
            assert hz_a_midi(midi_a_hz(nota)) == nota

    def test_calcular_rms_silencio():
        '''RMS de silencio debe ser 0.'''
        assert calcular_rms([0.0, 0.0, 0.0]) == 0.0

    def test_calcular_rms_senal_constante():
        '''RMS de una senal constante debe ser el valor absoluto.'''
        import math
        assert math.isclose(calcular_rms([0.5, 0.5, 0.5]), 0.5)
    ```

    ### Correr pytest

    Desde la terminal:
    ```bash
    # Correr todos los tests
    pytest

    # Correr un archivo especifico
    pytest test_audio_utils.py

    # Correr con detalle
    pytest -v

    # Correr un test especifico
    pytest test_audio_utils.py::test_midi_a_hz_a4
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplo: ejecutar tests dentro del notebook

    Podemos simular la ejecucion de tests para entender la logica:
    """)
    return


@app.cell
def _(calcular_rms, hz_a_midi, math, midi_a_hz):
    # Simulamos pytest ejecutando nuestros tests
    tests_pasados = 0
    tests_fallados = 0

    def run_test(nombre, condicion):
        nonlocal tests_pasados, tests_fallados
        if condicion:
            print(f"  PASS: {nombre}")
            tests_pasados += 1
        else:
            print(f"  FAIL: {nombre}")
            tests_fallados += 1

    print("Ejecutando tests...\n")

    # Tests de midi_a_hz
    run_test("midi_a_hz(69) == 440.0", midi_a_hz(69) == 440.0)
    run_test("midi_a_hz(81) == 880.0", midi_a_hz(81) == 880.0)
    run_test("midi_a_hz(57) == 220.0", midi_a_hz(57) == 220.0)

    # Test de roundtrip
    roundtrip_ok = all(hz_a_midi(midi_a_hz(n)) == n for n in [48, 60, 69, 72, 84])
    run_test("roundtrip MIDI->Hz->MIDI", roundtrip_ok)

    # Tests de calcular_rms
    run_test("RMS de silencio == 0", calcular_rms([0.0, 0.0, 0.0]) == 0.0)
    run_test("RMS de lista vacia == 0", calcular_rms([]) == 0.0)
    run_test("RMS de senal constante", math.isclose(calcular_rms([0.5, 0.5, 0.5]), 0.5))

    print(f"\n{'='*40}")
    print(f"Resultado: {tests_pasados} pasaron, {tests_fallados} fallaron")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 7. Arquitectura de proyecto

    A medida que nuestro codigo crece, necesitamos organizarlo bien. Un buen proyecto tiene:

    ### Estructura tipica

    ```
    mi_proyecto/
    ├── README.md              # Descripcion del proyecto
    ├── pyproject.toml         # Dependencias y configuracion
    ├── src/
    │   └── mi_proyecto/
    │       ├── __init__.py    # Marca el directorio como paquete
    │       ├── audio.py       # Funciones de audio
    │       ├── midi.py        # Funciones MIDI
    │       └── utils.py       # Utilidades generales
    └── tests/
        ├── test_audio.py      # Tests de audio.py
        ├── test_midi.py       # Tests de midi.py
        └── test_utils.py      # Tests de utils.py
    ```

    ### Principios basicos

    1. **Separacion de responsabilidades**: cada archivo/modulo tiene un proposito claro
    2. **Funciones pequenas**: cada funcion hace UNA cosa bien
    3. **Nombres descriptivos**: `calcular_rms()` es mejor que `calc()` o `f1()`
    4. **Tests para todo**: si una funcion es importante, tiene tests
    5. **Documentacion**: docstrings en funciones publicas

    ### Esto es lo que van a construir en el TP!

    El trabajo practico va a ser un proyecto de procesamiento de audio con esta estructura. Vamos a ir construyendolo de a poco a lo largo del curso.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen de la clase

    Hoy aprendimos:

    - **Funciones**: `def`, parametros, `return`, valores por defecto
    - **`*args` y `**kwargs`**: argumentos variables
    - **Docstrings**: documentacion estilo NumPy
    - **Type hints**: anotaciones de tipos para mayor claridad
    - **Scope**: variables locales vs globales
    - **Modulos**: crear archivos `.py` reutilizables, `__name__ == "__main__"`
    - **Testing**: `assert`, pytest, escribir tests automaticos
    - **Arquitectura**: como organizar un proyecto

    ### Para la proxima clase
    - Crear un archivo `audio_utils.py` con al menos 3 funciones
    - Escribir tests con pytest para cada funcion
    - Push al repositorio de GitHub
    """)
    return


if __name__ == "__main__":
    app.run()
