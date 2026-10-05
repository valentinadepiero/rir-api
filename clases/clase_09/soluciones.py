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
    # Clase 9: Soluciones
    ## Frecuencia y Filtros
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import signal
    from scipy.fft import rfft, rfftfreq
    return np, plt, signal, rfft, rfftfreq


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: FFT de un tono de 440 Hz
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Ejercicio 1: FFT de 440 Hz en dB
    fs_1 = 44100
    dur_1 = 1.0
    N_1 = int(fs_1 * dur_1)
    t_1 = np.arange(N_1) / fs_1

    x_1 = np.sin(2 * np.pi * 440 * t_1)

    X_1 = rfft(x_1)
    freqs_1 = rfftfreq(N_1, d=1/fs_1)
    mag_db_1 = 20 * np.log10(np.abs(X_1) / N_1 * 2 + 1e-12)

    fig_1, ax_1 = plt.subplots(figsize=(12, 4))
    ax_1.plot(freqs_1, mag_db_1, 'r-')
    ax_1.set_xlabel('Frecuencia (Hz)')
    ax_1.set_ylabel('Magnitud (dB)')
    ax_1.set_title('Ejercicio 1: Espectro de 440 Hz en dB')
    ax_1.set_xlim(0, 2000)
    ax_1.grid(True, alpha=0.3)
    ax_1.axvline(440, color='blue', linestyle='--', alpha=0.5, label='440 Hz')
    ax_1.legend()
    plt.tight_layout()

    idx_pico = np.argmax(mag_db_1)
    print(f"Pico encontrado en: {freqs_1[idx_pico]:.1f} Hz con {mag_db_1[idx_pico]:.1f} dB")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: FFT de senal con 3 frecuencias
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Ejercicio 2: 3 frecuencias
    fs_2 = 44100
    dur_2 = 1.0
    N_2 = int(fs_2 * dur_2)
    t_2 = np.arange(N_2) / fs_2

    x_2 = 1.0 * np.sin(2 * np.pi * 200 * t_2) + \
          0.5 * np.sin(2 * np.pi * 500 * t_2) + \
          0.3 * np.sin(2 * np.pi * 1200 * t_2)

    X_2 = rfft(x_2)
    freqs_2 = rfftfreq(N_2, d=1/fs_2)
    mag_2 = np.abs(X_2) / N_2 * 2

    fig_2, ax_2 = plt.subplots(figsize=(12, 4))
    ax_2.plot(freqs_2, mag_2, 'r-')
    for f_mark, amp in [(200, 1.0), (500, 0.5), (1200, 0.3)]:
        ax_2.axvline(f_mark, color='blue', linestyle='--', alpha=0.5)
        ax_2.annotate(f'{f_mark} Hz\n(A={amp})', xy=(f_mark, amp),
                      xytext=(f_mark + 50, amp + 0.05), fontsize=9)
    ax_2.set_xlabel('Frecuencia (Hz)')
    ax_2.set_ylabel('Magnitud')
    ax_2.set_title('Ejercicio 2: Espectro con 3 frecuencias')
    ax_2.set_xlim(0, 2000)
    ax_2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Fuga espectral
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Ejercicio 3: Fuga espectral con ventana
    fs_3 = 1000
    dur_3 = 1.0
    N_3 = int(fs_3 * dur_3)
    t_3 = np.arange(N_3) / fs_3

    f_leak = 100.5
    x_3 = np.sin(2 * np.pi * f_leak * t_3)

    # Sin ventana
    X_rect = rfft(x_3)
    freqs_3 = rfftfreq(N_3, d=1/fs_3)
    mag_rect = 20 * np.log10(np.abs(X_rect) / N_3 * 2 + 1e-12)

    # Con Hanning
    ventana = np.hanning(N_3)
    X_hann = rfft(x_3 * ventana)
    mag_hann = 20 * np.log10(np.abs(X_hann) / N_3 * 2 + 1e-12)

    fig_3, ax_3 = plt.subplots(figsize=(12, 5))
    ax_3.plot(freqs_3, mag_rect, 'b-', label='Sin ventana (rectangular)', alpha=0.7)
    ax_3.plot(freqs_3, mag_hann, 'r-', label='Con ventana Hanning', alpha=0.7)
    ax_3.set_xlim(50, 150)
    ax_3.set_ylim(-80, 5)
    ax_3.set_xlabel('Frecuencia (Hz)')
    ax_3.set_ylabel('Magnitud (dB)')
    ax_3.set_title(f'Ejercicio 3: Fuga espectral - Tono de {f_leak} Hz')
    ax_3.legend()
    ax_3.grid(True, alpha=0.3)
    plt.tight_layout()

    print("La ventana Hanning reduce los lobulos laterales (fuga espectral)")
    print("a costa de ensanchar el lobulo principal.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Espectro del ruido rosa (-3 dB/octava)
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq):
    # Ejercicio 4: Ruido rosa y verificacion de pendiente
    fs_4 = 44100
    dur_4 = 2.0
    N_4 = int(fs_4 * dur_4)

    # Generar ruido rosa
    blanco = np.random.randn(N_4)
    X_blanco = rfft(blanco)
    freqs_4 = rfftfreq(N_4, d=1/fs_4)

    filtro_rosa = np.ones(len(freqs_4))
    filtro_rosa[1:] = 1.0 / np.sqrt(freqs_4[1:])
    filtro_rosa[0] = 0

    rosa = np.fft.irfft(X_blanco * filtro_rosa, n=N_4)

    # Espectro del ruido rosa
    X_rosa = rfft(rosa)
    mag_rosa_db = 20 * np.log10(np.abs(X_rosa) / N_4 * 2 + 1e-12)

    # Suavizar con promedios en bandas (para ver tendencia)
    # Ajustar recta en log-log
    mask = (freqs_4 > 50) & (freqs_4 < 15000)
    log_f = np.log10(freqs_4[mask])
    coefs = np.polyfit(log_f, mag_rosa_db[mask], 1)
    recta = np.polyval(coefs, log_f)

    fig_4, ax_4 = plt.subplots(figsize=(12, 5))
    ax_4.semilogx(freqs_4[mask], mag_rosa_db[mask], 'r-', alpha=0.2, linewidth=0.3, label='Espectro')
    ax_4.semilogx(freqs_4[mask], recta, 'b-', linewidth=2,
                   label=f'Ajuste: {coefs[0]:.1f} dB/decada')
    ax_4.set_xlabel('Frecuencia (Hz)')
    ax_4.set_ylabel('Magnitud (dB)')
    ax_4.set_title('Ejercicio 4: Espectro del ruido rosa')
    ax_4.legend()
    ax_4.grid(True, alpha=0.3, which='both')
    plt.tight_layout()

    # -3 dB/octava = -10 dB/decada
    print(f"Pendiente medida: {coefs[0]:.1f} dB/decada")
    print(f"Esperada: -10 dB/decada (-3 dB/octava)")
    print(f"En dB/octava: {coefs[0] * np.log10(2):.1f} dB/octava")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Filtro pasa-bajos Butterworth a 1 kHz
    """)
    return


@app.cell
def _(np, plt, signal, rfft, rfftfreq):
    # Ejercicio 5: Butterworth LP 1 kHz
    fs_5 = 44100
    dur_5 = 2.0
    N_5 = int(fs_5 * dur_5)

    ruido_5 = np.random.randn(N_5)

    # Filtro
    sos_5 = signal.butter(6, 1000, btype='low', fs=fs_5, output='sos')
    filtrado_5 = signal.sosfilt(sos_5, ruido_5)

    # Espectros
    freqs_5 = rfftfreq(N_5, d=1/fs_5)
    esp_orig_5 = 20 * np.log10(np.abs(rfft(ruido_5)) / N_5 * 2 + 1e-12)
    esp_filt_5 = 20 * np.log10(np.abs(rfft(filtrado_5)) / N_5 * 2 + 1e-12)

    fig_5, axes_5 = plt.subplots(2, 1, figsize=(12, 8))

    # Espectros superpuestos
    axes_5[0].semilogx(freqs_5[1:], esp_orig_5[1:], 'b-', alpha=0.3, linewidth=0.3, label='Original')
    axes_5[0].semilogx(freqs_5[1:], esp_filt_5[1:], 'r-', alpha=0.5, linewidth=0.3, label='Filtrado LP 1 kHz')
    axes_5[0].set_xlabel('Frecuencia (Hz)')
    axes_5[0].set_ylabel('Magnitud (dB)')
    axes_5[0].set_title('Ejercicio 5: Espectros original vs filtrado')
    axes_5[0].legend()
    axes_5[0].set_xlim(20, fs_5/2)
    axes_5[0].grid(True, alpha=0.3, which='both')

    # Respuesta en frecuencia del filtro
    w_5, h_5 = signal.sosfreqz(sos_5, worN=8192, fs=fs_5)
    axes_5[1].semilogx(w_5, 20 * np.log10(np.abs(h_5) + 1e-12), 'g-', linewidth=2)
    axes_5[1].set_xlabel('Frecuencia (Hz)')
    axes_5[1].set_ylabel('Ganancia (dB)')
    axes_5[1].set_title('Respuesta en frecuencia: Butterworth LP orden 6, fc=1 kHz')
    axes_5[1].set_xlim(20, fs_5/2)
    axes_5[1].set_ylim(-80, 5)
    axes_5[1].axhline(-3, color='gray', linestyle='--', alpha=0.5, label='-3 dB')
    axes_5[1].axvline(1000, color='gray', linestyle='--', alpha=0.5, label='1 kHz')
    axes_5[1].legend()
    axes_5[1].grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Filtro pasa-banda para 1 kHz (una octava)
    """)
    return


