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
    # Senales y Sistemas - Clase 8
    ## Convolucion + Entrega 1

    **Fecha**: 19 de mayo de 2026 | **Pilares**: P1 (principal), P3 (principal)

    En esta clase vamos a:
    1. Entender la convolucion discreta
    2. Calcularla paso a paso y con codigo
    3. Conocer sus propiedades
    4. Aplicar convolucion al audio: reverb
    5. Introducir la deconvolucion
    6. Pautas para la revision de codigo del Milestone 1
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
    ## 1. Definicion de Convolucion

    La **convolucion discreta** es la operacion fundamental de los sistemas LTI. Dadas dos senales $x[n]$ y $h[n]$, su convolucion es:

    $$y[n] = (x * h)[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

    ### Interpretacion

    Para calcular $y[n]$ en un instante $n$ especifico:
    1. **Invertir** $h[k]$ para obtener $h[-k]$
    2. **Desplazar** para obtener $h[n-k]$
    3. **Multiplicar** $x[k] \cdot h[n-k]$ muestra a muestra
    4. **Sumar** todos los productos

    ### Por que convolucion?

    En un sistema LTI con respuesta al impulso $h[n]$, la salida para **cualquier** entrada $x[n]$ es:

    $$y[n] = x[n] * h[n]$$

    Es decir, la convolucion con la respuesta al impulso nos da la salida del sistema.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplo paso a paso

    Convolucionemos $x = [1, 2, 3]$ con $h = [1, 0, -1]$:

    | $n$ | Calculo | $y[n]$ |
    |-----|---------|--------|
    | 0 | $x[0] \cdot h[0] = 1 \cdot 1$ | **1** |
    | 1 | $x[0] \cdot h[1] + x[1] \cdot h[0] = 1 \cdot 0 + 2 \cdot 1$ | **2** |
    | 2 | $x[0] \cdot h[2] + x[1] \cdot h[1] + x[2] \cdot h[0] = 1 \cdot (-1) + 2 \cdot 0 + 3 \cdot 1$ | **2** |
    | 3 | $x[1] \cdot h[2] + x[2] \cdot h[1] = 2 \cdot (-1) + 3 \cdot 0$ | **-2** |
    | 4 | $x[2] \cdot h[2] = 3 \cdot (-1)$ | **-3** |

    Resultado: $y = [1, 2, 2, -2, -3]$

    **Nota**: si $x$ tiene $N$ muestras y $h$ tiene $M$ muestras, el resultado tiene $N + M - 1$ muestras.
    """)
    return


@app.cell
def _(np, plt):
    # Demostracion interactiva: convolucion paso a paso
    x_demo = np.array([1.0, 2.0, 3.0])
    h_demo = np.array([1.0, 0.0, -1.0])

    y_demo = np.convolve(x_demo, h_demo)
    print(f"x = {x_demo}")
    print(f"h = {h_demo}")
    print(f"y = x * h = {y_demo}")
    print(f"Largo: len(x)={len(x_demo)} + len(h)={len(h_demo)} - 1 = {len(y_demo)}")

    # Visualizacion del proceso paso a paso
    fig_paso, axes_paso = plt.subplots(3, 3, figsize=(14, 10))

    N_x = len(x_demo)
    N_h = len(h_demo)
    N_y = N_x + N_h - 1
    k_range = np.arange(-1, N_y + 1)

    for idx_n, n_val in enumerate(range(N_y)):
        row = idx_n // 3
        col = idx_n % 3
        ax = axes_paso[row, col]

        # x[k]
        x_padded = np.zeros(len(k_range))
        for i, k in enumerate(k_range):
            if 0 <= k < N_x:
                x_padded[i] = x_demo[k]

        # h[n-k] (h invertido y desplazado)
        h_shifted = np.zeros(len(k_range))
        for i, k in enumerate(k_range):
            idx_h = n_val - k
            if 0 <= idx_h < N_h:
                h_shifted[i] = h_demo[idx_h]

        ax.bar(k_range - 0.15, x_padded, width=0.3, color='blue', alpha=0.7, label='x[k]')
        ax.bar(k_range + 0.15, h_shifted, width=0.3, color='red', alpha=0.7, label='h[n-k]')
        ax.set_title(f'n={n_val}: y[{n_val}] = {y_demo[n_val]:.0f}')
        ax.set_xlabel('k')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(-1.5, N_y + 0.5)
        ax.set_ylim(-3.5, 3.5)

    # Ocultar subplot extra
    axes_paso[1, 2].set_visible(False)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Implementacion desde cero vs NumPy
    """)
    return


