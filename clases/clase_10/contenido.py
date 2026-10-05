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
    # Senales y Sistemas - Clase 10
    ## Procesamiento de la Respuesta al Impulso

    **Fecha**: 2 de junio de 2026 | **Pilares**: P1 (principal), P3 (principal)

    En esta clase vamos a:
    1. Extraer la envolvente de una senal con la transformada de Hilbert
    2. Suavizar senales con promedio movil
    3. Calcular la integral de Schroeder (Energy Decay Curve)
    4. Obtener EDT, T20, T30 con regresion lineal
    5. Armar un pipeline completo de analisis de RI
    6. Conocer el concepto de agentes de IA
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import signal
    return np, plt, signal


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Transformada de Hilbert y Envolvente

    La **transformada de Hilbert** nos permite obtener la **senal analitica**:

    $$x_a(t) = x(t) + j \hat{x}(t)$$

    donde $\hat{x}(t)$ es la transformada de Hilbert de $x(t)$.

    La **envolvente** es el modulo de la senal analitica:

    $$A(t) = |x_a(t)| = \sqrt{x(t)^2 + \hat{x}(t)^2}$$

    ### Aplicacion en acustica

    La respuesta al impulso (RI) de una sala es una senal que decae. La envolvente nos da la **curva de decaimiento** sin las oscilaciones rapidas.

    En SciPy:
    ```python
    from scipy.signal import hilbert
    analitica = hilbert(x)
    envolvente = np.abs(analitica)
    ```
    """)
    return


@app.cell
def _(np, plt, signal):
    # Ejemplo: envolvente de una sinusoide decayendo
    fs_1 = 44100
    dur_1 = 1.0
    N_1 = int(fs_1 * dur_1)
    t_1 = np.arange(N_1) / fs_1

    # Sinusoide con decaimiento exponencial (simula RI simplificada)
    tau_1 = 0.3  # constante de decaimiento
    x_1 = np.sin(2 * np.pi * 500 * t_1) * np.exp(-t_1 / tau_1)

    # Transformada de Hilbert
    analitica_1 = signal.hilbert(x_1)
    envolvente_1 = np.abs(analitica_1)

    fig_1, axes_1 = plt.subplots(2, 1, figsize=(12, 6))

    axes_1[0].plot(t_1 * 1000, x_1, 'b-', alpha=0.5, linewidth=0.5, label='Senal')
    axes_1[0].plot(t_1 * 1000, envolvente_1, 'r-', linewidth=2, label='Envolvente (Hilbert)')
    axes_1[0].plot(t_1 * 1000, -envolvente_1, 'r-', linewidth=2)
    axes_1[0].set_xlabel('Tiempo (ms)')
    axes_1[0].set_ylabel('Amplitud')
    axes_1[0].set_title('Senoidal con decaimiento exponencial')
    axes_1[0].legend()
    axes_1[0].grid(True, alpha=0.3)

    # Envolvente en dB
    env_db_1 = 20 * np.log10(envolvente_1 / np.max(envolvente_1) + 1e-12)
    axes_1[1].plot(t_1 * 1000, env_db_1, 'r-', linewidth=2)
    axes_1[1].set_xlabel('Tiempo (ms)')
    axes_1[1].set_ylabel('Nivel (dB)')
    axes_1[1].set_title('Envolvente en dB')
    axes_1[1].set_ylim(-60, 5)
    axes_1[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Promedio Movil (Moving Average)

    El **promedio movil** suaviza una senal calculando el promedio local en una ventana deslizante.

    $$y[n] = \frac{1}{M} \sum_{k=0}^{M-1} x[n-k]$$

    donde $M$ es el tamano de la ventana.

    ### Implementacion con convolución

    Se puede implementar eficientemente con `np.convolve`:

    ```python
    ventana = np.ones(M) / M
    suavizado = np.convolve(x, ventana, mode='same')
    ```

    ### Compromiso: suavidad vs detalle
    - Ventana **grande**: mas suave, pero pierde detalles y eventos rapidos
    - Ventana **chica**: preserva mas detalles, pero mas ruidoso
    """)
    return


