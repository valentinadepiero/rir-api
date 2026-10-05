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
    # Clase 5: Soluciones
    ## Operaciones con Senales
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Desplazamiento temporal
    """)
    return


@app.cell
def _(np, plt):
    # Senal original
    x_1 = np.array([1, 2, 3, 4, 5])
    n_orig = np.arange(5)  # n = 0, 1, 2, 3, 4

    # x[n - 2]: desplazamiento a la derecha por 2
    n_shifted = n_orig + 2  # n = 2, 3, 4, 5, 6

    fig_1, ax_1 = plt.subplots(figsize=(10, 5))

    markerline1, stemlines1, baseline1 = ax_1.stem(
        n_orig, x_1, linefmt='b-', markerfmt='bo', basefmt='k-', label='x[n]'
    )
    markerline2, stemlines2, baseline2 = ax_1.stem(
        n_shifted, x_1, linefmt='r-', markerfmt='rs', basefmt='k-', label='x[n-2]'
    )
    plt.setp(stemlines2, alpha=0.7)

    ax_1.set_xlim(-3, 9)
    ax_1.set_ylim(-0.5, 6)
    ax_1.set_title("Desplazamiento temporal: x[n] y x[n-2]")
    ax_1.set_xlabel("n (muestras)")
    ax_1.set_ylabel("Amplitud")
    ax_1.legend()
    ax_1.grid(True, alpha=0.3)
    ax_1.set_xticks(range(-2, 9))
    plt.tight_layout()
    fig_1
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Inversion temporal
    """)
    return


@app.cell
def _(np, plt):
    fs_2 = 44100
    duracion_2 = 1.0
    t_2 = np.arange(int(fs_2 * duracion_2)) / fs_2
    x_2 = np.sin(2 * np.pi * 440 * t_2)

    # Inversion temporal
    x_2_inv = x_2[::-1]

    # Mostrar solo los primeros 5 ms
    n_muestras_5ms = int(fs_2 * 0.005)
    t_5ms = t_2[:n_muestras_5ms] * 1000

    fig_2, (ax1_2, ax2_2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    ax1_2.plot(t_5ms, x_2[:n_muestras_5ms], 'b-', linewidth=1.5)
    ax1_2.set_title("x[n] - Senoidal original 440 Hz")
    ax1_2.set_ylabel("Amplitud")
    ax1_2.grid(True, alpha=0.3)

    ax2_2.plot(t_5ms, x_2_inv[:n_muestras_5ms], 'r-', linewidth=1.5)
    ax2_2.set_title("x[-n] - Senoidal invertida")
    ax2_2.set_xlabel("Tiempo (ms)")
    ax2_2.set_ylabel("Amplitud")
    ax2_2.grid(True, alpha=0.3)

    # Comentario: una senoidal pura invertida suena exactamente igual,
    # porque sin(-x) = -sin(x), y el oido no distingue la fase.
    # Solo se nota la diferencia con senales asimetricas o con envolvente.

    plt.tight_layout()
    fig_2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Mezcla de senoidales (tercera mayor)
    """)
    return


@app.cell
def _(np, plt):
    fs_3 = 44100
    duracion_3 = 0.020  # 20 ms
    t_3 = np.arange(int(fs_3 * duracion_3)) / fs_3

    x1_3 = 0.5 * np.sin(2 * np.pi * 440 * t_3)
    x2_3 = 0.5 * np.sin(2 * np.pi * 554.37 * t_3)
    suma_3 = x1_3 + x2_3

    fig_3, axes_3 = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes_3[0].plot(t_3 * 1000, x1_3, 'b-', linewidth=1.0)
    axes_3[0].set_title("440 Hz (La4), A=0.5")
    axes_3[0].set_ylabel("Amplitud")
    axes_3[0].set_ylim(-1.1, 1.1)
    axes_3[0].grid(True, alpha=0.3)

    axes_3[1].plot(t_3 * 1000, x2_3, 'r-', linewidth=1.0)
    axes_3[1].set_title("554.37 Hz (Do#5), A=0.5")
    axes_3[1].set_ylabel("Amplitud")
    axes_3[1].set_ylim(-1.1, 1.1)
    axes_3[1].grid(True, alpha=0.3)

    axes_3[2].plot(t_3 * 1000, suma_3, 'g-', linewidth=1.0)
    axes_3[2].set_title("Suma: acorde de tercera mayor (consonante)")
    axes_3[2].set_xlabel("Tiempo (ms)")
    axes_3[2].set_ylabel("Amplitud")
    axes_3[2].set_ylim(-1.1, 1.1)
    axes_3[2].grid(True, alpha=0.3)

    # Se escucharia un intervalo de tercera mayor, que es un sonido
    # consonante y agradable. La relacion de frecuencias es ~5:4.

    plt.tight_layout()
    fig_3
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Modulacion AM (tremolo)
    """)
    return


