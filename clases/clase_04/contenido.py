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
    ## Clase 4: El Universo NumPy y las Senales

    Hoy damos un salto fundamental: pasamos de Python puro a **NumPy**, la biblioteca que nos permite trabajar con senales de forma eficiente. Vamos a representar senales discretas como arrays, generar senales basicas, y visualizarlas con Matplotlib.

    **Pilares**: P1 (principal), P2 (secundario)
    """)
    return


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
    ---
    ## 1. Fundamentos de NumPy

    NumPy es la base del ecosistema cientifico de Python. Su objeto principal es el **ndarray** (N-dimensional array): un contenedor eficiente de datos numericos homogeneos.

    ### Por que NumPy y no listas?

    - **Velocidad**: operaciones vectorizadas en C, no loops en Python
    - **Memoria**: datos contiguos en memoria, no punteros dispersos
    - **Funcionalidad**: miles de funciones matematicas optimizadas
    - **Ecosistema**: SciPy, Matplotlib, scikit-learn, etc. trabajan con arrays
    """)
    return


@app.cell
def _(np):
    # Crear arrays de diferentes formas
    a1 = np.array([1, 2, 3, 4, 5])          # desde una lista
    a2 = np.zeros(10)                         # 10 ceros
    a3 = np.ones(5)                           # 5 unos
    a4 = np.linspace(0, 1, 11)               # 11 puntos entre 0 y 1
    a5 = np.arange(0, 1, 0.1)               # de 0 a 1 con paso 0.1

    print("np.array([1,2,3,4,5]):", a1)
    print("np.zeros(10):         ", a2)
    print("np.ones(5):           ", a3)
    print("np.linspace(0,1,11):  ", a4)
    print("np.arange(0,1,0.1):   ", a5)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Propiedades de un array

    Todo array tiene atributos que describen su estructura:
    """)
    return


@app.cell
def _(np):
    # Propiedades fundamentales
    senal = np.array([0.1, -0.3, 0.5, -0.7, 0.9, -0.2, 0.4])

    print(f"Array:  {senal}")
    print(f"Shape:  {senal.shape}")      # dimensiones
    print(f"Dtype:  {senal.dtype}")      # tipo de datos
    print(f"Size:   {senal.size}")       # numero total de elementos
    print(f"Ndim:   {senal.ndim}")       # numero de dimensiones
    print(f"Nbytes: {senal.nbytes}")     # bytes en memoria

    # Array 2D (como una matriz de senales)
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatriz:\n{matriz}")
    print(f"Shape: {matriz.shape}")  # (filas, columnas)
    print(f"Ndim:  {matriz.ndim}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Indexing y slicing

    Funcionan similar a las listas, pero mucho mas potentes. En audio, esto equivale a **extraer fragmentos** de una senal.
    """)
    return