@app.cell
def _(np):
    # Implementacion de convolucion desde cero
    def convolucion_manual(x, h):
        """Convolucion discreta implementada con loops."""
        N = len(x)
        M = len(h)
        y = np.zeros(N + M - 1)

        for n in range(N + M - 1):
            for k in range(N):
                if 0 <= n - k < M:
                    y[n] += x[k] * h[n - k]
        return y

    # Verificar contra np.convolve
    x_test = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    h_test = np.array([1.0, -1.0, 0.5])

    y_manual = convolucion_manual(x_test, h_test)
    y_numpy = np.convolve(x_test, h_test)

    print("Implementacion manual vs NumPy:")
    print(f"  x = {x_test}")
    print(f"  h = {h_test}")
    print(f"  y (manual): {y_manual}")
    print(f"  y (numpy):  {y_numpy}")
    print(f"  Error maximo: {np.max(np.abs(y_manual - y_numpy)):.2e}")
    return (convolucion_manual,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Propiedades de la Convolucion

    La convolucion tiene propiedades muy utiles que simplifican el analisis de sistemas.

    ### 2.1 Conmutativa: $x * h = h * x$
    El orden no importa.
    """)
    return


@app.cell
def _(np):
    # Propiedad conmutativa
    x_comm = np.array([1, 2, 3, 4])
    h_comm = np.array([0.5, 1, 0.5])

    y1_comm = np.convolve(x_comm, h_comm)
    y2_comm = np.convolve(h_comm, x_comm)

    print("Conmutativa: x * h = h * x")
    print(f"  x * h = {y1_comm}")
    print(f"  h * x = {y2_comm}")
    print(f"  Iguales: {np.allclose(y1_comm, y2_comm)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.2 Asociativa: $(x * h_1) * h_2 = x * (h_1 * h_2)$
    Podemos combinar dos filtros en uno.
    """)
    return


@app.cell
def _(np):
    # Propiedad asociativa
    x_assoc = np.array([1, 0, -1, 2, 1])
    h1_assoc = np.array([1, 0.5])
    h2_assoc = np.array([1, -1])

    # (x * h1) * h2
    y_izq = np.convolve(np.convolve(x_assoc, h1_assoc), h2_assoc)
    # x * (h1 * h2)
    h_combinado = np.convolve(h1_assoc, h2_assoc)
    y_der = np.convolve(x_assoc, h_combinado)

    print("Asociativa: (x * h1) * h2 = x * (h1 * h2)")
    print(f"  (x * h1) * h2 = {y_izq}")
    print(f"  x * (h1 * h2) = {y_der}")
    print(f"  Iguales: {np.allclose(y_izq, y_der)}")
    print(f"\n  h1 * h2 = {h_combinado} (filtro combinado)")
    print("  Utilidad: podemos combinar dos filtros en cascada en uno solo!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.3 Distributiva: $x * (h_1 + h_2) = x * h_1 + x * h_2$
    """)
    return


@app.cell
def _(np):
    # Propiedad distributiva
    x_dist = np.array([1, 2, 3])
    h1_dist = np.array([1, 0.5])
    h2_dist = np.array([0, -1, 0.3])

    # Necesitamos que h1 y h2 tengan el mismo largo para sumarlos
    max_len = max(len(h1_dist), len(h2_dist))
    h1_pad = np.pad(h1_dist, (0, max_len - len(h1_dist)))
    h2_pad = np.pad(h2_dist, (0, max_len - len(h2_dist)))

    y_izq_d = np.convolve(x_dist, h1_pad + h2_pad)
    y_der_d = np.convolve(x_dist, h1_pad) + np.convolve(x_dist, h2_pad)

    # Ajustar largos para la comparacion
    min_len = min(len(y_izq_d), len(y_der_d))
    print("Distributiva: x * (h1 + h2) = x * h1 + x * h2")
    print(f"  x * (h1 + h2) = {y_izq_d[:min_len]}")
    print(f"  x*h1 + x*h2   = {y_der_d[:min_len]}")
    print(f"  Iguales: {np.allclose(y_izq_d[:min_len], y_der_d[:min_len])}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.4 Identidad: $x * \delta = x$
    Convolucionar con el impulso devuelve la senal original.
    """)
    return


