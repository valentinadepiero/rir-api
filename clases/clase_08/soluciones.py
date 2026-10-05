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
    # Clase 8: Soluciones
    ## Convolucion + Entrega 1
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Convolucion manual
    """)
    return


@app.cell
def _(np):
    # Ejercicio 1: Convolucion manual
    print("x = [1, 2, 3], h = [1, 0, -1]\n")
    print("Calculo paso a paso:")
    print("  y[0] = x[0]*h[0]                   = 1*1                 = 1")
    print("  y[1] = x[0]*h[1] + x[1]*h[0]       = 1*0 + 2*1          = 2")
    print("  y[2] = x[0]*h[2] + x[1]*h[1] + x[2]*h[0] = 1*(-1) + 2*0 + 3*1 = 2")
    print("  y[3] = x[1]*h[2] + x[2]*h[1]       = 2*(-1) + 3*0       = -2")
    print("  y[4] = x[2]*h[2]                    = 3*(-1)             = -3")
    print()

    # Verificacion
    x_1 = np.array([1, 2, 3])
    h_1 = np.array([1, 0, -1])
    y_1 = np.convolve(x_1, h_1)
    y_manual = np.array([1, 2, 2, -2, -3])

    print(f"Resultado manual: {y_manual}")
    print(f"np.convolve:      {y_1}")
    print(f"Coinciden: {np.allclose(y_manual, y_1)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Convolucion desde cero
    """)
    return


