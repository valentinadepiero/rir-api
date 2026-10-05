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
    # Clase 7: Soluciones
    ## Sistemas y Clasificacion
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
    ### Ejercicio 1: Clasificacion de sistemas
    """)
    return


@app.cell
def _():
    # Ejercicio 1: Clasificacion
    print("=== Clasificacion de Sistemas ===\n")

    print("(a) y[n] = x[n-5] (retardo puro)")
    print("    Lineal:  SI  - T{ax1+bx2} = a*x1[n-5]+b*x2[n-5] = a*T{x1}+b*T{x2}")
    print("    TI:      SI  - desplazar entrada desplaza salida igual")
    print("    Causal:  SI  - solo usa x[n-5], que es pasado")
    print("    Estable: SI  - |y[n]| = |x[n-5]| <= M si |x[n]| <= M")
    print("    Memoria: SI  - depende de x[n-5], no solo de x[n]")
    print()

    print("(b) y[n] = x[n]^2 (cuadrador)")
    print("    Lineal:  NO  - T{ax} = (ax)^2 = a^2*x^2 != a*x^2 = a*T{x}")
    print("    TI:      SI  - (x[n-k])^2 = y[n-k]")
    print("    Causal:  SI  - solo usa x[n]")
    print("    Estable: SI  - si |x[n]|<=M, |y[n]|=|x[n]|^2 <= M^2")
    print("    Memoria: NO  - solo depende de x[n]")
    print()

    print("(c) y[n] = x[n] + 3 (offset)")
    print("    Lineal:  NO  - T{0} = 3 != 0 (falla homogeneidad)")
    print("    TI:      SI  - x[n-k]+3 = y[n-k]")
    print("    Causal:  SI  - solo usa x[n]")
    print("    Estable: SI  - si |x[n]|<=M, |y[n]|<=M+3")
    print("    Memoria: NO  - solo depende de x[n]")
    print()

    print("(d) y[n] = x[-n] (inversion temporal)")
    print("    Lineal:  SI  - T{ax1+bx2} = a*x1[-n]+b*x2[-n] = a*T{x1}+b*T{x2}")
    print("    TI:      NO  - T{x[n-k]} = x[-(n-k)] = x[-n+k] != y[n-k] = x[-(n-k)] = x[-n+k]")
    print("                   Ojo: en este caso T{x[n-k]}=x[k-n], pero y[n-k]=x[-(n-k)]=x[k-n]")
    print("                   En realidad SI parece TI, pero NO lo es porque T opera sobre la")
    print("                   senal completa: si x_d[n]=x[n-k], T{x_d}[n]=x_d[-n]=x[-n-k]")
    print("                   mientras que y[n-k]=x[-(n-k)]=x[-n+k]. Como -n-k != -n+k, NO es TI.")
    print("    Causal:  NO  - para n<0, y[n]=x[-n] usa valores futuros")
    print("    Estable: SI  - |y[n]|=|x[-n]|<=M")
    print("    Memoria: SI  - depende de x[-n], no solo de x[n]")

    print("\n--- Tabla resumen ---")
    print("Sistema          | Lineal | TI  | Causal | Estable | Memoria")
    print("(a) y[n]=x[n-5]  |   SI   | SI  |   SI   |   SI    |   SI")
    print("(b) y[n]=x[n]^2  |   NO   | SI  |   SI   |   SI    |   NO")
    print("(c) y[n]=x[n]+3  |   NO   | SI  |   SI   |   SI    |   NO")
    print("(d) y[n]=x[-n]   |   SI   | NO  |   NO   |   SI    |   SI")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Test numerico de linealidad
    """)
    return


