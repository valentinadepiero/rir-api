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
    return (np,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(mo):
    mo.md(r"""
    # Senales y Sistemas - Practica 2026
    ## Clase 5: Operaciones con Senales

    Hoy aprendemos a **transformar** senales: desplazarlas, invertirlas, escalarlas, sumarlas, multiplicarlas. Tambien vamos a entender **periodicidad**, **energia** y **potencia**, conceptos fundamentales para el analisis de senales.

    **Pilares**: P1 (principal), P3 (secundario)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Transformaciones de la variable independiente

    Las transformaciones de la variable independiente (el tiempo) nos permiten modificar **cuando** ocurren los eventos de una senal, sin cambiar su forma basica.

    ### 1.1 Desplazamiento temporal: $x[n - n_0]$

    Desplazar una senal en el tiempo es equivalente a un **delay** (retardo) en audio.

    - $x[n - n_0]$ con $n_0 > 0$: desplazamiento a la **derecha** (retardo)
    - $x[n - n_0]$ con $n_0 < 0$: desplazamiento a la **izquierda** (adelanto)
    """)
    return


@app.cell
def _(mo):
    shift_slider = mo.ui.slider(
        start=-20, stop=20, step=1, value=5, label="Desplazamiento n0"
    )
    mo.md(f"""
    ### Demo interactiva: desplazamiento temporal

    Ajusta $n_0$ para ver como se desplaza la senal:

    {shift_slider}
    """)
    return (shift_slider,)


@app.cell
def _(np, plt, shift_slider):
    # Senal original: un pulso triangular
    N_shift = 60
    n_shift = np.arange(N_shift)

    # Pulso triangular centrado en n=15
    x_orig = np.zeros(N_shift)
    for i in range(11):
        idx = 10 + i
        if idx < N_shift:
            x_orig[idx] = 1.0 - abs(i - 5) / 5.0

    # Desplazar
    n0 = shift_slider.value
    x_shifted = np.zeros(N_shift)
    for i in range(N_shift):
        src = i - n0
        if 0 <= src < N_shift:
            x_shifted[i] = x_orig[src]

    fig_sh, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    ax1.stem(n_shift, x_orig, linefmt='b-', markerfmt='bo', basefmt='k-')
    ax1.set_title("x[n] - Senal original")
    ax1.set_ylabel("Amplitud")
    ax1.set_ylim(-0.2, 1.3)
    ax1.grid(True, alpha=0.3)

    color_sh = 'r' if n0 > 0 else ('g' if n0 < 0 else 'b')
    ax2.stem(n_shift, x_shifted, linefmt=f'{color_sh}-', markerfmt=f'{color_sh}o', basefmt='k-')
    label_dir = "derecha (retardo)" if n0 > 0 else ("izquierda (adelanto)" if n0 < 0 else "sin cambio")
    ax2.set_title(f"x[n - ({n0})] - Desplazamiento: {abs(n0)} muestras a la {label_dir}")
    ax2.set_xlabel("n (muestras)")
    ax2.set_ylabel("Amplitud")
    ax2.set_ylim(-0.2, 1.3)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_sh
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 1.2 Escalado temporal: $x[an]$

    Modificar la escala temporal es equivalente a **acelerar** o **desacelerar** audio.

    - $|a| > 1$: **compresion** temporal (audio mas rapido, pitch mas alto)
    - $|a| < 1$: **expansion** temporal (audio mas lento, pitch mas bajo)

    En el dominio discreto, el escalado temporal tiene limitaciones: $x[2n]$ descarta muestras alternas (downsampling), mientras que $x[n/2]$ requiere interpolacion para las muestras intermedias.
    """)
    return


@app.cell
def _(np, plt):
    # Demostrar escalado temporal discreto
    fs_sc = 1000
    duracion_sc = 0.05
    t_sc = np.arange(int(fs_sc * duracion_sc)) / fs_sc
    x_sc = np.sin(2 * np.pi * 50 * t_sc)  # 50 Hz

    # x[2n] - compresion (tomar cada 2 muestras)
    x_comprimido = x_sc[::2]
    t_comprimido = t_sc[:len(x_comprimido)]

    # x[n/2] - expansion (repetir muestras, interpolacion simple)
    x_expandido = np.repeat(x_sc, 2)
    t_expandido = np.arange(len(x_expandido)) / fs_sc

    fig_sc, axes_sc = plt.subplots(3, 1, figsize=(12, 9), sharex=False)

    axes_sc[0].stem(np.arange(len(x_sc)), x_sc, linefmt='b-', markerfmt='bo', basefmt='k-')
    axes_sc[0].set_title(f"x[n] - Original ({len(x_sc)} muestras)")
    axes_sc[0].set_ylabel("Amplitud")
    axes_sc[0].grid(True, alpha=0.3)

    axes_sc[1].stem(np.arange(len(x_comprimido)), x_comprimido, linefmt='r-', markerfmt='ro', basefmt='k-')
    axes_sc[1].set_title(f"x[2n] - Compresion temporal ({len(x_comprimido)} muestras)")
    axes_sc[1].set_ylabel("Amplitud")
    axes_sc[1].grid(True, alpha=0.3)

    axes_sc[2].stem(np.arange(len(x_expandido)), x_expandido, linefmt='g-', markerfmt='go', basefmt='k-')
    axes_sc[2].set_title(f"Expansion temporal ({len(x_expandido)} muestras, repeat)")
    axes_sc[2].set_xlabel("n (muestras)")
    axes_sc[2].set_ylabel("Amplitud")
    axes_sc[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_sc
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 1.3 Inversion temporal: $x[-n]$

    Invertir una senal en el tiempo es como **reproducir audio al reves**. En NumPy es trivial:

    ```python
    x_invertido = x[::-1]
    ```
    """)
    return