@app.cell
def _(np):
    # Simulamos una senal de audio corta
    audio = np.array([0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1])

    print(f"Senal completa:          {audio}")
    print(f"Primera muestra:         {audio[0]}")
    print(f"Ultima muestra:          {audio[-1]}")
    print(f"Muestras 2 a 5:          {audio[2:6]}")
    print(f"Cada 2 muestras:         {audio[::2]}")
    print(f"Senal invertida:         {audio[::-1]}")

    # Indexing booleano: muy util para procesamiento
    print(f"\nMuestras > 0.5:          {audio[audio > 0.5]}")
    print(f"Indices donde > 0.5:     {np.where(audio > 0.5)[0]}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Broadcasting

    Broadcasting es la capacidad de NumPy de operar entre arrays de diferentes tamanos de forma automatica. Es fundamental para trabajar con senales.

    **Reglas de broadcasting**:
    1. Si los arrays tienen diferente numero de dimensiones, se agrega un 1 a la izquierda del shape mas corto
    2. Los arrays son compatibles en una dimension si tienen el mismo tamano o uno de ellos tiene tamano 1
    3. El resultado tiene el tamano maximo en cada dimension
    """)
    return


@app.cell
def _(np):
    # Broadcasting basico: escalar * array
    senal_b = np.array([0.5, -0.3, 0.8, -0.6])
    ganancia = 0.5
    senal_atenuada = ganancia * senal_b  # multiplica cada elemento
    print(f"Senal original:  {senal_b}")
    print(f"Senal * 0.5:     {senal_atenuada}")

    # Broadcasting: array + escalar (DC offset)
    senal_con_offset = senal_b + 0.2
    print(f"Senal + 0.2:     {senal_con_offset}")

    # Broadcasting 2D: aplicar diferentes ganancias a diferentes canales
    estereo = np.array([[0.5, 0.3, -0.2],    # canal izquierdo
                        [0.4, -0.1, 0.6]])    # canal derecho
    ganancias = np.array([[0.8],   # ganancia izquierda
                          [1.2]])  # ganancia derecha
    resultado_b = estereo * ganancias
    print(f"\nEstereo original:\n{estereo}")
    print(f"Ganancias: {ganancias.flatten()}")
    print(f"Resultado:\n{resultado_b}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Operaciones vectorizadas vs loops

    La diferencia de rendimiento entre un loop de Python y una operacion vectorizada de NumPy es **enorme**. Veamos un ejemplo con audio: generar 1 segundo a 44100 Hz.
    """)
    return


@app.cell
def _(np):
    import time
    import math

    fs_demo = 44100
    duracion_demo = 1.0
    freq_demo = 440.0
    N_demo = int(fs_demo * duracion_demo)

    # Metodo 1: loop de Python
    inicio = time.perf_counter()
    senal_loop = []
    for i in range(N_demo):
        t_i = i / fs_demo
        senal_loop.append(math.sin(2 * math.pi * freq_demo * t_i))
    senal_loop = np.array(senal_loop)
    tiempo_loop = time.perf_counter() - inicio

    # Metodo 2: NumPy vectorizado
    inicio = time.perf_counter()
    t_vec = np.arange(N_demo) / fs_demo
    senal_vec = np.sin(2 * np.pi * freq_demo * t_vec)
    tiempo_vec = time.perf_counter() - inicio

    print(f"Generando {N_demo} muestras de 440 Hz a {fs_demo} Hz:")
    print(f"  Loop Python: {tiempo_loop*1000:.2f} ms")
    print(f"  NumPy:       {tiempo_vec*1000:.2f} ms")
    print(f"  Speedup:     {tiempo_loop/tiempo_vec:.1f}x mas rapido")
    print(f"\n  Resultados iguales: {np.allclose(senal_loop, senal_vec)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Funciones matematicas esenciales

    NumPy incluye todas las funciones matematicas que necesitamos para senales:
    """)
    return


@app.cell
def _(np):
    x_math = np.array([0.1, 0.5, 1.0, 2.0, 10.0])

    print("Funciones trigonometricas:")
    print(f"  np.sin(pi/2)  = {np.sin(np.pi/2):.4f}")
    print(f"  np.cos(0)     = {np.cos(0):.4f}")

    print("\nFunciones exponenciales y logaritmicas:")
    print(f"  np.exp(1)     = {np.exp(1):.4f}")
    print(f"  np.log10({x_math}) = {np.log10(x_math)}")

    print("\nFunciones utiles para senales:")
    senal_m = np.array([-0.5, 0.3, -0.8, 0.6])
    print(f"  np.abs({senal_m})  = {np.abs(senal_m)}")
    print(f"  np.sqrt(abs):        {np.sqrt(np.abs(senal_m))}")

    print("\nEstadisticas:")
    datos = np.array([0.5, -0.3, 0.8, -0.6, 0.2])
    print(f"  np.mean({datos}) = {np.mean(datos):.4f}")
    print(f"  np.std({datos})  = {np.std(datos):.4f}")
    print(f"  np.max({datos})  = {np.max(datos):.4f}")
    print(f"  np.min({datos})  = {np.min(datos):.4f}")
    print(f"  np.sum({datos})  = {np.sum(datos):.4f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Senales discretas como arrays

    En el mundo digital, toda senal es una secuencia de numeros. Cada numero es una **muestra** tomada en un instante de tiempo. El **eje temporal** es fundamental.

    ### Construir el eje temporal

    Hay dos formas principales:
    - `np.arange(N) / fs` — N muestras a frecuencia de muestreo fs
    - `np.linspace(0, duracion, N, endpoint=False)` — N muestras en un intervalo

    **Importante**: usamos `endpoint=False` para senales periodicas. Si incluimos el endpoint, la ultima muestra coincide con la primera del siguiente periodo, duplicandola.
    """)
    return