@app.cell
def _(np, plt):
    # Demo: promedio movil con distintos tamanos de ventana
    fs_2 = 1000
    dur_2 = 1.0
    N_2 = int(fs_2 * dur_2)
    t_2 = np.arange(N_2) / fs_2

    # Senal: escalon + ruido
    senal_2 = np.zeros(N_2)
    senal_2[N_2//4:3*N_2//4] = 1.0
    senal_2 += 0.3 * np.random.randn(N_2)

    fig_2, ax_2 = plt.subplots(figsize=(12, 5))
    ax_2.plot(t_2, senal_2, 'b-', alpha=0.3, linewidth=0.5, label='Original (con ruido)')

    for M, color in [(5, 'green'), (20, 'orange'), (50, 'red'), (100, 'purple')]:
        ventana = np.ones(M) / M
        suavizado = np.convolve(senal_2, ventana, mode='same')
        ax_2.plot(t_2, suavizado, color=color, linewidth=2, label=f'M = {M}')

    ax_2.set_xlabel('Tiempo (s)')
    ax_2.set_ylabel('Amplitud')
    ax_2.set_title('Promedio movil con distintos tamanos de ventana')
    ax_2.legend()
    ax_2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Integral de Schroeder (Energy Decay Curve)

    La **integral de Schroeder** es la herramienta fundamental para calcular parametros acusticos a partir de la RI.

    ### Definicion

    La **Energy Decay Curve (EDC)** se calcula como la integral inversa de la energia:

    $$\text{EDC}(t) = \int_t^{\infty} h^2(\tau) \, d\tau$$

    En forma discreta:

    $$\text{EDC}[n] = \sum_{k=n}^{N-1} h^2[k]$$

    Esto es equivalente a la **suma acumulada inversa** de $h^2$:

    ```python
    EDC = np.cumsum(h**2)[::-1]  # o equivalente: np.flip(np.cumsum(np.flip(h**2)))
    ```

    ### EDC en dB

    Normalizamos y convertimos a dB:

    $$\text{EDC}_{dB}[n] = 10 \log_{10}\left(\frac{\text{EDC}[n]}{\text{EDC}[0]}\right)$$

    La EDC comienza en 0 dB y decae. Cuando llega a **-60 dB**, han pasado $T_{60}$ segundos.
    """)
    return


@app.cell
def _(np, plt):
    # Generar una RI sintetica con T60 conocido
    fs_3 = 44100
    T60_real = 2.0  # segundos
    dur_3 = 3.0  # mas larga que T60
    N_3 = int(fs_3 * dur_3)
    t_3 = np.arange(N_3) / fs_3

    # RI sintetica: ruido exponencialmente decayendo
    # T60 = tiempo para caer 60 dB -> tau = T60 / (6 * ln(10))
    tau_3 = T60_real / (6 * np.log(10))
    np.random.seed(42)
    h_3 = np.random.randn(N_3) * np.exp(-t_3 / tau_3)

    # Integral de Schroeder
    h2 = h_3 ** 2
    EDC = np.cumsum(h2[::-1])[::-1]
    EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)

    fig_3, axes_3 = plt.subplots(3, 1, figsize=(12, 10))

    # RI
    axes_3[0].plot(t_3, h_3, 'b-', linewidth=0.3)
    axes_3[0].set_xlabel('Tiempo (s)')
    axes_3[0].set_ylabel('Amplitud')
    axes_3[0].set_title(f'Respuesta al impulso sintetica (T60 = {T60_real} s)')
    axes_3[0].grid(True, alpha=0.3)

    # h^2
    axes_3[1].plot(t_3, 10 * np.log10(h2 / np.max(h2) + 1e-12), 'b-', linewidth=0.3)
    axes_3[1].set_xlabel('Tiempo (s)')
    axes_3[1].set_ylabel('Nivel (dB)')
    axes_3[1].set_title('Energia instantanea h^2(t) en dB')
    axes_3[1].set_ylim(-80, 5)
    axes_3[1].grid(True, alpha=0.3)

    # EDC
    axes_3[2].plot(t_3, EDC_dB, 'r-', linewidth=2)
    axes_3[2].axhline(-60, color='gray', linestyle='--', alpha=0.5, label='-60 dB')
    axes_3[2].set_xlabel('Tiempo (s)')
    axes_3[2].set_ylabel('EDC (dB)')
    axes_3[2].set_title('Integral de Schroeder (EDC)')
    axes_3[2].set_ylim(-80, 5)
    axes_3[2].legend()
    axes_3[2].grid(True, alpha=0.3)

    plt.tight_layout()

    # Estimar T60 desde la EDC
    idx_60 = np.where(EDC_dB <= -60)[0]
    if len(idx_60) > 0:
        T60_estimado = t_3[idx_60[0]]
        print(f"T60 real: {T60_real:.2f} s")
        print(f"T60 estimado (cruce -60 dB): {T60_estimado:.2f} s")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Regresion Lineal para Parametros Acusticos

    En vez de buscar el cruce exacto con -60 dB (que puede ser ruidoso), usamos **regresion lineal** sobre la EDC.

    ### Parametros acusticos

    | Parametro | Rango de ajuste | Factor | Formula |
    |-----------|----------------|--------|---------|
    | **EDT** (Early Decay Time) | 0 a -10 dB | $\times 6$ | $\text{EDT} = -60 / m$ |
    | **T20** | -5 a -25 dB | $\times 3$ | $T_{20} = -60 / m$ |
    | **T30** | -5 a -35 dB | $\times 2$ | $T_{30} = -60 / m$ |
    | **T60** (directo) | 0 a -60 dB | $\times 1$ | $T_{60} = -60 / m$ |

    Donde $m$ es la **pendiente** de la recta ajustada (en dB/s).

    ### Procedimiento

    1. Calcular la EDC en dB
    2. Seleccionar el rango de dB apropiado
    3. Ajustar una recta: $\text{EDC}_{dB}(t) = m \cdot t + b$
    4. Calcular: $T = -60 / m$

    Con `np.polyfit`:
    ```python
    m, b = np.polyfit(t_rango, EDC_dB_rango, 1)
    T60 = -60 / m
    ```
    """)
    return


