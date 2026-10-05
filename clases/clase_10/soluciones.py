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
    # Clase 10: Soluciones
    ## Procesamiento de la Respuesta al Impulso
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
    ### Ejercicio 1: Envolvente con Hilbert
    """)
    return


@app.cell
def _(np, plt, signal):
    # Ejercicio 1: Envolvente de sinusoide decayendo
    fs_1 = 44100
    dur_1 = 1.0
    N_1 = int(fs_1 * dur_1)
    t_1 = np.arange(N_1) / fs_1

    tau_1 = 0.2
    x_1 = np.sin(2 * np.pi * 1000 * t_1) * np.exp(-t_1 / tau_1)

    # Hilbert
    analitica_1 = signal.hilbert(x_1)
    envolvente_1 = np.abs(analitica_1)

    fig_1, axes_1 = plt.subplots(2, 1, figsize=(12, 6))

    axes_1[0].plot(t_1 * 1000, x_1, 'b-', alpha=0.5, linewidth=0.5, label='Senal')
    axes_1[0].plot(t_1 * 1000, envolvente_1, 'r-', linewidth=2, label='Envolvente')
    axes_1[0].plot(t_1 * 1000, -envolvente_1, 'r-', linewidth=2)
    axes_1[0].set_xlabel('Tiempo (ms)')
    axes_1[0].set_ylabel('Amplitud')
    axes_1[0].set_title(f'Ejercicio 1: Sinusoide 1 kHz con decaimiento (tau={tau_1} s)')
    axes_1[0].legend()
    axes_1[0].grid(True, alpha=0.3)

    env_db = 20 * np.log10(envolvente_1 / np.max(envolvente_1) + 1e-12)
    axes_1[1].plot(t_1 * 1000, env_db, 'r-', linewidth=2)
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
    ### Ejercicio 2: Promedio movil sobre ruido
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 2: Moving average con distintos M
    fs_2 = 1000
    dur_2 = 2.0
    N_2 = int(fs_2 * dur_2)
    t_2 = np.arange(N_2) / fs_2

    senal_limpia = np.sin(2 * np.pi * 5 * t_2)
    ruido_2 = 0.5 * np.random.randn(N_2)
    senal_ruidosa = senal_limpia + ruido_2

    fig_2, ax_2 = plt.subplots(figsize=(14, 5))
    ax_2.plot(t_2, senal_ruidosa, 'b-', alpha=0.2, linewidth=0.5, label='Con ruido')
    ax_2.plot(t_2, senal_limpia, 'k-', linewidth=2, label='Original (sin ruido)')

    for M, color in [(10, 'green'), (50, 'orange'), (100, 'red'), (200, 'purple')]:
        ventana = np.ones(M) / M
        suavizado = np.convolve(senal_ruidosa, ventana, mode='same')
        ax_2.plot(t_2, suavizado, color=color, linewidth=1.5, label=f'M = {M}')

    ax_2.set_xlabel('Tiempo (s)')
    ax_2.set_ylabel('Amplitud')
    ax_2.set_title('Ejercicio 2: Promedio movil con distintas ventanas')
    ax_2.legend(loc='upper right')
    ax_2.grid(True, alpha=0.3)
    plt.tight_layout()

    print("M=50 es un buen compromiso: suaviza el ruido sin distorsionar mucho la sinusoide.")
    print("M=200 ya distorsiona (ventana de 200ms es comparable al periodo de 5Hz = 200ms).")
    print("Regla: M deberia ser << periodo de la senal de interes.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Integral de Schroeder
    """)
    return


