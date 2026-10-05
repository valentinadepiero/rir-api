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
    ## Clase 2: Hablar en Python

    En esta clase vamos a aprender las estructuras de **control de flujo** y las **estructuras de datos** fundamentales de Python, siempre con ejemplos del mundo del audio.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Condicionales: if / elif / else

    Los condicionales nos permiten ejecutar codigo diferente segun una condicion.
    """)
    return


@app.cell
def _():
    # Ejemplo: clasificar sample rate
    sample_rate = 44100

    if sample_rate >= 96000:
        calidad = "Hi-Res / Professional"
    elif sample_rate >= 48000:
        calidad = "HD (Broadcast)"
    elif sample_rate >= 44100:
        calidad = "CD Quality"
    elif sample_rate >= 22050:
        calidad = "FM Radio Quality"
    else:
        calidad = "Baja calidad"

    print(f"Sample rate: {sample_rate} Hz -> {calidad}")
    return


@app.cell
def _():
    # Ejemplo: clasificar nivel de audio en dB
    nivel_db = -12.5

    if nivel_db > 0:
        estado = "CLIPPING! (distorsion)"
    elif nivel_db > -3:
        estado = "Peligro - muy cerca del clip"
    elif nivel_db > -12:
        estado = "Nivel alto - OK para peaks"
    elif nivel_db > -24:
        estado = "Nivel nominal - ideal"
    else:
        estado = "Nivel bajo"

    print(f"Nivel: {nivel_db} dB -> {estado}")
    return


@app.cell
def _():
    # Condicional en una linea (ternario)
    canales = 2
    tipo_audio = "estereo" if canales == 2 else "mono" if canales == 1 else "multicanal"
    print(f"{canales} canales -> {tipo_audio}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Bucles: for y while

    Los bucles permiten repetir operaciones. En audio, los usamos constantemente para procesar muestras, recorrer frecuencias, etc.

    ### Bucle for
    """)
    return


@app.cell
def _():
    # Iterar sobre bandas de frecuencia (bandas de octava)
    bandas_octava = [125, 250, 500, 1000, 2000, 4000, 8000]

    print("Bandas de octava estandar:")
    for banda in bandas_octava:
        if banda >= 1000:
            print(f"  {banda / 1000:.0f} kHz")
        else:
            print(f"  {banda} Hz")
    return (bandas_octava,)


@app.cell
def _():
    # range(): generar secuencias de numeros
    print("Primeros 5 armonicos de 100 Hz:")
    for n in range(1, 6):
        freq = 100 * n
        print(f"  Armonico {n}: {freq} Hz")
    return


@app.cell
def _():
    # enumerate(): obtener indice y valor
    pistas = ["Vocals", "Guitar", "Bass", "Drums", "Keys"]

    print("Listado de pistas:")
    for i, pista in enumerate(pistas, start=1):
        print(f"  Track {i:02d}: {pista}")
    return (pistas,)


@app.cell
def _():
    # zip(): combinar dos listas en paralelo
    canales_izq = [0.5, -0.3, 0.8, -0.1, 0.6]
    canales_der = [0.4, -0.2, 0.7, -0.3, 0.5]

    print("Muestras estereo (L, R):")
    for i, (izq, der) in enumerate(zip(canales_izq, canales_der)):
        print(f"  Muestra {i}: ({izq:+.1f}, {der:+.1f})")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Bucle while

    El bucle `while` se ejecuta mientras una condicion sea verdadera. Util para simular procesos que terminan cuando se cumple cierta condicion.
    """)
    return


@app.cell
def _():
    # Simular un decay: la senal se reduce hasta estar por debajo del umbral
    nivel = 1.0          # nivel inicial (lineal)
    decay_factor = 0.7   # factor de decaimiento por paso
    umbral = 0.01        # umbral minimo
    paso = 0

    print("Simulacion de decay:")
    while nivel > umbral:
        nivel_db = 20 * __import__('math').log10(nivel) if nivel > 0 else float('-inf')
        print(f"  Paso {paso:2d}: nivel = {nivel:.4f} ({nivel_db:.1f} dB)")
        nivel *= decay_factor
        paso += 1

    print(f"  -> Senal debajo del umbral despues de {paso} pasos")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. List Comprehensions

    Las list comprehensions son una forma concisa y "Pythonica" de crear listas. Son muy utiles para procesamiento de senales.
    """)
    return


