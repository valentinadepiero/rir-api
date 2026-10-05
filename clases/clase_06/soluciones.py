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
    # Clase 6: Soluciones
    ## Audio en Python + Generacion de Senales
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import soundfile as sf
    return np, plt, sf


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Tono puro
    """)
    return


@app.cell
def _(np, plt, sf):
    # Ejercicio 1: Tono puro de 440 Hz
    sr_1 = 44100
    duracion_1 = 1.0
    frecuencia_1 = 440.0
    amplitud_1 = 0.5

    t_1 = np.linspace(0, duracion_1, int(sr_1 * duracion_1), endpoint=False)
    tono_1 = amplitud_1 * np.sin(2 * np.pi * frecuencia_1 * t_1)

    sf.write('/tmp/ej1_tono_440.wav', tono_1, sr_1)

    # Graficar primeros 10 ms
    n_10ms = int(0.01 * sr_1)
    fig_1, ax_1 = plt.subplots(figsize=(10, 3))
    ax_1.plot(t_1[:n_10ms] * 1000, tono_1[:n_10ms], 'b-')
    ax_1.set_xlabel('Tiempo (ms)')
    ax_1.set_ylabel('Amplitud')
    ax_1.set_title('Ejercicio 1: Tono puro 440 Hz (primeros 10 ms)')
    ax_1.grid(True, alpha=0.3)
    plt.tight_layout()

    print(f"Tono generado: {frecuencia_1} Hz, {duracion_1} s, sr={sr_1}")
    print(f"Muestras: {len(tono_1)}, Pico: {np.max(np.abs(tono_1)):.2f}")
    plt.gca()
    return (sr_1,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Audio estereo
    """)
    return


@app.cell
def _(np, plt, sf, sr_1):
    # Ejercicio 2: Estereo - izquierda 440 Hz, derecha 880 Hz
    duracion_2 = 2.0
    n_muestras_2 = int(sr_1 * duracion_2)
    t_2 = np.linspace(0, duracion_2, n_muestras_2, endpoint=False)

    canal_izq = 0.5 * np.sin(2 * np.pi * 440 * t_2)
    canal_der = 0.5 * np.sin(2 * np.pi * 880 * t_2)

    estereo = np.column_stack([canal_izq, canal_der])
    sf.write('/tmp/ej2_estereo.wav', estereo, sr_1)

    print(f"Shape del array estereo: {estereo.shape}")
    print(f"Canal izquierdo: 440 Hz, Canal derecho: 880 Hz")

    # Graficar primeros 10 ms
    n_vis = int(0.01 * sr_1)
    fig_2, axes_2 = plt.subplots(2, 1, figsize=(10, 4))
    axes_2[0].plot(t_2[:n_vis] * 1000, canal_izq[:n_vis], 'b-')
    axes_2[0].set_title('Canal izquierdo: 440 Hz')
    axes_2[0].set_ylabel('Amplitud')
    axes_2[0].grid(True, alpha=0.3)

    axes_2[1].plot(t_2[:n_vis] * 1000, canal_der[:n_vis], 'r-')
    axes_2[1].set_title('Canal derecho: 880 Hz')
    axes_2[1].set_xlabel('Tiempo (ms)')
    axes_2[1].set_ylabel('Amplitud')
    axes_2[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Ruido blanco normalizado
    """)
    return


@app.cell
def _(np, plt, sf, sr_1):
    # Ejercicio 3: Ruido blanco normalizado
    duracion_3 = 3.0
    n_muestras_3 = int(sr_1 * duracion_3)

    ruido_3 = np.random.randn(n_muestras_3)
    ruido_3 = ruido_3 / np.max(np.abs(ruido_3)) * 0.8

    sf.write('/tmp/ej3_ruido.wav', ruido_3, sr_1)

    pico_3 = np.max(np.abs(ruido_3))
    rms_3 = np.sqrt(np.mean(ruido_3**2))
    print(f"Valor pico: {pico_3:.4f}")
    print(f"Valor RMS: {rms_3:.4f}")
    print(f"Pico en dBFS: {20 * np.log10(pico_3):.1f} dB")
    print(f"RMS en dBFS: {20 * np.log10(rms_3):.1f} dB")

    fig_3, ax_3 = plt.subplots(figsize=(10, 3))
    ax_3.hist(ruido_3, bins=100, density=True, alpha=0.7, color='steelblue')
    ax_3.set_title(f'Distribucion del ruido blanco (RMS={rms_3:.4f}, Pico={pico_3:.4f})')
    ax_3.set_xlabel('Amplitud')
    ax_3.set_ylabel('Densidad')
    ax_3.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Tonos DTMF
    """)
    return


