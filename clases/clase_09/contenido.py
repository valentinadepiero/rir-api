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
    # Senales y Sistemas - Clase 9
    ## Frecuencia y Filtros

    **Fecha**: 26 de mayo de 2026 | **Pilares**: P1 (principal), P3 (principal)

    En esta clase vamos a:
    1. Entender la DFT/FFT y el dominio de la frecuencia
    2. Analizar espectros de senales reales
    3. Crear espectrogramas
    4. Disenar filtros digitales
    5. Implementar filtros de bandas de octava (IEC 61260)
    6. Usar IA para investigar normas tecnicas
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import signal
    from scipy.fft import fft, fftfreq, rfft, rfftfreq
    return np, plt, signal, fft, fftfreq, rfft, rfftfreq


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. La Transformada Discreta de Fourier (DFT/FFT)

    ### Idea fundamental

    Cualquier senal periodica se puede descomponer en una suma de sinusoides.
    La **DFT** nos dice **que frecuencias** estan presentes y con **que amplitud y fase**.

    La formula de la DFT es:

    $$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j 2\pi k n / N}$$

    donde:
    - $x[n]$ es la senal en el tiempo (N muestras)
    - $X[k]$ es el coeficiente de la frecuencia $k$-esima
    - $|X[k]|$ es la **magnitud** (amplitud de esa frecuencia)
    - $\angle X[k]$ es la **fase**

    ### FFT: Fast Fourier Transform

    La FFT es un **algoritmo rapido** para calcular la DFT. En vez de $O(N^2)$ operaciones, usa $O(N \log N)$.

    En NumPy:
    - `np.fft.fft(x)` — FFT completa (frecuencias positivas y negativas)
    - `np.fft.rfft(x)` — FFT solo frecuencias positivas (para senales reales)
    - `np.fft.fftfreq(N, d=1/fs)` — eje de frecuencias
    - `np.fft.rfftfreq(N, d=1/fs)` — eje de frecuencias positivas
    """)
    return


@app.cell
def _(np, plt, fft, fftfreq):
    # Ejemplo basico: FFT de un tono puro
    fs_1 = 44100
    duracion_1 = 1.0
    N_1 = int(fs_1 * duracion_1)
    t_1 = np.arange(N_1) / fs_1

    # Senal: tono puro de 440 Hz
    f0_1 = 440
    x_1 = np.sin(2 * np.pi * f0_1 * t_1)

    # Calcular FFT
    X_1 = fft(x_1)
    freqs_1 = fftfreq(N_1, d=1/fs_1)

    # Magnitud (normalizada)
    magnitud_1 = np.abs(X_1) / N_1

    fig_1, axes_1 = plt.subplots(2, 1, figsize=(12, 6))

    # Senal en el tiempo (primeros 10 ms)
    n_10ms = int(0.01 * fs_1)
    axes_1[0].plot(t_1[:n_10ms] * 1000, x_1[:n_10ms], 'b-')
    axes_1[0].set_xlabel('Tiempo (ms)')
    axes_1[0].set_ylabel('Amplitud')
    axes_1[0].set_title('Senal en el tiempo: tono 440 Hz')
    axes_1[0].grid(True, alpha=0.3)

    # Espectro de magnitud (solo positivas)
    mask_pos = freqs_1 >= 0
    axes_1[1].plot(freqs_1[mask_pos], magnitud_1[mask_pos], 'r-')
    axes_1[1].set_xlabel('Frecuencia (Hz)')
    axes_1[1].set_ylabel('Magnitud')
    axes_1[1].set_title('Espectro de magnitud')
    axes_1[1].set_xlim(0, 2000)
    axes_1[1].grid(True, alpha=0.3)

    plt.tight_layout()
    print(f"Pico en: {freqs_1[mask_pos][np.argmax(magnitud_1[mask_pos])]:.1f} Hz")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### rfft: optimizado para senales reales

    Para senales reales, el espectro es **simetrico**: las frecuencias negativas son el conjugado de las positivas. Por eso `rfft` solo calcula la mitad positiva, ahorrando tiempo y memoria.
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Usando rfft (mas eficiente para senales reales)
    fs_2 = 44100
    duracion_2 = 1.0
    N_2 = int(fs_2 * duracion_2)
    t_2 = np.arange(N_2) / fs_2

    # Senal con dos tonos
    x_2 = 0.7 * np.sin(2 * np.pi * 440 * t_2) + 0.3 * np.sin(2 * np.pi * 1000 * t_2)

    # rfft: solo frecuencias positivas
    X_2 = rfft(x_2)
    freqs_2 = rfftfreq(N_2, d=1/fs_2)
    magnitud_2 = np.abs(X_2) / N_2 * 2  # x2 para compensar mitad negativa

    fig_2, ax_2 = plt.subplots(figsize=(12, 4))
    ax_2.plot(freqs_2, magnitud_2, 'r-')
    ax_2.set_xlabel('Frecuencia (Hz)')
    ax_2.set_ylabel('Magnitud')
    ax_2.set_title('Espectro con rfft: dos tonos (440 Hz + 1000 Hz)')
    ax_2.set_xlim(0, 2000)
    ax_2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Slider interactivo: frecuencia variable
    """)
    return