@app.cell
def _(np, plt, signal, rfft, rfftfreq):
    # Ejercicio 6: Banda de 1 kHz
    fs_6 = 44100
    fc_6 = 1000
    f_low_6 = fc_6 / np.sqrt(2)
    f_high_6 = fc_6 * np.sqrt(2)

    sos_6 = signal.butter(4, [f_low_6, f_high_6], btype='band', fs=fs_6, output='sos')

    # Respuesta en frecuencia
    w_6, h_6 = signal.sosfreqz(sos_6, worN=8192, fs=fs_6)
    h_db_6 = 20 * np.log10(np.abs(h_6) + 1e-12)

    fig_6, axes_6 = plt.subplots(2, 1, figsize=(12, 8))

    axes_6[0].semilogx(w_6, h_db_6, 'g-', linewidth=2)
    axes_6[0].axhline(-3, color='gray', linestyle='--', alpha=0.5, label='-3 dB')
    axes_6[0].axvline(f_low_6, color='r', linestyle='--', alpha=0.5, label=f'f_low={f_low_6:.0f} Hz')
    axes_6[0].axvline(f_high_6, color='b', linestyle='--', alpha=0.5, label=f'f_high={f_high_6:.0f} Hz')
    axes_6[0].set_xlabel('Frecuencia (Hz)')
    axes_6[0].set_ylabel('Ganancia (dB)')
    axes_6[0].set_title(f'Ejercicio 6: Filtro pasa-banda {fc_6} Hz (octava)')
    axes_6[0].set_xlim(100, 10000)
    axes_6[0].set_ylim(-60, 5)
    axes_6[0].legend()
    axes_6[0].grid(True, alpha=0.3, which='both')

    # Aplicar a ruido blanco
    N_6 = int(fs_6 * 2.0)
    ruido_6 = np.random.randn(N_6)
    filtrado_6 = signal.sosfilt(sos_6, ruido_6)

    freqs_6 = rfftfreq(N_6, d=1/fs_6)
    esp_6 = 20 * np.log10(np.abs(rfft(filtrado_6)) / N_6 * 2 + 1e-12)

    axes_6[1].semilogx(freqs_6[1:], esp_6[1:], 'r-', alpha=0.5, linewidth=0.3)
    axes_6[1].set_xlabel('Frecuencia (Hz)')
    axes_6[1].set_ylabel('Magnitud (dB)')
    axes_6[1].set_title('Espectro del ruido filtrado en banda de 1 kHz')
    axes_6[1].set_xlim(100, 10000)
    axes_6[1].grid(True, alpha=0.3, which='both')

    plt.tight_layout()

    # Verificar ancho de banda a -3 dB
    idx_3db = np.where(h_db_6 >= -3)[0]
    if len(idx_3db) > 0:
        f_inf = w_6[idx_3db[0]]
        f_sup = w_6[idx_3db[-1]]
        print(f"Ancho de banda a -3 dB: {f_inf:.0f} - {f_sup:.0f} Hz")
        print(f"Esperado: {f_low_6:.0f} - {f_high_6:.0f} Hz")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Banco de filtros de octava completo
    """)
    return


@app.cell
def _(np, plt, signal):
    # Ejercicio 7: Banco de filtros de octava
    def banco_octavas(x, fs, orden=4):
        """Filtra senal en bandas de octava de 125 a 8000 Hz."""
        fc_list = [125, 250, 500, 1000, 2000, 4000, 8000]
        bandas = {}
        for fc in fc_list:
            f_low = fc / np.sqrt(2)
            f_high = fc * np.sqrt(2)
            f_low = max(f_low, 10)
            f_high = min(f_high, fs / 2 - 1)
            sos = signal.butter(orden, [f_low, f_high], btype='band', fs=fs, output='sos')
            bandas[fc] = signal.sosfilt(sos, x)
        return bandas

    fs_7 = 44100
    fc_list_7 = [125, 250, 500, 1000, 2000, 4000, 8000]

    # Respuestas en frecuencia
    fig_7, axes_7 = plt.subplots(2, 1, figsize=(12, 8))
    colores_7 = plt.cm.tab10(np.linspace(0, 1, len(fc_list_7)))

    for i, fc in enumerate(fc_list_7):
        f_low = fc / np.sqrt(2)
        f_high = fc * np.sqrt(2)
        f_high = min(f_high, fs_7 / 2 - 1)
        sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs_7, output='sos')
        w, h = signal.sosfreqz(sos, worN=8192, fs=fs_7)
        axes_7[0].semilogx(w, 20 * np.log10(np.abs(h) + 1e-12),
                            color=colores_7[i], linewidth=2, label=f'{fc} Hz')

    axes_7[0].set_xlabel('Frecuencia (Hz)')
    axes_7[0].set_ylabel('Ganancia (dB)')
    axes_7[0].set_title('Banco de filtros de octava (125-8000 Hz)')
    axes_7[0].set_xlim(50, 20000)
    axes_7[0].set_ylim(-60, 5)
    axes_7[0].legend(loc='lower left')
    axes_7[0].grid(True, alpha=0.3, which='both')

    # Aplicar a ruido blanco
    N_7 = int(fs_7 * 2.0)
    ruido_7 = np.random.randn(N_7)
    bandas_7 = banco_octavas(ruido_7, fs_7)

    energias_7 = {fc: 20 * np.log10(np.sqrt(np.mean(b**2)) + 1e-12) for fc, b in bandas_7.items()}
    axes_7[1].bar([str(fc) for fc in energias_7.keys()],
                   list(energias_7.values()),
                   color='steelblue', edgecolor='navy')
    axes_7[1].set_xlabel('Frecuencia central (Hz)')
    axes_7[1].set_ylabel('Nivel RMS (dB)')
    axes_7[1].set_title('Energia por banda de octava - Ruido blanco')
    axes_7[1].grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    print("Ruido blanco: la energia por banda CRECE con la frecuencia")
    print("(cada octava tiene el doble de ancho de banda en Hz)")
    plt.gca()
    return (banco_octavas,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Espectrograma de sine sweep
    """)
    return