@app.cell
def _(np, plt):
    fs_4 = 44100
    duracion_4 = 0.5  # 500 ms
    t_4 = np.arange(int(fs_4 * duracion_4)) / fs_4

    portadora_4 = np.sin(2 * np.pi * 440 * t_4)
    moduladora_4 = 0.5 + 0.5 * np.sin(2 * np.pi * 5 * t_4)
    tremolo_4 = portadora_4 * moduladora_4

    fig_4, ax_4 = plt.subplots(figsize=(12, 5))
    ax_4.plot(t_4 * 1000, tremolo_4, 'b-', linewidth=0.5, label='Tremolo')
    ax_4.plot(t_4 * 1000, moduladora_4, 'r-', linewidth=2.0, alpha=0.7, label='Envolvente (moduladora)')
    ax_4.plot(t_4 * 1000, -moduladora_4, 'r-', linewidth=2.0, alpha=0.7)
    ax_4.set_title("Efecto tremolo: 440 Hz modulado a 5 Hz")
    ax_4.set_xlabel("Tiempo (ms)")
    ax_4.set_ylabel("Amplitud")
    ax_4.legend()
    ax_4.grid(True, alpha=0.3)
    plt.tight_layout()
    fig_4
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Interferencia constructiva y destructiva
    """)
    return


@app.cell
def _(np, plt):
    fs_5 = 44100
    f_5 = 1000
    duracion_5 = 0.005  # 5 ms
    t_5 = np.arange(int(fs_5 * duracion_5)) / fs_5

    fases = [0, np.pi / 2, np.pi]
    nombres_fase = ["0 (constructiva)", "pi/2 (parcial)", "pi (destructiva)"]
    colores_5 = ['green', 'orange', 'red']

    x1_5 = np.sin(2 * np.pi * f_5 * t_5)

    fig_5, axes_5 = plt.subplots(3, 1, figsize=(12, 9), sharex=True)

    for i, (phi, nombre, color) in enumerate(zip(fases, nombres_fase, colores_5)):
        x2_5 = np.sin(2 * np.pi * f_5 * t_5 + phi)
        suma_5 = x1_5 + x2_5
        amp_pico = np.max(np.abs(suma_5))

        axes_5[i].plot(t_5 * 1000, x1_5, 'b--', linewidth=0.8, alpha=0.5, label='x1')
        axes_5[i].plot(t_5 * 1000, x2_5, 'r--', linewidth=0.8, alpha=0.5, label='x2')
        axes_5[i].plot(t_5 * 1000, suma_5, color=color, linewidth=2.0, label=f'Suma (pico={amp_pico:.2f})')
        axes_5[i].set_title(f"Fase = {nombre}")
        axes_5[i].set_ylabel("Amplitud")
        axes_5[i].set_ylim(-2.5, 2.5)
        axes_5[i].legend(loc='upper right')
        axes_5[i].grid(True, alpha=0.3)

    axes_5[-1].set_xlabel("Tiempo (ms)")
    fig_5.suptitle("Interferencia: dos senoidales de 1000 Hz con diferente fase", fontsize=13)
    plt.tight_layout()
    fig_5
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Periodicidad
    """)
    return


