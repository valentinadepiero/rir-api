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
    # Senales y Sistemas - Clase 6
    ## Audio en Python + Generacion de Senales

    **Fecha**: 5 de mayo de 2026 | **Pilares**: P1 (principal), P3 (principal)

    En esta clase vamos a:
    1. Entender los fundamentos del audio digital
    2. Aprender a usar librerias de Python para audio
    3. Generar senales de audio en la practica
    4. Trabajar con grabacion y reproduccion simultanea
    5. Usar IA para debugging de codigo de audio
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Fundamentos del Audio Digital

    ### Teorema de Muestreo (Nyquist-Shannon)

    Para digitalizar una senal analogica, la muestreamos a una frecuencia $f_s$ (sample rate).

    **Teorema**: Para reconstruir una senal sin perdida, la frecuencia de muestreo debe ser al menos el doble de la frecuencia maxima presente en la senal:

    $$f_s \geq 2 \cdot f_{max}$$

    La **frecuencia de Nyquist** es $f_N = f_s / 2$, y representa la maxima frecuencia representable.

    | Sample Rate | Frecuencia de Nyquist | Uso tipico |
    |-------------|----------------------|------------|
    | 8000 Hz | 4000 Hz | Telefonia |
    | 22050 Hz | 11025 Hz | Radio AM |
    | 44100 Hz | 22050 Hz | CD de audio |
    | 48000 Hz | 24000 Hz | Video/cine |
    | 96000 Hz | 48000 Hz | Audio profesional |

    ### Aliasing

    Si muestreamos con $f_s$ insuficiente, las frecuencias altas se "disfrazan" como frecuencias bajas. Esto es **aliasing** y es irreversible.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np, plt):
    # Demostracion de aliasing
    # Senal original: seno de 900 Hz
    f_senal = 900  # Hz
    t_continuo = np.linspace(0, 0.01, 10000)
    senal_continua = np.sin(2 * np.pi * f_senal * t_continuo)

    # Muestreo correcto: fs = 8000 Hz (Nyquist = 4000 > 900)
    fs_ok = 8000
    t_ok = np.arange(0, 0.01, 1/fs_ok)
    senal_ok = np.sin(2 * np.pi * f_senal * t_ok)

    # Muestreo con aliasing: fs = 1000 Hz (Nyquist = 500 < 900)
    fs_alias = 1000
    t_alias = np.arange(0, 0.01, 1/fs_alias)
    senal_alias = np.sin(2 * np.pi * f_senal * t_alias)
    # La frecuencia percibida sera |900 - 1000| = 100 Hz

    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    axes[0].plot(t_continuo * 1000, senal_continua, 'b-', alpha=0.3, label='Senal original (900 Hz)')
    axes[0].stem(t_ok * 1000, senal_ok, linefmt='g-', markerfmt='go', basefmt='g-', label=f'Muestreo fs={fs_ok} Hz (OK)')
    axes[0].set_title('Muestreo correcto: fs = 8000 Hz')
    axes[0].set_xlabel('Tiempo (ms)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t_continuo * 1000, senal_continua, 'b-', alpha=0.3, label='Senal original (900 Hz)')
    axes[1].stem(t_alias * 1000, senal_alias, linefmt='r-', markerfmt='ro', basefmt='r-', label=f'Muestreo fs={fs_alias} Hz (ALIAS)')
    # Mostrar la frecuencia aliased
    f_alias_result = abs(f_senal - fs_alias)
    senal_alias_reconstruida = np.sin(2 * np.pi * f_alias_result * t_continuo)
    axes[1].plot(t_continuo * 1000, senal_alias_reconstruida, 'r--', alpha=0.5, label=f'Frecuencia percibida: {f_alias_result} Hz')
    axes[1].set_title(f'Aliasing: fs = {fs_alias} Hz -> se percibe {f_alias_result} Hz')
    axes[1].set_xlabel('Tiempo (ms)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Profundidad de Bits (Bit Depth)

    La **profundidad de bits** determina cuantos niveles de amplitud podemos representar:

    - $N$ bits $\rightarrow$ $2^N$ niveles posibles

    El **rango dinamico** se calcula como:

    $$DR = 6.02 \times N + 1.76 \text{ dB}$$

    | Bit Depth | Niveles | Rango Dinamico | Uso |
    |-----------|---------|----------------|-----|
    | 8 bits | 256 | 49.9 dB | Telefonia antigua |
    | 16 bits | 65,536 | 98.1 dB | CD de audio |
    | 24 bits | 16,777,216 | 146.2 dB | Estudio profesional |
    | 32-bit float | ~$10^{38}$ | ~1500 dB* | Procesamiento interno |

    *32-bit float tiene un rango dinamico practicamente ilimitado por su representacion en punto flotante.

    ### Representacion PCM

    **PCM** (*Pulse Code Modulation*) es el formato estandar de audio digital sin compresion:
    - Cada muestra es un numero que representa la amplitud
    - **int16**: valores de -32768 a 32767
    - **float32**: valores de -1.0 a 1.0 (normalizado)

    ### Canales
    - **Mono**: 1 canal
    - **Estereo**: 2 canales (izquierdo, derecho)
    - En numpy: mono es un array 1D, estereo es un array 2D con shape `(N, 2)`

    ### Formatos de archivo
    | Formato | Compresion | Calidad | Tamano |
    |---------|-----------|---------|--------|
    | WAV | Sin compresion | Perfecta | Grande |
    | FLAC | Lossless | Perfecta | ~60% del WAV |
    | MP3 | Lossy | Buena* | ~10% del WAV |
    | OGG | Lossy | Buena* | ~10% del WAV |

    *La calidad depende del bitrate seleccionado.
    """)
    return


@app.cell
def _(np):
    # Demostracion de rango dinamico
    for bits in [8, 16, 24, 32]:
        niveles = 2**bits
        dr = 6.02 * bits + 1.76
        print(f"{bits:2d} bits -> {niveles:>12,} niveles -> {dr:.1f} dB de rango dinamico")

    # Tamano de archivo WAV
    print("\n--- Tamano de un archivo WAV de 1 minuto, estereo, 44100 Hz ---")
    for bits in [16, 24, 32]:
        tamano_bytes = 44100 * 60 * 2 * (bits // 8)
        tamano_mb = tamano_bytes / (1024 * 1024)
        print(f"{bits} bits: {tamano_mb:.1f} MB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Librerias de Audio en Python

    Vamos a trabajar con tres librerias principales para audio en Python.

    | Libreria | Lectura/Escritura | Reproduccion | Grabacion | Mejor para |
    |----------|------------------|-------------|-----------|------------|
    | `soundfile` | WAV, FLAC, OGG | No | No | I/O de archivos |
    | `sounddevice` | No | Si | Si | Reproduccion y grabacion en tiempo real |
    | `scipy.io.wavfile` | Solo WAV | No | No | Lectura rapida de WAV |

    ### 2.1 soundfile: Lectura y escritura de archivos
    """)
    return


@app.cell
def _(np):
    import soundfile as sf

    # Crear una senal de ejemplo para guardar
    sr = 44100
    duracion = 1.0
    t = np.linspace(0, duracion, int(sr * duracion), endpoint=False)
    senal_ejemplo = 0.5 * np.sin(2 * np.pi * 440 * t)  # La 440 Hz

    # Guardar como WAV
    sf.write('/tmp/ejemplo_440hz.wav', senal_ejemplo, sr)
    print(f"Archivo guardado: /tmp/ejemplo_440hz.wav")

    # Leer el archivo
    data, sr_leido = sf.read('/tmp/ejemplo_440hz.wav')
    print(f"Sample rate: {sr_leido} Hz")
    print(f"Duracion: {len(data)/sr_leido:.2f} segundos")
    print(f"Muestras: {len(data)}")
    print(f"Tipo de datos: {data.dtype}")
    print(f"Rango: [{data.min():.4f}, {data.max():.4f}]")

    # Obtener informacion sin leer todo el archivo
    info = sf.info('/tmp/ejemplo_440hz.wav')
    print(f"\nInfo del archivo:")
    print(f"  Formato: {info.format}")
    print(f"  Subformato: {info.subtype}")
    print(f"  Canales: {info.channels}")
    print(f"  Duracion: {info.duration:.2f} s")
    return data, duracion, info, sf, sr, sr_leido, t


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.2 sounddevice: Reproduccion y grabacion

    `sounddevice` permite reproducir y grabar audio usando la placa de sonido del sistema.
    """)
    return


@app.cell
def _(np, sr):
    import sounddevice as sd

    # Crear un tono para reproducir
    t_play = np.linspace(0, 0.5, int(sr * 0.5), endpoint=False)
    tono = 0.3 * np.sin(2 * np.pi * 440 * t_play)

    # Reproducir (descomentar para escuchar)
    # sd.play(tono, sr)
    # sd.wait()  # Esperar a que termine

    print("sounddevice - Funciones principales:")
    print("  sd.play(data, sr)    -> Reproduce audio")
    print("  sd.wait()            -> Espera a que termine la reproduccion")
    print("  sd.stop()            -> Detiene la reproduccion")
    print("  sd.rec(frames, ...)  -> Graba audio")
    print("  sd.playrec(data, sr) -> Reproduce y graba simultaneamente")

    # Mostrar dispositivos disponibles
    print(f"\nDispositivo de entrada por defecto: {sd.default.device[0]}")
    print(f"Dispositivo de salida por defecto: {sd.default.device[1]}")
    return sd, t_play, tono


@app.cell
def _(sd, sr):
    # Grabacion (concepto - requiere microfono)
    duracion_grab = 2  # segundos
    print("--- Ejemplo de grabacion ---")
    print(f"grabacion = sd.rec(int({duracion_grab} * {sr}), samplerate={sr}, channels=1)")
    print("sd.wait()  # Esperar a que termine la grabacion")
    print(f"# grabacion.shape seria ({duracion_grab * sr}, 1)")

    # Si quisieramos grabar de verdad:
    # grabacion = sd.rec(int(duracion_grab * sr), samplerate=sr, channels=1)
    # sd.wait()
    return (duracion_grab,)


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.3 scipy.io.wavfile: Lectura simple de WAV
    """)
    return


