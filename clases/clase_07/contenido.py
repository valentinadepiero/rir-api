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
    # Senales y Sistemas - Clase 7
    ## Sistemas y Clasificacion

    **Fecha**: 12 de mayo de 2026 | **Pilares**: P1 (principal), P2 (secundario)

    En esta clase vamos a:
    1. Entender que es un sistema
    2. Clasificar sistemas por sus propiedades
    3. Comprender los sistemas LTI y la respuesta al impulso
    4. Conectar con el TP: la sala como sistema LTI
    5. Usar IA para escribir funciones a partir de especificaciones
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
    ## 1. Que es un Sistema?

    Un **sistema** es cualquier proceso que transforma una senal de entrada en una senal de salida:

    $$x[n] \xrightarrow{T\{\cdot\}} y[n]$$

    Donde:
    - $x[n]$: senal de entrada (excitacion)
    - $T\{\cdot\}$: el sistema (transformacion)
    - $y[n]$: senal de salida (respuesta)

    ### Ejemplos en audio

    | Sistema | Entrada | Salida |
    |---------|---------|--------|
    | Amplificador | Senal de guitarra | Senal amplificada |
    | Reverb (sala) | Sonido seco | Sonido con reverberacion |
    | Ecualizador | Audio plano | Audio con frecuencias modificadas |
    | Compresor | Audio con mucho rango dinamico | Audio con rango reducido |
    | Delay | Senal original | Senal con eco |

    En Python, un sistema es simplemente una **funcion** que recibe un array y devuelve otro:

    ```python
    def sistema(x):
        y = ...  # alguna transformacion
        return y
    ```
    """)
    return


@app.cell
def _(np, plt):
    # Ejemplo visual: entrada -> sistema -> salida
    n = np.arange(50)
    x = np.sin(2 * np.pi * 0.05 * n)  # Entrada: senoidal

    # Sistema 1: Amplificador (y = 2x)
    y_amp = 2 * x

    # Sistema 2: Retardo (y[n] = x[n-5])
    y_delay = np.zeros_like(x)
    y_delay[5:] = x[:-5]

    fig, axes = plt.subplots(3, 1, figsize=(10, 6))

    axes[0].stem(n, x, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes[0].set_title('Entrada: x[n] = sin(2pi * 0.05 * n)')
    axes[0].set_ylabel('Amplitud')
    axes[0].grid(True, alpha=0.3)

    axes[1].stem(n, y_amp, linefmt='g-', markerfmt='go', basefmt='g-')
    axes[1].set_title('Salida del amplificador: y[n] = 2 * x[n]')
    axes[1].set_ylabel('Amplitud')
    axes[1].grid(True, alpha=0.3)

    axes[2].stem(n, y_delay, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes[2].set_title('Salida del delay: y[n] = x[n-5]')
    axes[2].set_xlabel('n')
    axes[2].set_ylabel('Amplitud')
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Propiedades de los Sistemas

    Para clasificar un sistema, evaluamos 5 propiedades fundamentales.

    ### 2.1 Linealidad

    Un sistema es **lineal** si cumple el principio de **superposicion**:

    $$T\{a \cdot x_1[n] + b \cdot x_2[n]\} = a \cdot T\{x_1[n]\} + b \cdot T\{x_2[n]\}$$

    Esto combina dos propiedades:
    - **Homogeneidad**: $T\{a \cdot x[n]\} = a \cdot T\{x[n]\}$ (escalar la entrada escala la salida)
    - **Aditividad**: $T\{x_1[n] + x_2[n]\} = T\{x_1[n]\} + T\{x_2[n]\}$ (la suma de entradas da la suma de salidas)
    """)
    return