@app.cell
def _(np, plt):
    # Propiedad de identidad
    x_id = np.array([1, 3, -2, 5, 0, -1])
    delta_id = np.array([1.0])  # Impulso unitario

    y_id = np.convolve(x_id, delta_id)

    print("Identidad: x * delta = x")
    print(f"  x         = {x_id}")
    print(f"  x * delta = {y_id}")
    print(f"  Iguales: {np.allclose(x_id, y_id)}")
    print("\nEsto tiene sentido: delta[n] es el 'elemento neutro' de la convolucion,")
    print("como el 1 es el elemento neutro de la multiplicacion.")

    # Visualizar todas las propiedades
    fig_prop, axes_prop = plt.subplots(2, 2, figsize=(10, 6))

    # Conmutativa
    x_p = np.array([1, 2, 3, 0, 0])
    h_p = np.array([1, 0, -1])
    axes_prop[0, 0].stem(np.arange(len(np.convolve(x_p, h_p))), np.convolve(x_p, h_p),
                          linefmt='b-', markerfmt='bo', basefmt='b-', label='x*h')
    axes_prop[0, 0].stem(np.arange(len(np.convolve(h_p, x_p))), np.convolve(h_p, x_p),
                          linefmt='r--', markerfmt='rx', basefmt='r-', label='h*x')
    axes_prop[0, 0].set_title('Conmutativa: x*h = h*x')
    axes_prop[0, 0].legend()
    axes_prop[0, 0].grid(True, alpha=0.3)

    # Asociativa
    h1_p = np.array([1, 0.5])
    h2_p = np.array([1, -1])
    y_a1 = np.convolve(np.convolve(x_p, h1_p), h2_p)
    y_a2 = np.convolve(x_p, np.convolve(h1_p, h2_p))
    axes_prop[0, 1].stem(np.arange(len(y_a1)), y_a1, linefmt='b-', markerfmt='bo', basefmt='b-', label='(x*h1)*h2')
    axes_prop[0, 1].stem(np.arange(len(y_a2)), y_a2, linefmt='r--', markerfmt='rx', basefmt='r-', label='x*(h1*h2)')
    axes_prop[0, 1].set_title('Asociativa')
    axes_prop[0, 1].legend()
    axes_prop[0, 1].grid(True, alpha=0.3)

    # Identidad
    delta_p = np.array([1.0])
    y_id_p = np.convolve(x_p, delta_p)
    axes_prop[1, 0].stem(np.arange(len(x_p)), x_p, linefmt='b-', markerfmt='bo', basefmt='b-', label='x')
    axes_prop[1, 0].stem(np.arange(len(y_id_p)), y_id_p, linefmt='r--', markerfmt='rx', basefmt='r-', label='x*delta')
    axes_prop[1, 0].set_title(r'Identidad: x * $\delta$ = x')
    axes_prop[1, 0].legend()
    axes_prop[1, 0].grid(True, alpha=0.3)

    # Desplazamiento
    delta_d = np.zeros(5)
    delta_d[3] = 1.0  # delta desplazada 3 muestras
    y_desp = np.convolve(x_p, delta_d)
    axes_prop[1, 1].stem(np.arange(len(x_p)), x_p, linefmt='b-', markerfmt='bo', basefmt='b-', label='x')
    axes_prop[1, 1].stem(np.arange(len(y_desp)), y_desp, linefmt='r--', markerfmt='rx', basefmt='r-', label=r'x * $\delta$[n-3]')
    axes_prop[1, 1].set_title(r'x * $\delta$[n-3] = x[n-3] (desplazamiento)')
    axes_prop[1, 1].legend()
    axes_prop[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Convolucion Eficiente

    La convolucion directa (con loops) tiene complejidad $O(N \cdot M)$, lo cual es **muy lento** para senales de audio largas.

    ### Convolucion via FFT

    Gracias al **teorema de convolucion**, la convolucion en el dominio del tiempo equivale a una multiplicacion en frecuencia:

    $$x[n] * h[n] \quad \longleftrightarrow \quad X[k] \cdot H[k]$$

    Algoritmo:
    1. Calcular FFT de $x$ y $h$ (con zero-padding apropiado)
    2. Multiplicar: $Y[k] = X[k] \cdot H[k]$
    3. Calcular IFFT: $y[n] = \text{IFFT}(Y[k])$

    Complejidad: $O(N \log N)$ — mucho mas rapido para senales largas.

    `scipy.signal.fftconvolve` implementa esto de forma optimizada.
    """)
    return


@app.cell
def _(np):
    import time
    from scipy.signal import fftconvolve

    # Comparacion de rendimiento
    print("=== Comparacion de rendimiento ===\n")

    tamaños = [100, 1000, 10000, 44100]
    for N in tamaños:
        x_perf = np.random.randn(N)
        h_perf = np.random.randn(min(N, 4410))  # IR de ~100ms

        # np.convolve (directo)
        t_inicio = time.perf_counter()
        for _ in range(3):
            y_np = np.convolve(x_perf, h_perf, mode='full')
        t_np = (time.perf_counter() - t_inicio) / 3

        # fftconvolve
        t_inicio = time.perf_counter()
        for _ in range(3):
            y_fft = fftconvolve(x_perf, h_perf, mode='full')
        t_fft = (time.perf_counter() - t_inicio) / 3

        error = np.max(np.abs(y_np - y_fft))
        speedup = t_np / t_fft if t_fft > 0 else float('inf')

        print(f"N={N:>6d}, M={min(N,4410):>5d}: np.convolve={t_np*1000:>8.3f} ms, "
              f"fftconvolve={t_fft*1000:>8.3f} ms, speedup={speedup:>6.1f}x, error={error:.2e}")

    print("\nConclusion: para senales de audio (>10000 muestras), fftconvolve es mucho mas rapido.")
    return fftconvolve, time


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Convolucion en Audio: REVERB

    La aplicacion mas espectacular de la convolucion en audio es la **reverberacion por convolucion**:

    $$\text{audio\_wet}[n] = \text{audio\_seco}[n] * h_{\text{sala}}[n]$$

    Si tenemos la **respuesta al impulso** de una sala (catedral, estudio, sala de conciertos), podemos aplicar su acustica a cualquier grabacion seca.

    Esto es exactamente lo que hace un **reverb de convolucion** en un plugin de audio.
    """)
    return


