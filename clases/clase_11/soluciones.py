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
    # Clase 11: Soluciones
    ## Vibecoding en Profundidad

    Nota: los ejercicios 4, 5 y 6 son de configuracion/reflexion y no tienen una solucion unica.
    Aca se incluyen soluciones de referencia para los ejercicios 1, 2 y 3.
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
    ### Ejercicio 1: Spec First - filtro_octava

    **Especificacion:**
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```
    Funcion: filtro_octava(x, fc, fs, orden=4)

    Descripcion:
        Filtra una senal en una banda de octava centrada en fc,
        usando un filtro Butterworth pasa-banda.

    Parametros:
        x : numpy.ndarray (1D, float64)
            Senal de entrada.
        fc : float
            Frecuencia central de la banda de octava (Hz).
            Rango valido: 20 <= fc <= fs/2.
        fs : int o float
            Frecuencia de muestreo (Hz). Debe ser > 0.
        orden : int (default 4)
            Orden del filtro Butterworth. Rango: 1-8.

    Retorna:
        numpy.ndarray (1D, float64) - Senal filtrada, mismo largo que x.

    Comportamiento:
        - f_low = fc / sqrt(2)
        - f_high = fc * sqrt(2)
        - Si f_high >= fs/2, se ajusta a fs/2 - 1
        - Si f_low < 10, se ajusta a 10
        - Usa scipy.signal.butter con output='sos'
        - Aplica con scipy.signal.sosfilt

    Ejemplo:
        >>> fs = 44100
        >>> t = np.arange(fs) / fs
        >>> x = np.sin(2 * np.pi * 1000 * t)
        >>> y = filtro_octava(x, fc=1000, fs=fs)
        >>> np.max(np.abs(y)) > 0.5  # tono dentro de la banda pasa
        True
    ```
    """)
    return


@app.cell
def _(np, plt, signal):
    # Implementacion de referencia
    def filtro_octava(x, fc, fs, orden=4):
        """
        Filtra una senal en una banda de octava centrada en fc.

        Parametros:
            x: senal de entrada (numpy array 1D)
            fc: frecuencia central (Hz)
            fs: frecuencia de muestreo (Hz)
            orden: orden del filtro Butterworth (default 4)

        Retorna:
            Senal filtrada (numpy array 1D)
        """
        f_low = fc / np.sqrt(2)
        f_high = fc * np.sqrt(2)

        # Ajustar limites
        f_low = max(f_low, 10)
        f_high = min(f_high, fs / 2 - 1)

        if f_high <= f_low:
            return np.zeros_like(x)

        sos = signal.butter(orden, [f_low, f_high], btype='band', fs=fs, output='sos')
        return signal.sosfilt(sos, x)

    # Verificacion
    fs_1 = 44100
    t_1 = np.arange(fs_1) / fs_1

    # Tono dentro de la banda (1000 Hz, banda de 1000 Hz)
    tono_dentro = np.sin(2 * np.pi * 1000 * t_1)
    filtrado_dentro = filtro_octava(tono_dentro, fc=1000, fs=fs_1)

    # Tono fuera de la banda (5000 Hz, banda de 1000 Hz)
    tono_fuera = np.sin(2 * np.pi * 5000 * t_1)
    filtrado_fuera = filtro_octava(tono_fuera, fc=1000, fs=fs_1)

    fig_1, axes_1 = plt.subplots(2, 1, figsize=(12, 6))

    n_show = int(0.01 * fs_1)
    axes_1[0].plot(t_1[:n_show]*1000, tono_dentro[:n_show], 'b-', alpha=0.5, label='Original 1000 Hz')
    axes_1[0].plot(t_1[:n_show]*1000, filtrado_dentro[:n_show], 'r-', linewidth=2, label='Filtrado')
    axes_1[0].set_title('Tono DENTRO de la banda (1000 Hz)')
    axes_1[0].legend()
    axes_1[0].grid(True, alpha=0.3)

    axes_1[1].plot(t_1[:n_show]*1000, tono_fuera[:n_show], 'b-', alpha=0.5, label='Original 5000 Hz')
    axes_1[1].plot(t_1[:n_show]*1000, filtrado_fuera[:n_show], 'r-', linewidth=2, label='Filtrado')
    axes_1[1].set_title('Tono FUERA de la banda (5000 Hz)')
    axes_1[1].legend()
    axes_1[1].grid(True, alpha=0.3)

    for ax in axes_1:
        ax.set_xlabel('Tiempo (ms)')
        ax.set_ylabel('Amplitud')

    plt.tight_layout()

    print(f"Tono dentro (1000 Hz): amplitud filtrada = {np.max(np.abs(filtrado_dentro)):.3f}")
    print(f"Tono fuera (5000 Hz): amplitud filtrada = {np.max(np.abs(filtrado_fuera)):.4f}")
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Test First - calcular_rms
    """)
    return


