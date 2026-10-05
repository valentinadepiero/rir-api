import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 4: Soluciones
    ## El Universo NumPy y las Senales
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Eje temporal
    """)
    return


@app.cell
def _(np):
    fs_1 = 48000
    duracion_1 = 2.0
    N_1 = int(fs_1 * duracion_1)
    t_1 = np.arange(N_1) / fs_1

    print(f"Numero de muestras: {len(t_1)} (esperado: {N_1})")
    print(f"Primera muestra:    {t_1[0]:.6f} s")
    print(f"Ultima muestra:     {t_1[-1]:.6f} s")
    print(f"Duracion total:     {t_1[-1] + 1/fs_1:.6f} s")
    print(f"Verificacion: len(t) == 96000? {len(t_1) == 96000}")
    print(f"Verificacion: t[-1] < 2.0?     {t_1[-1] < 2.0}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Senoidal de 440 Hz
    """)
    return


@app.cell
def _(np, plt):
    fs_2 = 44100
    f_2 = 440
    periodo_2 = 1.0 / f_2  # en segundos
    n_periodos_2 = 5
    duracion_2 = n_periodos_2 * periodo_2
    N_2 = int(fs_2 * duracion_2)
    t_2 = np.arange(N_2) / fs_2
    x_2 = np.sin(2 * np.pi * f_2 * t_2)

    print(f"Periodo: {periodo_2*1000:.4f} ms")
    print(f"Muestras para 5 periodos: {N_2}")
    print(f"Duracion: {duracion_2*1000:.4f} ms")

    fig_2, ax_2 = plt.subplots(figsize=(12, 4))
    ax_2.plot(t_2 * 1000, x_2, 'b-', linewidth=1.0)
    ax_2.set_title(f"Senoidal de {f_2} Hz - 5 periodos")
    ax_2.set_xlabel("Tiempo (ms)")
    ax_2.set_ylabel("Amplitud")
    ax_2.grid(True, alpha=0.3)
    ax_2.axhline(y=0, color='k', linewidth=0.5)
    plt.tight_layout()
    fig_2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Suma de senoidales
    """)
    return


@app.cell
def _(np, plt):
    fs_3 = 44100
    duracion_3 = 0.01  # 10 ms
    t_3 = np.arange(int(fs_3 * duracion_3)) / fs_3

    fundamental = 1.0 * np.sin(2 * np.pi * 440 * t_3)
    armonico = 0.5 * np.sin(2 * np.pi * 880 * t_3)
    suma_3 = fundamental + armonico

    fig_3, axes_3 = plt.subplots(3, 1, figsize=(12, 9), sharex=True)

    axes_3[0].plot(t_3 * 1000, fundamental, 'b-', linewidth=1.0)
    axes_3[0].set_title("Fundamental: 440 Hz, A=1.0")
    axes_3[0].set_ylabel("Amplitud")
    axes_3[0].set_ylim(-1.6, 1.6)
    axes_3[0].grid(True, alpha=0.3)

    axes_3[1].plot(t_3 * 1000, armonico, 'r-', linewidth=1.0)
    axes_3[1].set_title("Armonico: 880 Hz, A=0.5")
    axes_3[1].set_ylabel("Amplitud")
    axes_3[1].set_ylim(-1.6, 1.6)
    axes_3[1].grid(True, alpha=0.3)

    axes_3[2].plot(t_3 * 1000, suma_3, 'g-', linewidth=1.0)
    axes_3[2].set_title("Suma: 440 Hz + 880 Hz")
    axes_3[2].set_xlabel("Tiempo (ms)")
    axes_3[2].set_ylabel("Amplitud")
    axes_3[2].set_ylim(-1.6, 1.6)
    axes_3[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_3
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Impulso unitario con stem
    """)
    return