@app.cell
def _(np, plt):
    # Ejercicio 3: Schroeder de RI sintetica
    fs_3 = 44100
    T60_3 = 2.0
    dur_3 = 3.0
    N_3 = int(fs_3 * dur_3)
    t_3 = np.arange(N_3) / fs_3

    tau_3 = T60_3 / (6 * np.log(10))
    np.random.seed(42)
    h_3 = np.random.randn(N_3) * np.exp(-t_3 / tau_3)

    # Integral de Schroeder
    EDC_3 = np.cumsum(h_3[::-1]**2)[::-1]
    EDC_3_dB = 10 * np.log10(EDC_3 / EDC_3[0] + 1e-12)

    fig_3, axes_3 = plt.subplots(2, 1, figsize=(12, 8))

    axes_3[0].plot(t_3, h_3, 'b-', linewidth=0.3)
    axes_3[0].set_xlabel('Tiempo (s)')
    axes_3[0].set_ylabel('Amplitud')
    axes_3[0].set_title(f'Ejercicio 3: RI sintetica (T60 = {T60_3} s)')
    axes_3[0].grid(True, alpha=0.3)

    axes_3[1].plot(t_3, EDC_3_dB, 'r-', linewidth=2)
    axes_3[1].axhline(-60, color='gray', linestyle='--', linewidth=2, label='-60 dB')
    axes_3[1].set_xlabel('Tiempo (s)')
    axes_3[1].set_ylabel('EDC (dB)')
    axes_3[1].set_title('Integral de Schroeder (EDC)')
    axes_3[1].set_ylim(-80, 5)
    axes_3[1].legend()
    axes_3[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return (EDC_3_dB, N_3, T60_3, fs_3, h_3, t_3, tau_3)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: T30 y T60 con regresion lineal
    """)
    return


@app.cell
def _(np, plt, EDC_3_dB, T60_3, t_3):
    # Ejercicio 4: T30 con regresion lineal
    # Seleccionar rango -5 a -35 dB
    mask_4 = (EDC_3_dB >= -35) & (EDC_3_dB <= -5)
    t_rango_4 = t_3[mask_4]
    edc_rango_4 = EDC_3_dB[mask_4]

    # Regresion lineal
    m_4, b_4 = np.polyfit(t_rango_4, edc_rango_4, 1)
    T30_4 = -60 / m_4

    # Recta de regresion
    recta_4 = m_4 * t_3 + b_4

    fig_4, ax_4 = plt.subplots(figsize=(12, 6))
    ax_4.plot(t_3, EDC_3_dB, 'k-', linewidth=2, label='EDC')
    mask_recta = (recta_4 >= -70) & (recta_4 <= 5)
    ax_4.plot(t_3[mask_recta], recta_4[mask_recta], 'r--', linewidth=2,
              label=f'Regresion T30 = {T30_4:.2f} s')
    ax_4.axhline(-5, color='green', linestyle=':', alpha=0.5, label='-5 dB')
    ax_4.axhline(-35, color='green', linestyle=':', alpha=0.5, label='-35 dB')
    ax_4.axhline(-60, color='gray', linestyle='--', alpha=0.5, label='-60 dB')
    ax_4.set_xlabel('Tiempo (s)')
    ax_4.set_ylabel('EDC (dB)')
    ax_4.set_title(f'Ejercicio 4: T30 por regresion lineal')
    ax_4.set_ylim(-70, 5)
    ax_4.legend()
    ax_4.grid(True, alpha=0.3)
    plt.tight_layout()

    print(f"T60 real:    {T60_3:.2f} s")
    print(f"T30 medido:  {T30_4:.2f} s")
    print(f"Pendiente:   {m_4:.1f} dB/s")
    print(f"Error:       {abs(T30_4 - T60_3):.3f} s ({abs(T30_4 - T60_3)/T60_3*100:.1f}%)")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: EDT (Early Decay Time)
    """)
    return