@app.cell
def _(np, plt, sf, sr_1):
    # Ejercicio 4: Tonos DTMF
    dtmf = {
        '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
        '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
        '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    }

    duracion_tono = 0.2
    duracion_silencio = 0.1
    secuencia = '123456789'

    senales_dtmf = []
    for digito in secuencia:
        f_low, f_high = dtmf[digito]
        t_d = np.linspace(0, duracion_tono, int(sr_1 * duracion_tono), endpoint=False)
        tono_dtmf = 0.3 * np.sin(2 * np.pi * f_low * t_d) + 0.3 * np.sin(2 * np.pi * f_high * t_d)
        senales_dtmf.append(tono_dtmf)
        # Silencio entre tonos
        silencio = np.zeros(int(sr_1 * duracion_silencio))
        senales_dtmf.append(silencio)

    dtmf_completo = np.concatenate(senales_dtmf)
    sf.write('/tmp/ej4_dtmf.wav', dtmf_completo, sr_1)

    print(f"Secuencia DTMF: {secuencia}")
    print(f"Duracion total: {len(dtmf_completo)/sr_1:.2f} s")

    fig_4, ax_4 = plt.subplots(figsize=(10, 3))
    t_dtmf = np.arange(len(dtmf_completo)) / sr_1
    ax_4.plot(t_dtmf, dtmf_completo, 'b-', linewidth=0.5)
    ax_4.set_title('Secuencia DTMF: 1-2-3-4-5-6-7-8-9')
    ax_4.set_xlabel('Tiempo (s)')
    ax_4.set_ylabel('Amplitud')
    ax_4.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Analisis de archivo WAV
    """)
    return


@app.cell
def _(np, sf):
    # Ejercicio 5: Analisis de archivo WAV
    data_5, sr_5 = sf.read('/tmp/ej4_dtmf.wav')
    info_5 = sf.info('/tmp/ej4_dtmf.wav')

    duracion_5 = len(data_5) / sr_5
    canales_5 = 1 if data_5.ndim == 1 else data_5.shape[1]
    pico_5 = np.max(np.abs(data_5))
    dbfs_5 = 20 * np.log10(pico_5) if pico_5 > 0 else float('-inf')

    print("=== Analisis de archivo WAV ===")
    print(f"  Archivo: /tmp/ej4_dtmf.wav")
    print(f"  Duracion: {duracion_5:.2f} segundos")
    print(f"  Canales: {canales_5}")
    print(f"  Sample rate: {sr_5} Hz")
    print(f"  Tipo de datos: {data_5.dtype}")
    print(f"  Formato: {info_5.subtype}")
    print(f"  Nivel pico: {pico_5:.4f} ({dbfs_5:.1f} dBFS)")
    print(f"  Total de muestras: {len(data_5):,}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Control de volumen
    """)
    return


