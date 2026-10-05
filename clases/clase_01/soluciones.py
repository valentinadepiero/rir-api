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
    # Clase 1: Soluciones
    ## El Punto de Partida
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Total de muestras
    """)
    return


@app.cell
def _():
    duracion_1 = 3           # segundos
    sample_rate_1 = 48000    # Hz
    total_muestras_1 = sample_rate_1 * duracion_1

    print(f"Total de muestras: {total_muestras_1:,}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Tamano de archivo WAV
    """)
    return


@app.cell
def _():
    sr_2 = 44100
    duracion_2 = 5
    canales_2 = 2
    bit_depth_2 = 16

    tamano_bytes_2 = sr_2 * duracion_2 * canales_2 * (bit_depth_2 // 8)
    tamano_mb_2 = tamano_bytes_2 / (1024 * 1024)

    print(f"Tamano: {tamano_bytes_2:,} bytes = {tamano_mb_2:.2f} MB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Convertir segundos a mm:ss
    """)
    return


@app.cell
def _():
    duracion_seg_3 = 197
    minutos_3 = duracion_seg_3 // 60
    segundos_3 = duracion_seg_3 % 60

    resultado_3 = f"{minutos_3}:{segundos_3:02d}"
    print(f"{duracion_seg_3} segundos = {resultado_3}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Extraer extension de archivo
    """)
    return


@app.cell
def _():
    nombre_4 = "mi_cancion_final_v2.wav"

    # Metodo 1: usando split
    extension_4 = nombre_4.split(".")[-1]
    nombre_sin_ext_4 = nombre_4.split(".")[0]  # Ojo: falla si hay varios puntos

    # Metodo 2: usando rfind (mas robusto)
    punto_pos = nombre_4.rfind(".")
    extension_4b = nombre_4[punto_pos + 1:]
    nombre_sin_ext_4b = nombre_4[:punto_pos]

    print(f"Archivo: {nombre_4}")
    print(f"Extension: {extension_4}")
    print(f"Sin extension: {nombre_sin_ext_4b}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Frecuencia de una nota MIDI
    """)
    return


@app.cell
def _():
    notas_midi_5 = [60, 69, 72]
    nombres_5 = ["C4 (Do central)", "A4 (La 440)", "C5 (Do octava arriba)"]

    for midi, nombre in zip(notas_midi_5, nombres_5):
        freq = 440.0 * (2.0 ** ((midi - 69) / 12.0))
        print(f"MIDI {midi} ({nombre}): {freq:.2f} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: f-string descriptivo
    """)
    return


@app.cell
def _():
    titulo_6 = "Bohemian Rhapsody"
    artista_6 = "Queen"
    duracion_seg_6 = 354
    sample_rate_6 = 44100
    bit_depth_6 = 24

    min_6 = duracion_seg_6 // 60
    seg_6 = duracion_seg_6 % 60
    total_muestras_6 = sample_rate_6 * duracion_seg_6

    info_6 = f"""Pista: {titulo_6} - {artista_6}
Duracion: {min_6}:{seg_6:02d}
Formato: {sample_rate_6:,} Hz / {bit_depth_6} bits
Total muestras: {total_muestras_6:,}"""

    print(info_6)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Logica booleana para calidad de audio
    """)
    return


@app.cell
def _():
    sr_7 = 48000
    bits_7 = 24
    canales_7 = 2

    es_profesional_7 = sr_7 >= 44100 and bits_7 >= 16
    es_hd_7 = sr_7 >= 96000 or bits_7 >= 24
    es_surround_7 = canales_7 > 2
    calidad_ok_7 = es_profesional_7 and not es_surround_7

    print(f"SR: {sr_7}, Bits: {bits_7}, Canales: {canales_7}")
    print(f"Es profesional:    {es_profesional_7}")
    print(f"Es HD:             {es_hd_7}")
    print(f"Es surround:       {es_surround_7}")
    print(f"Calidad OK:        {calidad_ok_7}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Frecuencia de Nyquist
    """)
    return


@app.cell
def _():
    sample_rates_8 = [22050, 44100, 48000, 96000, 192000]

    for sr in sample_rates_8:
        nyquist = sr / 2
        print(f"SR: {sr:>6} Hz -> Nyquist: {nyquist:>8.1f} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio BONUS: Calculadora de latencia
    """)
    return


@app.cell
def _():
    configuraciones_bonus = [
        (64, 44100),
        (128, 44100),
        (256, 48000),
        (512, 96000),
    ]

    for buffer_size, sr in configuraciones_bonus:
        latencia_ms = (buffer_size / sr) * 1000
        print(f"Buffer: {buffer_size:>4} @ {sr:>5} Hz -> Latencia: {latencia_ms:.2f} ms")
    return


if __name__ == "__main__":
    app.run()