@app.cell
def _(np, plt):
    # Inversion temporal
    fs_rev = 44100
    duracion_rev = 0.01  # 10 ms
    t_rev = np.arange(int(fs_rev * duracion_rev)) / fs_rev

    # Senal asimetrica: exponencial decreciente modulada
    x_rev = np.exp(-300 * t_rev) * np.sin(2 * np.pi * 440 * t_rev)

    # Invertir
    x_rev_inv = x_rev[::-1]

    fig_rev, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    ax1.plot(t_rev * 1000, x_rev, 'b-', linewidth=1.5)
    ax1.set_title("x[n] - Original (decae con el tiempo)")
    ax1.set_ylabel("Amplitud")
    ax1.grid(True, alpha=0.3)

    ax2.plot(t_rev * 1000, x_rev_inv, 'r-', linewidth=1.5)
    ax2.set_title("x[-n] - Invertida (crece con el tiempo)")
    ax2.set_xlabel("Tiempo (ms)")
    ax2.set_ylabel("Amplitud")
    ax2.grid(True, alpha=0.3)

    fig_rev.suptitle("Inversion temporal", fontsize=13)
    plt.tight_layout()
    fig_rev
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 1.4 Transformaciones combinadas

    Podemos combinar desplazamiento e inversion. El orden importa:

    - **Primero desplazar, luego invertir**: $x[-(n - n_0)] = x[n_0 - n]$
    - **Primero invertir, luego desplazar**: $x[-(n) - n_0] = x[-n - n_0]$

    Son operaciones diferentes! Veamos un ejemplo.
    """)
    return


@app.cell
def _(np, plt):
    N_comb = 40
    n_comb = np.arange(N_comb)
    n0_comb = 10

    # Senal original: pulso rectangular de n=5 a n=15
    x_comb = np.zeros(N_comb)
    x_comb[5:16] = np.linspace(0, 1, 11)

    # Opcion A: primero desplazar n0, luego invertir -> x[n0 - n]
    x_a = np.zeros(N_comb)
    for i in range(N_comb):
        src = n0_comb - i
        if 0 <= src < N_comb:
            x_a[i] = x_comb[src]

    # Opcion B: primero invertir, luego desplazar -> x[-n - n0] = x[-(n + n0)]
    x_b = np.zeros(N_comb)
    for i in range(N_comb):
        src = -(i) - n0_comb
        if 0 <= -src < N_comb:
            x_b[i] = x_comb[-src]

    fig_comb, axes_comb = plt.subplots(3, 1, figsize=(12, 9))

    axes_comb[0].stem(n_comb, x_comb, linefmt='b-', markerfmt='bo', basefmt='k-')
    axes_comb[0].set_title("x[n] - Original")
    axes_comb[0].set_ylabel("Amplitud")
    axes_comb[0].grid(True, alpha=0.3)

    axes_comb[1].stem(n_comb, x_a, linefmt='r-', markerfmt='ro', basefmt='k-')
    axes_comb[1].set_title(f"x[{n0_comb} - n]: desplazar luego invertir")
    axes_comb[1].set_ylabel("Amplitud")
    axes_comb[1].grid(True, alpha=0.3)

    axes_comb[2].stem(n_comb, x_b, linefmt='g-', markerfmt='go', basefmt='k-')
    axes_comb[2].set_title(f"x[-n - {n0_comb}]: invertir luego desplazar")
    axes_comb[2].set_xlabel("n (muestras)")
    axes_comb[2].set_ylabel("Amplitud")
    axes_comb[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_comb
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Operaciones de amplitud

    ### 2.1 Escalado: $A \cdot x[n]$ — Control de volumen

    Multiplicar por una constante cambia la amplitud sin alterar la forma de onda.
    """)
    return