@app.cell
def _():
    from fractions import Fraction

    fs_6 = 44100
    frecuencias_6 = [441, 440, 1000, 882]

    print(f"Analisis de periodicidad (fs = {fs_6} Hz)\n")
    print(f"{'Freq (Hz)':>10} {'f0/fs (fraccion)':>20} {'Periodo N':>12} {'Practico?':>12}")
    print("-" * 60)

    for f0 in frecuencias_6:
        frac = Fraction(f0, fs_6)
        N_periodo = frac.denominator
        practico = "Si" if N_periodo < 1000 else "No (largo)"
        print(f"{f0:>10} {str(frac):>20} {N_periodo:>12} {practico:>12}")

    print(f"\nExplicacion:")
    print(f"  441 Hz: 441/44100 = 1/100, periodo = 100 muestras (exacto y corto)")
    print(f"  440 Hz: 440/44100 = 44/4410 = 4/441, periodo = 441 muestras")
    print(f"  1000 Hz: 1000/44100 = 10/441, periodo = 441 muestras")
    print(f"  882 Hz: 882/44100 = 1/50, periodo = 50 muestras (exacto y corto)")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Energia y potencia
    """)
    return


@app.cell
def _(np):
    fs_7 = 44100

    # (a) Impulso unitario
    delta_7 = np.zeros(1000)
    delta_7[0] = 1.0

    # (b) Senoidal 440 Hz, 1 segundo
    t_7 = np.arange(fs_7) / fs_7
    sen_7 = np.sin(2 * np.pi * 440 * t_7)

    # (c) Silencio
    sil_7 = np.zeros(fs_7)

    senales_7 = [
        ("Impulso unitario", delta_7),
        ("Senoidal 440 Hz", sen_7),
        ("Silencio", sil_7),
    ]

    print(f"{'Senal':<22} {'Energia':>12} {'Potencia':>12} {'RMS':>12} {'dBFS':>10}")
    print("-" * 72)

    for nombre, x in senales_7:
        E = np.sum(np.abs(x)**2)
        P = E / len(x)
        rms = np.sqrt(P)
        dbfs = 20 * np.log10(rms) if rms > 0 else float('-inf')
        print(f"{nombre:<22} {E:>12.4f} {P:>12.6f} {rms:>12.6f} {dbfs:>10.2f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Conversion a dBFS
    """)
    return


@app.cell
def _(np):
    fs_8 = 44100
    A_8 = 0.5
    t_8 = np.arange(fs_8) / fs_8
    x_8 = A_8 * np.sin(2 * np.pi * 440 * t_8)

    # Calculo numerico
    rms_8 = np.sqrt(np.mean(x_8**2))
    dbfs_8 = 20 * np.log10(rms_8)

    # Calculo analitico
    rms_analitico = A_8 / np.sqrt(2)
    dbfs_analitico = 20 * np.log10(rms_analitico)

    print(f"Senoidal de amplitud A = {A_8}")
    print(f"\nCalculo numerico:")
    print(f"  RMS  = {rms_8:.6f}")
    print(f"  dBFS = {dbfs_8:.2f}")
    print(f"\nCalculo analitico (A/sqrt(2)):")
    print(f"  RMS  = {rms_analitico:.6f}")
    print(f"  dBFS = {dbfs_analitico:.2f}")
    print(f"\nDiferencia RMS: {abs(rms_8 - rms_analitico):.2e}")
    print(f"Coinciden (tolerancia 1e-4): {abs(rms_8 - rms_analitico) < 1e-4}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Fade-in lineal
    """)
    return


@app.cell
def _(np, plt):
    fs_9 = 44100
    duracion_9 = 2.0
    t_9 = np.arange(int(fs_9 * duracion_9)) / fs_9

    # Tono original
    tono_9 = 0.8 * np.sin(2 * np.pi * 440 * t_9)

    # Envolvente de fade-in: 0 a 1 en 500 ms, luego 1
    n_fade = int(0.5 * fs_9)  # 500 ms
    envolvente_9 = np.ones(len(t_9))
    envolvente_9[:n_fade] = np.linspace(0, 1, n_fade)

    # Aplicar fade-in
    resultado_9 = tono_9 * envolvente_9

    fig_9, axes_9 = plt.subplots(3, 1, figsize=(12, 9), sharex=True)

    axes_9[0].plot(t_9 * 1000, tono_9, 'b-', linewidth=0.5)
    axes_9[0].set_title("Tono original: 440 Hz, A=0.8")
    axes_9[0].set_ylabel("Amplitud")
    axes_9[0].grid(True, alpha=0.3)

    axes_9[1].plot(t_9 * 1000, envolvente_9, 'r-', linewidth=2.0)
    axes_9[1].set_title("Envolvente de fade-in (500 ms)")
    axes_9[1].set_ylabel("Amplitud")
    axes_9[1].grid(True, alpha=0.3)
    axes_9[1].axvline(x=500, color='g', linestyle='--', alpha=0.7, label='Fin del fade')
    axes_9[1].legend()

    axes_9[2].plot(t_9 * 1000, resultado_9, 'g-', linewidth=0.5)
    axes_9[2].set_title("Resultado: tono con fade-in")
    axes_9[2].set_xlabel("Tiempo (ms)")
    axes_9[2].set_ylabel("Amplitud")
    axes_9[2].grid(True, alpha=0.3)

    plt.tight_layout()
    fig_9
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Crossfade entre dos senales
    """)
    return