@app.cell
def _():
    from scipy.io import wavfile

    # Leer archivo WAV con scipy
    sr_scipy, data_scipy = wavfile.read('/tmp/ejemplo_440hz.wav')
    print(f"scipy.io.wavfile.read:")
    print(f"  Sample rate: {sr_scipy} Hz")
    print(f"  Shape: {data_scipy.shape}")
    print(f"  Dtype: {data_scipy.dtype}")
    print(f"  Rango: [{data_scipy.min():.4f}, {data_scipy.max():.4f}]")
    print()
    print("ATENCION: scipy devuelve int16 o float dependiendo del archivo.")
    print("soundfile SIEMPRE devuelve float64 normalizado [-1, 1].")
    print("Esto es una fuente comun de bugs!")
    return data_scipy, sr_scipy, wavfile


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Generacion de Senales de Audio en Practica

    Ahora vamos a generar senales de audio utiles y guardarlas como archivos WAV.

    ### 3.1 Tono puro: La 440 Hz (A4)
    """)
    return


@app.cell
def _(np, plt, sf):
    # Generar un tono puro de 440 Hz (La4 / A4)
    sr_gen = 44100
    duracion_gen = 2.0
    frecuencia_gen = 440.0  # A4

    t_gen = np.linspace(0, duracion_gen, int(sr_gen * duracion_gen), endpoint=False)
    tono_puro = 0.5 * np.sin(2 * np.pi * frecuencia_gen * t_gen)

    # Guardar
    sf.write('/tmp/tono_440hz.wav', tono_puro, sr_gen)

    # Visualizar los primeros 10 ms
    muestras_vis = int(0.01 * sr_gen)  # 10 ms
    fig_tono, ax_tono = plt.subplots(figsize=(10, 3))
    ax_tono.plot(t_gen[:muestras_vis] * 1000, tono_puro[:muestras_vis], 'b-')
    ax_tono.set_xlabel('Tiempo (ms)')
    ax_tono.set_ylabel('Amplitud')
    ax_tono.set_title('Tono puro: 440 Hz (A4) - primeros 10 ms')
    ax_tono.grid(True, alpha=0.3)
    ax_tono.set_ylim(-0.7, 0.7)
    plt.tight_layout()
    plt.gca()
    return duracion_gen, frecuencia_gen, sr_gen, t_gen


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.2 Acorde: La Mayor (A Major)

    Un acorde es la suma de varias frecuencias simultaneas. La Mayor = A4 + C#5 + E5
    """)
    return