@app.cell
def _(np, plt):
    N_4 = 1000
    delta_4 = np.zeros(N_4)
    delta_4[100] = 1.0

    # Mostrar solo muestras 80 a 120
    n_4 = np.arange(80, 121)
    fig_4, ax_4 = plt.subplots(figsize=(10, 4))
    ax_4.stem(n_4, delta_4[80:121], linefmt='b-', markerfmt='bo', basefmt='k-')
    ax_4.set_title("Impulso unitario en n=100")
    ax_4.set_xlabel("n (muestras)")
    ax_4.set_ylabel("Amplitud")
    ax_4.set_ylim(-0.1, 1.2)
    ax_4.grid(True, alpha=0.3)
    plt.tight_layout()
    fig_4
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Exponencial decreciente en dB
    """)
    return


@app.cell
def _(np, plt):
    fs_5 = 44100
    T60_5 = 2.0
    alpha_5 = 6.908 / T60_5
    duracion_5 = 3.0
    t_5 = np.arange(int(fs_5 * duracion_5)) / fs_5
    x_5 = np.exp(-alpha_5 * t_5)

    fig_5, (ax_lin5, ax_db5) = plt.subplots(1, 2, figsize=(14, 5))

    # Escala lineal
    ax_lin5.plot(t_5, x_5, 'b-', linewidth=1.0)
    ax_lin5.axvline(x=T60_5, color='r', linestyle='--', linewidth=1.5, label=f'T60 = {T60_5} s')
    ax_lin5.set_title("Escala lineal")
    ax_lin5.set_xlabel("Tiempo (s)")
    ax_lin5.set_ylabel("Amplitud")
    ax_lin5.legend()
    ax_lin5.grid(True, alpha=0.3)

    # Escala en dB
    x_5_db = 20 * np.log10(np.maximum(x_5, 1e-10))
    ax_db5.plot(t_5, x_5_db, 'b-', linewidth=1.0)
    ax_db5.axvline(x=T60_5, color='r', linestyle='--', linewidth=1.5, label=f'T60 = {T60_5} s')
    ax_db5.axhline(y=-60, color='g', linestyle=':', linewidth=1.5, label='-60 dB')
    ax_db5.set_title("Escala en dB")
    ax_db5.set_xlabel("Tiempo (s)")
    ax_db5.set_ylabel("Amplitud (dB)")
    ax_db5.set_ylim(-80, 5)
    ax_db5.legend()
    ax_db5.grid(True, alpha=0.3)

    fig_5.suptitle(f"Exponencial decreciente: T60={T60_5}s, alpha={alpha_5:.3f}", fontsize=13)
    plt.tight_layout()
    fig_5
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Envolvente ADSR
    """)
    return


@app.cell
def _(np, plt):
    fs_6 = 44100

    # Duraciones en segundos
    t_attack = 0.010   # 10 ms
    t_decay = 0.020    # 20 ms
    t_sustain = 0.200  # 200 ms
    t_release = 0.050  # 50 ms
    sustain_level = 0.7

    # Numero de muestras por segmento
    n_attack = int(fs_6 * t_attack)
    n_decay = int(fs_6 * t_decay)
    n_sustain = int(fs_6 * t_sustain)
    n_release = int(fs_6 * t_release)

    # Generar cada segmento
    attack = np.linspace(0, 1.0, n_attack, endpoint=False)
    decay = np.linspace(1.0, sustain_level, n_decay, endpoint=False)
    sustain = np.full(n_sustain, sustain_level)
    release = np.linspace(sustain_level, 0, n_release, endpoint=True)

    # Concatenar
    adsr = np.concatenate([attack, decay, sustain, release])
    t_6 = np.arange(len(adsr)) / fs_6

    # Graficar
    fig_6, ax_6 = plt.subplots(figsize=(12, 5))
    ax_6.plot(t_6 * 1000, adsr, 'b-', linewidth=1.5)

    # Lineas de transicion
    tiempos_transicion = [
        t_attack * 1000,
        (t_attack + t_decay) * 1000,
        (t_attack + t_decay + t_sustain) * 1000,
    ]
    labels_fase = ['A->D', 'D->S', 'S->R']
    for tt, label in zip(tiempos_transicion, labels_fase):
        ax_6.axvline(x=tt, color='r', linestyle=':', alpha=0.7, linewidth=1)
        ax_6.text(tt + 1, 1.05, label, fontsize=9, color='red')

    ax_6.set_title("Envolvente ADSR")
    ax_6.set_xlabel("Tiempo (ms)")
    ax_6.set_ylabel("Amplitud")
    ax_6.set_ylim(-0.05, 1.15)
    ax_6.grid(True, alpha=0.3)

    # Anotar fases
    ax_6.text(t_attack * 500, 0.5, 'A', fontsize=14, ha='center', fontweight='bold', color='blue')
    ax_6.text((t_attack + t_decay / 2) * 1000, 0.5, 'D', fontsize=14, ha='center', fontweight='bold', color='blue')
    ax_6.text((t_attack + t_decay + t_sustain / 2) * 1000, 0.5, 'S', fontsize=14, ha='center', fontweight='bold', color='blue')
    ax_6.text((t_attack + t_decay + t_sustain + t_release / 2) * 1000, 0.3, 'R', fontsize=14, ha='center', fontweight='bold', color='blue')

    plt.tight_layout()
    print(f"Total de muestras: {len(adsr)}")
    print(f"Duracion total: {len(adsr)/fs_6*1000:.1f} ms")
    fig_6
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Broadcasting - Matriz de senoidales
    """)
    return


@app.cell
def _(np, plt):
    fs_7 = 44100
    duracion_7 = 0.020  # 20 ms
    frecuencias_7 = np.array([100, 200, 400, 800, 1600])

    N_7 = int(fs_7 * duracion_7)
    t_7 = np.arange(N_7) / fs_7  # shape (N,)

    # Broadcasting: (5,1) * (1,N) -> (5,N)
    freqs_col = frecuencias_7.reshape(-1, 1)  # shape (5, 1)
    t_row = t_7.reshape(1, -1)                # shape (1, N)
    matriz_7 = np.sin(2 * np.pi * freqs_col * t_row)

    print(f"Shape de la matriz: {matriz_7.shape}")
    print(f"Frecuencias: {frecuencias_7} Hz")

    fig_7, axes_7 = plt.subplots(5, 1, figsize=(12, 10), sharex=True)

    colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for i in range(5):
        axes_7[i].plot(t_7 * 1000, matriz_7[i], color=colores[i], linewidth=1.0)
        axes_7[i].set_ylabel("Amp")
        axes_7[i].set_title(f"{frecuencias_7[i]} Hz", fontsize=10)
        axes_7[i].grid(True, alpha=0.3)
        axes_7[i].set_ylim(-1.2, 1.2)

    axes_7[-1].set_xlabel("Tiempo (ms)")
    fig_7.suptitle("Matriz de senoidales (broadcasting)", fontsize=13)
    plt.tight_layout()
    fig_7
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Comparacion de rendimiento
    """)
    return