@app.cell
def _(np, plt):
    fs_amp = 44100
    t_amp = np.arange(int(fs_amp * 0.01)) / fs_amp
    x_amp = np.sin(2 * np.pi * 440 * t_amp)

    fig_amp, axes_amp = plt.subplots(3, 1, figsize=(12, 7), sharex=True)
    ganancias = [1.0, 0.3, 2.0]
    colores_amp = ['b', 'g', 'r']
    titulos_amp = ["Original (A=1.0)", "Atenuada (A=0.3)", "Amplificada (A=2.0)"]

    for ax, g, c, titulo in zip(axes_amp, ganancias, colores_amp, titulos_amp):
        ax.plot(t_amp * 1000, g * x_amp, f'{c}-', linewidth=1.5)
        ax.set_title(titulo)
        ax.set_ylabel("Amplitud")
        ax.set_ylim(-2.5, 2.5)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)

    axes_amp[-1].set_xlabel("Tiempo (ms)")
    plt.tight_layout()
    fig_amp
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.2 DC offset: $x[n] + C$

    Agregar una constante desplaza toda la senal verticalmente. En audio, un DC offset es indeseable porque desperdicia rango dinamico.
    """)
    return


@app.cell
def _(np, plt):
    fs_dc = 44100
    t_dc = np.arange(int(fs_dc * 0.01)) / fs_dc
    x_dc = np.sin(2 * np.pi * 440 * t_dc)

    fig_dc, (ax1_dc, ax2_dc) = plt.subplots(1, 2, figsize=(12, 4))

    ax1_dc.plot(t_dc * 1000, x_dc, 'b-', linewidth=1.5, label='Original')
    ax1_dc.plot(t_dc * 1000, x_dc + 0.5, 'r-', linewidth=1.5, label='+ 0.5 (DC offset)')
    ax1_dc.set_title("Senal con DC offset")
    ax1_dc.set_xlabel("Tiempo (ms)")
    ax1_dc.set_ylabel("Amplitud")
    ax1_dc.legend()
    ax1_dc.grid(True, alpha=0.3)
    ax1_dc.axhline(y=0, color='k', linewidth=0.5)

    # Remover DC offset
    x_con_dc = x_dc + 0.5
    x_sin_dc = x_con_dc - np.mean(x_con_dc)
    ax2_dc.plot(t_dc * 1000, x_con_dc, 'r-', linewidth=1.5, alpha=0.5, label='Con DC')
    ax2_dc.plot(t_dc * 1000, x_sin_dc, 'g-', linewidth=1.5, label='DC removido (- mean)')
    ax2_dc.set_title("Remover DC offset con np.mean()")
    ax2_dc.set_xlabel("Tiempo (ms)")
    ax2_dc.set_ylabel("Amplitud")
    ax2_dc.legend()
    ax2_dc.grid(True, alpha=0.3)
    ax2_dc.axhline(y=0, color='k', linewidth=0.5)

    plt.tight_layout()
    fig_dc
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.3 Clipping: $\text{clip}(x[n], -T, T)$ — Distorsion

    Recortar la senal a un umbral es el principio de la **distorsion** en guitarras electricas y sintetizadores.
    """)
    return