@app.cell
def _(np, plt):
    # Demostrar por que endpoint=False importa
    fs_ep = 1000  # Hz
    f_ep = 100    # Hz
    duracion_ep = 0.01  # 10 ms = 1 periodo

    # CON endpoint (mal para senales periodicas)
    t_con = np.linspace(0, duracion_ep, int(fs_ep * duracion_ep) + 1, endpoint=True)
    x_con = np.sin(2 * np.pi * f_ep * t_con)

    # SIN endpoint (correcto)
    t_sin = np.linspace(0, duracion_ep, int(fs_ep * duracion_ep), endpoint=False)
    x_sin = np.sin(2 * np.pi * f_ep * t_sin)

    fig_ep, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.stem(t_con * 1000, x_con, linefmt='r-', markerfmt='ro', basefmt='k-')
    ax1.set_title(f"endpoint=True ({len(t_con)} muestras)")
    ax1.set_xlabel("Tiempo (ms)")
    ax1.set_ylabel("Amplitud")
    ax1.grid(True, alpha=0.3)
    ax1.annotate("Muestra duplicada!", xy=(t_con[-1]*1000, x_con[-1]),
                fontsize=9, color='red',
                xytext=(t_con[-1]*1000 - 2, 0.5),
                arrowprops=dict(arrowstyle='->', color='red'))

    ax2.stem(t_sin * 1000, x_sin, linefmt='b-', markerfmt='bo', basefmt='k-')
    ax2.set_title(f"endpoint=False ({len(t_sin)} muestras)")
    ax2.set_xlabel("Tiempo (ms)")
    ax2.set_ylabel("Amplitud")
    ax2.grid(True, alpha=0.3)

    fig_ep.suptitle("Por que usar endpoint=False para senales periodicas", fontsize=13)
    plt.tight_layout()
    fig_ep
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Senales basicas

    Toda la teoria de senales y sistemas se construye sobre un puñado de senales fundamentales.

    #### Impulso unitario $\delta[n]$

    $$\delta[n] = \begin{cases} 1 & n = 0 \\ 0 & n \neq 0 \end{cases}$$
    """)
    return


@app.cell
def _(np, plt):
    # Impulso unitario
    N_imp = 50
    n_imp = np.arange(N_imp)
    delta = np.zeros(N_imp)
    delta[0] = 1

    # Impulso desplazado en n0=10
    delta_n0 = np.zeros(N_imp)
    delta_n0[10] = 1

    fig_imp, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.stem(n_imp, delta, linefmt='b-', markerfmt='bo', basefmt='k-')
    ax1.set_title(r"Impulso unitario $\delta[n]$")
    ax1.set_xlabel("n (muestras)")
    ax1.set_ylabel("Amplitud")
    ax1.set_ylim(-0.2, 1.3)
    ax1.grid(True, alpha=0.3)

    ax2.stem(n_imp, delta_n0, linefmt='r-', markerfmt='ro', basefmt='k-')
    ax2.set_title(r"Impulso desplazado $\delta[n - 10]$")
    ax2.set_xlabel("n (muestras)")
    ax2.set_ylabel("Amplitud")
    ax2.set_ylim(-0.2, 1.3)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_imp
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Escalon unitario $u[n]$

    $$u[n] = \begin{cases} 1 & n \geq 0 \\ 0 & n < 0 \end{cases}$$
    """)
    return