@app.cell
def _(mo):
    slider_freq = mo.ui.slider(100, 4000, value=440, step=10, label="Frecuencia (Hz)")
    slider_freq
    return (slider_freq,)


@app.cell
def _(np, plt, rfft, rfftfreq, slider_freq):
    fs_s = 44100
    dur_s = 0.5
    N_s = int(fs_s * dur_s)
    t_s = np.arange(N_s) / fs_s

    f_sel = slider_freq.value
    x_s = np.sin(2 * np.pi * f_sel * t_s)

    X_s = rfft(x_s)
    freqs_s = rfftfreq(N_s, d=1/fs_s)
    mag_s = np.abs(X_s) / N_s * 2

    fig_s, axes_s = plt.subplots(1, 2, figsize=(14, 4))
    n_show = int(0.005 * fs_s)
    axes_s[0].plot(t_s[:n_show] * 1000, x_s[:n_show], 'b-')
    axes_s[0].set_xlabel('Tiempo (ms)')
    axes_s[0].set_ylabel('Amplitud')
    axes_s[0].set_title(f'Senal: {f_sel} Hz')
    axes_s[0].grid(True, alpha=0.3)

    axes_s[1].plot(freqs_s, mag_s, 'r-')
    axes_s[1].set_xlim(0, 5000)
    axes_s[1].set_xlabel('Frecuencia (Hz)')
    axes_s[1].set_ylabel('Magnitud')
    axes_s[1].set_title(f'Espectro: pico en {f_sel} Hz')
    axes_s[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. FFT en la Practica

    ### Espectro de distintos tipos de senales

    Veamos como se ven en frecuencia distintas senales que ya conocemos:
    - **Tono puro**: un pico en la frecuencia fundamental
    - **Dos tonos**: dos picos
    - **Ruido blanco**: espectro plano (todas las frecuencias con energia similar)
    - **Ruido rosa**: energia decae -3 dB/octava
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    fs_3 = 44100
    duracion_3 = 2.0
    N_3 = int(fs_3 * duracion_3)
    t_3 = np.arange(N_3) / fs_3

    # Generar senales
    tono_puro = np.sin(2 * np.pi * 1000 * t_3)
    dos_tonos = 0.5 * np.sin(2 * np.pi * 500 * t_3) + 0.5 * np.sin(2 * np.pi * 1500 * t_3)
    ruido_blanco = np.random.randn(N_3)

    # Ruido rosa (filtrado de ruido blanco)
    blanco_f = rfft(ruido_blanco)
    freqs_rosa = rfftfreq(N_3, d=1/fs_3)
    # Filtro 1/sqrt(f) para obtener ruido rosa
    filtro_rosa = np.ones_like(freqs_rosa)
    filtro_rosa[1:] = 1.0 / np.sqrt(freqs_rosa[1:])
    filtro_rosa[0] = 0
    ruido_rosa = np.fft.irfft(blanco_f * filtro_rosa, n=N_3)
    ruido_rosa = ruido_rosa / np.max(np.abs(ruido_rosa))

    senales = [tono_puro, dos_tonos, ruido_blanco, ruido_rosa]
    nombres = ['Tono puro 1 kHz', 'Dos tonos (500+1500 Hz)', 'Ruido blanco', 'Ruido rosa']

    fig_3, axes_3 = plt.subplots(4, 2, figsize=(14, 12))

    for i, (s, nombre) in enumerate(zip(senales, nombres)):
        # Tiempo
        n_show = int(0.01 * fs_3)
        axes_3[i, 0].plot(t_3[:n_show] * 1000, s[:n_show], 'b-', linewidth=0.5)
        axes_3[i, 0].set_title(f'{nombre} - Tiempo')
        axes_3[i, 0].set_xlabel('Tiempo (ms)')
        axes_3[i, 0].grid(True, alpha=0.3)

        # Frecuencia (en dB)
        X = rfft(s)
        f = rfftfreq(N_3, d=1/fs_3)
        mag_db = 20 * np.log10(np.abs(X) / N_3 * 2 + 1e-12)
        axes_3[i, 1].plot(f, mag_db, 'r-', linewidth=0.3)
        axes_3[i, 1].set_title(f'{nombre} - Espectro')
        axes_3[i, 1].set_xlabel('Frecuencia (Hz)')
        axes_3[i, 1].set_ylabel('dB')
        axes_3[i, 1].set_xlim(20, fs_3/2)
        axes_3[i, 1].set_xscale('log')
        axes_3[i, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ventanas (Windowing) y Fuga Espectral

    Cuando tomamos un tramo finito de una senal, estamos multiplicando por una **ventana rectangular**.
    Esto introduce **fuga espectral** (spectral leakage): energia se "desparrama" a frecuencias vecinas.

    **Solucion**: usar ventanas suaves como **Hanning** o **Hamming** que atenuan los bordes.

    $$w_{hann}[n] = 0.5 \left(1 - \cos\left(\frac{2\pi n}{N-1}\right)\right)$$
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Demostracion de fuga espectral
    fs_4 = 1000
    duracion_4 = 1.0
    N_4 = int(fs_4 * duracion_4)
    t_4 = np.arange(N_4) / fs_4

    # Frecuencia que NO es multiplo exacto de 1/duracion -> fuga
    f_leak = 100.5  # Hz (no encaja exactamente en la grilla de frecuencias)
    x_4 = np.sin(2 * np.pi * f_leak * t_4)

    # Sin ventana
    X_rect = rfft(x_4)
    freqs_4 = rfftfreq(N_4, d=1/fs_4)
    mag_rect = 20 * np.log10(np.abs(X_rect) / N_4 * 2 + 1e-12)

    # Con ventana de Hanning
    ventana = np.hanning(N_4)
    X_hann = rfft(x_4 * ventana)
    mag_hann = 20 * np.log10(np.abs(X_hann) / N_4 * 2 + 1e-12)

    # Con ventana de Hamming
    ventana_hamm = np.hamming(N_4)
    X_hamm = rfft(x_4 * ventana_hamm)
    mag_hamm = 20 * np.log10(np.abs(X_hamm) / N_4 * 2 + 1e-12)

    fig_4, axes_4 = plt.subplots(2, 1, figsize=(12, 8))

    # Ventanas en el tiempo
    axes_4[0].plot(t_4, np.ones(N_4), 'b-', label='Rectangular', alpha=0.7)
    axes_4[0].plot(t_4, ventana, 'r-', label='Hanning', alpha=0.7)
    axes_4[0].plot(t_4, ventana_hamm, 'g-', label='Hamming', alpha=0.7)
    axes_4[0].set_title('Funciones ventana')
    axes_4[0].set_xlabel('Tiempo (s)')
    axes_4[0].legend()
    axes_4[0].grid(True, alpha=0.3)

    # Espectros
    axes_4[1].plot(freqs_4, mag_rect, 'b-', label='Sin ventana (rectangular)', alpha=0.7)
    axes_4[1].plot(freqs_4, mag_hann, 'r-', label='Hanning', alpha=0.7)
    axes_4[1].plot(freqs_4, mag_hamm, 'g-', label='Hamming', alpha=0.7)
    axes_4[1].set_xlim(50, 150)
    axes_4[1].set_ylim(-80, 5)
    axes_4[1].set_xlabel('Frecuencia (Hz)')
    axes_4[1].set_ylabel('Magnitud (dB)')
    axes_4[1].set_title(f'Fuga espectral: tono de {f_leak} Hz')
    axes_4[1].legend()
    axes_4[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Espectrogramas

    El espectrograma muestra como cambia el contenido frecuencial de una senal **a lo largo del tiempo**.

    Es una representacion **tiempo-frecuencia**: el eje X es tiempo, el eje Y es frecuencia, y el color representa la magnitud.

    Se calcula dividiendo la senal en **segmentos** (con overlap) y aplicando la FFT a cada uno (**STFT**: Short-Time Fourier Transform).
    """)
    return


@app.cell
def _(np, plt, signal):
    # Espectrograma de un sine sweep (barrido de frecuencia)
    fs_5 = 44100
    duracion_5 = 3.0
    N_5 = int(fs_5 * duracion_5)
    t_5 = np.arange(N_5) / fs_5

    # Sine sweep: de 100 Hz a 10000 Hz
    sweep = signal.chirp(t_5, f0=100, f1=10000, t1=duracion_5, method='logarithmic')

    # Calcular espectrograma
    f_spec, t_spec, Sxx = signal.spectrogram(sweep, fs=fs_5, nperseg=2048, noverlap=1536)

    fig_5, axes_5 = plt.subplots(2, 1, figsize=(12, 8))

    # Senal en el tiempo
    axes_5[0].plot(t_5, sweep, 'b-', linewidth=0.3)
    axes_5[0].set_xlabel('Tiempo (s)')
    axes_5[0].set_ylabel('Amplitud')
    axes_5[0].set_title('Sine sweep 100 - 10000 Hz')
    axes_5[0].grid(True, alpha=0.3)

    # Espectrograma
    axes_5[1].pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx + 1e-12), shading='gouraud', cmap='inferno')
    axes_5[1].set_xlabel('Tiempo (s)')
    axes_5[1].set_ylabel('Frecuencia (Hz)')
    axes_5[1].set_title('Espectrograma del sine sweep')
    axes_5[1].set_ylim(0, 12000)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(np, plt, signal):
    # Espectrograma de un acorde (lineas horizontales)
    fs_6 = 44100
    duracion_6 = 2.0
    N_6 = int(fs_6 * duracion_6)
    t_6 = np.arange(N_6) / fs_6

    # Acorde Do mayor: C4 (262), E4 (330), G4 (392)
    acorde = (0.33 * np.sin(2 * np.pi * 261.63 * t_6) +
              0.33 * np.sin(2 * np.pi * 329.63 * t_6) +
              0.33 * np.sin(2 * np.pi * 392.00 * t_6))

    f_ac, t_ac, Sxx_ac = signal.spectrogram(acorde, fs=fs_6, nperseg=4096, noverlap=3072)

    fig_6, ax_6 = plt.subplots(figsize=(12, 5))
    ax_6.pcolormesh(t_ac, f_ac, 10 * np.log10(Sxx_ac + 1e-12), shading='gouraud', cmap='inferno')
    ax_6.set_xlabel('Tiempo (s)')
    ax_6.set_ylabel('Frecuencia (Hz)')
    ax_6.set_title('Espectrograma de acorde Do mayor (C4-E4-G4): lineas horizontales')
    ax_6.set_ylim(0, 600)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Filtros Digitales

    Un **filtro digital** modifica el contenido frecuencial de una senal: puede dejar pasar ciertas frecuencias y atenuar otras.

    ### Tipos de filtro por respuesta en frecuencia
    - **Pasa-bajos (LP)**: deja pasar frecuencias bajas, atenua altas
    - **Pasa-altos (HP)**: deja pasar frecuencias altas, atenua bajas
    - **Pasa-banda (BP)**: deja pasar un rango de frecuencias
    - **Rechaza-banda (BS)**: atenua un rango de frecuencias

    ### FIR vs IIR

    | Caracteristica | FIR | IIR |
    |---------------|-----|-----|
    | Respuesta al impulso | Finita (N coeficientes) | Infinita (recursivo) |
    | Fase | Puede ser lineal | No lineal |
    | Orden necesario | Alto (muchos coeficientes) | Bajo (pocos coeficientes) |
    | Estabilidad | Siempre estable | Puede ser inestable |
    | Ejemplo | Media movil | Butterworth |

    ### Butterworth (IIR)

    El filtro **Butterworth** tiene una respuesta en frecuencia **maximamente plana** en la banda de paso.
    Es el mas usado en audio y acustica.

    En SciPy usamos **SOS (Second-Order Sections)** que es la forma mas estable numericamente:
    ```python
    sos = signal.butter(N, Wn, btype, fs, output='sos')
    y = signal.sosfilt(sos, x)
    ```
    """)
    return


@app.cell
def _(np, plt, signal):
    # Diseno de filtros Butterworth: LP, HP, BP
    fs_7 = 44100
    orden = 4

    # Pasa-bajos a 1 kHz
    sos_lp = signal.butter(orden, 1000, btype='low', fs=fs_7, output='sos')

    # Pasa-altos a 1 kHz
    sos_hp = signal.butter(orden, 1000, btype='high', fs=fs_7, output='sos')

    # Pasa-banda 500 - 2000 Hz
    sos_bp = signal.butter(orden, [500, 2000], btype='band', fs=fs_7, output='sos')

    # Respuesta en frecuencia
    fig_7, axes_7 = plt.subplots(1, 3, figsize=(16, 4))

    filtros = [(sos_lp, 'Pasa-bajos 1 kHz', 'b'),
               (sos_hp, 'Pasa-altos 1 kHz', 'r'),
               (sos_bp, 'Pasa-banda 500-2000 Hz', 'g')]

    for ax, (sos, nombre, color) in zip(axes_7, filtros):
        w, h = signal.sosfreqz(sos, worN=8192, fs=fs_7)
        ax.semilogx(w, 20 * np.log10(np.abs(h) + 1e-12), color=color, linewidth=2)
        ax.set_title(nombre)
        ax.set_xlabel('Frecuencia (Hz)')
        ax.set_ylabel('Ganancia (dB)')
        ax.set_xlim(20, fs_7/2)
        ax.set_ylim(-60, 5)
        ax.grid(True, alpha=0.3, which='both')
        ax.axhline(-3, color='gray', linestyle='--', alpha=0.5, label='-3 dB')
        ax.legend()

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(np, plt, signal):
    # Aplicar filtro a ruido blanco
    fs_8 = 44100
    duracion_8 = 2.0
    N_8 = int(fs_8 * duracion_8)

    ruido = np.random.randn(N_8)

    # Filtro pasa-bajos a 1 kHz
    sos_demo = signal.butter(6, 1000, btype='low', fs=fs_8, output='sos')
    filtrado = signal.sosfilt(sos_demo, ruido)

    # Comparar espectros
    from scipy.fft import rfft as rfft_8, rfftfreq as rfftfreq_8
    freqs_8 = rfftfreq_8(N_8, d=1/fs_8)
    esp_original = 20 * np.log10(np.abs(rfft_8(ruido)) / N_8 * 2 + 1e-12)
    esp_filtrado = 20 * np.log10(np.abs(rfft_8(filtrado)) / N_8 * 2 + 1e-12)

    fig_8, ax_8 = plt.subplots(figsize=(12, 5))
    ax_8.semilogx(freqs_8[1:], esp_original[1:], 'b-', alpha=0.3, linewidth=0.3, label='Original (ruido blanco)')
    ax_8.semilogx(freqs_8[1:], esp_filtrado[1:], 'r-', alpha=0.5, linewidth=0.3, label='Filtrado (LP 1 kHz)')
    ax_8.set_xlabel('Frecuencia (Hz)')
    ax_8.set_ylabel('Magnitud (dB)')
    ax_8.set_title('Efecto del filtro pasa-bajos sobre ruido blanco')
    ax_8.set_xlim(20, fs_8/2)
    ax_8.legend()
    ax_8.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Filtros de Banda de Octava (IEC 61260)

    En acustica, se analiza el sonido en **bandas de octava** o **tercios de octava**.

    La norma **IEC 61260** define las frecuencias centrales y los anchos de banda.

    ### Bandas de octava

    Las frecuencias centrales estandar son:

    | $f_c$ (Hz) | 31.5 | 63 | 125 | 250 | 500 | 1000 | 2000 | 4000 | 8000 | 16000 |
    |------------|------|-----|------|------|------|-------|-------|-------|-------|--------|

    Para cada banda, los limites son:

    $$f_{low} = \frac{f_c}{\sqrt{2}}, \quad f_{high} = f_c \cdot \sqrt{2}$$

    Esto significa que cada banda cubre una **octava** completa (la frecuencia se duplica).

    ### Implementacion

    Para cada banda, disenamos un filtro **Butterworth pasa-banda**:
    """)
    return


@app.cell
def _(np, plt, signal):
    # Banco de filtros de octava
    fs_9 = 44100
    frecuencias_centrales = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]

    fig_9, ax_9 = plt.subplots(figsize=(14, 6))
    colores = plt.cm.tab10(np.linspace(0, 1, len(frecuencias_centrales)))

    for i, fc in enumerate(frecuencias_centrales):
        f_low = fc / np.sqrt(2)
        f_high = fc * np.sqrt(2)

        # Limitar frecuencias al rango valido
        f_low = max(f_low, 10)
        f_high = min(f_high, fs_9 / 2 - 1)

        if f_high <= f_low:
            continue

        sos_oct = signal.butter(4, [f_low, f_high], btype='band', fs=fs_9, output='sos')
        w, h = signal.sosfreqz(sos_oct, worN=8192, fs=fs_9)

        ax_9.semilogx(w, 20 * np.log10(np.abs(h) + 1e-12),
                       color=colores[i], linewidth=2, label=f'{fc} Hz')

    ax_9.set_xlabel('Frecuencia (Hz)')
    ax_9.set_ylabel('Ganancia (dB)')
    ax_9.set_title('Banco de filtros de octava (IEC 61260) - Butterworth orden 4')
    ax_9.set_xlim(20, fs_9/2)
    ax_9.set_ylim(-60, 5)
    ax_9.axhline(-3, color='gray', linestyle='--', alpha=0.5)
    ax_9.legend(loc='lower left', ncol=2)
    ax_9.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(np, plt, signal):
    # Funcion reutilizable para filtrar por bandas de octava
    def filtrar_por_octavas(x, fs, frecuencias_centrales_fn, orden=4):
        """
        Filtra una senal en bandas de octava.

        Parametros:
            x: senal de entrada
            fs: frecuencia de muestreo
            frecuencias_centrales_fn: lista de frecuencias centrales
            orden: orden del filtro Butterworth

        Retorna:
            dict con {fc: senal_filtrada}
        """
        bandas = {}
        for fc in frecuencias_centrales_fn:
            f_low = fc / np.sqrt(2)
            f_high = fc * np.sqrt(2)
            f_low = max(f_low, 10)
            f_high = min(f_high, fs / 2 - 1)
            if f_high <= f_low:
                continue
            sos = signal.butter(orden, [f_low, f_high], btype='band', fs=fs, output='sos')
            bandas[fc] = signal.sosfilt(sos, x)
        return bandas

    # Demo: ruido blanco filtrado por octavas
    fs_demo = 44100
    N_demo = int(fs_demo * 2.0)
    ruido_demo = np.random.randn(N_demo)
    fc_list = [125, 250, 500, 1000, 2000, 4000, 8000]

    bandas_demo = filtrar_por_octavas(ruido_demo, fs_demo, fc_list)

    # Energia por banda
    energias = {fc: np.sqrt(np.mean(b**2)) for fc, b in bandas_demo.items()}

    fig_demo, ax_demo = plt.subplots(figsize=(10, 5))
    ax_demo.bar([str(fc) for fc in energias.keys()],
                [20 * np.log10(e + 1e-12) for e in energias.values()],
                color='steelblue', edgecolor='navy')
    ax_demo.set_xlabel('Frecuencia central (Hz)')
    ax_demo.set_ylabel('Nivel RMS (dB)')
    ax_demo.set_title('Energia por banda de octava - Ruido blanco')
    ax_demo.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.gca()
    return (filtrar_por_octavas,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. IA para Investigacion de Normas Tecnicas

    Las normas tecnicas como la IEC 61260 son documentos complejos y costosos.
    La IA puede ayudarnos a **entender** el contenido, aunque debemos verificar siempre.

    ### Ejemplo de prompt para investigar una norma

    > "Explica los requisitos principales de la norma IEC 61260-1:2014 para filtros de bandas de octava.
    > Incluye: frecuencias centrales, anchos de banda, tolerancias, y como verificar que un filtro cumple la norma.
    > Dame un ejemplo en Python para implementar un filtro de banda de octava que cumpla la norma."

    ### Buenas practicas
    - Pedir **citas especificas** de secciones de la norma
    - **Verificar** la informacion con fuentes confiables
    - Usar la IA para **entender conceptos**, no como fuente definitiva
    - Comparar con implementaciones de referencia (ej: `acoustics` en Python)

    ### Limitaciones
    - La IA puede **inventar** requisitos que no existen en la norma
    - Las normas se actualizan y la IA puede tener informacion desactualizada
    - No reemplaza la lectura de la norma original para trabajo profesional
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    | Concepto | Herramienta | Uso |
    |----------|------------|-----|
    | DFT/FFT | `np.fft.rfft` | Pasar al dominio frecuencia |
    | Espectro | magnitud + fase | Ver contenido frecuencial |
    | Ventanas | `np.hanning`, `np.hamming` | Reducir fuga espectral |
    | Espectrograma | `signal.spectrogram` | Tiempo-frecuencia |
    | Filtros IIR | `signal.butter` + `signal.sosfilt` | Filtrar senales |
    | Bandas de octava | IEC 61260 | Analisis en bandas |

    ### Para la proxima clase
    Vamos a usar estas herramientas para **procesar respuestas al impulso** y calcular parametros acusticos como el T60.
    """)
    return


if __name__ == "__main__":
    app.run()