@app.cell
def _(np, plt):
    fs_clip = 44100
    t_clip = np.arange(int(fs_clip * 0.01)) / fs_clip
    x_clip = 1.5 * np.sin(2 * np.pi * 440 * t_clip)  # amplitud > 1

    umbrales = [1.0, 0.5, 0.2]
    fig_clip, axes_clip = plt.subplots(len(umbrales) + 1, 1, figsize=(12, 10), sharex=True)

    axes_clip[0].plot(t_clip * 1000, x_clip, 'b-', linewidth=1.5)
    axes_clip[0].set_title("Original (amplitud 1.5)")
    axes_clip[0].set_ylabel("Amplitud")
    axes_clip[0].set_ylim(-2, 2)
    axes_clip[0].grid(True, alpha=0.3)

    for i, th in enumerate(umbrales):
        x_clipped = np.clip(x_clip, -th, th)
        axes_clip[i + 1].plot(t_clip * 1000, x_clipped, 'r-', linewidth=1.5)
        axes_clip[i + 1].set_title(f"Clipping en +/- {th}")
        axes_clip[i + 1].set_ylabel("Amplitud")
        axes_clip[i + 1].set_ylim(-2, 2)
        axes_clip[i + 1].grid(True, alpha=0.3)
        axes_clip[i + 1].axhline(y=th, color='g', linestyle=':', alpha=0.7)
        axes_clip[i + 1].axhline(y=-th, color='g', linestyle=':', alpha=0.7)

    axes_clip[-1].set_xlabel("Tiempo (ms)")
    fig_clip.suptitle("Efecto de clipping (distorsion)", fontsize=13)
    plt.tight_layout()
    fig_clip
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Operaciones entre senales

    ### 3.1 Suma: mezcla de audio

    Sumar dos senales es equivalente a **mezclar** sonidos. Es la operacion mas basica en produccion musical.
    """)
    return


@app.cell
def _(np, plt):
    fs_mix = 44100
    duracion_mix = 0.02  # 20 ms
    t_mix = np.arange(int(fs_mix * duracion_mix)) / fs_mix

    x1_mix = 0.7 * np.sin(2 * np.pi * 440 * t_mix)   # La
    x2_mix = 0.5 * np.sin(2 * np.pi * 554 * t_mix)   # Do# (tercera mayor)
    mezcla = x1_mix + x2_mix

    fig_mix, axes_mix = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes_mix[0].plot(t_mix * 1000, x1_mix, 'b-', linewidth=1.0)
    axes_mix[0].set_title("Senal 1: 440 Hz (La)")
    axes_mix[0].set_ylabel("Amplitud")
    axes_mix[0].set_ylim(-1.3, 1.3)
    axes_mix[0].grid(True, alpha=0.3)

    axes_mix[1].plot(t_mix * 1000, x2_mix, 'r-', linewidth=1.0)
    axes_mix[1].set_title("Senal 2: 554 Hz (Do#)")
    axes_mix[1].set_ylabel("Amplitud")
    axes_mix[1].set_ylim(-1.3, 1.3)
    axes_mix[1].grid(True, alpha=0.3)

    axes_mix[2].plot(t_mix * 1000, mezcla, 'g-', linewidth=1.0)
    axes_mix[2].set_title("Mezcla: 440 Hz + 554 Hz (intervalo de tercera mayor)")
    axes_mix[2].set_xlabel("Tiempo (ms)")
    axes_mix[2].set_ylabel("Amplitud")
    axes_mix[2].set_ylim(-1.3, 1.3)
    axes_mix[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_mix
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.2 Multiplicacion: modulacion AM y ventaneo

    Multiplicar dos senales tiene dos aplicaciones principales:

    - **Modulacion AM (amplitud modulada)**: una senal lenta (moduladora) controla la amplitud de una senal rapida (portadora). En audio, esto es el efecto **tremolo**.
    - **Ventaneo (windowing)**: multiplicar por una funcion ventana para seleccionar un fragmento de senal.
    """)
    return