@app.cell
def _(np, plt):
    # Escalon unitario
    N_esc = 50
    n_esc = np.arange(-10, N_esc)
    u = np.heaviside(n_esc, 1)  # np.heaviside: 1 si n >= 0

    # Escalon desplazado
    n0_esc = 15
    u_n0 = np.heaviside(n_esc - n0_esc, 1)

    fig_esc, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.stem(n_esc, u, linefmt='b-', markerfmt='bo', basefmt='k-')
    ax1.set_title(r"Escalon unitario $u[n]$")
    ax1.set_xlabel("n (muestras)")
    ax1.set_ylabel("Amplitud")
    ax1.set_ylim(-0.2, 1.3)
    ax1.grid(True, alpha=0.3)

    ax2.stem(n_esc, u_n0, linefmt='r-', markerfmt='ro', basefmt='k-')
    ax2.set_title(r"Escalon desplazado $u[n - 15]$")
    ax2.set_xlabel("n (muestras)")
    ax2.set_ylabel("Amplitud")
    ax2.set_ylim(-0.2, 1.3)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_esc
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Rampa $r[n] = n \cdot u[n]$

    Crece linealmente a partir de $n = 0$.
    """)
    return


@app.cell
def _(np, plt):
    N_ramp = 50
    n_ramp = np.arange(N_ramp)
    rampa = n_ramp * np.heaviside(n_ramp, 1)

    fig_ramp, ax_ramp = plt.subplots(figsize=(8, 4))
    ax_ramp.stem(n_ramp, rampa, linefmt='g-', markerfmt='go', basefmt='k-')
    ax_ramp.set_title(r"Rampa $r[n] = n \cdot u[n]$")
    ax_ramp.set_xlabel("n (muestras)")
    ax_ramp.set_ylabel("Amplitud")
    ax_ramp.grid(True, alpha=0.3)
    plt.tight_layout()
    fig_ramp
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Senoidal $x[n] = A \sin(2\pi f_0 n / f_s + \phi)$

    La senal mas importante en audio. Cada sonido puede descomponerse en senoidales (lo veremos con Fourier).
    """)
    return


@app.cell
def _(mo):
    freq_slider = mo.ui.slider(
        start=100, stop=2000, step=10, value=440, label="Frecuencia (Hz)"
    )
    amp_slider = mo.ui.slider(
        start=0.1, stop=1.0, step=0.1, value=1.0, label="Amplitud"
    )
    phase_slider = mo.ui.slider(
        start=0, stop=360, step=15, value=0, label="Fase (grados)"
    )
    mo.md(f"""
    ### Senoidal interactiva

    Ajusta los parametros para ver como cambia la senal:

    {freq_slider}
    {amp_slider}
    {phase_slider}
    """)
    return amp_slider, freq_slider, phase_slider