@app.cell
def _(fftconvolve, np, plt):
    # Crear una IR sintetica de sala
    fs_conv = 44100
    T60_conv = 1.8  # segundos
    duracion_ir_conv = 2.5
    N_ir = int(fs_conv * duracion_ir_conv)
    n_ir_conv = np.arange(N_ir)
    t_ir_conv = n_ir_conv / fs_conv

    # IR sintetica: pico directo + reflexiones + cola reverberante
    np.random.seed(123)
    alpha_conv = 6.908 / T60_conv
    envolvente = np.exp(-alpha_conv * t_ir_conv)

    h_sala = np.zeros(N_ir)
    h_sala[0] = 1.0  # Sonido directo

    # Reflexiones tempranas
    reflexiones_conv = [(0.015, 0.65), (0.028, -0.45), (0.042, 0.35),
                        (0.051, -0.28), (0.063, 0.22), (0.078, -0.18)]
    for t_ref, amp_ref in reflexiones_conv:
        idx = int(t_ref * fs_conv)
        if idx < N_ir:
            h_sala[idx] += amp_ref

    # Cola reverberante
    ruido_cola = np.random.randn(N_ir) * 0.12
    h_sala += ruido_cola * envolvente
    h_sala[0] = 1.0

    # Normalizar
    h_sala = h_sala / np.max(np.abs(h_sala))

    # Crear senal "seca": clicks periodicos (simulando palmadas)
    duracion_seca = 3.0
    N_seco = int(fs_conv * duracion_seca)
    senal_seca = np.zeros(N_seco)

    # Clicks cada 0.5 segundos
    for i in range(6):
        idx_click = int(i * 0.5 * fs_conv)
        if idx_click < N_seco:
            # Click corto con ventana
            largo_click = 50
            click_ventana = np.hanning(largo_click) * 0.8
            fin = min(idx_click + largo_click, N_seco)
            senal_seca[idx_click:fin] = click_ventana[:fin - idx_click]

    # Convolucionar!
    senal_wet = fftconvolve(senal_seca, h_sala, mode='full')
    senal_wet = senal_wet[:N_seco + N_ir]  # Recortar
    senal_wet = senal_wet / np.max(np.abs(senal_wet)) * 0.9  # Normalizar

    t_seca = np.arange(N_seco) / fs_conv
    t_wet = np.arange(len(senal_wet)) / fs_conv

    fig_reverb, axes_reverb = plt.subplots(3, 1, figsize=(12, 8))

    axes_reverb[0].plot(t_ir_conv * 1000, h_sala, 'b-', linewidth=0.5)
    axes_reverb[0].set_title(f'Respuesta al impulso de sala (T60 = {T60_conv} s)')
    axes_reverb[0].set_xlabel('Tiempo (ms)')
    axes_reverb[0].set_ylabel('Amplitud')
    axes_reverb[0].grid(True, alpha=0.3)

    axes_reverb[1].plot(t_seca, senal_seca, 'g-')
    axes_reverb[1].set_title('Senal seca: clicks periodicos')
    axes_reverb[1].set_xlabel('Tiempo (s)')
    axes_reverb[1].set_ylabel('Amplitud')
    axes_reverb[1].grid(True, alpha=0.3)

    axes_reverb[2].plot(t_wet, senal_wet, 'purple', linewidth=0.5)
    axes_reverb[2].set_title('Senal con reverb: seca * IR de sala')
    axes_reverb[2].set_xlabel('Tiempo (s)')
    axes_reverb[2].set_ylabel('Amplitud')
    axes_reverb[2].grid(True, alpha=0.3)

    plt.tight_layout()
    print("REVERB = CONVOLUCION: senal_seca * h_sala = senal_con_reverb")
    print("Cada click ahora tiene la 'firma acustica' de la sala.")
    print(f"\nDuracion de la IR: {duracion_ir_conv} s ({N_ir:,} muestras)")
    print(f"Duracion de la senal seca: {duracion_seca} s ({N_seco:,} muestras)")
    print(f"Duracion del resultado: {len(senal_wet)/fs_conv:.1f} s ({len(senal_wet):,} muestras)")
    plt.gca()
    return fs_conv, h_sala