@app.cell
def _(np, plt):
    # Modulacion AM: tremolo
    fs_am = 44100
    duracion_am = 0.5  # 500 ms
    t_am = np.arange(int(fs_am * duracion_am)) / fs_am

    portadora = np.sin(2 * np.pi * 440 * t_am)
    moduladora = 0.5 + 0.5 * np.sin(2 * np.pi * 5 * t_am)  # 5 Hz, rango 0 a 1
    tremolo = portadora * moduladora

    fig_am, axes_am = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes_am[0].plot(t_am * 1000, portadora, 'b-', linewidth=0.5)
    axes_am[0].set_title("Portadora: 440 Hz")
    axes_am[0].set_ylabel("Amplitud")
    axes_am[0].grid(True, alpha=0.3)

    axes_am[1].plot(t_am * 1000, moduladora, 'r-', linewidth=1.5)
    axes_am[1].set_title("Moduladora: 5 Hz (controla el volumen)")
    axes_am[1].set_ylabel("Amplitud")
    axes_am[1].grid(True, alpha=0.3)

    axes_am[2].plot(t_am * 1000, tremolo, 'g-', linewidth=0.5)
    axes_am[2].plot(t_am * 1000, moduladora, 'r--', linewidth=1.0, alpha=0.5, label='Envolvente')
    axes_am[2].plot(t_am * 1000, -moduladora, 'r--', linewidth=1.0, alpha=0.5)
    axes_am[2].set_title("Resultado: efecto tremolo (AM)")
    axes_am[2].set_xlabel("Tiempo (ms)")
    axes_am[2].set_ylabel("Amplitud")
    axes_am[2].legend()
    axes_am[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_am
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.3 Interferencia constructiva y destructiva

    Cuando sumamos dos senoidales de la **misma frecuencia** pero con diferente **fase**, pueden reforzarse o cancelarse.

    - **Fase 0 grados**: interferencia constructiva (se suman)
    - **Fase 180 grados ($\pi$)**: interferencia destructiva (se cancelan)
    """)
    return


@app.cell
def _(mo):
    phase_interf_slider = mo.ui.slider(
        start=0, stop=360, step=5, value=0, label="Fase de la segunda senal (grados)"
    )
    mo.md(f"""
    ### Demo interactiva: interferencia

    Ajusta la fase de la segunda senal para ver como interactuan:

    {phase_interf_slider}
    """)
    return (phase_interf_slider,)


@app.cell
def _(np, phase_interf_slider, plt):
    fs_interf = 44100
    f_interf = 1000
    duracion_interf = 3.0 / f_interf  # 3 periodos
    t_interf = np.arange(int(fs_interf * duracion_interf)) / fs_interf

    phi_interf = np.deg2rad(phase_interf_slider.value)
    x1_interf = np.sin(2 * np.pi * f_interf * t_interf)
    x2_interf = np.sin(2 * np.pi * f_interf * t_interf + phi_interf)
    suma_interf = x1_interf + x2_interf

    amp_resultado = np.max(np.abs(suma_interf))

    fig_interf, axes_interf = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes_interf[0].plot(t_interf * 1000, x1_interf, 'b-', linewidth=1.5)
    axes_interf[0].set_title("Senal 1: sin(2*pi*1000*t)")
    axes_interf[0].set_ylabel("Amplitud")
    axes_interf[0].set_ylim(-2.2, 2.2)
    axes_interf[0].grid(True, alpha=0.3)

    axes_interf[1].plot(t_interf * 1000, x2_interf, 'r-', linewidth=1.5)
    axes_interf[1].set_title(f"Senal 2: sin(2*pi*1000*t + {phase_interf_slider.value} grados)")
    axes_interf[1].set_ylabel("Amplitud")
    axes_interf[1].set_ylim(-2.2, 2.2)
    axes_interf[1].grid(True, alpha=0.3)

    color_sum = 'green' if amp_resultado > 0.1 else 'gray'
    axes_interf[2].plot(t_interf * 1000, suma_interf, color=color_sum, linewidth=1.5)
    tipo = "CONSTRUCTIVA" if amp_resultado > 1.0 else ("DESTRUCTIVA" if amp_resultado < 0.5 else "PARCIAL")
    axes_interf[2].set_title(f"Suma: amplitud pico = {amp_resultado:.2f} (interferencia {tipo})")
    axes_interf[2].set_xlabel("Tiempo (ms)")
    axes_interf[2].set_ylabel("Amplitud")
    axes_interf[2].set_ylim(-2.2, 2.2)
    axes_interf[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_interf
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.4 Vista previa: convolucion

    La **convolucion** es la operacion mas importante en sistemas lineales e invariantes en el tiempo (LTI). Es la base de:

    - **Filtros** (pasa-bajos, pasa-altos, ecualizadores)
    - **Reverberacion** (convolucionar con la respuesta al impulso de una sala)
    - **Efectos** (eco, chorus, flanger)

    La formula es:

    $$(x * h)[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n - k]$$

    Intuitivamente: para cada muestra de salida, **deslizamos** la respuesta al impulso sobre la senal de entrada, multiplicamos y sumamos.

    Veremos la convolucion en detalle en la **Clase 8**. Por ahora, solo un ejemplo visual:
    """)
    return