@app.cell
def _(np, plt, sr_1):
    # Ejercicio 6: Control de volumen
    def control_volumen(senal, ganancia_db):
        """Aplica ganancia en dB a una senal, con clipping a [-1, 1]."""
        ganancia_lineal = 10 ** (ganancia_db / 20.0)
        senal_amplificada = senal * ganancia_lineal
        senal_clipped = np.clip(senal_amplificada, -1.0, 1.0)
        return senal_clipped

    # Generar tono de prueba
    t_6 = np.linspace(0, 0.01, int(sr_1 * 0.01), endpoint=False)
    tono_6 = 0.3 * np.sin(2 * np.pi * 440 * t_6)

    ganancias = [-6, 0, 6, 20]
    colores = ['blue', 'green', 'orange', 'red']

    fig_6, ax_6 = plt.subplots(figsize=(10, 4))
    for g, color in zip(ganancias, colores):
        resultado = control_volumen(tono_6, g)
        g_lineal = 10 ** (g / 20.0)
        ax_6.plot(t_6[:int(0.005 * sr_1)] * 1000, resultado[:int(0.005 * sr_1)],
                  color=color, label=f'{g:+d} dB (x{g_lineal:.2f})')

    ax_6.set_xlabel('Tiempo (ms)')
    ax_6.set_ylabel('Amplitud')
    ax_6.set_title('Control de volumen con diferentes ganancias')
    ax_6.legend()
    ax_6.grid(True, alpha=0.3)
    ax_6.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3)
    ax_6.axhline(y=-1.0, color='gray', linestyle='--', alpha=0.3)
    plt.tight_layout()

    print("Nota: con +20 dB, la senal se clipea (se aplana en +-1.0)")
    plt.gca()
    return (control_volumen,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Barrido de senos (sine sweep)
    """)
    return


@app.cell
def _(np, plt, sf, sr_1):
    # Ejercicio 7: Barrido de senos logaritmico
    duracion_7 = 5.0
    f1_7 = 20.0
    f2_7 = 20000.0
    n_7 = int(sr_1 * duracion_7)
    t_7 = np.linspace(0, duracion_7, n_7, endpoint=False)

    # Barrido logaritmico
    sweep_7 = 0.5 * np.sin(
        2 * np.pi * f1_7 * duracion_7 / np.log(f2_7 / f1_7) *
        (np.exp(t_7 / duracion_7 * np.log(f2_7 / f1_7)) - 1)
    )

    sf.write('/tmp/ej7_sweep.wav', sweep_7, sr_1)

    # Tres zooms
    fig_7, axes_7 = plt.subplots(3, 1, figsize=(10, 7))

    # Inicio (frecuencias bajas)
    n_zoom_7 = int(0.1 * sr_1)
    axes_7[0].plot(t_7[:n_zoom_7] * 1000, sweep_7[:n_zoom_7], 'b-')
    axes_7[0].set_title('Inicio del barrido (0-100 ms, frecuencias bajas)')
    axes_7[0].set_xlabel('Tiempo (ms)')
    axes_7[0].set_ylabel('Amplitud')
    axes_7[0].grid(True, alpha=0.3)

    # Medio
    medio = n_7 // 2
    axes_7[1].plot((t_7[medio:medio+n_zoom_7] - t_7[medio]) * 1000,
                   sweep_7[medio:medio+n_zoom_7], 'g-')
    axes_7[1].set_title(f'Medio del barrido (t={duracion_7/2:.1f} s, frecuencias medias)')
    axes_7[1].set_xlabel('Tiempo relativo (ms)')
    axes_7[1].set_ylabel('Amplitud')
    axes_7[1].grid(True, alpha=0.3)

    # Final (frecuencias altas)
    axes_7[2].plot((t_7[-n_zoom_7:] - t_7[-n_zoom_7]) * 1000,
                   sweep_7[-n_zoom_7:], 'r-', linewidth=0.5)
    axes_7[2].set_title('Final del barrido (frecuencias altas)')
    axes_7[2].set_xlabel('Tiempo relativo (ms)')
    axes_7[2].set_ylabel('Amplitud')
    axes_7[2].grid(True, alpha=0.3)

    plt.tight_layout()
    print(f"Barrido logaritmico: {f1_7} Hz -> {f2_7} Hz, {duracion_7} s")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Reproduccion y grabacion simultanea (concepto)
    """)
    return


@app.cell
def _(np, sr_1):
    # Ejercicio 8: Concepto de playrec
    print("=== Reproduccion y grabacion simultanea ===\n")

    # Codigo conceptual (comentado para no requerir hardware)
    print("# 1. Generar barrido de senos de 3 segundos")
    print("duracion = 3.0")
    print("t = np.linspace(0, duracion, int(sr * duracion), endpoint=False)")
    print("f1, f2 = 20.0, 20000.0")
    print("sweep = 0.5 * np.sin(2*np.pi*f1*duracion/np.log(f2/f1) * (np.exp(t/duracion*np.log(f2/f1)) - 1))")
    print()
    print("# 2. Reproducir y grabar simultaneamente")
    print("import sounddevice as sd")
    print("grabacion = sd.playrec(sweep, samplerate=sr, channels=1)")
    print("sd.wait()  # Esperar a que termine")
    print()
    print("# 3. Guardar ambas senales")
    print("sf.write('sweep_emitido.wav', sweep, sr)")
    print("sf.write('respuesta_grabada.wav', grabacion, sr)")

    print("\n=== Respuestas a las preguntas ===\n")

    print("P: Que pasa si el sample rate no coincide con el del dispositivo?")
    print("R: sounddevice hace resampling automatico, pero esto puede introducir")
    print("   artefactos. Es mejor usar el sample rate nativo del dispositivo")
    print("   (tipicamente 44100 o 48000 Hz).\n")

    print("P: Que efecto tiene el blocksize en la latencia?")
    print("R: blocksize define cuantas muestras se procesan por bloque.")
    print("   - Menor blocksize = menor latencia pero mas carga de CPU")
    print("   - Mayor blocksize = mayor latencia pero mas eficiente")
    print(f"   - Ejemplo: blocksize=512 a {sr_1} Hz = {512/sr_1*1000:.1f} ms de latencia\n")

    print("P: Por que usar playrec() en vez de play() + rec() por separado?")
    print("R: playrec() garantiza sincronizacion exacta entre reproduccion y")
    print("   grabacion (usan el mismo reloj de la placa de sonido). Con play()")
    print("   y rec() por separado, hay un desfase temporal impredecible que")
    print("   arruina la medicion de la respuesta al impulso.")
    return


if __name__ == "__main__":
    app.run()