@app.cell
def _(mo):
    mo.md(r"""
    ### La conexion con el TP

    En el trabajo practico:
    1. **Emiten** un barrido de senos (sine sweep) en la sala
    2. **Graban** la respuesta de la sala
    3. La grabacion es: $y[n] = \text{sweep}[n] * h_{\text{sala}}[n]$
    4. Necesitan **recuperar** $h_{\text{sala}}[n]$ a partir de $y[n]$ y el sweep
    5. Esto es la **deconvolucion**

    Es decir, el TP es el proceso **inverso** de lo que acabamos de hacer!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Deconvolucion (Introduccion)

    Si $y = x * h$, queremos encontrar $h$ conociendo $x$ e $y$.

    En el dominio de la frecuencia:

    $$Y[k] = X[k] \cdot H[k] \quad \Rightarrow \quad H[k] = \frac{Y[k]}{X[k]}$$

    $$h[n] = \text{IFFT}\left(\frac{Y[k]}{X[k]}\right)$$

    ### Para barridos de senos (sine sweep)

    El metodo de Farina (2000) es mas elegante:
    1. Se genera un **filtro inverso** del sweep
    2. Se convoluciona la grabacion con el filtro inverso
    3. El resultado es la respuesta al impulso

    Veremos esto en detalle en la Clase 9. Por ahora, veamos el concepto basico:
    """)
    return