@app.cell
def _():
    import math

    # Ejemplo basico: cuadrados de frecuencias
    frecuencias = [100, 200, 500, 1000, 2000, 5000]
    freq_cuadrado = [f ** 2 for f in frecuencias]
    print(f"Frecuencias:      {frecuencias}")
    print(f"Frecuencias al 2: {freq_cuadrado}")
    return (math,)


@app.cell
def _(math):
    # Filtrar: solo frecuencias por encima de 1000 Hz
    todas_las_freq = [100, 250, 500, 800, 1000, 2000, 4000, 8000, 16000]
    agudos = [f for f in todas_las_freq if f > 1000]
    graves = [f for f in todas_las_freq if f <= 500]

    print(f"Todas: {todas_las_freq}")
    print(f"Agudos (>1kHz): {agudos}")
    print(f"Graves (<=500): {graves}")
    return (todas_las_freq,)


@app.cell
def _(math):
    # Convertir amplitudes lineales a dB
    amplitudes = [1.0, 0.5, 0.25, 0.1, 0.01]
    amplitudes_db = [20 * math.log10(a) for a in amplitudes]

    print("Lineal -> dB:")
    for lin, db in zip(amplitudes, amplitudes_db):
        print(f"  {lin:5.2f} -> {db:6.1f} dB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. f-strings avanzados

    Ya conocemos f-strings basicos. Ahora veamos opciones de formato mas avanzadas.
    """)
    return


@app.cell
def _():
    # Formato avanzado de numeros
    frecuencia_fmt = 44100
    nivel_fmt = -6.234567
    porcentaje = 0.856

    print(f"Entero con separador de miles: {frecuencia_fmt:,}")
    print(f"Float con 2 decimales: {nivel_fmt:.2f}")
    print(f"Float con 1 decimal:   {nivel_fmt:.1f}")
    print(f"Porcentaje:            {porcentaje:.1%}")
    print(f"Notacion cientifica:   {frecuencia_fmt:.2e}")
    return


@app.cell
def _():
    # Alineacion de texto
    datos = [
        ("Vocals", -6.2, 44100),
        ("Guitar", -3.1, 48000),
        ("Bass", -8.5, 44100),
        ("Drums", -4.0, 96000),
    ]

    print(f"{'Pista':<10} {'Nivel':>8} {'SR':>8}")
    print("-" * 28)
    for nombre, nivel, sr in datos:
        print(f"{nombre:<10} {nivel:>7.1f}dB {sr:>6,} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Estructuras de datos

    Python tiene 4 estructuras de datos fundamentales:
    - **Listas** (`list`): colecciones ordenadas, mutables
    - **Tuplas** (`tuple`): colecciones ordenadas, inmutables
    - **Diccionarios** (`dict`): pares clave-valor
    - **Conjuntos** (`set`): colecciones sin duplicados

    ### Listas
    """)
    return


