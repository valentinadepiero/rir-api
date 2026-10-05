import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 3: Soluciones
    ## Construir con Funciones
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: midi_a_hz
    """)
    return


@app.cell
def _():
    def midi_a_hz(nota_midi: int) -> float:
        """Convierte un numero de nota MIDI a frecuencia en Hz.

        Parameters
        ----------
        nota_midi : int
            Numero de nota MIDI (0-127).

        Returns
        -------
        float
            Frecuencia correspondiente en Hz.

        Raises
        ------
        ValueError
            Si nota_midi no esta en el rango [0, 127].
        """
        if not (0 <= nota_midi <= 127):
            raise ValueError(f"nota_midi debe estar entre 0 y 127, se recibio {nota_midi}")
        return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))

    # Pruebas
    for midi in [48, 60, 69, 72]:
        print(f"MIDI {midi:3d} -> {midi_a_hz(midi):>8.2f} Hz")
    return (midi_a_hz,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: hz_a_midi
    """)
    return


@app.cell
def _(math):
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

        Raises
        ------
        ValueError
            Si la frecuencia no es positiva.
        """
        if frecuencia <= 0:
            raise ValueError(f"La frecuencia debe ser positiva, se recibio {frecuencia}")
        return round(69 + 12 * math.log2(frecuencia / 440.0))

    # Pruebas
    for freq in [440.0, 261.63, 880.0, 130.81]:
        print(f"{freq:>8.2f} Hz -> MIDI {hz_a_midi(freq)}")
    return (hz_a_midi,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: aplicar_fade
    """)
    return


@app.cell
def _():
    def aplicar_fade(
        signal: list[float],
        tipo: str = "in",
        duracion_ms: float = 100,
        fs: int = 44100,
    ) -> list[float]:
        """Aplica un fade lineal (in o out) a una senal.

        Parameters
        ----------
        signal : list[float]
            Senal de entrada.
        tipo : str, optional
            Tipo de fade: "in" o "out" (default "in").
        duracion_ms : float, optional
            Duracion del fade en milisegundos (default 100).
        fs : int, optional
            Frecuencia de muestreo en Hz (default 44100).

        Returns
        -------
        list[float]
            Nueva senal con el fade aplicado.

        Raises
        ------
        ValueError
            Si tipo no es "in" ni "out".
        """
        if tipo not in ("in", "out"):
            raise ValueError(f"tipo debe ser 'in' o 'out', se recibio '{tipo}'")

        n_fade = int(fs * duracion_ms / 1000)
        n_fade = min(n_fade, len(signal))  # No exceder la longitud de la senal

        resultado = list(signal)  # Copiar la senal

        for i in range(n_fade):
            factor = i / n_fade if n_fade > 0 else 1.0

            if tipo == "in":
                resultado[i] *= factor
            else:  # tipo == "out"
                resultado[-(i + 1)] *= factor

        return resultado

    # Prueba con senal simple
    senal_test = [1.0] * 20
    fade_in = aplicar_fade(senal_test, tipo="in", duracion_ms=0.2, fs=44100)
    fade_out = aplicar_fade(senal_test, tipo="out", duracion_ms=0.2, fs=44100)

    print("Original:", [f"{s:.2f}" for s in senal_test[:10]])
    print("Fade in: ", [f"{s:.2f}" for s in fade_in[:10]])
    print("Fade out:", [f"{s:.2f}" for s in fade_out[-10:]])

    # Prueba mas visual con duracion exacta
    senal_corta = [1.0] * 8
    fade_in_corto = aplicar_fade(senal_corta, tipo="in", duracion_ms=90.7, fs=44.1)
    # ~4 muestras de fade a ese sr y duracion
    print(f"\nFade in (8 muestras): {[f'{s:.3f}' for s in fade_in_corto]}")
    return (aplicar_fade,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: mezclar_senales
    """)
    return


@app.cell
def _():
    def mezclar_senales(*signals: list[float], pesos: list[float] | None = None) -> list[float]:
        """Mezcla multiples senales con pesos opcionales.

        Parameters
        ----------
        *signals : list[float]
            Senales a mezclar (todas deben tener la misma longitud).
        pesos : list[float] | None, optional
            Pesos para cada senal. Si es None, se usa peso uniforme (1/N).

        Returns
        -------
        list[float]
            Senal mezclada.

        Raises
        ------
        ValueError
            Si no se proporcionan senales o las longitudes no coinciden.
        """
        if not signals:
            raise ValueError("Se necesita al menos una senal")

        longitud = len(signals[0])
        if not all(len(s) == longitud for s in signals):
            raise ValueError("Todas las senales deben tener la misma longitud")

        n = len(signals)

        if pesos is None:
            pesos_efectivos = [1.0 / n] * n
        else:
            if len(pesos) != n:
                raise ValueError("La cantidad de pesos debe coincidir con la cantidad de senales")
            pesos_efectivos = pesos

        mezcla = [0.0] * longitud
        for senal, peso in zip(signals, pesos_efectivos):
            for i in range(longitud):
                mezcla[i] += senal[i] * peso

        return mezcla

    # Pruebas
    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]

    mezcla_uniforme = mezclar_senales(a, b)
    mezcla_pesos = mezclar_senales(a, b, pesos=[0.8, 0.2])

    print(f"Senal A:          {a}")
    print(f"Senal B:          {b}")
    print(f"Mezcla uniforme:  {mezcla_uniforme}")
    print(f"Mezcla 80/20:     {mezcla_pesos}")
    return (mezclar_senales,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: info_audio
    """)
    return