@app.cell
def _(np, plt, signal):
    # Ejercicio 8: Espectrograma de sweep con distintas resoluciones
    fs_8 = 44100
    dur_8 = 5.0
    N_8 = int(fs_8 * dur_8)
    t_8 = np.arange(N_8) / fs_8

    sweep_8 = signal.chirp(t_8, f0=20, f1=20000, t1=dur_8, method='logarithmic')

    fig_8, axes_8 = plt.subplots(3, 1, figsize=(14, 10))
    nperseg_vals = [256, 1024, 4096]

    for ax, nperseg in zip(axes_8, nperseg_vals):
        f_sp, t_sp, Sxx = signal.spectrogram(sweep_8, fs=fs_8,
                                                nperseg=nperseg, noverlap=nperseg*3//4)
        ax.pcolormesh(t_sp, f_sp, 10 * np.log10(Sxx + 1e-12),
                       shading='gouraud', cmap='inferno')
        ax.set_ylabel('Frecuencia (Hz)')
        ax.set_title(f'nperseg = {nperseg} (resolucion freq: {fs_8/nperseg:.1f} Hz, '
                     f'resolucion temporal: {nperseg/fs_8*1000:.1f} ms)')
        ax.set_ylim(0, 20000)

    axes_8[2].set_xlabel('Tiempo (s)')
    plt.tight_layout()

    print("nperseg grande -> mejor resolucion en frecuencia, peor en tiempo")
    print("nperseg chico -> mejor resolucion en tiempo, peor en frecuencia")
    print("Esto es el principio de incertidumbre tiempo-frecuencia.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Energia por banda de ruido rosa
    """)
    return


@app.cell
def _(np, plt, rfft, rfftfreq, banco_octavas):
    # Ejercicio 9: Energia por banda - ruido rosa vs blanco
    fs_9 = 44100
    dur_9 = 5.0
    N_9 = int(fs_9 * dur_9)

    # Ruido blanco
    blanco_9 = np.random.randn(N_9)

    # Ruido rosa
    X_b9 = rfft(blanco_9)
    freqs_9 = rfftfreq(N_9, d=1/fs_9)
    filt_rosa_9 = np.ones(len(freqs_9))
    filt_rosa_9[1:] = 1.0 / np.sqrt(freqs_9[1:])
    filt_rosa_9[0] = 0
    rosa_9 = np.fft.irfft(X_b9 * filt_rosa_9, n=N_9)

    # Filtrar por bandas
    bandas_blanco = banco_octavas(blanco_9, fs_9)
    bandas_rosa = banco_octavas(rosa_9, fs_9)

    fcs = list(bandas_blanco.keys())
    rms_blanco = [20 * np.log10(np.sqrt(np.mean(bandas_blanco[fc]**2)) + 1e-12) for fc in fcs]
    rms_rosa = [20 * np.log10(np.sqrt(np.mean(bandas_rosa[fc]**2)) + 1e-12) for fc in fcs]

    fig_9, axes_9 = plt.subplots(1, 2, figsize=(14, 5))

    x_pos = np.arange(len(fcs))
    axes_9[0].bar(x_pos, rms_blanco, color='steelblue', edgecolor='navy')
    axes_9[0].set_xticks(x_pos)
    axes_9[0].set_xticklabels([str(fc) for fc in fcs])
    axes_9[0].set_xlabel('Frecuencia central (Hz)')
    axes_9[0].set_ylabel('Nivel RMS (dB)')
    axes_9[0].set_title('Ruido BLANCO por banda')
    axes_9[0].grid(True, alpha=0.3, axis='y')

    axes_9[1].bar(x_pos, rms_rosa, color='salmon', edgecolor='darkred')
    axes_9[1].set_xticks(x_pos)
    axes_9[1].set_xticklabels([str(fc) for fc in fcs])
    axes_9[1].set_xlabel('Frecuencia central (Hz)')
    axes_9[1].set_ylabel('Nivel RMS (dB)')
    axes_9[1].set_title('Ruido ROSA por banda')
    axes_9[1].grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    rango_blanco = max(rms_blanco) - min(rms_blanco)
    rango_rosa = max(rms_rosa) - min(rms_rosa)
    print(f"Rango de variacion - Blanco: {rango_blanco:.1f} dB, Rosa: {rango_rosa:.1f} dB")
    print("El ruido rosa tiene energia mas uniforme por banda de octava.")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Analizador de frecuencia interactivo
    """)
    return


@app.cell
def _(mo):
    slider_f1 = mo.ui.slider(100, 5000, value=440, step=10, label="Frecuencia 1 (Hz)")
    slider_f2 = mo.ui.slider(100, 5000, value=880, step=10, label="Frecuencia 2 (Hz)")
    mo.vstack([slider_f1, slider_f2])
    return (slider_f1, slider_f2)


@app.cell
def _(np, plt, rfft, rfftfreq, slider_f1, slider_f2):
    fs_10 = 44100
    dur_10 = 0.5
    N_10 = int(fs_10 * dur_10)
    t_10 = np.arange(N_10) / fs_10

    f1_val = slider_f1.value
    f2_val = slider_f2.value
    x_10 = 0.5 * np.sin(2 * np.pi * f1_val * t_10) + 0.5 * np.sin(2 * np.pi * f2_val * t_10)

    X_10 = rfft(x_10)
    freqs_10 = rfftfreq(N_10, d=1/fs_10)
    mag_10 = np.abs(X_10) / N_10 * 2

    fig_10, axes_10 = plt.subplots(1, 2, figsize=(14, 4))

    # Tiempo (primeros 20 ms)
    n_20ms = int(0.02 * fs_10)
    axes_10[0].plot(t_10[:n_20ms] * 1000, x_10[:n_20ms], 'b-')
    axes_10[0].set_xlabel('Tiempo (ms)')
    axes_10[0].set_ylabel('Amplitud')
    axes_10[0].set_title(f'Senal: {f1_val} Hz + {f2_val} Hz')
    axes_10[0].grid(True, alpha=0.3)

    # Espectro
    axes_10[1].plot(freqs_10, mag_10, 'r-')
    axes_10[1].set_xlabel('Frecuencia (Hz)')
    axes_10[1].set_ylabel('Magnitud')
    axes_10[1].set_title('Espectro de magnitud')
    axes_10[1].set_xlim(0, max(f1_val, f2_val) * 2)
    axes_10[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