@app.cell
def _(np, plt, EDC_3_dB, T60_3, t_3):
    # Ejercicio 5: EDT (0 a -10 dB)
    mask_5 = (EDC_3_dB >= -10) & (EDC_3_dB <= 0)
    t_rango_5 = t_3[mask_5]
    edc_rango_5 = EDC_3_dB[mask_5]

    m_5, b_5 = np.polyfit(t_rango_5, edc_rango_5, 1)
    EDT_5 = -60 / m_5

    # Tambien T30 para comparar
    mask_t30 = (EDC_3_dB >= -35) & (EDC_3_dB <= -5)
    m_t30, b_t30 = np.polyfit(t_3[mask_t30], EDC_3_dB[mask_t30], 1)
    T30_5 = -60 / m_t30

    recta_edt = m_5 * t_3 + b_5
    recta_t30 = m_t30 * t_3 + b_t30

    fig_5, ax_5 = plt.subplots(figsize=(12, 6))
    ax_5.plot(t_3, EDC_3_dB, 'k-', linewidth=2, label='EDC')

    mask_r_edt = (recta_edt >= -70) & (recta_edt <= 5)
    ax_5.plot(t_3[mask_r_edt], recta_edt[mask_r_edt], 'b--', linewidth=2,
              label=f'EDT = {EDT_5:.2f} s')
    mask_r_t30 = (recta_t30 >= -70) & (recta_t30 <= 5)
    ax_5.plot(t_3[mask_r_t30], recta_t30[mask_r_t30], 'r--', linewidth=2,
              label=f'T30 = {T30_5:.2f} s')

    ax_5.set_xlabel('Tiempo (s)')
    ax_5.set_ylabel('EDC (dB)')
    ax_5.set_title('Ejercicio 5: EDT vs T30')
    ax_5.set_ylim(-70, 5)
    ax_5.legend()
    ax_5.grid(True, alpha=0.3)
    plt.tight_layout()

    print(f"T60 real:  {T60_3:.2f} s")
    print(f"EDT:       {EDT_5:.2f} s")
    print(f"T30:       {T30_5:.2f} s")
    print(f"EDT/T30:   {EDT_5/T30_5:.2f}")
    print("En RI sintetica con decaimiento uniforme, EDT ≈ T30 ≈ T60")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Efecto del piso de ruido
    """)
    return


@app.cell
def _(np, plt, fs_3, N_3, t_3, tau_3, T60_3):
    # Ejercicio 6: Piso de ruido
    np.random.seed(42)
    h_limpia = np.random.randn(N_3) * np.exp(-t_3 / tau_3)

    niveles_ruido = [0, 0.001, 0.01, 0.05]
    colores_6 = ['black', 'green', 'orange', 'red']

    fig_6, axes_6 = plt.subplots(2, 1, figsize=(12, 8))

    t30_resultados = {}
    for nivel, color in zip(niveles_ruido, colores_6):
        if nivel == 0:
            h_ruidosa = h_limpia.copy()
            label = 'Sin ruido'
        else:
            h_ruidosa = h_limpia + nivel * np.random.randn(N_3)
            label = f'Ruido = {nivel}'

        EDC = np.cumsum(h_ruidosa[::-1]**2)[::-1]
        EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)

        axes_6[0].plot(t_3, EDC_dB, color=color, linewidth=2, label=label)

        # T30
        mask = (EDC_dB >= -35) & (EDC_dB <= -5)
        if np.sum(mask) > 2:
            m, b = np.polyfit(t_3[mask], EDC_dB[mask], 1)
            T30 = -60 / m
            t30_resultados[label] = T30

    axes_6[0].axhline(-60, color='gray', linestyle='--', alpha=0.5)
    axes_6[0].set_xlabel('Tiempo (s)')
    axes_6[0].set_ylabel('EDC (dB)')
    axes_6[0].set_title('Ejercicio 6: Efecto del piso de ruido en la EDC')
    axes_6[0].set_ylim(-80, 5)
    axes_6[0].legend()
    axes_6[0].grid(True, alpha=0.3)

    # T30 comparados
    axes_6[1].barh(list(t30_resultados.keys()), list(t30_resultados.values()),
                    color=colores_6[:len(t30_resultados)], edgecolor='black')
    axes_6[1].axvline(T60_3, color='blue', linestyle='--', linewidth=2, label=f'T60 real = {T60_3} s')
    axes_6[1].set_xlabel('T30 (s)')
    axes_6[1].set_title('T30 medido con distintos niveles de ruido')
    axes_6[1].legend()
    axes_6[1].grid(True, alpha=0.3, axis='x')

    plt.tight_layout()

    print(f"T60 real: {T60_3:.2f} s")
    for label, t30 in t30_resultados.items():
        print(f"  {label}: T30 = {t30:.2f} s (error: {abs(t30-T60_3)/T60_3*100:.1f}%)")
    print("\nEl piso de ruido hace que la EDC 'suba' al final, subestimando el T60.")
    print("El metodo de Lundeby detecta el punto donde el ruido domina y lo compensa.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: T60 por banda de octava
    """)
    return