@app.cell
def _(np, plt):
    # Vista previa de convolucion: eco simple
    fs_conv = 44100
    duracion_conv = 0.05
    t_conv = np.arange(int(fs_conv * duracion_conv)) / fs_conv

    # Senal: click (impulso)
    x_conv = np.zeros(int(fs_conv * duracion_conv))
    x_conv[0] = 1.0

    # Respuesta al impulso: eco a 10ms con atenuacion
    h_conv = np.zeros(int(fs_conv * 0.02))
    h_conv[0] = 1.0
    h_conv[int(0.01 * fs_conv)] = 0.5  # eco a 10ms

    # Convolucion
    y_conv = np.convolve(x_conv, h_conv)[:len(x_conv)]
    t_y = np.arange(len(y_conv)) / fs_conv

    fig_conv, axes_conv = plt.subplots(3, 1, figsize=(12, 8))

    axes_conv[0].stem(t_conv[:100] * 1000, x_conv[:100], linefmt='b-', markerfmt='bo', basefmt='k-')
    axes_conv[0].set_title("Entrada: impulso (click)")
    axes_conv[0].set_ylabel("Amplitud")
    axes_conv[0].grid(True, alpha=0.3)

    t_h = np.arange(len(h_conv)) / fs_conv
    axes_conv[1].stem(t_h * 1000, h_conv, linefmt='r-', markerfmt='ro', basefmt='k-')
    axes_conv[1].set_title("Respuesta al impulso: eco a 10 ms")
    axes_conv[1].set_ylabel("Amplitud")
    axes_conv[1].grid(True, alpha=0.3)

    axes_conv[2].stem(t_y[:100] * 1000, y_conv[:100], linefmt='g-', markerfmt='go', basefmt='k-')
    axes_conv[2].set_title("Salida: impulso + eco (convolucion)")
    axes_conv[2].set_xlabel("Tiempo (ms)")
    axes_conv[2].set_ylabel("Amplitud")
    axes_conv[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_conv
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Periodicidad en senales discretas

    Una senal discreta $x[n]$ es **periodica** si existe un entero positivo $N$ tal que:

    $$x[n] = x[n + N] \quad \forall n$$

    El menor $N$ que cumple esto es el **periodo fundamental**.

    ### Cuando es periodica una senoidal discreta?

    La senoidal $x[n] = \sin(2\pi f_0 n / f_s)$ es periodica si y solo si $f_0 / f_s$ es un numero **racional**:

    $$\frac{f_0}{f_s} = \frac{p}{q} \quad \text{con } p, q \text{ enteros}$$

    El periodo fundamental es $N = q$ (despues de simplificar la fraccion).
    """)
    return


@app.cell
def _(np, plt):
    from fractions import Fraction

    fs_per = 44100

    # Frecuencias a analizar
    frecuencias_per = [441, 440, 1000, 882]

    print("Analisis de periodicidad (fs = 44100 Hz):\n")
    print(f"{'Freq (Hz)':>10} {'f0/fs':>15} {'Periodica?':>12} {'Periodo N':>12}")
    print("-" * 55)

    for f0 in frecuencias_per:
        fraccion = Fraction(f0, fs_per)
        es_periodica = True  # siempre racional si f0 es entero y fs es entero
        periodo = fraccion.denominator
        print(f"{f0:>10} {str(fraccion):>15} {'Si':>12} {periodo:>12}")

    print(f"\nNota: cuando f0 y fs son enteros, f0/fs siempre es racional.")
    print(f"La pregunta practica es: el periodo es razonablemente corto?")
    print(f"\n441 Hz: periodo = {Fraction(441, 44100).denominator} muestras (exacto, corto)")
    print(f"440 Hz: periodo = {Fraction(440, 44100).denominator} muestras (exacto, pero largo!)")
    print(f"1000 Hz: periodo = {Fraction(1000, 44100).denominator} muestras")
    print(f"882 Hz: periodo = {Fraction(882, 44100).denominator} muestras")
    return


@app.cell
def _(np, plt):
    # Visualizar: 441 Hz vs 440 Hz
    fs_vis = 44100

    fig_per, axes_per = plt.subplots(2, 1, figsize=(12, 7))

    # 441 Hz: periodo exacto = 100 muestras
    N_441 = 200
    n_441 = np.arange(N_441)
    x_441 = np.sin(2 * np.pi * 441 * n_441 / fs_vis)
    axes_per[0].stem(n_441, x_441, linefmt='b-', markerfmt='bo', basefmt='k-')
    axes_per[0].axvline(x=100, color='r', linestyle='--', label='Periodo = 100')
    axes_per[0].set_title("441 Hz a 44100 Hz: periodo exacto = 100 muestras")
    axes_per[0].set_ylabel("Amplitud")
    axes_per[0].legend()
    axes_per[0].grid(True, alpha=0.3)

    # 440 Hz: periodo = 44100/440 = 100.227... no es entero
    N_440 = 200
    n_440 = np.arange(N_440)
    x_440 = np.sin(2 * np.pi * 440 * n_440 / fs_vis)
    axes_per[1].stem(n_440, x_440, linefmt='r-', markerfmt='ro', basefmt='k-')
    ratio_440 = 44100 / 440
    axes_per[1].axvline(x=ratio_440, color='g', linestyle='--',
                        label=f'44100/440 = {ratio_440:.3f} (no entero!)')
    axes_per[1].set_title("440 Hz a 44100 Hz: 44100/440 = 100.227... (periodo largo)")
    axes_per[1].set_xlabel("n (muestras)")
    axes_per[1].set_ylabel("Amplitud")
    axes_per[1].legend()
    axes_per[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_per
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Energia y potencia de senales

    ### Energia

    La **energia** de una senal discreta de duracion finita es:

    $$E = \sum_{n=0}^{N-1} |x[n]|^2$$

    Senales de energia finita: pulsos, transitorios (un clap, un golpe de puerta).

    ### Potencia

    La **potencia promedio** es la energia por muestra:

    $$P = \frac{1}{N} \sum_{n=0}^{N-1} |x[n]|^2$$

    Senales de potencia finita: senoidales, ruido (sonidos sostenidos).

    ### RMS (Root Mean Square)

    $$\text{RMS} = \sqrt{P} = \sqrt{\frac{1}{N} \sum_{n=0}^{N-1} |x[n]|^2}$$

    El RMS es la medida mas usada de "nivel" de una senal de audio.

    ### Conversion a dB

    $$\text{dB} = 20 \log_{10}\left(\frac{\text{RMS}}{\text{ref}}\right)$$

    - **dBFS** (Full Scale): referencia = 1.0 (maximo digital)
    - **dBSPL** (Sound Pressure Level): referencia = 20 $\mu$Pa
    """)
    return