@app.cell
def _(np, plt, sf, sr_gen, t_gen):
    # Acorde La Mayor: A4 (440 Hz) + C#5 (554.37 Hz) + E5 (659.25 Hz)
    frecuencias_acorde = [440.0, 554.37, 659.25]
    nombres_notas = ['A4', 'C#5', 'E5']

    acorde = np.zeros_like(t_gen)
    for f in frecuencias_acorde:
        acorde += 0.3 * np.sin(2 * np.pi * f * t_gen)

    # Normalizar para evitar clipping
    acorde = acorde / np.max(np.abs(acorde)) * 0.8

    sf.write('/tmp/acorde_la_mayor.wav', acorde, sr_gen)

    # Visualizar
    muestras_acorde = int(0.02 * sr_gen)  # 20 ms
    fig_ac, axes_ac = plt.subplots(2, 1, figsize=(10, 5))

    # Notas individuales
    for f, nombre in zip(frecuencias_acorde, nombres_notas):
        nota = 0.3 * np.sin(2 * np.pi * f * t_gen[:muestras_acorde])
        axes_ac[0].plot(t_gen[:muestras_acorde] * 1000, nota, alpha=0.7, label=f'{nombre} ({f} Hz)')
    axes_ac[0].set_title('Notas individuales del acorde La Mayor')
    axes_ac[0].set_ylabel('Amplitud')
    axes_ac[0].legend()
    axes_ac[0].grid(True, alpha=0.3)

    # Acorde completo
    axes_ac[1].plot(t_gen[:muestras_acorde] * 1000, acorde[:muestras_acorde], 'purple')
    axes_ac[1].set_title('Acorde La Mayor (suma de las 3 notas)')
    axes_ac[1].set_xlabel('Tiempo (ms)')
    axes_ac[1].set_ylabel('Amplitud')
    axes_ac[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.3 Ruido blanco
    """)
    return


@app.cell
def _(np, plt, sf, sr_gen):
    # Generar ruido blanco
    duracion_ruido = 3.0
    n_muestras_ruido = int(sr_gen * duracion_ruido)
    ruido = np.random.randn(n_muestras_ruido)

    # Normalizar para que el pico sea 0.8
    ruido = ruido / np.max(np.abs(ruido)) * 0.8

    sf.write('/tmp/ruido_blanco.wav', ruido, sr_gen)
    print(f"Ruido blanco generado: {duracion_ruido} s, pico = {np.max(np.abs(ruido)):.2f}")

    # Visualizar
    fig_ruido, axes_ruido = plt.subplots(2, 1, figsize=(10, 5))

    # Forma de onda (primeros 50 ms)
    muestras_r = int(0.05 * sr_gen)
    t_ruido = np.arange(muestras_r) / sr_gen * 1000
    axes_ruido[0].plot(t_ruido, ruido[:muestras_r], 'gray', linewidth=0.5)
    axes_ruido[0].set_title('Ruido blanco - forma de onda (50 ms)')
    axes_ruido[0].set_xlabel('Tiempo (ms)')
    axes_ruido[0].set_ylabel('Amplitud')
    axes_ruido[0].grid(True, alpha=0.3)

    # Histograma (distribucion gaussiana)
    axes_ruido[1].hist(ruido, bins=100, density=True, alpha=0.7, color='steelblue')
    axes_ruido[1].set_title('Distribucion del ruido (debe ser gaussiana)')
    axes_ruido[1].set_xlabel('Amplitud')
    axes_ruido[1].set_ylabel('Densidad')
    axes_ruido[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.4 Click / Impulso

    Un impulso (delta de Kronecker) es una senal que vale 1 en un solo instante y 0 en todos los demas. Es fundamental para medir sistemas LTI.
    """)
    return