@app.cell
def _(amp_slider, freq_slider, np, phase_slider, plt):
    fs_sin = 44100
    duracion_sin = 5.0 / freq_slider.value  # mostrar 5 periodos
    t_sin = np.arange(int(fs_sin * duracion_sin)) / fs_sin
    phi_rad = np.deg2rad(phase_slider.value)
    x_sin = amp_slider.value * np.sin(2 * np.pi * freq_slider.value * t_sin + phi_rad)

    fig_sin, ax_sin = plt.subplots(figsize=(12, 4))
    ax_sin.plot(t_sin * 1000, x_sin, 'b-', linewidth=1.5)
    ax_sin.set_title(
        f"Senoidal: A={amp_slider.value:.1f}, "
        f"f={freq_slider.value} Hz, "
        f"$\\phi$={phase_slider.value} grados"
    )
    ax_sin.set_xlabel("Tiempo (ms)")
    ax_sin.set_ylabel("Amplitud")
    ax_sin.set_ylim(-1.1, 1.1)
    ax_sin.grid(True, alpha=0.3)
    ax_sin.axhline(y=0, color='k', linewidth=0.5)
    plt.tight_layout()
    fig_sin
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Exponencial compleja $x[n] = A e^{j 2\pi f_0 n / f_s}$

    La exponencial compleja es la base de la transformada de Fourier. Tiene una parte real (coseno) y una imaginaria (seno).

    $$e^{j\theta} = \cos(\theta) + j\sin(\theta)$$
    """)
    return


@app.cell
def _(np, plt):
    fs_cexp = 44100
    f_cexp = 440
    duracion_cexp = 5.0 / f_cexp
    t_cexp = np.arange(int(fs_cexp * duracion_cexp)) / fs_cexp
    x_cexp = np.exp(1j * 2 * np.pi * f_cexp * t_cexp)

    fig_cexp, axes_cexp = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    axes_cexp[0].plot(t_cexp * 1000, np.real(x_cexp), 'b-', linewidth=1.5, label='Re (coseno)')
    axes_cexp[0].set_ylabel("Parte Real")
    axes_cexp[0].legend()
    axes_cexp[0].grid(True, alpha=0.3)
    axes_cexp[0].set_title(f"Exponencial compleja: $e^{{j 2\\pi \\cdot {f_cexp} \\cdot t}}$")

    axes_cexp[1].plot(t_cexp * 1000, np.imag(x_cexp), 'r-', linewidth=1.5, label='Im (seno)')
    axes_cexp[1].set_xlabel("Tiempo (ms)")
    axes_cexp[1].set_ylabel("Parte Imaginaria")
    axes_cexp[1].legend()
    axes_cexp[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_cexp
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Exponencial decreciente $x(t) = A e^{-\alpha t}$

    Muy relevante en acustica: modela la **reverberacion** de una sala. El parametro $T_{60}$ es el tiempo que tarda el sonido en decaer 60 dB. La relacion es:

    $$\alpha = \frac{\ln(10^3)}{T_{60}} = \frac{6.908}{T_{60}}$$
    """)
    return


@app.cell
def _(mo):
    t60_slider = mo.ui.slider(
        start=0.1, stop=5.0, step=0.1, value=2.0, label="T60 (segundos)"
    )
    mo.md(f"""
    ### Exponencial decreciente interactiva

    El T60 controla que tan rapido decae la reverberacion:

    {t60_slider}
    """)
    return (t60_slider,)