@app.cell
def _(np, plt, signal, fs_3, N_3, t_3, tau_3, T60_3):
    # Ejercicio 7: T30 por banda de octava
    np.random.seed(42)
    h_7 = np.random.randn(N_3) * np.exp(-t_3 / tau_3)

    fc_list_7 = [125, 250, 500, 1000, 2000, 4000]
    t30_por_banda = {}

    for fc in fc_list_7:
        f_low = fc / np.sqrt(2)
        f_high = fc * np.sqrt(2)
        f_high = min(f_high, fs_3 / 2 - 1)

        sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs_3, output='sos')
        h_banda = signal.sosfilt(sos, h_7)

        EDC = np.cumsum(h_banda[::-1]**2)[::-1]
        EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)

        mask = (EDC_dB >= -35) & (EDC_dB <= -5)
        if np.sum(mask) > 2:
            m, b = np.polyfit(t_3[mask], EDC_dB[mask], 1)
            t30_por_banda[fc] = -60 / m

    fig_7, ax_7 = plt.subplots(figsize=(10, 5))
    ax_7.bar([str(fc) for fc in t30_por_banda.keys()],
             list(t30_por_banda.values()),
             color='steelblue', edgecolor='navy')
    ax_7.axhline(T60_3, color='red', linestyle='--', linewidth=2, label=f'T60 real = {T60_3} s')
    ax_7.set_xlabel('Frecuencia central (Hz)')
    ax_7.set_ylabel('T30 (s)')
    ax_7.set_title('Ejercicio 7: T30 por banda de octava')
    ax_7.legend()
    ax_7.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()

    print(f"T60 real: {T60_3:.2f} s")
    for fc, t30 in t30_por_banda.items():
        print(f"  {fc:>5} Hz: T30 = {t30:.2f} s")
    print("\nCon RI sintetica, T30 es similar en todas las bandas.")
    print("En salas reales, las bajas frecuencias suelen tener mayor T60.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Funcion completa de analisis
    """)
    return


@app.cell
def _(np, plt, signal):
    # Ejercicio 8: Funcion analizar_ri completa
    def analizar_ri_sol(h, fs):
        """
        Analiza una RI y retorna EDT, T20, T30 por banda y broadband.

        Parametros:
            h: respuesta al impulso (array)
            fs: frecuencia de muestreo

        Retorna:
            dict con parametros por banda y broadband
        """
        t = np.arange(len(h)) / fs
        frecuencias_centrales = [125, 250, 500, 1000, 2000, 4000, 8000]

        def _calcular_param(t_arr, edc_db, db_ini, db_fin):
            mask = (edc_db >= db_fin) & (edc_db <= db_ini)
            if np.sum(mask) < 2:
                return None
            m, _ = np.polyfit(t_arr[mask], edc_db[mask], 1)
            return -60 / m

        def _analizar_banda(h_banda):
            EDC = np.cumsum(h_banda[::-1]**2)[::-1]
            EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)
            return {
                'EDT': _calcular_param(t, EDC_dB, 0, -10),
                'T20': _calcular_param(t, EDC_dB, -5, -25),
                'T30': _calcular_param(t, EDC_dB, -5, -35),
            }

        resultados = {}

        # Broadband
        resultados['broadband'] = _analizar_banda(h)

        # Por banda de octava
        for fc in frecuencias_centrales:
            f_low = fc / np.sqrt(2)
            f_high = fc * np.sqrt(2)
            f_high = min(f_high, fs / 2 - 1)
            if f_high <= f_low:
                continue
            sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs, output='sos')
            h_banda = signal.sosfilt(sos, h)
            resultados[fc] = _analizar_banda(h_banda)

        return resultados

    # Probar con RI sintetica de T60 = 1.8 s
    fs_8 = 44100
    T60_8 = 1.8
    dur_8 = 3.0
    N_8 = int(fs_8 * dur_8)
    t_8 = np.arange(N_8) / fs_8
    tau_8 = T60_8 / (6 * np.log(10))
    np.random.seed(99)
    h_8 = np.random.randn(N_8) * np.exp(-t_8 / tau_8)

    res = analizar_ri_sol(h_8, fs_8)

    # Tabla de resultados
    print(f"{'Banda':<12} {'EDT (s)':<10} {'T20 (s)':<10} {'T30 (s)':<10}")
    print("-" * 42)
    for banda, params in res.items():
        edt_s = f"{params['EDT']:.2f}" if params['EDT'] is not None else "N/A"
        t20_s = f"{params['T20']:.2f}" if params['T20'] is not None else "N/A"
        t30_s = f"{params['T30']:.2f}" if params['T30'] is not None else "N/A"
        print(f"{str(banda):<12} {edt_s:<10} {t20_s:<10} {t30_s:<10}")

    print(f"\nT60 real: {T60_8} s")

    # Grafico
    fcs = [k for k in res.keys() if k != 'broadband']
    t30_vals = [res[fc]['T30'] for fc in fcs if res[fc]['T30'] is not None]
    fcs_valid = [fc for fc in fcs if res[fc]['T30'] is not None]

    fig_8, ax_8 = plt.subplots(figsize=(10, 5))
    ax_8.bar([str(fc) for fc in fcs_valid], t30_vals, color='steelblue', edgecolor='navy')
    ax_8.axhline(T60_8, color='red', linestyle='--', linewidth=2, label=f'T60 real = {T60_8} s')
    ax_8.set_xlabel('Frecuencia central (Hz)')
    ax_8.set_ylabel('T30 (s)')
    ax_8.set_title('Ejercicio 8: Analisis completo - T30 por banda')
    ax_8.legend()
    ax_8.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