@app.cell
def _():
    def info_audio(nombre: str, sr: int = 44100, **kwargs) -> str:
        """Genera un string formateado con informacion de un archivo de audio.

        Parameters
        ----------
        nombre : str
            Nombre del archivo.
        sr : int, optional
            Sample rate en Hz (default 44100).
        **kwargs
            Parametros adicionales a mostrar (bits, canales, artista, etc.)

        Returns
        -------
        str
            String formateado con la informacion del archivo.
        """
        lineas = [
            f"=== {nombre} ===",
            f"Sample Rate: {sr:,} Hz",
        ]
        for clave, valor in kwargs.items():
            lineas.append(f"{clave}: {valor}")
        return "\n".join(lineas)

    # Pruebas
    info1 = info_audio("cancion.wav", sr=48000, bits=24, canales=2, artista="Queen")
    print(info1)
    print()

    info2 = info_audio("test.wav")
    print(info2)
    return (info_audio,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Crear un modulo

    Contenido del archivo `mis_funciones.py`:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```python
    # mis_funciones.py
    import math


    def midi_a_hz(nota_midi: int) -> float:
        '''Convierte un numero de nota MIDI a frecuencia en Hz.

        Parameters
        ----------
        nota_midi : int
            Numero de nota MIDI (0-127).

        Returns
        -------
        float
            Frecuencia correspondiente en Hz.
        '''
        if not (0 <= nota_midi <= 127):
            raise ValueError(f"nota_midi debe estar entre 0 y 127, se recibio {nota_midi}")
        return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))


    def hz_a_midi(frecuencia: float) -> int:
        '''Convierte una frecuencia en Hz al numero de nota MIDI mas cercano.

        Parameters
        ----------
        frecuencia : float
            Frecuencia en Hz (debe ser positiva).

        Returns
        -------
        int
            Numero de nota MIDI mas cercano.
        '''
        if frecuencia <= 0:
            raise ValueError(f"La frecuencia debe ser positiva, se recibio {frecuencia}")
        return round(69 + 12 * math.log2(frecuencia / 440.0))


    def calcular_rms(signal: list[float]) -> float:
        '''Calcula el valor RMS (Root Mean Square) de una senal.

        Parameters
        ----------
        signal : list[float]
            Senal de entrada como lista de muestras.

        Returns
        -------
        float
            Valor RMS de la senal.
        '''
        if not signal:
            return 0.0
        return math.sqrt(sum(m ** 2 for m in signal) / len(signal))


    if __name__ == "__main__":
        print("=== Demo de mis_funciones.py ===")
        print(f"MIDI 69 -> {midi_a_hz(69)} Hz")
        print(f"MIDI 60 -> {midi_a_hz(60):.2f} Hz")
        print(f"440 Hz -> MIDI {hz_a_midi(440)}")
        print(f"RMS de [0.5, -0.5, 0.5, -0.5] = {calcular_rms([0.5, -0.5, 0.5, -0.5]):.4f}")
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Tests para midi_a_hz
    """)
    return


@app.cell
def _(midi_a_hz):
    def test_midi_a_hz_a4():
        """Verifica que MIDI 69 retorna 440.0 Hz."""
        assert midi_a_hz(69) == 440.0

    def test_midi_a_hz_octavas():
        """Verifica que subir 12 semitonos duplica la frecuencia."""
        freq_a4 = midi_a_hz(69)
        freq_a5 = midi_a_hz(81)
        assert abs(freq_a5 - 2 * freq_a4) < 0.001, "A5 debe ser el doble de A4"

        freq_a3 = midi_a_hz(57)
        assert abs(freq_a3 - freq_a4 / 2) < 0.001, "A3 debe ser la mitad de A4"

    def test_midi_a_hz_rango_invalido():
        """Verifica que notas fuera de rango lanzan ValueError."""
        # MIDI -1
        try:
            midi_a_hz(-1)
            assert False, "Deberia haber lanzado ValueError para -1"
        except ValueError:
            pass  # OK

        # MIDI 128
        try:
            midi_a_hz(128)
            assert False, "Deberia haber lanzado ValueError para 128"
        except ValueError:
            pass  # OK

    # Ejecutar tests
    tests = [test_midi_a_hz_a4, test_midi_a_hz_octavas, test_midi_a_hz_rango_invalido]

    print("Ejecutando tests de midi_a_hz:\n")
    for test in tests:
        try:
            test()
            print(f"  PASS: {test.__name__}")
        except AssertionError as e:
            print(f"  FAIL: {test.__name__} - {e}")

    print("\nTodos los tests pasaron!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: normalizar con tests
    """)
    return


@app.cell
def _(math):
    def normalizar(signal: list[float]) -> list[float]:
        """Normaliza una senal al rango [-1, 1].

        Divide todas las muestras por el valor absoluto maximo.
        Si la senal es toda ceros, retorna la senal sin cambios.

        Parameters
        ----------
        signal : list[float]
            Senal de entrada.

        Returns
        -------
        list[float]
            Senal normalizada al rango [-1, 1].
        """
        if not signal:
            return []

        valor_max = max(abs(m) for m in signal)

        if valor_max == 0:
            return list(signal)  # Retornar copia

        return [m / valor_max for m in signal]

    # Tests
    def test_normalizar_basico():
        """Una senal con pico en 0.5 debe tener pico en 1.0."""
        senal = [0.5, -0.3, 0.2, -0.5, 0.4]
        resultado = normalizar(senal)
        assert max(abs(m) for m in resultado) == 1.0
        # Verificar que el primer valor (0.5/0.5 = 1.0)
        assert resultado[0] == 1.0
        assert resultado[3] == -1.0

    def test_normalizar_ya_normalizada():
        """Una senal con pico en 1.0 no cambia."""
        senal = [1.0, -0.5, 0.3, -1.0]
        resultado = normalizar(senal)
        for orig, norm in zip(senal, resultado):
            assert math.isclose(orig, norm), f"{orig} != {norm}"

    def test_normalizar_silencio():
        """Una senal de ceros retorna ceros."""
        senal = [0.0, 0.0, 0.0, 0.0]
        resultado = normalizar(senal)
        assert all(m == 0.0 for m in resultado)

    # Ejecutar tests
    tests_norm = [test_normalizar_basico, test_normalizar_ya_normalizada, test_normalizar_silencio]

    print("Ejecutando tests de normalizar:\n")
    for test in tests_norm:
        try:
            test()
            print(f"  PASS: {test.__name__}")
        except AssertionError as e:
            print(f"  FAIL: {test.__name__} - {e}")

    # Demo visual
    senal_demo = [0.3, -0.6, 0.2, 0.6, -0.1]
    normalizada = normalizar(senal_demo)
    print(f"\nDemo:")
    print(f"  Original:    {senal_demo}")
    print(f"  Normalizada: {[f'{m:.3f}' for m in normalizada]}")
    print(f"  Pico: {max(abs(m) for m in normalizada):.3f}")
    return


if __name__ == "__main__":
    app.run()