@app.cell
def _():
    # Listas: colecciones ordenadas y mutables
    muestras = [0.0, 0.5, 1.0, 0.5, 0.0, -0.5, -1.0, -0.5]

    print(f"Muestras: {muestras}")
    print(f"Longitud: {len(muestras)}")
    print(f"Primera:  {muestras[0]}")
    print(f"Ultima:   {muestras[-1]}")
    print(f"Slice [2:5]: {muestras[2:5]}")

    # Agregar elementos
    muestras.append(0.0)
    print(f"Despues de append: {muestras}")

    # Extender con otra lista
    muestras.extend([0.3, 0.6])
    print(f"Despues de extend: {muestras}")

    # Estadisticas basicas
    print(f"Max: {max(muestras)}, Min: {min(muestras)}, Sum: {sum(muestras):.2f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Tuplas
    """)
    return


@app.cell
def _():
    # Tuplas: inmutables, ideales para datos que no cambian
    formato_audio = (44100, 16, 2)  # (sample_rate, bit_depth, canales)

    print(f"Formato: {formato_audio}")
    print(f"Sample rate: {formato_audio[0]}")

    # Unpacking
    sr, bits, ch = formato_audio
    print(f"SR={sr}, Bits={bits}, Canales={ch}")

    # Las tuplas son inmutables - esto daria error:
    # formato_audio[0] = 48000  # TypeError!

    # Multiples formatos
    formatos = [
        (44100, 16, 2),
        (48000, 24, 2),
        (96000, 32, 6),
    ]

    for sr, bits, ch in formatos:
        tipo = "estereo" if ch == 2 else f"{ch} canales"
        print(f"  {sr} Hz / {bits} bits / {tipo}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Diccionarios
    """)
    return


@app.cell
def _():
    # Diccionarios: pares clave-valor
    nota_freq = {
        "C4": 261.63,
        "D4": 293.66,
        "E4": 329.63,
        "F4": 349.23,
        "G4": 392.00,
        "A4": 440.00,
        "B4": 493.88,
    }

    print(f"Frecuencia de A4: {nota_freq['A4']} Hz")
    print(f"Todas las notas: {list(nota_freq.keys())}")

    # Iterar sobre un diccionario
    print("\nEscala de Do mayor:")
    for nota, freq in nota_freq.items():
        print(f"  {nota}: {freq:>7.2f} Hz")
    return (nota_freq,)


@app.cell
def _():
    # Diccionario como metadata de audio
    metadata = {
        "titulo": "Senal de prueba",
        "artista": "Laboratorio SyS",
        "sample_rate": 44100,
        "bit_depth": 24,
        "canales": 1,
        "duracion_seg": 10.5,
        "formato": "WAV",
    }

    print("Metadata del archivo:")
    for clave, valor in metadata.items():
        print(f"  {clave:>15}: {valor}")

    # Acceso seguro con .get()
    genero = metadata.get("genero", "No especificado")
    print(f"\n  Genero: {genero}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Conjuntos (Sets)
    """)
    return


@app.cell
def _():
    # Sets: sin duplicados, operaciones de conjuntos
    sr_equipo_a = {44100, 48000, 96000, 192000}
    sr_equipo_b = {22050, 44100, 48000, 88200}

    print(f"Equipo A: {sr_equipo_a}")
    print(f"Equipo B: {sr_equipo_b}")
    print(f"Comunes (interseccion):   {sr_equipo_a & sr_equipo_b}")
    print(f"Todos (union):            {sr_equipo_a | sr_equipo_b}")
    print(f"Solo en A (diferencia):   {sr_equipo_a - sr_equipo_b}")

    # Eliminar duplicados de una lista
    muestras_rates = [44100, 48000, 44100, 96000, 48000, 44100]
    unicos = sorted(set(muestras_rates))
    print(f"\nLista con duplicados: {muestras_rates}")
    print(f"Unicos y ordenados:   {unicos}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Estructuras anidadas

    En la practica, los datos vienen en estructuras mas complejas. Un caso comun es una **lista de diccionarios**:
    """)
    return