@app.cell
def _(np, plt):
    # Demostracion de linealidad

    # Sistema LINEAL: amplificador y[n] = 2*x[n]
    def amplificador(x):
        return 2 * x

    # Sistema NO LINEAL: cuadrador y[n] = x[n]^2
    def cuadrador(x):
        return x**2

    # Senales de prueba
    n_lin = np.arange(20)
    x1 = np.sin(2 * np.pi * 0.1 * n_lin)
    x2 = np.cos(2 * np.pi * 0.15 * n_lin)
    a, b = 0.7, 1.3

    # Test de linealidad para amplificador
    entrada_combinada = a * x1 + b * x2
    salida_combinada_amp = amplificador(entrada_combinada)
    salida_separada_amp = a * amplificador(x1) + b * amplificador(x2)
    error_amp = np.max(np.abs(salida_combinada_amp - salida_separada_amp))

    # Test de linealidad para cuadrador
    salida_combinada_cuad = cuadrador(entrada_combinada)
    salida_separada_cuad = a * cuadrador(x1) + b * cuadrador(x2)
    error_cuad = np.max(np.abs(salida_combinada_cuad - salida_separada_cuad))

    print("=== Test de Linealidad ===")
    print(f"Amplificador y[n] = 2*x[n]: error = {error_amp:.10f} -> {'LINEAL' if error_amp < 1e-10 else 'NO LINEAL'}")
    print(f"Cuadrador y[n] = x[n]^2:    error = {error_cuad:.10f} -> {'LINEAL' if error_cuad < 1e-10 else 'NO LINEAL'}")

    fig_lin, axes_lin = plt.subplots(2, 2, figsize=(12, 6))

    axes_lin[0, 0].stem(n_lin, salida_combinada_amp, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_lin[0, 0].set_title('Amplificador: T{ax1 + bx2}')
    axes_lin[0, 0].grid(True, alpha=0.3)

    axes_lin[0, 1].stem(n_lin, salida_separada_amp, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_lin[0, 1].set_title('Amplificador: aT{x1} + bT{x2}')
    axes_lin[0, 1].grid(True, alpha=0.3)

    axes_lin[1, 0].stem(n_lin, salida_combinada_cuad, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_lin[1, 0].set_title('Cuadrador: T{ax1 + bx2}')
    axes_lin[1, 0].grid(True, alpha=0.3)

    axes_lin[1, 1].stem(n_lin, salida_separada_cuad, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_lin[1, 1].set_title('Cuadrador: aT{x1} + bT{x2} (DIFERENTE!)')
    axes_lin[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.2 Invarianza Temporal (Time-Invariance)

    Un sistema es **invariante en el tiempo** (TI) si un desplazamiento en la entrada produce el mismo desplazamiento en la salida:

    $$\text{Si } x[n] \rightarrow y[n], \text{ entonces } x[n-k] \rightarrow y[n-k]$$

    Es decir, el sistema se comporta igual sin importar **cuando** le apliquemos la entrada.
    """)
    return


@app.cell
def _(np, plt):
    # Demostracion de invarianza temporal

    N_ti = 50

    # Sistema TI: y[n] = x[n] + x[n-1] (filtro FIR simple)
    def filtro_fir(x):
        y = np.zeros_like(x)
        y[0] = x[0]
        for i in range(1, len(x)):
            y[i] = x[i] + x[i-1]
        return y

    # Sistema TV (variante en el tiempo): y[n] = n * x[n]
    def sistema_tv(x):
        n = np.arange(len(x))
        return n * x

    # Entrada original y desplazada
    n_ti = np.arange(N_ti)
    x_orig = np.zeros(N_ti)
    x_orig[5:15] = np.sin(2 * np.pi * 0.1 * np.arange(10))

    k_delay = 10
    x_despl = np.zeros(N_ti)
    x_despl[5+k_delay:15+k_delay] = np.sin(2 * np.pi * 0.1 * np.arange(10))

    # Test TI para filtro FIR
    y_orig_fir = filtro_fir(x_orig)
    y_despl_fir = filtro_fir(x_despl)
    y_orig_fir_despl = np.zeros(N_ti)
    y_orig_fir_despl[k_delay:] = y_orig_fir[:-k_delay]

    # Test TI para sistema TV
    y_orig_tv = sistema_tv(x_orig)
    y_despl_tv = sistema_tv(x_despl)
    y_orig_tv_despl = np.zeros(N_ti)
    y_orig_tv_despl[k_delay:] = y_orig_tv[:-k_delay]

    print("=== Test de Invarianza Temporal ===")
    error_ti_fir = np.max(np.abs(y_despl_fir - y_orig_fir_despl))
    error_ti_tv = np.max(np.abs(y_despl_tv - y_orig_tv_despl))
    print(f"Filtro FIR y[n]=x[n]+x[n-1]: error = {error_ti_fir:.10f} -> {'TI' if error_ti_fir < 1e-10 else 'TV'}")
    print(f"Sistema y[n]=n*x[n]:         error = {error_ti_tv:.10f} -> {'TI' if error_ti_tv < 1e-10 else 'TV'}")

    fig_ti, axes_ti = plt.subplots(2, 2, figsize=(12, 6))

    axes_ti[0, 0].stem(n_ti, y_despl_fir, linefmt='b-', markerfmt='bo', basefmt='b-', label='T{x[n-k]}')
    axes_ti[0, 0].stem(n_ti, y_orig_fir_despl, linefmt='g--', markerfmt='gx', basefmt='g-', label='y[n-k]')
    axes_ti[0, 0].set_title('FIR: comparacion (iguales -> TI)')
    axes_ti[0, 0].legend()
    axes_ti[0, 0].grid(True, alpha=0.3)

    axes_ti[0, 1].stem(n_ti, y_despl_fir - y_orig_fir_despl, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_ti[0, 1].set_title(f'FIR: diferencia (max = {error_ti_fir:.2e})')
    axes_ti[0, 1].grid(True, alpha=0.3)

    axes_ti[1, 0].stem(n_ti, y_despl_tv, linefmt='b-', markerfmt='bo', basefmt='b-', label='T{x[n-k]}')
    axes_ti[1, 0].stem(n_ti, y_orig_tv_despl, linefmt='r--', markerfmt='rx', basefmt='r-', label='y[n-k]')
    axes_ti[1, 0].set_title('TV: comparacion (diferentes -> NO TI)')
    axes_ti[1, 0].legend()
    axes_ti[1, 0].grid(True, alpha=0.3)

    axes_ti[1, 1].stem(n_ti, y_despl_tv - y_orig_tv_despl, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_ti[1, 1].set_title(f'TV: diferencia (max = {error_ti_tv:.2e})')
    axes_ti[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.3 Causalidad

    Un sistema es **causal** si la salida en el instante $n$ depende solo de las entradas **actuales y pasadas**:

    $$y[n] = f(x[n], x[n-1], x[n-2], \ldots)$$

    Un sistema **no causal** necesita valores futuros de la entrada:

    $$y[n] = f(\ldots, x[n+1], x[n], x[n-1], \ldots)$$

    **Importante**:
    - Los sistemas en **tiempo real** deben ser causales (no podemos ver el futuro)
    - En **procesamiento offline** (post-produccion), podemos usar sistemas no causales porque tenemos toda la senal
    """)
    return


@app.cell
def _(np, plt):
    # Demostracion de causalidad

    N_c = 30
    n_c = np.arange(N_c)
    x_c = np.zeros(N_c)
    x_c[10:20] = 1.0  # Pulso rectangular

    # Sistema CAUSAL: y[n] = x[n] + x[n-1] (solo usa pasado)
    def sistema_causal(x):
        y = np.zeros_like(x)
        y[0] = x[0]
        for i in range(1, len(x)):
            y[i] = x[i] + x[i-1]
        return y

    # Sistema NO CAUSAL: y[n] = x[n] + x[n+1] (usa futuro)
    def sistema_no_causal(x):
        y = np.zeros_like(x)
        for i in range(len(x)-1):
            y[i] = x[i] + x[i+1]
        y[-1] = x[-1]
        return y

    y_causal = sistema_causal(x_c)
    y_no_causal = sistema_no_causal(x_c)

    fig_c, axes_c = plt.subplots(3, 1, figsize=(10, 6))

    axes_c[0].stem(n_c, x_c, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_c[0].set_title('Entrada: pulso rectangular')
    axes_c[0].set_ylabel('x[n]')
    axes_c[0].grid(True, alpha=0.3)

    axes_c[1].stem(n_c, y_causal, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_c[1].set_title('CAUSAL: y[n] = x[n] + x[n-1] (responde al mismo tiempo o despues)')
    axes_c[1].set_ylabel('y[n]')
    axes_c[1].grid(True, alpha=0.3)
    axes_c[1].axvline(x=10, color='gray', linestyle='--', alpha=0.5, label='Inicio del pulso')
    axes_c[1].legend()

    axes_c[2].stem(n_c, y_no_causal, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_c[2].set_title('NO CAUSAL: y[n] = x[n] + x[n+1] (responde ANTES de la entrada!)')
    axes_c[2].set_xlabel('n')
    axes_c[2].set_ylabel('y[n]')
    axes_c[2].grid(True, alpha=0.3)
    axes_c[2].axvline(x=10, color='gray', linestyle='--', alpha=0.5, label='Inicio del pulso')
    axes_c[2].legend()

    plt.tight_layout()
    print("Nota: el sistema no causal responde en n=9, ANTES de que el pulso empiece en n=10")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.4 Estabilidad (BIBO)

    Un sistema es **BIBO estable** (*Bounded Input, Bounded Output*) si toda entrada acotada produce una salida acotada:

    $$|x[n]| \leq M_x < \infty \quad \Rightarrow \quad |y[n]| \leq M_y < \infty$$

    Un sistema inestable puede producir salidas que crecen sin limite, lo cual en audio significa **distorsion masiva o dano a equipos**.
    """)
    return


@app.cell
def _(np, plt):
    # Demostracion de estabilidad

    N_s = 50
    n_s = np.arange(N_s)
    x_s = np.ones(N_s) * 0.5  # Entrada acotada (constante 0.5)

    # Sistema ESTABLE: y[n] = 0.5 * x[n]
    y_estable = 0.5 * x_s

    # Sistema INESTABLE: y[n] = 2^n * x[n] (crece exponencialmente)
    y_inestable = (1.05 ** n_s) * x_s  # Usamos 1.05 en vez de 2 para que se vea

    # Sistema acumulador (marginalmente estable): y[n] = sum(x[0..n])
    y_acumulador = np.cumsum(x_s)

    fig_s, axes_s = plt.subplots(2, 2, figsize=(12, 6))

    axes_s[0, 0].stem(n_s, x_s, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_s[0, 0].set_title('Entrada acotada: x[n] = 0.5')
    axes_s[0, 0].set_ylim(-0.1, 1.5)
    axes_s[0, 0].grid(True, alpha=0.3)

    axes_s[0, 1].stem(n_s, y_estable, linefmt='g-', markerfmt='go', basefmt='g-')
    axes_s[0, 1].set_title('ESTABLE: y[n] = 0.5 * x[n]')
    axes_s[0, 1].set_ylim(-0.1, 1.5)
    axes_s[0, 1].grid(True, alpha=0.3)

    axes_s[1, 0].stem(n_s, y_inestable, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_s[1, 0].set_title('INESTABLE: y[n] = 1.05^n * x[n] (crece sin limite)')
    axes_s[1, 0].grid(True, alpha=0.3)

    axes_s[1, 1].stem(n_s, y_acumulador, linefmt='orange', markerfmt='o', basefmt='orange')
    axes_s[1, 1].set_title('MARGINALMENTE ESTABLE: y[n] = sum(x[0..n])')
    axes_s[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    print("El acumulador no es BIBO estable: una entrada constante produce una salida que crece sin limite.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2.5 Memoria / Sin Memoria

    - **Sin memoria** (memoryless): la salida depende SOLO de la entrada en el instante actual
      $$y[n] = f(x[n])$$
    - **Con memoria**: la salida depende de entradas pasadas (o futuras)
      $$y[n] = f(x[n], x[n-1], x[n-2], \ldots)$$

    | Ejemplo | Con/Sin memoria |
    |---------|----------------|
    | $y[n] = 3 \cdot x[n]$ (ganancia) | Sin memoria |
    | $y[n] = x[n]^2$ (distorsion) | Sin memoria |
    | $y[n] = x[n] + x[n-1]$ (FIR) | Con memoria |
    | $y[n] = x[n] + 0.6 \cdot y[n-1]$ (IIR) | Con memoria |
    | $y[n] = \max(x[0], \ldots, x[n])$ (pico) | Con memoria |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Sistemas LTI (Lineales e Invariantes en el Tiempo)

    Un sistema **LTI** es un sistema que es **lineal** Y **invariante en el tiempo** al mismo tiempo.

    ### Por que los sistemas LTI son especiales?

    Porque un sistema LTI queda **completamente caracterizado** por su **respuesta al impulso** $h[n]$:

    $$h[n] = T\{\delta[n]\}$$

    donde $\delta[n]$ es el impulso unitario (delta de Kronecker):

    $$\delta[n] = \begin{cases} 1 & \text{si } n = 0 \\ 0 & \text{si } n \neq 0 \end{cases}$$

    **Si conoces $h[n]$, conoces TODO sobre el sistema.** La salida para cualquier entrada se obtiene por **convolucion**:

    $$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

    (La convolucion la veremos en detalle en la Clase 8)
    """)
    return


@app.cell
def _(np, plt):
    # Encontrar la respuesta al impulso de un sistema LTI

    # Sistema: y[n] = x[n] + 0.8*x[n-1] + 0.3*x[n-2]
    def sistema_fir(x):
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = x[i]
            if i >= 1:
                y[i] += 0.8 * x[i-1]
            if i >= 2:
                y[i] += 0.3 * x[i-2]
        return y

    # Generar impulso
    N_h = 20
    delta = np.zeros(N_h)
    delta[0] = 1.0

    # Respuesta al impulso
    h = sistema_fir(delta)

    fig_h, axes_h = plt.subplots(2, 1, figsize=(10, 5))

    axes_h[0].stem(np.arange(N_h), delta, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_h[0].set_title(r'Entrada: impulso $\delta[n]$')
    axes_h[0].set_ylabel('Amplitud')
    axes_h[0].grid(True, alpha=0.3)

    axes_h[1].stem(np.arange(N_h), h, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_h[1].set_title('Respuesta al impulso: h[n] = T{delta[n]}')
    axes_h[1].set_xlabel('n')
    axes_h[1].set_ylabel('Amplitud')
    axes_h[1].grid(True, alpha=0.3)

    plt.tight_layout()

    print("Sistema: y[n] = x[n] + 0.8*x[n-1] + 0.3*x[n-2]")
    print(f"Respuesta al impulso: h = {h[:5]}")
    print("h[0]=1.0, h[1]=0.8, h[2]=0.3, h[3:]=0")
    print("\nLos coeficientes del sistema SON la respuesta al impulso!")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Conexion con Acustica de Salas

    Una sala es (aproximadamente) un **sistema LTI**:

    - **Lineal**: si hablo mas fuerte, el sonido reflejado es proporcionalmente mas fuerte
    - **Invariante en el tiempo**: la acustica de la sala no cambia (a corto plazo)

    La **respuesta al impulso** de una sala es exactamente lo que mide la norma **ISO 3382**:

    1. Se emite un sonido impulsivo (aplauso, globo, barrido de senos)
    2. Se graba la respuesta de la sala
    3. Se procesa para obtener $h[n]$
    4. De $h[n]$ se calculan parametros acusticos: T60, EDT, C80, D50, etc.

    **Esto es exactamente lo que hacen en el TP!**

    La respuesta al impulso de una sala tipicamente:
    - Tiene un pico inicial (sonido directo)
    - Seguido de reflexiones tempranas
    - Y luego un decaimiento exponencial (reverberacion)
    """)
    return


@app.cell
def _(np, plt):
    # Simular una respuesta al impulso de sala
    fs = 44100
    duracion_ir = 1.5  # segundos
    n_ir = int(fs * duracion_ir)
    t_ir = np.arange(n_ir) / fs

    # Construir IR sintetica
    h_sala = np.zeros(n_ir)

    # Sonido directo (t = 0)
    h_sala[0] = 1.0

    # Reflexiones tempranas (primeros 80 ms)
    reflexiones = [(0.012, 0.7), (0.025, -0.5), (0.038, 0.4),
                   (0.045, -0.3), (0.055, 0.25), (0.067, -0.2)]
    for tiempo, amplitud in reflexiones:
        idx = int(tiempo * fs)
        if idx < n_ir:
            h_sala[idx] = amplitud

    # Cola reverberante (decaimiento exponencial con ruido)
    np.random.seed(42)
    ruido_reverb = np.random.randn(n_ir) * 0.15
    T60 = 1.2  # tiempo de reverberacion
    envolvente = np.exp(-6.91 * t_ir / T60)  # -60dB en T60
    h_sala += ruido_reverb * envolvente
    h_sala[0] = 1.0  # Restaurar pico directo

    fig_sala, axes_sala = plt.subplots(2, 1, figsize=(10, 6))

    # IR completa
    axes_sala[0].plot(t_ir * 1000, h_sala, 'b-', linewidth=0.5)
    axes_sala[0].set_title(f'Respuesta al impulso de sala simulada (T60 = {T60} s)')
    axes_sala[0].set_xlabel('Tiempo (ms)')
    axes_sala[0].set_ylabel('Amplitud')
    axes_sala[0].grid(True, alpha=0.3)

    # IR en dB (envolvente)
    h_abs = np.abs(h_sala)
    h_abs[h_abs < 1e-10] = 1e-10
    h_db = 20 * np.log10(h_abs / np.max(h_abs))

    axes_sala[1].plot(t_ir * 1000, h_db, 'b-', linewidth=0.3, alpha=0.5)
    # Envolvente suavizada
    from scipy.signal import savgol_filter
    ventana = min(1001, len(h_db) - 1)
    if ventana % 2 == 0:
        ventana -= 1
    h_db_suave = savgol_filter(np.maximum(h_db, -80), ventana, 3)
    axes_sala[1].plot(t_ir * 1000, h_db_suave, 'r-', linewidth=2, label='Envolvente')
    axes_sala[1].axhline(y=-60, color='green', linestyle='--', alpha=0.7, label='-60 dB (T60)')
    axes_sala[1].set_title('Respuesta al impulso en dB (decaimiento)')
    axes_sala[1].set_xlabel('Tiempo (ms)')
    axes_sala[1].set_ylabel('Nivel (dB)')
    axes_sala[1].set_ylim(-80, 5)
    axes_sala[1].legend()
    axes_sala[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Tabla Resumen: Sistemas de Audio

    | Sistema | Lineal | TI | Causal | Estable | Con memoria |
    |---------|--------|-----|--------|---------|-------------|
    | Amplificador ideal | Si | Si | Si | Si | No |
    | Reverb (sala) | ~Si | ~Si | Si | Si | Si |
    | Compresor | No | Si | Si | Si | Si |
    | Delay | Si | Si | Si | Si | Si |
    | Distorsion | No | Si | Si | Si | No |
    | Ecualizador lineal | Si | Si | Si | Si | Si |
    | Limitador | No | Si | Si | Si | No |
    | Auto-tune | No | No | No* | Si | Si |

    *Auto-tune usa look-ahead (analisis de pitch futuro), por eso no es causal en modo offline.

    **Nota**: El reverb y la sala son "aproximadamente" lineales y TI. Para niveles muy altos (distorsion del aire) o periodos largos (cambios de temperatura), estas propiedades no se cumplen exactamente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. IA para Escribir Funciones a Partir de Especificaciones (P2)

    Una de las mejores aplicaciones de la IA es **implementar funciones a partir de especificaciones detalladas**. Veamos un ejemplo:

    ### Ejemplo: Pedir a la IA que escriba un test de linealidad

    **Prompt:**
    > Escribi una funcion en Python llamada `test_linealidad(sistema, x1, x2, a, b)` que:
    > 1. Reciba un sistema como funcion (callable)
    > 2. Reciba dos senales x1 y x2 (arrays de numpy)
    > 3. Reciba dos escalares a y b
    > 4. Calcule T{a*x1 + b*x2} y compare con a*T{x1} + b*T{x2}
    > 5. Retorne True si el error maximo es menor a 1e-10, False en caso contrario
    > 6. Imprima el error maximo

    La IA probablemente genere algo como esto:
    """)
    return


@app.cell
def _(np):
    # Funcion generada (ejemplo de lo que la IA produciria)
    def test_linealidad(sistema, x1, x2, a, b):
        """Testea si un sistema es lineal usando el principio de superposicion."""
        # Lado izquierdo: T{a*x1 + b*x2}
        entrada_combinada = a * x1 + b * x2
        salida_combinada = sistema(entrada_combinada)

        # Lado derecho: a*T{x1} + b*T{x2}
        salida_separada = a * sistema(x1) + b * sistema(x2)

        # Comparar
        error = np.max(np.abs(salida_combinada - salida_separada))
        es_lineal = error < 1e-10

        print(f"  Error maximo: {error:.2e} -> {'LINEAL' if es_lineal else 'NO LINEAL'}")
        return es_lineal

    # Probar con diferentes sistemas
    x1_test = np.random.randn(100)
    x2_test = np.random.randn(100)
    a_test, b_test = 2.5, -1.3

    print("Test de linealidad:")
    print("  y[n] = 3*x[n] (ganancia):")
    test_linealidad(lambda x: 3*x, x1_test, x2_test, a_test, b_test)

    print("  y[n] = x[n]^2 (cuadrador):")
    test_linealidad(lambda x: x**2, x1_test, x2_test, a_test, b_test)

    print("  y[n] = x[n] + 1 (offset):")
    test_linealidad(lambda x: x + 1, x1_test, x2_test, a_test, b_test)

    print("  y[n] = abs(x[n]) (rectificador):")
    test_linealidad(lambda x: np.abs(x), x1_test, x2_test, a_test, b_test)
    return (test_linealidad,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Discusion critica: El test numerico prueba linealidad?

    **No.** El test numerico solo verifica la propiedad para **valores especificos** de $x_1$, $x_2$, $a$, $b$. Para demostrar matematicamente que un sistema es lineal, necesitamos una **prueba formal** que funcione para todos los valores posibles.

    Sin embargo, el test numerico es muy util para:
    - **Descartar** linealidad: si falla para un caso, el sistema NO es lineal
    - **Ganar confianza**: si pasa para muchos casos aleatorios, es probable (pero no seguro) que sea lineal
    - **Debugging**: verificar que tu implementacion de un sistema lineal es correcta

    **Moraleja**: La IA puede generar codigo correcto, pero debemos **entender las limitaciones** de lo que genera. Un test numerico no reemplaza una demostracion matematica.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy aprendimos:

    1. **Que es un sistema**: transformacion $x[n] \rightarrow y[n]$
    2. **Propiedades de sistemas**:
       - **Linealidad**: superposicion (escalado + aditividad)
       - **Invarianza temporal**: desplazar entrada desplaza salida
       - **Causalidad**: solo depende del pasado y presente
       - **Estabilidad BIBO**: entrada acotada produce salida acotada
       - **Memoria**: depende o no de valores pasados
    3. **Sistemas LTI**: los mas importantes, caracterizados por $h[n]$
    4. **Respuesta al impulso**: si la conocemos, sabemos todo del sistema
    5. **Conexion con el TP**: la sala es un sistema LTI, medimos $h[n]$

    ### Para la proxima clase
    - Completar los 8 ejercicios de `ejercicios.py`
    - Proxima clase: **Convolucion** (como usar $h[n]$ para calcular cualquier salida)
    """)
    return


if __name__ == "__main__":
    app.run()