@app.cell
def _(np):
    # Ejercicio 2: Test de linealidad
    def test_linealidad(sistema, x1, x2, a, b):
        """Testea linealidad usando superposicion."""
        # T{a*x1 + b*x2}
        salida_combinada = sistema(a * x1 + b * x2)
        # a*T{x1} + b*T{x2}
        salida_separada = a * sistema(x1) + b * sistema(x2)
        # Comparar
        error = np.max(np.abs(salida_combinada - salida_separada))
        es_lineal = error < 1e-10
        print(f"    Error maximo: {error:.2e} -> {'LINEAL' if es_lineal else 'NO LINEAL'}")
        return es_lineal

    # Pruebas
    x1_2 = np.random.randn(100)
    x2_2 = np.random.randn(100)
    a_2, b_2 = 2.5, -1.3

    print("Test de linealidad:")
    print("  y[n] = 3*x[n]:")
    test_linealidad(lambda x: 3 * x, x1_2, x2_2, a_2, b_2)

    print("  y[n] = x[n]^2:")
    test_linealidad(lambda x: x**2, x1_2, x2_2, a_2, b_2)

    print("  y[n] = clip(x[n], -0.5, 0.5):")
    test_linealidad(lambda x: np.clip(x, -0.5, 0.5), x1_2, x2_2, a_2, b_2)
    return (test_linealidad,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Test numerico de invarianza temporal
    """)
    return


@app.cell
def _(np):
    # Ejercicio 3: Test de invarianza temporal
    def test_invarianza_temporal(sistema, x, k):
        """Testea invarianza temporal desplazando entrada y salida."""
        N = len(x)

        # Calcular salida original
        y = sistema(x)

        # Desplazar entrada
        x_despl = np.zeros(N)
        if k >= 0:
            x_despl[k:] = x[:N-k]
        else:
            x_despl[:N+k] = x[-k:]

        # Calcular salida de entrada desplazada
        y_despl = sistema(x_despl)

        # Desplazar salida original
        y_orig_despl = np.zeros(N)
        if k >= 0:
            y_orig_despl[k:] = y[:N-k]
        else:
            y_orig_despl[:N+k] = y[-k:]

        # Comparar
        error = np.max(np.abs(y_despl - y_orig_despl))
        es_ti = error < 1e-10
        print(f"    Error maximo: {error:.2e} -> {'TI' if es_ti else 'TV (variante en el tiempo)'}")
        return es_ti

    # Filtro FIR: y[n] = x[n] + 0.5*x[n-1]
    def filtro_fir_3(x):
        y = np.zeros(len(x))
        y[0] = x[0]
        for i in range(1, len(x)):
            y[i] = x[i] + 0.5 * x[i-1]
        return y

    # Sistema TV: y[n] = n * x[n]
    def sistema_tv_3(x):
        n = np.arange(len(x))
        return n * x

    x_3 = np.random.randn(100)
    k_3 = 5

    print("Test de invarianza temporal:")
    print("  Filtro FIR y[n] = x[n] + 0.5*x[n-1]:")
    test_invarianza_temporal(filtro_fir_3, x_3, k_3)

    print("  Sistema TV y[n] = n * x[n]:")
    test_invarianza_temporal(sistema_tv_3, x_3, k_3)
    return (test_invarianza_temporal,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Media movil de 2 muestras
    """)
    return