@app.cell
def _(np):
    fs_ep2 = 44100

    # 1. Impulso unitario
    delta_ep = np.zeros(1000)
    delta_ep[0] = 1.0
    E_delta = np.sum(np.abs(delta_ep)**2)
    P_delta = E_delta / len(delta_ep)
    rms_delta = np.sqrt(P_delta)

    # 2. Senoidal 440 Hz, 1 segundo
    t_ep = np.arange(fs_ep2) / fs_ep2
    senoidal_ep = np.sin(2 * np.pi * 440 * t_ep)
    E_sen = np.sum(np.abs(senoidal_ep)**2)
    P_sen = E_sen / len(senoidal_ep)
    rms_sen = np.sqrt(P_sen)

    # 3. Silencio
    silencio = np.zeros(fs_ep2)
    E_sil = np.sum(np.abs(silencio)**2)
    P_sil = E_sil / len(silencio)
    rms_sil = np.sqrt(P_sil)

    print("Comparacion de energia, potencia y RMS:\n")
    print(f"{'Senal':<25} {'Energia':>12} {'Potencia':>12} {'RMS':>12} {'dBFS':>10}")
    print("-" * 75)

    for nombre, E, P, rms_val in [
        ("Impulso unitario", E_delta, P_delta, rms_delta),
        ("Senoidal 440 Hz (1s)", E_sen, P_sen, rms_sen),
        ("Silencio (1s)", E_sil, P_sil, rms_sil),
    ]:
        db = 20 * np.log10(rms_val) if rms_val > 0 else float('-inf')
        print(f"{nombre:<25} {E:>12.4f} {P:>12.6f} {rms_val:>12.6f} {db:>10.2f}")

    print(f"\nNota: el RMS de una senoidal de amplitud 1 es 1/sqrt(2) = {1/np.sqrt(2):.6f}")
    print(f"Esto equivale a {20*np.log10(1/np.sqrt(2)):.2f} dBFS")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Contexto de audio: energia de un clap vs tono sostenido
    """)
    return


@app.cell
def _(np, plt):
    fs_ctx = 44100
    duracion_ctx = 1.0
    t_ctx = np.arange(int(fs_ctx * duracion_ctx)) / fs_ctx

    # Clap: impulso corto con decaimiento rapido
    clap = np.zeros(len(t_ctx))
    n_clap = int(0.005 * fs_ctx)  # 5 ms de duracion
    clap[:n_clap] = np.random.randn(n_clap) * np.exp(-np.arange(n_clap) / (0.001 * fs_ctx))
    clap = clap / np.max(np.abs(clap))  # normalizar

    # Tono sostenido
    tono = 0.3 * np.sin(2 * np.pi * 440 * t_ctx)

    E_clap = np.sum(clap**2)
    E_tono = np.sum(tono**2)
    rms_clap = np.sqrt(np.mean(clap**2))
    rms_tono = np.sqrt(np.mean(tono**2))

    fig_ctx, axes_ctx = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    axes_ctx[0].plot(t_ctx * 1000, clap, 'b-', linewidth=0.5)
    axes_ctx[0].set_title(
        f"Clap: E={E_clap:.1f}, RMS={rms_clap:.4f} ({20*np.log10(max(rms_clap,1e-10)):.1f} dBFS)"
    )
    axes_ctx[0].set_ylabel("Amplitud")
    axes_ctx[0].grid(True, alpha=0.3)

    axes_ctx[1].plot(t_ctx * 1000, tono, 'r-', linewidth=0.5)
    axes_ctx[1].set_title(
        f"Tono 440 Hz: E={E_tono:.1f}, RMS={rms_tono:.4f} ({20*np.log10(max(rms_tono,1e-10)):.1f} dBFS)"
    )
    axes_ctx[1].set_xlabel("Tiempo (ms)")
    axes_ctx[1].set_ylabel("Amplitud")
    axes_ctx[1].grid(True, alpha=0.3)

    fig_ctx.suptitle("Energia vs Potencia: un clap tiene poca energia total pero alto pico", fontsize=12)
    plt.tight_layout()
    fig_ctx
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Trabajo Practico: Arquitectura (P3)

    ### Milestone 0: Plan de arquitectura

    Para la proxima clase deben presentar el **plan de arquitectura** de su proyecto AcoustiPy.

    ### Que debe incluir el Milestone 0:

    1. **Diagrama de arquitectura** del proyecto (puede ser un diagrama Mermaid en el README)
    2. **GitHub Issues** creados para las primeras tareas
    3. **Estructura de directorios** propuesta

    ### Ejemplo de diagrama de arquitectura (Mermaid):

    ```mermaid
    graph TD
        A[main.py] --> B[audio/loader.py]
        A --> C[analysis/spectral.py]
        A --> D[effects/reverb.py]
        B --> E[audio/formats.py]
        C --> F[analysis/features.py]
        D --> G[effects/delay.py]
        H[tests/] --> B
        H --> C
        H --> D
    ```

    ### Estructura de directorios sugerida:

    ```
    acoustipy/
    ├── README.md
    ├── pyproject.toml
    ├── src/
    │   └── acoustipy/
    │       ├── __init__.py
    │       ├── audio/
    │       │   ├── __init__.py
    │       │   ├── loader.py      # Cargar y guardar archivos de audio
    │       │   └── formats.py     # Conversion entre formatos
    │       ├── analysis/
    │       │   ├── __init__.py
    │       │   ├── temporal.py    # Analisis en dominio temporal
    │       │   ├── spectral.py    # Analisis espectral (FFT)
    │       │   └── features.py    # Extraccion de caracteristicas
    │       └── effects/
    │           ├── __init__.py
    │           ├── reverb.py      # Reverberacion
    │           ├── delay.py       # Delay y eco
    │           └── filters.py     # Filtros (EQ, pasa-bajos, etc.)
    ├── tests/
    │   ├── test_audio.py
    │   ├── test_analysis.py
    │   └── test_effects.py
    └── examples/
        └── demo.py
    ```

    ### Template de GitHub Issue:

    ```markdown
    ## Descripcion
    Implementar la funcion `load_wav()` en `audio/loader.py`.

    ## Criterios de aceptacion
    - [ ] Carga archivos WAV mono y estereo
    - [ ] Normaliza a float64 entre -1.0 y 1.0
    - [ ] Retorna tupla (fs, data)
    - [ ] Maneja errores (archivo no encontrado, formato invalido)
    - [ ] Tests con pytest

    ## Etiquetas
    - milestone: M1
    - tipo: feature
    ```

    ### Estrategia de branching sugerida:

    - `main`: branch principal, siempre funcional
    - `develop`: branch de desarrollo
    - `feature/nombre-feature`: branches para cada feature
    - Pull Requests para integrar features a develop
    - Merge de develop a main para cada milestone
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen de la clase

    Hoy aprendimos:

    - **Transformaciones temporales**: desplazamiento ($x[n - n_0]$), escalado ($x[an]$), inversion ($x[-n]$)
    - **Operaciones de amplitud**: escalado, DC offset, clipping
    - **Operaciones entre senales**: suma (mezcla), multiplicacion (AM, ventaneo)
    - **Interferencia**: constructiva y destructiva
    - **Convolucion**: concepto basico (detalles en Clase 8)
    - **Periodicidad**: condicion $f_0/f_s$ racional
    - **Energia y potencia**: E, P, RMS, dBFS
    - **TP**: plan de arquitectura para Milestone 0

    ### Para la proxima clase
    - Completar los ejercicios de `ejercicios.py`
    - Preparar Milestone 0: diagrama de arquitectura, GitHub Issues, estructura de directorios
    """)
    return


if __name__ == "__main__":
    app.run()