@app.cell
def _(np, plt):
    fs_10 = 44100
    duracion_a = 1.0  # 1 segundo
    duracion_b = 1.0
    duracion_xfade = 0.1  # 100 ms

    # Generar senales completas
    N_a = int(fs_10 * duracion_a)
    N_b = int(fs_10 * duracion_b)
    N_xfade = int(fs_10 * duracion_xfade)

    t_a = np.arange(N_a) / fs_10
    t_b = np.arange(N_b) / fs_10

    senal_a = 0.7 * np.sin(2 * np.pi * 440 * t_a)
    senal_b = 0.7 * np.sin(2 * np.pi * 660 * t_b)

    # Longitud total: A + B - crossfade
    N_total = N_a + N_b - N_xfade
    resultado_10 = np.zeros(N_total)

    # Parte de A antes del crossfade
    resultado_10[:N_a - N_xfade] = senal_a[:N_a - N_xfade]

    # Zona de crossfade
    fade_out = np.linspace(1, 0, N_xfade)
    fade_in = np.linspace(0, 1, N_xfade)
    inicio_xfade = N_a - N_xfade
    resultado_10[inicio_xfade:N_a] = (
        senal_a[N_a - N_xfade:] * fade_out +
        senal_b[:N_xfade] * fade_in
    )

    # Parte de B despues del crossfade
    resultado_10[N_a:] = senal_b[N_xfade:]

    t_total = np.arange(N_total) / fs_10

    fig_10, ax_10 = plt.subplots(figsize=(14, 5))
    ax_10.plot(t_total * 1000, resultado_10, 'b-', linewidth=0.5)

    # Sombrear zona de crossfade
    xfade_start_ms = (N_a - N_xfade) / fs_10 * 1000
    xfade_end_ms = N_a / fs_10 * 1000
    ax_10.axvspan(xfade_start_ms, xfade_end_ms, alpha=0.2, color='red', label='Zona de crossfade')
    ax_10.axvline(x=xfade_start_ms, color='r', linestyle='--', alpha=0.5)
    ax_10.axvline(x=xfade_end_ms, color='r', linestyle='--', alpha=0.5)

    ax_10.set_title(f"Crossfade: 440 Hz -> 660 Hz (transicion de {duracion_xfade*1000:.0f} ms)")
    ax_10.set_xlabel("Tiempo (ms)")
    ax_10.set_ylabel("Amplitud")
    ax_10.legend()
    ax_10.grid(True, alpha=0.3)
    plt.tight_layout()

    print(f"Duracion senal A: {duracion_a*1000:.0f} ms")
    print(f"Duracion senal B: {duracion_b*1000:.0f} ms")
    print(f"Duracion crossfade: {duracion_xfade*1000:.0f} ms")
    print(f"Duracion total: {N_total/fs_10*1000:.0f} ms (esperado: {(duracion_a+duracion_b-duracion_xfade)*1000:.0f} ms)")

    fig_10
    return


if __name__ == "__main__":
    app.run()