@app.cell
def _(np, plt, t60_slider):
    fs_exp = 1000  # baja fs para visualizacion
    T60 = t60_slider.value
    alpha = 6.908 / T60
    duracion_exp = T60 * 1.5  # mostrar un poco mas que T60
    t_exp = np.arange(int(fs_exp * duracion_exp)) / fs_exp
    x_exp = np.exp(-alpha * t_exp)

    fig_exp, (ax_lin, ax_db) = plt.subplots(1, 2, figsize=(14, 5))

    # Escala lineal
    ax_lin.plot(t_exp, x_exp, 'b-', linewidth=1.5)
    ax_lin.axvline(x=T60, color='r', linestyle='--', label=f'T60 = {T60:.1f} s')
    ax_lin.set_title("Escala lineal")
    ax_lin.set_xlabel("Tiempo (s)")
    ax_lin.set_ylabel("Amplitud")
    ax_lin.legend()
    ax_lin.grid(True, alpha=0.3)

    # Escala en dB
    x_exp_db = 20 * np.log10(np.maximum(x_exp, 1e-10))
    ax_db.plot(t_exp, x_exp_db, 'b-', linewidth=1.5)
    ax_db.axvline(x=T60, color='r', linestyle='--', label=f'T60 = {T60:.1f} s')
    ax_db.axhline(y=-60, color='g', linestyle=':', label='-60 dB')
    ax_db.set_title("Escala en dB")
    ax_db.set_xlabel("Tiempo (s)")
    ax_db.set_ylabel("Amplitud (dB)")
    ax_db.set_ylim(-80, 5)
    ax_db.legend()
    ax_db.grid(True, alpha=0.3)

    fig_exp.suptitle(f"Exponencial decreciente: T60 = {T60:.1f} s, alpha = {alpha:.2f}", fontsize=13)
    plt.tight_layout()
    fig_exp
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Matplotlib para senales

    Ya usamos Matplotlib en los ejemplos anteriores. Ahora veamos las **buenas practicas** de visualizacion para senales.

    ### Buenas vs malas practicas
    """)
    return


@app.cell
def _(np, plt):
    # Generar senal de ejemplo
    fs_plot = 44100
    t_plot = np.arange(int(fs_plot * 0.01)) / fs_plot
    x_plot = 0.8 * np.sin(2 * np.pi * 440 * t_plot) + 0.3 * np.sin(2 * np.pi * 880 * t_plot)

    fig_prac, (ax_bad, ax_good) = plt.subplots(1, 2, figsize=(14, 5))

    # MAL: sin labels, sin titulo, sin grid
    ax_bad.plot(x_plot)
    ax_bad.set_title("MAL: sin contexto", color='red', fontsize=12)

    # BIEN: labels, titulo, grid, unidades
    ax_good.plot(t_plot * 1000, x_plot, 'b-', linewidth=1.0)
    ax_good.set_title("BIEN: informacion completa", color='green', fontsize=12)
    ax_good.set_xlabel("Tiempo (ms)")
    ax_good.set_ylabel("Amplitud")
    ax_good.grid(True, alpha=0.3)
    ax_good.axhline(y=0, color='k', linewidth=0.5)

    plt.tight_layout()
    fig_prac
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Subplots: multiples graficos organizados

    En procesamiento de senales, frecuentemente necesitamos ver la misma senal de diferentes formas (tiempo, frecuencia, envolvente, etc.).
    """)
    return


