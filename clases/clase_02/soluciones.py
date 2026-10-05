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
    # Clase 2: Soluciones
    ## Hablar en Python
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Clasificar frecuencias
    """)
    return


@app.cell
def _():
    def clasificar_frecuencia(freq):
        if freq < 20:
            return "Infrasonica"
        elif freq <= 60:
            return "Sub-bass"
        elif freq <= 250:
            return "Bass"
        elif freq <= 4000:
            return "Mid"
        elif freq <= 12000:
            return "Treble"
        elif freq <= 20000:
            return "Ultra-treble"
        else:
            return "Ultrasonica"

    for f in [35, 880, 100, 5000, 15000]:
        print(f"{f:>6} Hz -> {clasificar_frecuencia(f)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Primeros 10 armonicos
    """)
    return


@app.cell
def _():
    fundamental_2 = 220  # A3

    print(f"Armonicos de {fundamental_2} Hz (A3):")
    for n in range(1, 11):
        freq = fundamental_2 * n
        print(f"  Armonico {n:2d}: {freq:>5} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Amplitudes a dB
    """)
    return


@app.cell
def _(math):
    amplitudes_3 = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]
    amplitudes_db_3 = [20 * math.log10(a) for a in amplitudes_3]

    print("Lineal  ->    dB")
    print("------  --------")
    for lin, db in zip(amplitudes_3, amplitudes_db_3):
        print(f"{lin:6.3f}  -> {db:7.2f} dB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Diccionario de bandas de octava
    """)
    return


@app.cell
def _(math):
    fc_list = [125, 250, 500, 1000, 2000, 4000, 8000]
    sqrt2 = math.sqrt(2)
    bandas_bw = {fc: fc * (sqrt2 - 1 / sqrt2) for fc in fc_list}

    print("Banda de octava -> Ancho de banda")
    print("-" * 35)
    for fc, bw in bandas_bw.items():
        if fc >= 1000:
            fc_str = f"{fc / 1000:.0f} kHz"
        else:
            fc_str = f"{fc} Hz"
        print(f"  {fc_str:>6}: BW = {bw:.1f} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Filtrar archivos por metadata
    """)
    return


@app.cell
def _():
    archivos_5 = [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]

    buenos = [a for a in archivos_5 if a["sr"] >= 44100]
    nombres_buenos = [a["nombre"] for a in buenos]

    print(f"Archivos con SR >= 44100 Hz: {nombres_buenos}")
    print(f"\nDetalle:")
    for a in buenos:
        print(f"  {a['nombre']:>15}: {a['sr']:>6} Hz, {a['bits']} bits, {a['duracion']:.0f}s")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Tabla frecuencia x armonico
    """)
    return


@app.cell
def _():
    fundamentales_6 = [100, 200, 440]
    armonicos_6 = [1, 2, 3, 4, 5]

    # Encabezado
    header = "     |"
    for h in armonicos_6:
        header += f"   x{h:d}"
    print(header)
    print("-----|" + "-" * (6 * len(armonicos_6)))

    # Filas
    for fund in fundamentales_6:
        fila = f" {fund:>3d} |"
        for h in armonicos_6:
            fila += f" {fund * h:>5d}"
        print(fila)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Track listing con enumerate
    """)
    return


@app.cell
def _():
    album_7 = [
        "Speak to Me", "Breathe", "On the Run", "Time",
        "The Great Gig in the Sky", "Money", "Us and Them",
        "Any Colour You Like", "Brain Damage", "Eclipse",
    ]

    print("The Dark Side of the Moon - Track Listing:")
    print()
    for i, track in enumerate(album_7, start=1):
        print(f"  {i:02d}. {track}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Stereo pairs con zip
    """)
    return


@app.cell
def _():
    left_8 = [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right_8 = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]

    # 1. Crear stereo pairs
    stereo_pairs = list(zip(left_8, right_8))

    # 2 y 3. Calcular mono e imprimir
    print("Muestra  |    L    |    R    |  Mono")
    print("---------|---------|---------|--------")
    for i, (l, r) in enumerate(stereo_pairs):
        mono = (l + r) / 2
        print(f"   {i:2d}    | {l:+5.2f}  | {r:+5.2f}  | {mono:+5.2f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Operaciones con sets
    """)
    return


@app.cell
def _():
    interface_a = {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b = {44100, 48000, 96000}

    print(f"Interfaz A: {sorted(interface_a)}")
    print(f"Interfaz B: {sorted(interface_b)}")
    print()

    # 1. Comunes
    comunes = interface_a & interface_b
    print(f"1. Comunes (A & B):     {sorted(comunes)}")

    # 2. Union
    todos = interface_a | interface_b
    print(f"2. Todos (A | B):       {sorted(todos)}")

    # 3. Solo en A
    solo_a = interface_a - interface_b
    print(f"3. Solo en A (A - B):   {sorted(solo_a)}")

    # 4. Subconjunto
    es_subconjunto = interface_b.issubset(interface_a)
    print(f"4. B es subconjunto de A: {es_subconjunto}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Dict comprehension - Notas y frecuencias
    """)
    return


@app.cell
def _():
    nombres_notas = [
        "A3", "B3", "C4", "D4", "E4", "F4", "G4",
        "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5",
    ]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]

    nota_freq_10 = {
        nombre: 440.0 * (2.0 ** ((midi - 69) / 12.0))
        for nombre, midi in zip(nombres_notas, midi_base)
    }

    print("Nota -> Frecuencia")
    print("-" * 25)
    for nota, freq in nota_freq_10.items():
        print(f"  {nota:3s}: {freq:>8.2f} Hz")
    return


if __name__ == "__main__":
    app.run()
