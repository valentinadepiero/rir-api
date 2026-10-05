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
    # Clase 11: Ejercicios Practicos
    ## Vibecoding en Profundidad

    Estos ejercicios combinan programacion con reflexion sobre el uso de IA.
    Algunos requieren usar una herramienta de IA (ChatGPT, Claude, etc.) como parte del ejercicio.
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

    **Parte A**: Escribi la especificacion completa para una funcion `filtro_octava(x, fc, fs, orden=4)`:
    - Que hace
    - Parametros (con tipos y rangos validos)
    - Que retorna
    - Casos borde (que pasa si fc es muy alta?)
    - Ejemplo de uso

    **Parte B**: Pedi a una IA que implemente la funcion usando tu especificacion.

    **Parte C**: Implementa la funcion vos mismo sin IA.

    **Parte D**: Compara ambas implementaciones. Son iguales? Alguna tiene errores?
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu especificacion (Parte A)
    # Escribila como un docstring o comentarios

    # Parte B: Pega aca la implementacion de la IA


    # Parte C: Tu implementacion manual


    # Parte D: Comparacion
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Test First - calcular_rms

    **Parte A**: Escribi tests para una funcion `calcular_rms(x)` que calcula el valor RMS de una senal:

    Tests sugeridos:
    - RMS de un array de ceros deberia ser 0
    - RMS de [1, 1, 1, 1] deberia ser 1.0
    - RMS de una sinusoide de amplitud A deberia ser A/sqrt(2)
    - Deberia funcionar con arrays de distintos largos

    **Parte B**: Pedi a una IA que implemente la funcion para que pase tus tests.

    **Parte C**: Verifica que la implementacion pasa todos los tests.
    """)
    return


@app.cell
def _(np):
    # EJERCICIO 2 - Parte A: Escribi los tests
    def test_rms_ceros():
        """RMS de ceros debe ser 0."""
        x = np.zeros(100)
        # assert calcular_rms(x) == 0.0
        pass

    def test_rms_constante():
        """RMS de array constante debe ser ese valor."""
        x = np.ones(100)
        # assert np.isclose(calcular_rms(x), 1.0)
        pass

    def test_rms_sinusoide():
        """RMS de sinusoide de amplitud A debe ser A/sqrt(2)."""
        A = 2.0
        t = np.linspace(0, 1, 44100, endpoint=False)
        x = A * np.sin(2 * np.pi * 100 * t)
        # assert np.isclose(calcular_rms(x), A / np.sqrt(2), rtol=0.01)
        pass

    # Parte B: Pega aca la implementacion de la IA


    # Parte C: Ejecuta los tests
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Encontrar el bug

    El siguiente codigo fue "generado por IA" y tiene un bug sutil.
    Tu tarea: encontrar el bug, explicar por que es incorrecto, y corregirlo.

    Pista: proba con una RI sintetica de T60 conocido y verifica el resultado.
    """)
    return


@app.cell
def _(np):
    # Codigo "generado por IA" con bug sutil
    def calcular_t30_buggy(h, fs):
        """Calcula T30 a partir de una respuesta al impulso."""
        t = np.arange(len(h)) / fs

        # Integral de Schroeder
        edc = np.cumsum(h**2[::-1])[::-1]  # BUG: h**2[::-1] vs (h[::-1])**2... o hay otro?
        edc_db = 10 * np.log10(edc / np.max(edc) + 1e-12)

        # Regresion lineal entre -5 y -35 dB
        mask = (edc_db >= -35) & (edc_db <= -5)
        m, b = np.polyfit(t[mask], edc_db[mask], 1)

        # T30
        t30 = 60 / m  # Deberia ser -60/m?
        return t30

    # Proba aca con una RI sintetica
    fs_bug = 44100
    t_bug = np.arange(3 * fs_bug) / fs_bug
    tau_bug = 2.0 / (6 * np.log(10))
    np.random.seed(42)
    h_bug = np.random.randn(len(t_bug)) * np.exp(-t_bug / tau_bug)

    t30_buggy = calcular_t30_buggy(h_bug, fs_bug)
    print(f"T30 calculado: {t30_buggy:.2f} s (esperado: ~2.0 s)")
    print(f"Es correcto? {'Si' if abs(t30_buggy - 2.0) < 0.2 else 'NO - hay un bug!'}")

    # EJERCICIO: Identifica y corrige el/los bug(s)
    # Tu version corregida aca:
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Configurar ruff

    Crea un archivo `pyproject.toml` con la configuracion de ruff para tu TP.

    Requisitos:
    - Line length: 100
    - Target version: Python 3.10
    - Reglas: E (errores), F (logica), I (imports), UP (modernizacion)
    - Ignorar E501 (lineas largas)
    - Quote style: double

    Luego ejecuta `ruff check` sobre alguno de tus archivos del TP y corrige los errores.

    Escribe abajo la configuracion y los resultados de ejecutar ruff.
    """)
    return


@app.cell
def _(mo):
    # EJERCICIO 4: Tu configuracion pyproject.toml
    mo.md(r"""
    ```toml
    # Escribe tu configuracion aca
    [tool.ruff]

    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: GitHub Actions workflow

    Escribe un archivo de workflow de GitHub Actions para el TP de tu grupo.

    El workflow debe:
    1. Ejecutarse en push a main y en pull requests
    2. Usar Python 3.10
    3. Instalar dependencias de requirements.txt
    4. Ejecutar `ruff check .`
    5. Ejecutar `ruff format --check .`
    6. Ejecutar `pytest tests/ -v`

    Escribe el contenido del archivo `.github/workflows/ci.yml` abajo.
    """)
    return


@app.cell
def _(mo):
    # EJERCICIO 5: Tu workflow
    mo.md(r"""
    ```yaml
    # Escribe tu workflow aca
    name: CI

    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Reflexion - Diario de desarrollo con IA

    Escribe una entrada de **200 palabras** en tu diario de desarrollo reflexionando sobre:

    1. Como usaste IA en el TP hasta ahora
    2. Algun error que la IA introdujo y como lo detectaste
    3. En que tareas la IA te ayudo mas
    4. En que tareas preferis trabajar sin IA
    5. Como vas a usar IA en el resto del TP

    Esta reflexion es parte de la evaluacion del Pilar 2 (IA para ingenieria).
    """)
    return


@app.cell
def _(mo):
    # EJERCICIO 6: Tu reflexion
    mo.md(r"""
    **Diario de desarrollo con IA - Entrada del [fecha]**

    [Escribe tu reflexion aca - minimo 200 palabras]


    """)
    return


if __name__ == "__main__":
    app.run()