@app.cell
def _(np, plt):
    # Ejemplo completo: senal con armonicos y su espectro
    fs_sub = 44100
    duracion_sub = 0.05  # 50 ms
    t_sub = np.arange(int(fs_sub * duracion_sub)) / fs_sub
    f0_sub = 440

    # Senal con fundamental + 2 armonicos
    x_sub = (1.0 * np.sin(2 * np.pi * f0_sub * t_sub) +
             0.5 * np.sin(2 * np.pi * 2 * f0_sub * t_sub) +
             0.25 * np.sin(2 * np.pi * 3 * f0_sub * t_sub))

    # Espectro (FFT simple, lo veremos en detalle mas adelante)
    X_sub = np.fft.rfft(x_sub)
    freqs_sub = np.fft.rfftfreq(len(x_sub), 1/fs_sub)
    magnitud_sub = np.abs(X_sub) / len(x_sub) * 2

    fig_sub, axes_sub = plt.subplots(2, 1, figsize=(12, 8))

    # Dominio temporal
    axes_sub[0].plot(t_sub * 1000, x_sub, 'b-', linewidth=1.0)
    axes_sub[0].set_title("Dominio temporal: 440 Hz + armonicos")
    axes_sub[0].set_xlabel("Tiempo (ms)")
    axes_sub[0].set_ylabel("Amplitud")
    axes_sub[0].grid(True, alpha=0.3)

    # Dominio frecuencial
    axes_sub[1].plot(freqs_sub, magnitud_sub, 'r-', linewidth=1.0)
    axes_sub[1].set_title("Dominio frecuencial (FFT)")
    axes_sub[1].set_xlabel("Frecuencia (Hz)")
    axes_sub[1].set_ylabel("Magnitud")
    axes_sub[1].set_xlim(0, 2000)
    axes_sub[1].grid(True, alpha=0.3)

    # Marcar los picos
    for k, amp in enumerate([1.0, 0.5, 0.25], 1):
        axes_sub[1].annotate(f'{k * f0_sub} Hz',
                            xy=(k * f0_sub, amp),
                            xytext=(k * f0_sub + 100, amp),
                            arrowprops=dict(arrowstyle='->', color='black'),
                            fontsize=10)

    plt.tight_layout()
    fig_sub
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Stem plots para senales discretas

    Para senales discretas cortas, `stem` es mas apropiado que `plot`, porque enfatiza la naturaleza **discreta** de la senal.
    """)
    return


@app.cell
def _(np, plt):
    # Comparar plot vs stem
    N_stem = 30
    n_stem = np.arange(N_stem)
    x_stem = np.sin(2 * np.pi * 3 * n_stem / N_stem)

    fig_stem, (ax_p, ax_s) = plt.subplots(1, 2, figsize=(12, 4))

    ax_p.plot(n_stem, x_stem, 'b-o', markersize=4)
    ax_p.set_title("plot() - sugiere continuidad")
    ax_p.set_xlabel("n")
    ax_p.set_ylabel("x[n]")
    ax_p.grid(True, alpha=0.3)

    ax_s.stem(n_stem, x_stem, linefmt='b-', markerfmt='bo', basefmt='k-')
    ax_s.set_title("stem() - enfatiza lo discreto")
    ax_s.set_xlabel("n")
    ax_s.set_ylabel("x[n]")
    ax_s.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_stem
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Introduccion a SciPy

    **SciPy** extiende NumPy con algoritmos cientificos. Para senales y sistemas, los modulos mas importantes son:

    | Modulo | Uso |
    |--------|-----|
    | `scipy.signal` | Filtros, convolucion, ventanas, espectrogramas |
    | `scipy.fft` | Transformada de Fourier (mas completa que `np.fft`) |
    | `scipy.io.wavfile` | Leer y escribir archivos WAV |
    | `scipy.linalg` | Algebra lineal avanzada |

    ### Leer y escribir archivos WAV

    ```python
    from scipy.io import wavfile

    # Leer un archivo WAV
    fs, data = wavfile.read("mi_audio.wav")
    # fs: frecuencia de muestreo (int)
    # data: array de NumPy con las muestras
    # - int16: valores entre -32768 y 32767
    # - float32: valores entre -1.0 y 1.0

    # Escribir un archivo WAV
    wavfile.write("salida.wav", fs, data)
    ```

    ### Ejemplo conceptual: cargar y analizar audio

    ```python
    from scipy.io import wavfile
    import numpy as np

    # Cargar audio
    fs, audio = wavfile.read("grabacion.wav")

    # Si es int16, normalizar a float
    if audio.dtype == np.int16:
        audio = audio.astype(np.float64) / 32768.0

    # Si es estereo, tomar un canal
    if audio.ndim == 2:
        audio = audio[:, 0]  # canal izquierdo

    # Informacion basica
    duracion = len(audio) / fs
    pico = np.max(np.abs(audio))
    rms = np.sqrt(np.mean(audio**2))
    rms_db = 20 * np.log10(rms) if rms > 0 else -np.inf
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### scipy.signal: una vista previa

    Vamos a usar `scipy.signal` extensivamente en clases futuras. Por ahora, un vistazo:
    """)
    return