@app.cell
def _(fftconvolve, fs_conv, h_sala, np, plt):
    # Demostracion basica de deconvolucion con FFT
    # Senal conocida
    N_deconv = 44100  # 1 segundo
    x_conocida = np.random.randn(N_deconv) * 0.1  # Ruido (senal conocida)
    x_conocida[:100] = 0  # Un poco de silencio al inicio

    # Respuesta (convolucion con la IR de sala)
    h_corta = h_sala[:int(0.5 * fs_conv)]  # IR de 0.5 s para simplificar
    y_respuesta = fftconvolve(x_conocida, h_corta, mode='full')

    # Deconvolucion via FFT
    N_fft = len(y_respuesta)
    X_fft = np.fft.fft(x_conocida, n=N_fft)
    Y_fft = np.fft.fft(y_respuesta, n=N_fft)

    # Division en frecuencia (con regularizacion para evitar division por cero)
    epsilon = 1e-6 * np.max(np.abs(X_fft))
    H_recuperada = Y_fft / (X_fft + epsilon)
    h_recuperada = np.real(np.fft.ifft(H_recuperada))

    # Comparar
    fig_deconv, axes_deconv = plt.subplots(2, 1, figsize=(10, 5))

    t_h = np.arange(len(h_corta)) / fs_conv * 1000
    t_hr = np.arange(min(len(h_corta), len(h_recuperada))) / fs_conv * 1000
    n_comp = min(len(h_corta), len(h_recuperada))

    axes_deconv[0].plot(t_h, h_corta, 'b-', linewidth=0.5, label='h original')
    axes_deconv[0].set_title('Respuesta al impulso original')
    axes_deconv[0].set_xlabel('Tiempo (ms)')
    axes_deconv[0].legend()
    axes_deconv[0].grid(True, alpha=0.3)

    axes_deconv[1].plot(t_hr, h_recuperada[:n_comp], 'r-', linewidth=0.5, label='h recuperada')
    axes_deconv[1].set_title('Respuesta al impulso recuperada por deconvolucion')
    axes_deconv[1].set_xlabel('Tiempo (ms)')
    axes_deconv[1].legend()
    axes_deconv[1].grid(True, alpha=0.3)

    plt.tight_layout()

    error_deconv = np.max(np.abs(h_corta - h_recuperada[:len(h_corta)]))
    print(f"Error maximo de la deconvolucion: {error_deconv:.6f}")
    print("\nNota: la deconvolucion no es perfecta debido a la regularizacion (epsilon).")
    print("En la practica, usar barridos de senos da mejores resultados que ruido.")
    print("Veremos el metodo de Farina en detalle en la Clase 9.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Pautas para Revision de Codigo (Entrega 1 / Milestone 1)

    La revision de codigo (*code review*) es una practica fundamental en desarrollo de software. Hoy cada grupo presentara su Milestone 1 y recibira feedback.

    ### Que buscar en una revision de codigo

    1. **Funcionalidad**: El codigo hace lo que dice?
    2. **Legibilidad**: Se entiende que hace cada parte?
    3. **Organizacion**: Los archivos y funciones estan bien organizados?
    4. **Documentacion**: Hay docstrings y comentarios donde hacen falta?
    5. **Testing**: Hay tests? Cubren los casos importantes?
    6. **Errores comunes**: Hay bugs potenciales?

    ### Checklist para el Milestone 1 del TP

    - [ ] Generacion de senal de excitacion (barrido de senos) implementada
    - [ ] Funcionalidad de grabacion/reproduccion implementada (o simulada)
    - [ ] Codigo organizado en funciones/modulos
    - [ ] Repositorio en GitHub con README basico
    - [ ] Al menos un test unitario
    - [ ] Documentacion minima (docstrings en funciones principales)
    - [ ] Sin credenciales o datos sensibles en el repo
    - [ ] .gitignore configurado (ignorar __pycache__, .pyc, archivos de audio grandes)

    ### Como dar feedback constructivo

    | En vez de... | Decir... |
    |-------------|---------|
    | "Esto esta mal" | "Podrias considerar usar X en vez de Y porque..." |
    | "No entiendo nada" | "Me cuesta seguir esta parte, podrias agregar un comentario?" |
    | "Esto es ineficiente" | "Para senales largas, fftconvolve seria mas rapido aca" |
    | "Falta testing" | "Estaria bueno agregar un test para el caso de..." |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy aprendimos:

    1. **Convolucion discreta**: $y[n] = \sum_k x[k] \cdot h[n-k]$
    2. **Propiedades**: conmutativa, asociativa, distributiva, identidad
    3. **Convolucion eficiente**: FFT-based es $O(N \log N)$ vs $O(NM)$ directo
    4. **Reverb por convolucion**: senal_seca * IR_sala = senal_con_reverb
    5. **Deconvolucion**: proceso inverso, recuperar h a partir de x e y
    6. **Code review**: pautas para la revision del Milestone 1

    ### Para la proxima clase
    - Completar los 8 ejercicios de `ejercicios.py`
    - Proxima clase: Barridos de senos y medicion de respuesta al impulso (metodo de Farina)
    """)
    return


if __name__ == "__main__":
    app.run()