@app.cell
def _(np):
    # Implementacion
    def calcular_rms(x):
        """Calcula el valor RMS (Root Mean Square) de una senal."""
        return np.sqrt(np.mean(x ** 2))

    # Tests
    def test_rms_ceros():
        x = np.zeros(100)
        assert calcular_rms(x) == 0.0
        print("test_rms_ceros: PASO")

    def test_rms_constante():
        x = np.ones(100)
        assert np.isclose(calcular_rms(x), 1.0)
        print("test_rms_constante: PASO")

    def test_rms_sinusoide():
        A = 2.0
        t = np.linspace(0, 1, 44100, endpoint=False)
        x = A * np.sin(2 * np.pi * 100 * t)
        esperado = A / np.sqrt(2)
        resultado = calcular_rms(x)
        assert np.isclose(resultado, esperado, rtol=0.01), f"Esperado {esperado:.4f}, obtenido {resultado:.4f}"
        print(f"test_rms_sinusoide: PASO (esperado={esperado:.4f}, obtenido={resultado:.4f})")

    def test_rms_negativo():
        x = -3 * np.ones(50)
        assert np.isclose(calcular_rms(x), 3.0)
        print("test_rms_negativo: PASO")

    def test_rms_largo_variable():
        for n in [10, 100, 1000, 10000]:
            x = np.ones(n)
            assert np.isclose(calcular_rms(x), 1.0)
        print("test_rms_largo_variable: PASO")

    # Ejecutar todos los tests
    test_rms_ceros()
    test_rms_constante()
    test_rms_sinusoide()
    test_rms_negativo()
    test_rms_largo_variable()
    print("\nTodos los tests pasaron!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Encontrar el bug

    La funcion `calcular_t30_buggy` tiene **dos bugs**:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Bug 1: `h**2[::-1]` vs `(h**2)[::-1]`**

    ```python
    edc = np.cumsum(h**2[::-1])[::-1]
    ```

    `h**2[::-1]` primero revierte h y luego eleva al cuadrado. El resultado es el mismo que `(h[::-1])**2` porque $(x^2) = (-x)^2$... asi que en realidad **este no es el bug** (es una trampa!).

    El verdadero problema es la **normalizacion**: usa `np.max(edc)` en vez de `edc[0]`.
    Como `edc[0]` ES el maximo (la integral de toda la energia), en este caso `np.max(edc) == edc[0]` y tampoco cambia... pero es conceptualmente incorrecto y puede fallar con senales ruidosas.

    **Bug 2: `t30 = 60 / m` (falta el signo negativo)**

    ```python
    t30 = 60 / m  # INCORRECTO
    t30 = -60 / m  # CORRECTO
    ```

    La pendiente `m` es **negativa** (la EDC decae). Si no ponemos el `-`, el T30 sale **negativo**.
    """)
    return


@app.cell
def _(np, plt):
    # Version corregida
    def calcular_t30_correcto(h, fs):
        """Calcula T30 a partir de una respuesta al impulso (version corregida)."""
        t = np.arange(len(h)) / fs

        # Integral de Schroeder (correcta)
        edc = np.cumsum(h[::-1]**2)[::-1]
        edc_db = 10 * np.log10(edc / edc[0] + 1e-12)

        # Regresion lineal entre -5 y -35 dB
        mask = (edc_db >= -35) & (edc_db <= -5)
        if np.sum(mask) < 2:
            return None
        m, b = np.polyfit(t[mask], edc_db[mask], 1)

        # T30 (con signo negativo!)
        t30 = -60 / m
        return t30

    # Verificar
    fs_corr = 44100
    t_corr = np.arange(3 * fs_corr) / fs_corr
    tau_corr = 2.0 / (6 * np.log(10))
    np.random.seed(42)
    h_corr = np.random.randn(len(t_corr)) * np.exp(-t_corr / tau_corr)

    t30_resultado = calcular_t30_correcto(h_corr, fs_corr)
    print(f"T30 corregido: {t30_resultado:.2f} s (esperado: ~2.0 s)")
    print(f"Error: {abs(t30_resultado - 2.0):.3f} s ({abs(t30_resultado - 2.0)/2.0*100:.1f}%)")

    # Comparar version buggy vs corregida visualmente
    edc_corr = np.cumsum(h_corr[::-1]**2)[::-1]
    edc_corr_db = 10 * np.log10(edc_corr / edc_corr[0] + 1e-12)

    fig_3, ax_3 = plt.subplots(figsize=(12, 5))
    ax_3.plot(t_corr, edc_corr_db, 'k-', linewidth=2, label='EDC')

    mask_reg = (edc_corr_db >= -35) & (edc_corr_db <= -5)
    m_corr, b_corr = np.polyfit(t_corr[mask_reg], edc_corr_db[mask_reg], 1)
    recta = m_corr * t_corr + b_corr
    mask_recta = (recta >= -70) & (recta <= 5)
    ax_3.plot(t_corr[mask_recta], recta[mask_recta], 'r--', linewidth=2,
              label=f'T30 = {t30_resultado:.2f} s')
    ax_3.axhline(-60, color='gray', linestyle='--', alpha=0.5)
    ax_3.set_xlabel('Tiempo (s)')
    ax_3.set_ylabel('EDC (dB)')
    ax_3.set_title('Ejercicio 3: Version corregida')
    ax_3.set_ylim(-70, 5)
    ax_3.legend()
    ax_3.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Configuracion de ruff (referencia)

    ```toml
    [tool.ruff]
    line-length = 100
    target-version = "py310"

    [tool.ruff.lint]
    select = [
        "E",    # errores de estilo (pycodestyle)
        "F",    # errores logicos (pyflakes)
        "I",    # imports ordenados (isort)
        "UP",   # modernizacion de sintaxis
    ]
    ignore = [
        "E501",  # lineas largas
    ]

    [tool.ruff.format]
    quote-style = "double"
    ```

    Comandos para ejecutar:
    ```bash
    ruff check tu_archivo.py
    ruff check --fix tu_archivo.py
    ruff format tu_archivo.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: GitHub Actions workflow (referencia)

    ```yaml
    name: CI

    on:
      push:
        branches: [main, develop]
      pull_request:
        branches: [main]

    jobs:
      lint-and-test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout codigo
            uses: actions/checkout@v4

          - name: Setup Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.10'

          - name: Instalar dependencias
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
              pip install ruff pytest

          - name: Lint con ruff
            run: ruff check .

          - name: Verificar formateo
            run: ruff format --check .

          - name: Ejecutar tests
            run: pytest tests/ -v
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Reflexion

    No hay una solucion unica. El objetivo es reflexionar honestamente sobre la experiencia con IA.

    Puntos a cubrir:
    - Ejemplos concretos de uso de IA en el TP
    - Al menos un error que la IA introdujo
    - Tareas donde la IA fue util vs donde no
    - Plan para el resto del TP

    La reflexion se evalua por profundidad y honestidad, no por longitud.
    """)
    return


if __name__ == "__main__":
    app.run()