@app.cell
def _(np, plt):
    # Regresion lineal para EDT, T20, T30
    fs_4 = 44100
    T60_conocido = 2.0
    dur_4 = 3.0
    N_4 = int(fs_4 * dur_4)
    t_4 = np.arange(N_4) / fs_4

    tau_4 = T60_conocido / (6 * np.log(10))
    np.random.seed(42)
    h_4 = np.random.randn(N_4) * np.exp(-t_4 / tau_4)

    # Schroeder
    EDC_4 = np.cumsum(h_4[::-1]**2)[::-1]
    EDC_4_dB = 10 * np.log10(EDC_4 / EDC_4[0] + 1e-12)

    def calcular_Tx(t, edc_db, db_inicio, db_fin, factor):
        """Calcula parametro acustico por regresion lineal."""
        mask = (edc_db >= db_fin) & (edc_db <= db_inicio)
        if np.sum(mask) < 2:
            return None, None, None
        t_rango = t[mask]
        edc_rango = edc_db[mask]
        m, b = np.polyfit(t_rango, edc_rango, 1)
        T = -60 / m
        recta = m * t + b
        return T, m, recta

    # Calcular parametros
    EDT, m_edt, recta_edt = calcular_Tx(t_4, EDC_4_dB, 0, -10, 6)
    T20, m_t20, recta_t20 = calcular_Tx(t_4, EDC_4_dB, -5, -25, 3)
    T30, m_t30, recta_t30 = calcular_Tx(t_4, EDC_4_dB, -5, -35, 2)

    fig_4, ax_4 = plt.subplots(figsize=(12, 6))
    ax_4.plot(t_4, EDC_4_dB, 'k-', linewidth=2, label='EDC')

    # Dibujar regresiones
    if EDT is not None:
        mask_edt = (recta_edt >= -70) & (recta_edt <= 5)
        ax_4.plot(t_4[mask_edt], recta_edt[mask_edt], 'b--', linewidth=2,
                  label=f'EDT = {EDT:.2f} s (0 a -10 dB)')
    if T20 is not None:
        mask_t20 = (recta_t20 >= -70) & (recta_t20 <= 5)
        ax_4.plot(t_4[mask_t20], recta_t20[mask_t20], 'g--', linewidth=2,
                  label=f'T20 = {T20:.2f} s (-5 a -25 dB)')
    if T30 is not None:
        mask_t30 = (recta_t30 >= -70) & (recta_t30 <= 5)
        ax_4.plot(t_4[mask_t30], recta_t30[mask_t30], 'r--', linewidth=2,
                  label=f'T30 = {T30:.2f} s (-5 a -35 dB)')

    ax_4.axhline(-10, color='blue', linestyle=':', alpha=0.3)
    ax_4.axhline(-25, color='green', linestyle=':', alpha=0.3)
    ax_4.axhline(-35, color='red', linestyle=':', alpha=0.3)
    ax_4.axhline(-60, color='gray', linestyle='--', alpha=0.5, label='-60 dB')

    ax_4.set_xlabel('Tiempo (s)')
    ax_4.set_ylabel('EDC (dB)')
    ax_4.set_title(f'Regresion lineal sobre EDC (T60 real = {T60_conocido} s)')
    ax_4.set_ylim(-70, 5)
    ax_4.legend(loc='upper right')
    ax_4.grid(True, alpha=0.3)
    plt.tight_layout()

    print(f"T60 real:    {T60_conocido:.2f} s")
    print(f"EDT:         {EDT:.2f} s")
    print(f"T20:         {T20:.2f} s")
    print(f"T30:         {T30:.2f} s")
    plt.gca()
    return (calcular_Tx,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Pipeline Completo: RI a Parametros Acusticos

    Veamos todo el proceso junto: desde una RI sintetica hasta los parametros acusticos.

    El pipeline es:

    1. **Cargar/generar RI**
    2. **Filtrar por bandas de octava** (clase 9)
    3. **Calcular Schroeder (EDC)** por banda
    4. **Regresion lineal** -> EDT, T20, T30 por banda
    5. **Validar** comparando con el valor conocido
    """)
    return


@app.cell
def _(np, plt, signal, calcular_Tx):
    def analizar_ri(h, fs, frecuencias_centrales=None):
        """
        Pipeline completo: RI -> parametros acusticos por banda.

        Parametros:
            h: respuesta al impulso
            fs: frecuencia de muestreo
            frecuencias_centrales: lista de fc (default: 125-8000 Hz)

        Retorna:
            dict con resultados por banda y broadband
        """
        if frecuencias_centrales is None:
            frecuencias_centrales = [125, 250, 500, 1000, 2000, 4000, 8000]

        t = np.arange(len(h)) / fs
        resultados = {}

        # Broadband
        EDC = np.cumsum(h[::-1]**2)[::-1]
        EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)
        EDT_bb, _, _ = calcular_Tx(t, EDC_dB, 0, -10, 6)
        T20_bb, _, _ = calcular_Tx(t, EDC_dB, -5, -25, 3)
        T30_bb, _, _ = calcular_Tx(t, EDC_dB, -5, -35, 2)
        resultados['broadband'] = {'EDT': EDT_bb, 'T20': T20_bb, 'T30': T30_bb}

        # Por banda de octava
        for fc in frecuencias_centrales:
            f_low = fc / np.sqrt(2)
            f_high = fc * np.sqrt(2)
            f_high = min(f_high, fs / 2 - 1)
            if f_high <= f_low:
                continue

            sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs, output='sos')
            h_banda = signal.sosfilt(sos, h)

            EDC_b = np.cumsum(h_banda[::-1]**2)[::-1]
            EDC_b_dB = 10 * np.log10(EDC_b / EDC_b[0] + 1e-12)

            EDT_b, _, _ = calcular_Tx(t, EDC_b_dB, 0, -10, 6)
            T20_b, _, _ = calcular_Tx(t, EDC_b_dB, -5, -25, 3)
            T30_b, _, _ = calcular_Tx(t, EDC_b_dB, -5, -35, 2)

            resultados[fc] = {'EDT': EDT_b, 'T20': T20_b, 'T30': T30_b}

        return resultados

    # Demo con RI sintetica
    fs_5 = 44100
    T60_demo = 1.5
    dur_5 = 2.5
    N_5 = int(fs_5 * dur_5)
    t_5 = np.arange(N_5) / fs_5
    tau_5 = T60_demo / (6 * np.log(10))
    np.random.seed(123)
    h_5 = np.random.randn(N_5) * np.exp(-t_5 / tau_5)

    resultados = analizar_ri(h_5, fs_5)

    # Mostrar resultados
    print(f"{'Banda':<12} {'EDT (s)':<10} {'T20 (s)':<10} {'T30 (s)':<10}")
    print("-" * 42)
    for banda, params in resultados.items():
        edt_str = f"{params['EDT']:.2f}" if params['EDT'] is not None else "N/A"
        t20_str = f"{params['T20']:.2f}" if params['T20'] is not None else "N/A"
        t30_str = f"{params['T30']:.2f}" if params['T30'] is not None else "N/A"
        print(f"{str(banda):<12} {edt_str:<10} {t20_str:<10} {t30_str:<10}")

    # Grafico de T30 por banda
    fcs = [k for k in resultados.keys() if k != 'broadband']
    t30_vals = [resultados[fc]['T30'] for fc in fcs if resultados[fc]['T30'] is not None]
    fcs_valid = [fc for fc in fcs if resultados[fc]['T30'] is not None]

    fig_5, ax_5 = plt.subplots(figsize=(10, 5))
    ax_5.bar([str(fc) for fc in fcs_valid], t30_vals, color='steelblue', edgecolor='navy')
    ax_5.axhline(T60_demo, color='red', linestyle='--', linewidth=2, label=f'T60 real = {T60_demo} s')
    ax_5.set_xlabel('Frecuencia central (Hz)')
    ax_5.set_ylabel('T30 (s)')
    ax_5.set_title('T30 por banda de octava')
    ax_5.legend()
    ax_5.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.gca()
    return (analizar_ri,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Introduccion a Agentes de IA

    ### Chatbot vs Agente

    | Caracteristica | Chatbot | Agente |
    |---------------|---------|--------|
    | Interaccion | Pregunta-respuesta | Autonomo con herramientas |
    | Herramientas | Ninguna | Ejecuta codigo, lee archivos, busca |
    | Memoria | Contexto de conversacion | Estado persistente |
    | Ejemplo | ChatGPT basico | Claude Code, Cursor |

    ### Que es un agente de IA?

    Un **agente** es un sistema de IA que puede:
    1. **Planificar**: descomponer una tarea en pasos
    2. **Usar herramientas**: ejecutar codigo, leer archivos, hacer busquedas
    3. **Iterar**: revisar resultados y ajustar su enfoque
    4. **Tomar decisiones**: elegir que hacer en cada paso

    ### Claude Code como agente

    **Claude Code** es un agente que puede:
    - Leer y modificar archivos de codigo
    - Ejecutar comandos en la terminal
    - Correr tests y analizar errores
    - Crear commits y pull requests

    Es como tener un "programador junior" que entiende tu codebase y puede hacer cambios.

    ### Implicaciones para el TP
    - Pueden usar agentes para **implementar** funciones a partir de especificaciones
    - Pero deben **entender** y **verificar** todo lo que genera
    - El agente no reemplaza el conocimiento del dominio (acustica, senales)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    | Concepto | Herramienta | Uso en el TP |
    |----------|------------|-------------|
    | Hilbert | `signal.hilbert` | Envolvente de la RI |
    | Moving average | `np.convolve` | Suavizar senales |
    | Schroeder (EDC) | `np.cumsum` inverso | Curva de decaimiento |
    | Regresion | `np.polyfit` | EDT, T20, T30 |
    | Pipeline | `analizar_ri()` | Analisis completo |

    ### Para la proxima clase
    Vamos a explorar el **vibecoding** en profundidad: como usar IA de forma efectiva y responsable para el desarrollo de codigo.
    """)
    return


if __name__ == "__main__":
    app.run()