@app.cell
def _(np):
    import time
    import math

    N_8 = 1_000_000
    fs_8 = 44100
    f_8 = 440

    # Metodo 1: loop
    inicio_loop = time.perf_counter()
    senal_loop_8 = []
    for i in range(N_8):
        t_i = i / fs_8
        senal_loop_8.append(math.sin(2 * math.pi * f_8 * t_i))
    senal_loop_8 = np.array(senal_loop_8)
    tiempo_loop_8 = time.perf_counter() - inicio_loop

    # Metodo 2: NumPy vectorizado
    inicio_vec = time.perf_counter()
    t_8 = np.arange(N_8) / fs_8
    senal_vec_8 = np.sin(2 * np.pi * f_8 * t_8)
    tiempo_vec_8 = time.perf_counter() - inicio_vec

    print(f"Generando {N_8:,} muestras de senoidal de 440 Hz:")
    print(f"  Loop Python: {tiempo_loop_8 * 1000:.1f} ms")
    print(f"  NumPy:       {tiempo_vec_8 * 1000:.1f} ms")
    print(f"  Speedup:     {tiempo_loop_8 / tiempo_vec_8:.1f}x")
    print(f"  Resultados iguales: {np.allclose(senal_loop_8, senal_vec_8)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Senoidal interactiva
    """)
    return


@app.cell
def _(mo):
    freq_slider_9 = mo.ui.slider(
        start=100, stop=2000, step=10, value=440, label="Frecuencia (Hz)"
    )
    amp_slider_9 = mo.ui.slider(
        start=0.1, stop=1.0, step=0.1, value=1.0, label="Amplitud"
    )
    mo.md(f"""
    {freq_slider_9}
    {amp_slider_9}
    """)
    return amp_slider_9, freq_slider_9


@app.cell
def _(amp_slider_9, freq_slider_9, np, plt):
    fs_9 = 44100
    f_9 = freq_slider_9.value
    a_9 = amp_slider_9.value
    periodos_9 = 5
    duracion_9 = periodos_9 / f_9
    t_9 = np.arange(int(fs_9 * duracion_9)) / fs_9
    x_9 = a_9 * np.sin(2 * np.pi * f_9 * t_9)

    fig_9, ax_9 = plt.subplots(figsize=(12, 4))
    ax_9.plot(t_9 * 1000, x_9, 'b-', linewidth=1.5)
    ax_9.set_title(f"Senoidal: f={f_9} Hz, A={a_9:.1f}")
    ax_9.set_xlabel("Tiempo (ms)")
    ax_9.set_ylabel("Amplitud")
    ax_9.set_ylim(-1.1, 1.1)
    ax_9.grid(True, alpha=0.3)
    ax_9.axhline(y=0, color='k', linewidth=0.5)
    plt.tight_layout()
    fig_9
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Analisis de una senal
    """)
    return


@app.cell
def _(np):
    # Senal de ejemplo
    np.random.seed(42)
    fs_10 = 44100
    duracion_10_s = 2.0
    t_10 = np.arange(int(fs_10 * duracion_10_s)) / fs_10
    audio_10 = (0.5 * np.sin(2 * np.pi * 440 * t_10) +
                0.3 * np.sin(2 * np.pi * 880 * t_10) +
                0.05 * np.random.randn(len(t_10)))
    return audio_10, fs_10


@app.cell
def _(audio_10, fs_10, np):
    # Analisis
    duracion_calc = len(audio_10) / fs_10
    pico = np.max(np.abs(audio_10))
    rms_10 = np.sqrt(np.mean(audio_10**2))
    rms_dbfs = 20 * np.log10(rms_10) if rms_10 > 0 else float('-inf')
    factor_cresta = pico / rms_10

    print(f"Analisis de la senal:")
    print(f"  Muestras:         {len(audio_10):,}")
    print(f"  Frecuencia de m.: {fs_10} Hz")
    print(f"  Duracion:         {duracion_calc:.3f} s")
    print(f"  Amplitud pico:    {pico:.4f}")
    print(f"  RMS:              {rms_10:.4f}")
    print(f"  RMS en dBFS:      {rms_dbfs:.2f} dBFS")
    print(f"  Factor de cresta: {factor_cresta:.2f} ({20*np.log10(factor_cresta):.2f} dB)")
    return


if __name__ == "__main__":
    app.run()