@app.cell
def _():
    # Lista de diccionarios: pistas de una sesion
    sesion = [
        {"nombre": "Vocals", "nivel_db": -6.2, "pan": 0, "mute": False, "sr": 48000},
        {"nombre": "Guitar L", "nivel_db": -8.5, "pan": -50, "mute": False, "sr": 48000},
        {"nombre": "Guitar R", "nivel_db": -8.5, "pan": 50, "mute": False, "sr": 48000},
        {"nombre": "Bass", "nivel_db": -10.0, "pan": 0, "mute": False, "sr": 48000},
        {"nombre": "Drums OH", "nivel_db": -4.0, "pan": 0, "mute": True, "sr": 96000},
        {"nombre": "Kick", "nivel_db": -3.5, "pan": 0, "mute": False, "sr": 96000},
    ]

    # Mostrar la sesion
    print(f"{'Track':<12} {'Nivel':>7} {'Pan':>5} {'Mute':>5}")
    print("-" * 32)
    for track in sesion:
        estado = "MUTE" if track["mute"] else "  ON"
        print(f"{track['nombre']:<12} {track['nivel_db']:>6.1f}dB {track['pan']:>+4d} {estado:>5}")

    # Filtrar tracks activos
    activos = [t["nombre"] for t in sesion if not t["mute"]]
    print(f"\nTracks activos: {activos}")

    # Promedio de nivel de tracks activos
    niveles_activos = [t["nivel_db"] for t in sesion if not t["mute"]]
    promedio = sum(niveles_activos) / len(niveles_activos)
    print(f"Nivel promedio (activos): {promedio:.1f} dB")
    return (sesion,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 7. IA como asistente de codigo

    Una de las habilidades mas utiles que van a desarrollar es **saber pedirle a una IA** que escriba codigo. No se trata de copiar y pegar sin entender, sino de aprender a:

    1. **Formular buenos prompts**: ser claro, especifico, dar contexto
    2. **Evaluar el resultado**: leer el codigo, entenderlo, verificarlo
    3. **Iterar**: pedir cambios, mejoras, explicaciones

    ### Ejemplo: pedir una funcion a la IA

    **Prompt que enviamos:**
    > Escribi una funcion en Python llamada `midi_a_hz` que convierta un numero de nota MIDI
    > a frecuencia en Hz. La formula es: f = 440 * 2^((midi - 69) / 12).
    > Quiero que tenga docstring explicativo y type hints.

    **Respuesta de la IA:**
    """)
    return


@app.cell
def _():
    # Codigo generado por IA (ejemplo)
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

        Examples
        --------
        >>> midi_a_hz(69)
        440.0
        >>> midi_a_hz(60)
        261.6255653005986
        """
        return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))

    # Verificamos que funciona correctamente
    print(f"MIDI 69 (A4): {midi_a_hz(69):.2f} Hz (esperado: 440.00)")
    print(f"MIDI 60 (C4): {midi_a_hz(60):.2f} Hz (esperado: 261.63)")
    print(f"MIDI 48 (C3): {midi_a_hz(48):.2f} Hz (esperado: 130.81)")
    print(f"MIDI 81 (A5): {midi_a_hz(81):.2f} Hz (esperado: 880.00)")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Que mirar cuando la IA genera codigo?

    1. **La formula es correcta?** Verificar contra la definicion conocida.
    2. **Maneja casos borde?** Que pasa si `nota_midi` es negativo? O mayor a 127?
    3. **El docstring es claro?** Describe bien lo que hace?
    4. **Se puede mejorar?** Agregar validacion, tests, etc.

    En las proximas clases vamos a usar IA de forma mas activa para generar funciones, escribir tests, y construir modulos completos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen de la clase

    Hoy aprendimos:

    - **Condicionales**: `if / elif / else` para tomar decisiones
    - **Bucles**: `for` (iterar sobre colecciones) y `while` (repetir hasta condicion)
    - **Herramientas de iteracion**: `range()`, `enumerate()`, `zip()`
    - **List comprehensions**: crear listas de forma concisa
    - **f-strings avanzados**: alineacion, formato de numeros
    - **Estructuras de datos**: listas, tuplas, diccionarios, sets
    - **Estructuras anidadas**: lista de diccionarios
    - **IA como asistente**: formular prompts y evaluar resultados

    ### Para la proxima clase
    - Practicar los ejercicios de esta clase
    - Experimentar con al menos un prompt de IA para generar una funcion
    """)
    return


if __name__ == "__main__":
    app.run()