@app.cell
def _(np, plt):
    from scipy import signal as sig

    # Generar un chirp: senal que barre frecuencias
    fs_chirp = 44100
    duracion_chirp = 1.0
    t_chirp = np.arange(int(fs_chirp * duracion_chirp)) / fs_chirp
    x_chirp = sig.chirp(t_chirp, f0=20, t1=duracion_chirp, f1=2000, method='linear')

    # Espectrograma
    fig_chirp, (ax_t, ax_s) = plt.subplots(2, 1, figsize=(12, 8))

    # Senal en el tiempo
    ax_t.plot(t_chirp, x_chirp, 'b-', linewidth=0.5)
    ax_t.set_title("Chirp: 20 Hz a 2000 Hz en 1 segundo")
    ax_t.set_xlabel("Tiempo (s)")
    ax_t.set_ylabel("Amplitud")
    ax_t.grid(True, alpha=0.3)

    # Espectrograma
    f_spec, t_spec, Sxx = sig.spectrogram(x_chirp, fs_chirp, nperseg=1024, noverlap=900)
    ax_s.pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='viridis')
    ax_s.set_title("Espectrograma del chirp")
    ax_s.set_xlabel("Tiempo (s)")
    ax_s.set_ylabel("Frecuencia (Hz)")
    ax_s.set_ylim(0, 2500)

    plt.tight_layout()
    fig_chirp
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Inteligencia Artificial para NumPy (P2)

    ### Nivel 2: Evaluar criticamente codigo generado por IA

    Ahora que conocemos NumPy, podemos empezar a usar IA como asistente de codigo. Pero **la IA comete errores**, especialmente en:

    - Formulas matematicas (signos, constantes)
    - Dimensiones de arrays
    - Eficiencia (a veces genera loops innecesarios)
    - Casos borde (division por cero, arrays vacios)

    ### Prompt engineering para codigo numerico

    **Ejemplo de prompt**:
    > "Genera una senal chirp que va de 20 Hz a 20 kHz en 5 segundos, muestreada a 44100 Hz, usando NumPy."

    ### Respuesta hipotetica de la IA:
    ```python
    import numpy as np

    fs = 44100
    duracion = 5.0
    t = np.linspace(0, duracion, int(fs * duracion))
    f0 = 20
    f1 = 20000

    # Frecuencia instantanea lineal
    frecuencia = f0 + (f1 - f0) * t / duracion
    fase = 2 * np.pi * np.cumsum(frecuencia) / fs
    chirp = np.sin(fase)
    ```

    ### Preguntas para evaluar este codigo:

    1. **Dimensiones correctas?** `np.linspace` sin `endpoint=False` va a generar una muestra de mas.

    2. **Formula matematica correcta?** La fase de un chirp lineal es:
       $$\phi(t) = 2\pi \left(f_0 t + \frac{f_1 - f_0}{2T} t^2\right)$$
       El metodo de `cumsum` es una aproximacion numerica. La formula analitica es mas precisa.

    3. **Eficiencia?** Esta bien, usa operaciones vectorizadas.

    4. **Casos borde?** Si `duracion = 0`, hay division por cero. Si `f0 > f1`, el chirp va hacia abajo (valido pero conviene documentar).

    ### Codigo corregido:
    ```python
    import numpy as np

    fs = 44100
    duracion = 5.0
    N = int(fs * duracion)
    t = np.arange(N) / fs  # mejor para audio
    f0 = 20
    f1 = 20000

    # Formula analitica de fase para chirp lineal
    fase = 2 * np.pi * (f0 * t + (f1 - f0) / (2 * duracion) * t**2)
    chirp = np.sin(fase)
    ```

    ### Tips para prompts efectivos:

    - **Especificar la frecuencia de muestreo** y la duracion
    - **Pedir que use operaciones vectorizadas** (no loops)
    - **Pedir que documente las formulas** usadas
    - **Pedir que maneje casos borde**
    - Siempre **verificar las formulas** contra fuentes confiables
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen de la clase

    Hoy aprendimos:

    - **NumPy**: arrays, propiedades, indexing, slicing, broadcasting, operaciones vectorizadas
    - **Senales discretas**: impulso, escalon, rampa, senoidal, exponencial compleja, exponencial decreciente
    - **Eje temporal**: `np.arange(N) / fs` y por que usar `endpoint=False`
    - **Matplotlib**: plot, stem, subplots, buenas practicas de visualizacion
    - **SciPy**: `scipy.io.wavfile`, `scipy.signal`, vista previa
    - **IA**: como evaluar criticamente codigo numerico generado por IA

    ### Para la proxima clase
    - Completar los ejercicios de `ejercicios.py`
    - Experimentar generando diferentes senales con los sliders
    - Intentar cargar un archivo WAV propio y analizarlo
    """)
    return


if __name__ == "__main__":
    app.run()