@app.cell
def _(np, plt, test_invarianza_temporal, test_linealidad):
    # Ejercicio 4: Media movil de 2 muestras
    def media_movil_2(x):
        """y[n] = 0.5*x[n] + 0.5*x[n-1]"""
        y = np.zeros(len(x))
        y[0] = 0.5 * x[0]
        for i in range(1, len(x)):
            y[i] = 0.5 * x[i] + 0.5 * x[i-1]
        return y

    # Test linealidad
    x1_4 = np.random.randn(100)
    x2_4 = np.random.randn(100)
    print("Media movil de 2 muestras: y[n] = 0.5*x[n] + 0.5*x[n-1]")
    print("  Linealidad:")
    test_linealidad(media_movil_2, x1_4, x2_4, 2.0, -0.5)
    print("  Invarianza temporal:")
    test_invarianza_temporal(media_movil_2, x1_4, 5)

    # Respuesta al impulso
    N_4 = 20
    delta_4 = np.zeros(N_4)
    delta_4[0] = 1.0
    h_4 = media_movil_2(delta_4)

    fig_4, axes_4 = plt.subplots(2, 1, figsize=(10, 4))
    axes_4[0].stem(np.arange(N_4), delta_4, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_4[0].set_title(r'Entrada: $\delta[n]$')
    axes_4[0].grid(True, alpha=0.3)

    axes_4[1].stem(np.arange(N_4), h_4, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_4[1].set_title('Respuesta al impulso: h[0]=0.5, h[1]=0.5')
    axes_4[1].set_xlabel('n')
    axes_4[1].grid(True, alpha=0.3)

    plt.tight_layout()
    print(f"\n  Respuesta al impulso: h = {h_4[:5]}")
    print("  Es un filtro FIR de 2 coeficientes: [0.5, 0.5]")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Sistema de eco
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 5: Sistema de eco
    def eco(x, D):
        """y[n] = x[n] + 0.6 * x[n-D]"""
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = x[i]
            if i >= D:
                y[i] += 0.6 * x[i - D]
        return y

    fs_5 = 44100
    D_5 = int(0.3 * fs_5)  # 0.3 s de retardo = 13230 muestras
    print(f"Retardo D = {D_5} muestras ({D_5/fs_5:.3f} s)")

    # Clasificacion
    print("\nPropiedades del sistema de eco y[n] = x[n] + 0.6*x[n-D]:")
    print("  Lineal:  SI  - es suma de versiones escaladas de x")
    print("  TI:      SI  - los coeficientes no dependen de n")
    print("  Causal:  SI  - solo usa x[n] y x[n-D] (pasado)")
    print("  Estable: SI  - |y[n]| <= |x[n]| + 0.6|x[n-D]| <= 1.6*M")
    print("  Memoria: SI  - depende de x[n-D]")

    # Aplicar a un click
    duracion_5 = 1.0
    N_5 = int(fs_5 * duracion_5)
    click_5 = np.zeros(N_5)
    click_5[100] = 1.0

    y_eco = eco(click_5, D_5)

    # Respuesta al impulso
    delta_5 = np.zeros(N_5)
    delta_5[0] = 1.0
    h_5 = eco(delta_5, D_5)

    fig_5, axes_5 = plt.subplots(3, 1, figsize=(10, 7))

    t_5 = np.arange(N_5) / fs_5 * 1000

    axes_5[0].plot(t_5, click_5)
    axes_5[0].set_title('Entrada: click')
    axes_5[0].set_ylabel('Amplitud')
    axes_5[0].grid(True, alpha=0.3)

    axes_5[1].plot(t_5, y_eco)
    axes_5[1].set_title('Salida: click con eco (D = 0.3 s)')
    axes_5[1].set_ylabel('Amplitud')
    axes_5[1].grid(True, alpha=0.3)

    axes_5[2].plot(t_5, h_5)
    axes_5[2].set_title('Respuesta al impulso: h[0]=1, h[D]=0.6')
    axes_5[2].set_xlabel('Tiempo (ms)')
    axes_5[2].set_ylabel('Amplitud')
    axes_5[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Hard clipper
    """)
    return


@app.cell
def _(np, plt, test_linealidad):
    # Ejercicio 6: Hard clipper
    def hard_clipper(x, T=0.5):
        """Clipea la senal en [-T, T]."""
        return np.clip(x, -T, T)

    # Test de linealidad
    x1_6 = np.random.randn(100) * 0.3
    x2_6 = np.random.randn(100) * 0.3
    print("Hard clipper (T=0.5):")
    print("  Linealidad:")
    test_linealidad(lambda x: hard_clipper(x, 0.5), x1_6, x2_6, 2.0, 1.5)

    # Curva de transferencia
    x_curva = np.linspace(-1.5, 1.5, 1000)
    y_curva = hard_clipper(x_curva, 0.5)

    # Aplicar a senoidal
    t_6 = np.linspace(0, 0.01, 441, endpoint=False)
    senal_6 = np.sin(2 * np.pi * 440 * t_6)
    senal_clipped = hard_clipper(senal_6, 0.5)

    fig_6, axes_6 = plt.subplots(1, 2, figsize=(12, 4))

    axes_6[0].plot(x_curva, x_curva, 'b--', alpha=0.3, label='Lineal (sin clip)')
    axes_6[0].plot(x_curva, y_curva, 'r-', linewidth=2, label='Hard clipper (T=0.5)')
    axes_6[0].set_xlabel('Entrada x')
    axes_6[0].set_ylabel('Salida y')
    axes_6[0].set_title('Curva de transferencia')
    axes_6[0].legend()
    axes_6[0].grid(True, alpha=0.3)
    axes_6[0].set_aspect('equal')

    axes_6[1].plot(t_6 * 1000, senal_6, 'b-', alpha=0.5, label='Original')
    axes_6[1].plot(t_6 * 1000, senal_clipped, 'r-', label='Clipped (T=0.5)')
    axes_6[1].set_xlabel('Tiempo (ms)')
    axes_6[1].set_ylabel('Amplitud')
    axes_6[1].set_title('Senoidal antes y despues del clipper')
    axes_6[1].legend()
    axes_6[1].grid(True, alpha=0.3)

    plt.tight_layout()
    print("\nEl clipper NO es lineal: la curva de transferencia no es una recta.")
    print("En la zona |x| < T se comporta linealmente, pero fuera de esa zona no.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Respuesta al impulso de la derivada discreta
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 7: Derivada discreta
    def derivada_discreta(x):
        """y[n] = x[n] - x[n-1]"""
        y = np.zeros(len(x))
        y[0] = x[0]
        for i in range(1, len(x)):
            y[i] = x[i] - x[i-1]
        return y

    N_7 = 20
    delta_7 = np.zeros(N_7)
    delta_7[0] = 1.0
    h_7 = derivada_discreta(delta_7)

    fig_7, axes_7 = plt.subplots(2, 1, figsize=(10, 4))

    axes_7[0].stem(np.arange(N_7), delta_7, linefmt='b-', markerfmt='bo', basefmt='b-')
    axes_7[0].set_title(r'Entrada: $\delta[n]$')
    axes_7[0].set_ylabel('Amplitud')
    axes_7[0].grid(True, alpha=0.3)

    axes_7[1].stem(np.arange(N_7), h_7, linefmt='r-', markerfmt='ro', basefmt='r-')
    axes_7[1].set_title('Respuesta al impulso h[n] de la derivada discreta')
    axes_7[1].set_xlabel('n')
    axes_7[1].set_ylabel('Amplitud')
    axes_7[1].grid(True, alpha=0.3)

    plt.tight_layout()
    print(f"h = {h_7[:5]}")
    print("h[0] = 1, h[1] = -1, h[n] = 0 para n >= 2")
    print("Tiene 2 muestras no nulas.")
    print("Es un sistema FIR (Finite Impulse Response) de orden 1.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: T60 y decaimiento exponencial
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 8: T60 y decaimiento exponencial

    # h[n] = exp(-alpha * n / fs)
    # En T60: 20*log10(exp(-alpha*T60)) = -60
    # => -alpha*T60 * 20*log10(e) = -60
    # => alpha*T60 * 8.686 = 60
    # => alpha = 60 / (8.686 * T60) = 6.908 / T60

    T60_8 = 1.5  # segundos
    alpha_8 = 6.908 / T60_8
    fs_8 = 44100

    print(f"T60 = {T60_8} s")
    print(f"alpha = 6.908 / T60 = 6.908 / {T60_8} = {alpha_8:.4f}")

    # Generar h[n]
    duracion_8 = 2.0  # un poco mas que T60 para ver el decaimiento completo
    N_8 = int(fs_8 * duracion_8)
    n_8 = np.arange(N_8)
    t_8 = n_8 / fs_8

    h_8 = np.exp(-alpha_8 * n_8 / fs_8)

    # Verificar: nivel a t = T60
    idx_T60 = int(T60_8 * fs_8)
    nivel_T60_db = 20 * np.log10(h_8[idx_T60])
    print(f"\nNivel a t = T60 ({T60_8} s): {nivel_T60_db:.1f} dB (deberia ser -60 dB)")

    # IR realista: envolvente * ruido
    np.random.seed(42)
    h_realista = h_8 * np.random.randn(N_8) * 0.5
    h_realista[0] = 1.0  # Pico directo

    fig_8, axes_8 = plt.subplots(3, 1, figsize=(10, 8))

    # Envolvente exponencial
    axes_8[0].plot(t_8, h_8, 'b-')
    axes_8[0].set_title(f'Envolvente exponencial: h[n] = exp(-{alpha_8:.2f} * n / fs)')
    axes_8[0].set_ylabel('Amplitud')
    axes_8[0].axvline(x=T60_8, color='r', linestyle='--', label=f'T60 = {T60_8} s')
    axes_8[0].legend()
    axes_8[0].grid(True, alpha=0.3)

    # En dB
    h_8_db = 20 * np.log10(np.maximum(h_8, 1e-10))
    axes_8[1].plot(t_8, h_8_db, 'b-')
    axes_8[1].axhline(y=-60, color='r', linestyle='--', label='-60 dB')
    axes_8[1].axvline(x=T60_8, color='r', linestyle=':', alpha=0.5, label=f'T60 = {T60_8} s')
    axes_8[1].set_title('Envolvente en dB (decaimiento lineal en escala log)')
    axes_8[1].set_ylabel('Nivel (dB)')
    axes_8[1].set_ylim(-80, 5)
    axes_8[1].legend()
    axes_8[1].grid(True, alpha=0.3)

    # IR realista
    axes_8[2].plot(t_8, h_realista, 'b-', linewidth=0.3)
    axes_8[2].set_title('IR realista: envolvente * ruido blanco')
    axes_8[2].set_xlabel('Tiempo (s)')
    axes_8[2].set_ylabel('Amplitud')
    axes_8[2].axvline(x=T60_8, color='r', linestyle='--', alpha=0.5, label=f'T60 = {T60_8} s')
    axes_8[2].legend()
    axes_8[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