@app.cell
def _(np, plt, sf, sr_gen):
    # Generar un click (impulso)
    duracion_click = 0.5  # segundos
    n_click = int(sr_gen * duracion_click)
    click = np.zeros(n_click)
    click[int(0.1 * sr_gen)] = 1.0  # Impulso en t = 0.1 s

    sf.write('/tmp/click.wav', click, sr_gen)

    # Tambien un click mas "realista" (pulso corto)
    click_real = np.zeros(n_click)
    idx_inicio = int(0.1 * sr_gen)
    pulso = np.hanning(44)  # Pulso de ~1 ms con ventana de Hanning
    click_real[idx_inicio:idx_inicio + len(pulso)] = pulso * 0.9

    sf.write('/tmp/click_real.wav', click_real, sr_gen)

    fig_click, axes_click = plt.subplots(2, 1, figsize=(10, 4))

    t_click = np.arange(n_click) / sr_gen * 1000
    axes_click[0].plot(t_click, click, 'b-')
    axes_click[0].set_title('Impulso ideal (delta de Kronecker)')
    axes_click[0].set_ylabel('Amplitud')
    axes_click[0].grid(True, alpha=0.3)

    axes_click[1].plot(t_click, click_real, 'r-')
    axes_click[1].set_title('Click realista (pulso corto con ventana Hanning)')
    axes_click[1].set_xlabel('Tiempo (ms)')
    axes_click[1].set_ylabel('Amplitud')
    axes_click[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Reproduccion y Grabacion Simultanea

    Para medir la acustica de una sala (como en el TP), necesitamos:
    1. **Reproducir** una senal conocida (ej: barrido de senos)
    2. **Grabar** la respuesta de la sala simultaneamente

    Esto se hace con `sd.playrec()`:

    ```python
    import sounddevice as sd

    # Reproducir senal y grabar al mismo tiempo
    grabacion = sd.playrec(senal_a_reproducir, samplerate=sr, channels=1)
    sd.wait()
    ```

    ### Conceptos importantes:

    - **Latencia**: tiempo entre que el programa envia audio y se escucha. Depende del buffer.
    - **Buffer size**: cantidad de muestras procesadas por bloque. Menor buffer = menor latencia, pero mas carga de CPU.
    - **Sincronizacion**: `playrec` garantiza que reproduccion y grabacion estan sincronizadas (misma placa de sonido).

    ### Conexion con el TP

    En el trabajo practico de acustica de salas:
    1. Generan un **barrido de senos** (sine sweep)
    2. Lo reproducen en la sala con un parlante
    3. Graban con un microfono la respuesta de la sala
    4. Procesan la grabacion para obtener la **respuesta al impulso** de la sala
    5. A partir de la respuesta al impulso, calculan parametros acusticos (T60, etc.)

    `sd.playrec()` es la funcion clave para los pasos 2 y 3.
    """)
    return


@app.cell
def _(np, plt, sf, sr_gen):
    # Ejemplo: generar un barrido de senos (sine sweep) logaritmico
    duracion_sweep = 5.0
    f_inicio = 20.0
    f_fin = 20000.0
    n_sweep = int(sr_gen * duracion_sweep)
    t_sweep = np.linspace(0, duracion_sweep, n_sweep, endpoint=False)

    # Barrido logaritmico
    sweep = 0.5 * np.sin(
        2 * np.pi * f_inicio * duracion_sweep / np.log(f_fin / f_inicio) *
        (np.exp(t_sweep / duracion_sweep * np.log(f_fin / f_inicio)) - 1)
    )

    sf.write('/tmp/sweep_20_20k.wav', sweep, sr_gen)

    # Visualizar
    fig_sw, axes_sw = plt.subplots(3, 1, figsize=(10, 7))

    # Forma de onda completa
    axes_sw[0].plot(t_sweep, sweep, 'b-', linewidth=0.3)
    axes_sw[0].set_title('Barrido de senos logaritmico (20 Hz - 20 kHz, 5 s)')
    axes_sw[0].set_xlabel('Tiempo (s)')
    axes_sw[0].set_ylabel('Amplitud')
    axes_sw[0].grid(True, alpha=0.3)

    # Zoom al inicio (frecuencias bajas)
    n_zoom = int(0.1 * sr_gen)
    axes_sw[1].plot(t_sweep[:n_zoom] * 1000, sweep[:n_zoom], 'b-')
    axes_sw[1].set_title('Zoom: inicio del barrido (frecuencias bajas)')
    axes_sw[1].set_xlabel('Tiempo (ms)')
    axes_sw[1].set_ylabel('Amplitud')
    axes_sw[1].grid(True, alpha=0.3)

    # Zoom al final (frecuencias altas)
    axes_sw[2].plot(t_sweep[-n_zoom:] * 1000 + (duracion_sweep - 0.1) * 1000, sweep[-n_zoom:], 'b-', linewidth=0.5)
    axes_sw[2].set_title('Zoom: final del barrido (frecuencias altas)')
    axes_sw[2].set_xlabel('Tiempo (ms)')
    axes_sw[2].set_ylabel('Amplitud')
    axes_sw[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return duracion_sweep, f_fin, f_inicio


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. IA para Debugging de Codigo de Audio (P2)

    Los errores en codigo de audio son particularmente dificiles de detectar porque el programa puede correr sin errores, pero el resultado **suena mal**. Veamos los errores mas comunes:

    ### Error 1: Sample rate incorrecto -> cambio de tono
    """)
    return