@app.cell
def _(np):
    # Ejercicio 2: Convolucion desde cero
    def mi_convolucion(x, h):
        """Convolucion discreta implementada con loops."""
        N = len(x)
        M = len(h)
        y = np.zeros(N + M - 1)
        for n in range(N + M - 1):
            for k in range(N):
                if 0 <= n - k < M:
                    y[n] += x[k] * h[n - k]
        return y

    # Verificacion con 3 pares de senales
    pares = [
        (np.array([1, 2, 3]), np.array([1, 0, -1])),
        (np.array([1, 0, 0, 1]), np.array([0.5, 0.5])),
        (np.random.randn(20), np.random.randn(10)),
    ]

    print("Verificacion de mi_convolucion vs np.convolve:")
    for i, (x, h) in enumerate(pares):
        y_mi = mi_convolucion(x, h)
        y_np = np.convolve(x, h)
        error = np.max(np.abs(y_mi - y_np))
        print(f"  Par {i+1}: error maximo = {error:.2e} -> {'OK' if error < 1e-10 else 'ERROR'}")
    return (mi_convolucion,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Propiedad de identidad
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 3: Identidad
    x_3 = np.array([1, -2, 3, 0, 5, -1])

    # Convolucion con delta
    delta_3 = np.array([1.0])
    y_delta = np.convolve(x_3, delta_3)

    print("x * delta[n] = x:")
    print(f"  x       = {x_3}")
    print(f"  x*delta = {y_delta}")
    print(f"  Iguales: {np.allclose(x_3, y_delta)}")

    # Convolucion con delta desplazada
    delta_desp = np.array([0.0, 0.0, 0.0, 1.0])
    y_desp = np.convolve(x_3, delta_desp)

    print(f"\nx * delta[n-3]:")
    print(f"  x            = {x_3}")
    print(f"  x*delta[n-3] = {y_desp}")
    print("  El resultado es x desplazado 3 muestras a la derecha!")
    print("  Fisicamente: convolucionar con un delta desplazado = RETARDAR la senal.")

    fig_3, axes_3 = plt.subplots(3, 1, figsize=(10, 5))
    axes_3[0].stem(np.arange(len(x_3)), x_3, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_3[0].set_title('x original')
    axes_3[0].grid(True, alpha=0.3)

    axes_3[1].stem(np.arange(len(y_delta)), y_delta, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_3[1].set_title(r'x * $\delta$[n] (identidad)')
    axes_3[1].grid(True, alpha=0.3)

    axes_3[2].stem(np.arange(len(y_desp)), y_desp, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_3[2].set_title(r'x * $\delta$[n-3] (desplazamiento)')
    axes_3[2].set_xlabel('n')
    axes_3[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Convolucion de pulsos rectangulares
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 4: Pulsos rectangulares
    x1_4 = np.ones(10)   # Pulso de 10 muestras
    x2_4 = np.ones(5)    # Pulso de 5 muestras

    y_4 = np.convolve(x1_4, x2_4)

    fig_4, axes_4 = plt.subplots(3, 1, figsize=(10, 6))

    axes_4[0].stem(np.arange(len(x1_4)), x1_4, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_4[0].set_title('x1: pulso rectangular (10 muestras)')
    axes_4[0].set_ylim(-0.5, 6)
    axes_4[0].grid(True, alpha=0.3)

    axes_4[1].stem(np.arange(len(x2_4)), x2_4, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_4[1].set_title('x2: pulso rectangular (5 muestras)')
    axes_4[1].set_ylim(-0.5, 6)
    axes_4[1].grid(True, alpha=0.3)

    axes_4[2].stem(np.arange(len(y_4)), y_4, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_4[2].set_title('x1 * x2: forma trapezoidal')
    axes_4[2].set_xlabel('n')
    axes_4[2].set_ylim(-0.5, 6)
    axes_4[2].grid(True, alpha=0.3)

    plt.tight_layout()

    print(f"y = {y_4}")
    print(f"\nForma del resultado: TRAPEZOIDAL")
    print("La convolucion de dos pulsos rectangulares da un trapecio.")
    print("Si los dos pulsos tuvieran el mismo largo, daria un TRIANGULO.")
    print("Largo del resultado: 10 + 5 - 1 = 14 muestras.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Efecto de eco por convolucion
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 5: Eco por convolucion
    fs_5 = 44100
    retardo_s = 0.3
    D_5 = int(retardo_s * fs_5)  # 13230 muestras

    print(f"D = {retardo_s} s * {fs_5} Hz = {D_5} muestras")

    # Construir h[n] del eco
    h_eco = np.zeros(D_5 + 1)
    h_eco[0] = 1.0      # Senal directa
    h_eco[D_5] = 0.5     # Eco atenuado

    # Senal de prueba: tono corto de 0.1 s
    duracion_tono = 0.1
    n_tono = int(fs_5 * duracion_tono)
    t_tono = np.arange(n_tono) / fs_5
    senal_5 = np.zeros(int(fs_5 * 1.0))  # 1 segundo total
    senal_5[:n_tono] = 0.8 * np.sin(2 * np.pi * 440 * t_tono) * np.hanning(n_tono)

    # Aplicar eco por convolucion
    y_eco = np.convolve(senal_5, h_eco)

    fig_5, axes_5 = plt.subplots(3, 1, figsize=(10, 7))

    t_senal = np.arange(len(senal_5)) / fs_5
    t_eco = np.arange(len(y_eco)) / fs_5

    axes_5[0].plot(np.arange(len(h_eco)) / fs_5 * 1000, h_eco, 'b-')
    axes_5[0].set_title(f'IR del eco: h[0]=1, h[{D_5}]=0.5 (retardo={retardo_s} s)')
    axes_5[0].set_xlabel('Tiempo (ms)')
    axes_5[0].grid(True, alpha=0.3)

    axes_5[1].plot(t_senal, senal_5, 'g-')
    axes_5[1].set_title('Senal original: tono de 440 Hz (0.1 s)')
    axes_5[1].set_xlabel('Tiempo (s)')
    axes_5[1].grid(True, alpha=0.3)

    axes_5[2].plot(t_eco, y_eco, 'purple')
    axes_5[2].set_title('Senal con eco (convolucion)')
    axes_5[2].set_xlabel('Tiempo (s)')
    axes_5[2].grid(True, alpha=0.3)
    axes_5[2].axvline(x=retardo_s, color='r', linestyle='--', alpha=0.5, label=f'Inicio del eco ({retardo_s} s)')
    axes_5[2].legend()

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Comparacion de rendimiento
    """)
    return


@app.cell
def _(np):
    import time
    from scipy.signal import fftconvolve

    # Ejercicio 6: Comparacion de rendimiento
    N_6 = 44100
    x_6 = np.random.randn(N_6)
    h_6 = np.random.randn(N_6)

    # np.convolve
    t_start = time.perf_counter()
    y_np_6 = np.convolve(x_6, h_6, mode='full')
    t_np = time.perf_counter() - t_start

    # fftconvolve
    t_start = time.perf_counter()
    y_fft_6 = fftconvolve(x_6, h_6, mode='full')
    t_fft = time.perf_counter() - t_start

    # Verificar resultados
    error_6 = np.max(np.abs(y_np_6 - y_fft_6))
    speedup = t_np / t_fft

    print("=== Comparacion de rendimiento ===")
    print(f"Largo de senales: {N_6} muestras (1 segundo a 44100 Hz)")
    print(f"np.convolve:   {t_np*1000:.2f} ms")
    print(f"fftconvolve:   {t_fft*1000:.2f} ms")
    print(f"Speedup:       {speedup:.1f}x mas rapido")
    print(f"Error maximo:  {error_6:.2e} (resultados practicamente identicos)")
    print(f"\nConclusion: para audio, siempre usar fftconvolve!")
    return fftconvolve, time


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: IR sintetica de sala
    """)
    return


@app.cell
def _(fftconvolve, np, plt):
    # Ejercicio 7: IR sintetica
    fs_7 = 44100
    T60_7 = 1.0
    duracion_ir_7 = 1.5
    N_ir_7 = int(fs_7 * duracion_ir_7)
    t_ir_7 = np.arange(N_ir_7) / fs_7

    # Construir IR
    h_7 = np.zeros(N_ir_7)

    # 1. Sonido directo
    h_7[0] = 1.0

    # 2. Reflexiones tempranas (5 reflexiones entre 10-80 ms)
    np.random.seed(7)
    tiempos_ref = np.sort(np.random.uniform(0.01, 0.08, 5))
    amplitudes_ref = np.array([0.6, -0.45, 0.35, -0.25, 0.18])
    for t_r, a_r in zip(tiempos_ref, amplitudes_ref):
        idx = int(t_r * fs_7)
        h_7[idx] = a_r

    # 3. Cola reverberante
    alpha_7 = 6.908 / T60_7
    envolvente_7 = np.exp(-alpha_7 * t_ir_7)
    ruido_7 = np.random.randn(N_ir_7) * 0.08
    h_7 += ruido_7 * envolvente_7
    h_7[0] = 1.0  # Restaurar pico

    # Normalizar
    h_7 = h_7 / np.max(np.abs(h_7))

    # Generar click
    N_click_7 = int(fs_7 * 0.5)
    click_7 = np.zeros(N_click_7)
    click_largo = 44  # ~1 ms
    click_7[100:100+click_largo] = np.hanning(click_largo) * 0.9

    # Convolucionar
    y_7 = fftconvolve(click_7, h_7, mode='full')
    y_7 = y_7 / np.max(np.abs(y_7)) * 0.9

    fig_7, axes_7 = plt.subplots(3, 1, figsize=(10, 7))

    axes_7[0].plot(t_ir_7 * 1000, h_7, 'b-', linewidth=0.5)
    axes_7[0].set_title(f'IR sintetica de sala (T60 = {T60_7} s)')
    axes_7[0].set_xlabel('Tiempo (ms)')
    axes_7[0].set_ylabel('Amplitud')
    axes_7[0].grid(True, alpha=0.3)

    t_click_7 = np.arange(N_click_7) / fs_7 * 1000
    axes_7[1].plot(t_click_7, click_7, 'g-')
    axes_7[1].set_title('Click original')
    axes_7[1].set_xlabel('Tiempo (ms)')
    axes_7[1].set_ylabel('Amplitud')
    axes_7[1].grid(True, alpha=0.3)

    t_y_7 = np.arange(len(y_7)) / fs_7 * 1000
    axes_7[2].plot(t_y_7, y_7, 'purple', linewidth=0.5)
    axes_7[2].set_title('Click convolucionado con IR (click con reverb de sala)')
    axes_7[2].set_xlabel('Tiempo (ms)')
    axes_7[2].set_ylabel('Amplitud')
    axes_7[2].grid(True, alpha=0.3)

    plt.tight_layout()
    print("El click ahora tiene la 'firma acustica' de la sala sintetica.")
    print("Se puede escuchar: el click original seguido de reflexiones y una cola reverberante.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Deconvolucion basica
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 8: Deconvolucion
    fs_8 = 44100

    # Senal conocida: barrido de senos corto (0.1 s)
    duracion_8 = 0.1
    N_8 = int(fs_8 * duracion_8)
    t_8 = np.linspace(0, duracion_8, N_8, endpoint=False)
    f1_8, f2_8 = 100.0, 10000.0
    x_8 = 0.5 * np.sin(
        2 * np.pi * f1_8 * duracion_8 / np.log(f2_8 / f1_8) *
        (np.exp(t_8 / duracion_8 * np.log(f2_8 / f1_8)) - 1)
    )

    # IR conocida
    h_8 = np.array([1.0, 0.5, -0.3, 0.1])

    # Convolucion
    y_8 = np.convolve(x_8, h_8)

    # Deconvolucion via FFT
    N_fft_8 = len(y_8)
    X_8 = np.fft.fft(x_8, n=N_fft_8)
    Y_8 = np.fft.fft(y_8, n=N_fft_8)

    # Division con regularizacion
    epsilon_8 = 1e-6 * np.max(np.abs(X_8))
    H_8 = Y_8 / (X_8 + epsilon_8)
    h_recuperada_8 = np.real(np.fft.ifft(H_8))

    # Comparar (solo las primeras muestras relevantes)
    n_comp_8 = len(h_8)
    error_8 = np.max(np.abs(h_8 - h_recuperada_8[:n_comp_8]))

    print("Deconvolucion via FFT:")
    print(f"  h original:    {h_8}")
    print(f"  h recuperada:  {np.round(h_recuperada_8[:n_comp_8], 6)}")
    print(f"  Error maximo:  {error_8:.2e}")

    fig_8, axes_8 = plt.subplots(2, 2, figsize=(12, 6))

    axes_8[0, 0].plot(t_8 * 1000, x_8, 'b-')
    axes_8[0, 0].set_title('x: barrido de senos (senal conocida)')
    axes_8[0, 0].set_xlabel('Tiempo (ms)')
    axes_8[0, 0].grid(True, alpha=0.3)

    axes_8[0, 1].stem(np.arange(len(h_8)), h_8, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_8[0, 1].set_title('h original (IR a recuperar)')
    axes_8[0, 1].set_xlabel('n')
    axes_8[0, 1].grid(True, alpha=0.3)

    t_y8 = np.arange(len(y_8)) / fs_8 * 1000
    axes_8[1, 0].plot(t_y8, y_8, 'purple')
    axes_8[1, 0].set_title('y = x * h (convolucion)')
    axes_8[1, 0].set_xlabel('Tiempo (ms)')
    axes_8[1, 0].grid(True, alpha=0.3)

    axes_8[1, 1].stem(np.arange(n_comp_8), h_8, linefmt='g-', markerfmt='go', basefmt='g-', label='h original')
    axes_8[1, 1].stem(np.arange(n_comp_8) + 0.2, h_recuperada_8[:n_comp_8],
                       linefmt='r--', markerfmt='rx', basefmt='r-', label='h recuperada')
    axes_8[1, 1].set_title(f'Comparacion (error = {error_8:.2e})')
    axes_8[1, 1].set_xlabel('n')
    axes_8[1, 1].legend()
    axes_8[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    print("\nLa deconvolucion recupera la IR con muy alta precision.")
    print("El pequeno error se debe a la regularizacion (epsilon).")
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