@app.cell
def _(np, plt, sf):
    # Error clasico: guardar con sample rate incorrecto
    sr_original = 44100
    t_bug1 = np.linspace(0, 1.0, sr_original, endpoint=False)
    tono_original = 0.5 * np.sin(2 * np.pi * 440 * t_bug1)

    # Guardamos con sr correcto
    sf.write('/tmp/tono_sr_correcto.wav', tono_original, 44100)

    # ERROR: guardamos con sr incorrecto (la mitad)
    sf.write('/tmp/tono_sr_incorrecto.wav', tono_original, 22050)

    print("Senal original: 440 Hz, 1 segundo, sr=44100")
    print()
    print("BUG: si guardamos con sr=22050:")
    print("  - La duracion se DUPLICA (2 segundos en vez de 1)")
    print("  - La frecuencia se REDUCE a la mitad (220 Hz en vez de 440 Hz)")
    print("  - El tono suena una octava mas grave!")
    print()
    print("Este error es muy comun y dificil de detectar si no se verifica.")

    fig_bug1, axes_bug1 = plt.subplots(2, 1, figsize=(10, 4))
    ms = 20
    n_ms = int(ms * sr_original / 1000)

    axes_bug1[0].plot(t_bug1[:n_ms] * 1000, tono_original[:n_ms])
    axes_bug1[0].set_title('Correcto: 440 Hz interpretado a 44100 Hz')
    axes_bug1[0].grid(True, alpha=0.3)

    t_mal = np.linspace(0, 2.0, sr_original, endpoint=False)
    axes_bug1[1].plot(t_mal[:n_ms] * 1000, tono_original[:n_ms])
    axes_bug1[1].set_title('BUG: 440 Hz interpretado a 22050 Hz -> suena como 220 Hz')
    axes_bug1[1].set_xlabel('Tiempo (ms)')
    axes_bug1[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Error 2: Clipping por no normalizar
    """)
    return


@app.cell
def _(np, plt):
    # Error: sumar senales sin normalizar -> clipping
    sr_bug2 = 44100
    t_bug2 = np.linspace(0, 0.02, int(sr_bug2 * 0.02), endpoint=False)

    # Sumamos 5 senales de amplitud 0.5 cada una
    senal_suma = np.zeros_like(t_bug2)
    freqs_bug = [200, 400, 600, 800, 1000]
    for f in freqs_bug:
        senal_suma += 0.5 * np.sin(2 * np.pi * f * t_bug2)

    # Clipping duro a [-1, 1]
    senal_clipped = np.clip(senal_suma, -1.0, 1.0)

    # Normalizacion correcta
    senal_normalizada = senal_suma / np.max(np.abs(senal_suma)) * 0.9

    fig_bug2, axes_bug2 = plt.subplots(3, 1, figsize=(10, 6))

    axes_bug2[0].plot(t_bug2 * 1000, senal_suma, 'b-')
    axes_bug2[0].set_title(f'Suma de 5 senos (sin normalizar, pico = {np.max(np.abs(senal_suma)):.2f})')
    axes_bug2[0].grid(True, alpha=0.3)
    axes_bug2[0].axhline(y=1.0, color='r', linestyle='--', alpha=0.5)
    axes_bug2[0].axhline(y=-1.0, color='r', linestyle='--', alpha=0.5)

    axes_bug2[1].plot(t_bug2 * 1000, senal_clipped, 'r-')
    axes_bug2[1].set_title('BUG: Clipping (distorsion!)')
    axes_bug2[1].grid(True, alpha=0.3)

    axes_bug2[2].plot(t_bug2 * 1000, senal_normalizada, 'g-')
    axes_bug2[2].set_title('Correcto: Normalizado a 0.9')
    axes_bug2[2].set_xlabel('Tiempo (ms)')
    axes_bug2[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Error 3: Tipo de datos incorrecto (int16 vs float32)
    """)
    return


@app.cell
def _(np):
    # Demostracion del problema de tipos de datos
    print("--- Representaciones de audio ---")
    print()

    # float32: rango [-1.0, 1.0]
    muestra_float = np.float32(0.5)
    print(f"float32: {muestra_float} (rango tipico: -1.0 a 1.0)")

    # int16: rango [-32768, 32767]
    muestra_int16 = np.int16(16384)  # equivale a 0.5 en float
    print(f"int16:   {muestra_int16} (rango: -32768 a 32767)")
    print(f"         {muestra_int16} en int16 = {muestra_int16/32768:.4f} en float")

    print()
    print("ERROR COMUN:")
    print("  Leer un archivo int16 con scipy y tratar los valores como float.")
    print("  Una muestra de valor 16384 (que es 0.5 normalizado) se interpreta")
    print("  como amplitud 16384.0, causando distorsion masiva!")
    print()
    print("SOLUCION: Siempre verificar dtype y convertir si es necesario:")
    print("  data_float = data_int16.astype(np.float32) / 32768.0")

    # Conversion correcta
    senal_int16 = np.array([0, 8192, 16384, 32767, -32768], dtype=np.int16)
    senal_float = senal_int16.astype(np.float32) / 32768.0
    print()
    print("Ejemplo de conversion:")
    for i16, f32 in zip(senal_int16, senal_float):
        print(f"  int16: {i16:>6d}  ->  float32: {f32:>7.4f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Template para pedir ayuda a la IA

    Cuando tengas un error en codigo de audio, usa este template:

    ```
    Tengo un problema con mi codigo de audio en Python.

    **Que deberia hacer**: [descripcion del comportamiento esperado]
    **Que hace realmente**: [descripcion del problema - suena mal, hay ruido, etc.]

    **Mi codigo**:
    [pegar codigo relevante]

    **Informacion de la senal**:
    - Sample rate: [44100 Hz, etc.]
    - Tipo de datos: [float32, int16, etc.]
    - Shape del array: [ej: (44100,) para 1 segundo mono]
    - Rango de valores: [ej: min=-0.5, max=0.5]

    **Error** (si hay):
    [pegar error completo]
    ```

    Cuanta mas informacion des, mejor sera la respuesta de la IA.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy aprendimos:

    1. **Fundamentos del audio digital**: muestreo (Nyquist), bit depth (rango dinamico), PCM, formatos
    2. **Librerias de Python**:
       - `soundfile`: lectura/escritura de archivos
       - `sounddevice`: reproduccion y grabacion
       - `scipy.io.wavfile`: lectura simple de WAV
    3. **Generacion de senales**: tonos puros, acordes, ruido, clicks, barridos
    4. **Reproduccion y grabacion simultanea**: `sd.playrec()` para mediciones acusticas
    5. **Debugging de audio**: errores comunes y como usar IA para resolverlos

    ### Para la proxima clase
    - Completar los 8 ejercicios de `ejercicios.py`
    - Avanzar con el Milestone 1 del TP
    """)
    return


if __name__ == "__main__":
    app.run()
