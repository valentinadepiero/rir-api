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
    # Senales y Sistemas - Clase 11
    ## Vibecoding en Profundidad

    **Fecha**: 9 de junio de 2026 | **Pilares**: P2 (principal), P3 (secundario)

    En esta clase vamos a:
    1. Entender que es el vibecoding y su espectro
    2. Identificar cuando conviene y cuando no
    3. Analizar riesgos del codigo generado por IA
    4. Aprender patrones efectivos de desarrollo con IA
    5. Configurar herramientas de calidad de codigo
    6. Implementar CI/CD con GitHub Actions
    7. Workshop: Schroeder con IA
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Que es el Vibecoding

    ### Definicion de Andrej Karpathy (2025)

    > "Vibecoding es un nuevo tipo de programacion donde te entregas al vibes,
    > abrazas lo exponencial, y te olvidas de que el codigo existe."

    ### El espectro del desarrollo con IA

    No es blanco o negro. Hay un espectro continuo:

    | Nivel | Descripcion | Ejemplo |
    |-------|------------|---------|
    | **0 - Manual** | Todo escrito a mano | Programacion clasica |
    | **1 - Autocompletado** | IA sugiere lineas | GitHub Copilot inline |
    | **2 - Asistido** | IA genera bloques, humano revisa | Chat + copiar/pegar |
    | **3 - Dirigido** | Humano da specs, IA implementa | Claude Code con specs |
    | **4 - Vibecoding** | Humano describe resultado, IA hace todo | "Haceme una app que..." |
    | **5 - Full autonomo** | IA decide que hacer | Agentes autonomos |

    ### Donde estamos en este curso?

    Apuntamos al **nivel 2-3**: la IA es una herramienta poderosa, pero el humano
    entiende el dominio (senales, acustica) y verifica el resultado.

    El **nivel 4-5** puede funcionar para prototipos rapidos, pero es riesgoso
    para codigo de produccion o de investigacion.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Cuando Vibecoding Funciona (y Cuando No)

    ### Bueno para vibecoding

    - **Boilerplate**: configuraciones, setup, archivos repetitivos
    - **Visualizaciones**: graficos con matplotlib, dashboards
    - **Scripts de una vez**: procesamiento batch, conversion de formatos
    - **Prototipos rapidos**: probar una idea antes de invertir tiempo
    - **Codigo estandar**: CRUD, parsers, adaptadores

    ### Malo para vibecoding

    - **Algoritmos criticos**: la integral de Schroeder DEBE ser correcta
    - **Codigo de seguridad**: autenticacion, encriptacion, sanitizacion
    - **Implementacion de normas**: IEC 61260 tiene tolerancias estrictas
    - **Codigo novedoso**: si no existe en el training data, la IA inventa
    - **Optimizacion de rendimiento**: la IA no entiende tu hardware

    ### Regla de oro

    > Si no podes verificar que el codigo es correcto, no uses vibecoding.
    > Si podes verificarlo pero te ahorra tiempo, usalo con cuidado.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Riesgos del Codigo Generado por IA

    ### 3.1 APIs inventadas (alucinaciones)

    La IA puede inventar funciones o parametros que no existen:

    ```python
    # La IA podria generar esto (INCORRECTO):
    from scipy.signal import octave_filter  # NO EXISTE
    resultado = octave_filter(senal, fc=1000, fs=44100)
    ```

    Siempre verificar en la documentacion oficial.

    ### 3.2 Bugs sutiles

    El codigo "parece" correcto pero tiene errores logicos:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Caso de estudio 1: Error en el calculo de Schroeder**
    """)
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(np):
    # ERROR SUTIL: Schroeder mal implementado
    def schroeder_MAL(h):
        """Implementacion INCORRECTA - error comun de IA."""
        # Error: cumsum en vez de cumsum reverso
        EDC = np.cumsum(h**2)
        EDC_dB = 10 * np.log10(EDC / EDC[-1] + 1e-12)
        return EDC_dB

    def schroeder_BIEN(h):
        """Implementacion CORRECTA."""
        EDC = np.cumsum(h[::-1]**2)[::-1]
        EDC_dB = 10 * np.log10(EDC / EDC[0] + 1e-12)
        return EDC_dB

    # Demo
    t_demo = np.linspace(0, 2, 88200)
    h_demo = np.random.randn(len(t_demo)) * np.exp(-t_demo / 0.3)

    edc_mal = schroeder_MAL(h_demo)
    edc_bien = schroeder_BIEN(h_demo)

    print("Schroeder MAL:  la curva SUBE en vez de bajar")
    print(f"  Primer valor: {edc_mal[0]:.1f} dB, ultimo: {edc_mal[-1]:.1f} dB")
    print("Schroeder BIEN: la curva BAJA desde 0 dB")
    print(f"  Primer valor: {edc_bien[0]:.1f} dB, ultimo: {edc_bien[-1]:.1f} dB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Caso de estudio 2: Filtro con frecuencias invertidas**

    ```python
    # ERROR: frecuencias al reves en el filtro
    sos = signal.butter(4, [f_high, f_low], btype='band', fs=fs, output='sos')
    # No da error, pero el filtro es incorrecto!
    ```

    **Caso de estudio 3: Normalizacion olvidada en FFT**

    ```python
    # ERROR: olvidar normalizar por N
    magnitud = np.abs(np.fft.rfft(x))  # Escala con N!
    # CORRECTO:
    magnitud = np.abs(np.fft.rfft(x)) / len(x) * 2
    ```

    ### 3.3 Seguridad y licencias

    - Codigo generado puede tener vulnerabilidades conocidas
    - Puede reproducir codigo con licencias restrictivas (GPL, etc.)
    - Nunca poner datos sensibles en prompts a la IA

    ### 3.4 Sesgo de confianza

    El mayor riesgo: **confiar en el codigo porque "la IA lo hizo"**.
    La IA genera codigo con mucha confianza, pero eso no significa que sea correcto.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Patrones Efectivos de Desarrollo con IA

    ### Patron 1: Spec First (Especificacion primero)

    Antes de pedir codigo, escribir una especificacion clara:

    ```
    Funcion: filtro_octava(x, fc, fs, orden=4)

    Parametros:
    - x: senal de entrada (array 1D)
    - fc: frecuencia central de la banda (Hz)
    - fs: frecuencia de muestreo (Hz)
    - orden: orden del filtro Butterworth (default 4)

    Retorna:
    - senal filtrada (mismo largo que x)

    Comportamiento:
    - Calcula f_low = fc / sqrt(2), f_high = fc * sqrt(2)
    - Disena filtro Butterworth pasa-banda con scipy.signal.butter (output='sos')
    - Aplica con sosfilt
    - Si f_high >= fs/2, ajustar a fs/2 - 1
    ```

    ### Patron 2: Test First (Tests primero)

    Escribir los tests antes de pedir la implementacion:

    ```python
    def test_filtro_octava():
        fs = 44100
        t = np.arange(fs) / fs  # 1 segundo
        # Un tono en la banda deberia pasar
        tono_dentro = np.sin(2 * np.pi * 1000 * t)
        filtrado = filtro_octava(tono_dentro, fc=1000, fs=fs)
        assert np.max(np.abs(filtrado)) > 0.5  # no atenua mucho

        # Un tono fuera de la banda deberia ser atenuado
        tono_fuera = np.sin(2 * np.pi * 5000 * t)
        filtrado_fuera = filtro_octava(tono_fuera, fc=1000, fs=fs)
        assert np.max(np.abs(filtrado_fuera)) < 0.1  # atenua mucho
    ```

    ### Patron 3: Review Always (Revisar siempre)

    - Leer **cada linea** del codigo generado
    - Verificar imports, parametros, logica
    - Ejecutar con datos conocidos
    - Comparar con implementaciones de referencia

    ### Patron 4: Iterate (Iterar)

    Si el primer resultado no es correcto:
    1. Explicar que esta mal y por que
    2. Dar el error o resultado incorrecto
    3. Pedir correccion especifica
    4. No empezar de cero cada vez

    ### Patron 5: Context Management (Gestionar contexto)

    - Dar contexto relevante (que librerias usar, que estilo de codigo)
    - No asumir que la IA recuerda conversaciones anteriores
    - Ser explicito sobre restricciones y requisitos
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Herramientas de Calidad de Codigo: Ruff

    ### Que es Ruff?

    **Ruff** es un linter y formateador de Python ultrarapido (escrito en Rust).
    Reemplaza a flake8, isort, black, y mas.

    ### Instalacion

    ```bash
    pip install ruff
    ```

    ### Comandos principales

    ```bash
    # Verificar errores de estilo y logica
    ruff check .

    # Corregir automaticamente
    ruff check --fix .

    # Formatear codigo (como black)
    ruff format .
    ```

    ### Configuracion en pyproject.toml

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
        "B",    # bugs comunes (flake8-bugbear)
        "SIM",  # simplificaciones
    ]
    ignore = [
        "E501",  # lineas largas (a veces necesarias)
    ]

    [tool.ruff.format]
    quote-style = "double"
    ```

    ### Type hints

    Las anotaciones de tipo ayudan a documentar y verificar el codigo:

    ```python
    import numpy as np
    from numpy.typing import NDArray

    def schroeder(h: NDArray[np.float64], fs: int) -> NDArray[np.float64]:
        '''Calcula la integral de Schroeder (EDC) en dB.'''
        edc = np.cumsum(h[::-1]**2)[::-1]
        return 10 * np.log10(edc / edc[0] + 1e-12)
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. GitHub Actions: CI/CD

    ### Que es CI/CD?

    - **CI (Continuous Integration)**: ejecutar tests y checks automaticamente en cada push/PR
    - **CD (Continuous Deployment)**: desplegar automaticamente si todo pasa

    Para el TP, nos interesa CI: que cada push verifique que el codigo es correcto.

    ### Archivo de workflow

    Crear `.github/workflows/ci.yml`:

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
              pip install -r requirements.txt
              pip install ruff pytest

          - name: Lint con ruff
            run: ruff check .

          - name: Formateo con ruff
            run: ruff format --check .

          - name: Tests
            run: pytest tests/ -v
    ```

    ### Como funciona

    1. Haces `git push` o abris un Pull Request
    2. GitHub ejecuta el workflow automaticamente
    3. Si algo falla, ves un :x: rojo en el PR
    4. Si todo pasa, ves un :white_check_mark: verde

    ### Leer resultados

    - En la pagina del PR o commit, click en "Checks" o "Actions"
    - Ver logs de cada paso
    - Si falla el lint: corregir el estilo
    - Si fallan los tests: hay un bug
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 7. Workshop: Implementar Schroeder con IA

    ### Objetivo

    Cada grupo va a implementar la funcion `integral_schroeder` usando un agente de IA (Claude Code o similar).

    ### Especificacion

    ```
    Funcion: integral_schroeder(h, fs)

    Parametros:
        h: respuesta al impulso (numpy array 1D, float64)
        fs: frecuencia de muestreo (int, Hz)

    Retorna:
        dict con:
            - 'edc_db': EDC normalizada en dB (numpy array)
            - 't': eje de tiempo en segundos (numpy array)
            - 'T30': tiempo de reverberacion T30 en segundos (float)
            - 'EDT': early decay time en segundos (float)

    Requisitos:
        - EDC calculada con integral de Schroeder (cumsum inverso de h^2)
        - T30: regresion lineal de EDC entre -5 y -35 dB, extrapolado a -60
        - EDT: regresion lineal de EDC entre 0 y -10 dB, extrapolado a -60
        - Si no se puede calcular (rango insuficiente), retornar None
    ```

    ### Pasos del workshop

    1. **Escribir tests** para la funcion (10 min)
    2. **Pedir a la IA** que implemente la funcion (5 min)
    3. **Verificar** que pasa los tests (5 min)
    4. **Comparar** implementaciones entre grupos (10 min)
    5. **Discutir** diferencias y errores encontrados (10 min)

    ### Tests sugeridos

    ```python
    def test_schroeder_basico():
        fs = 44100
        t = np.arange(3 * fs) / fs
        tau = 2.0 / (6 * np.log(10))
        h = np.random.randn(len(t)) * np.exp(-t / tau)
        resultado = integral_schroeder(h, fs)
        assert 'edc_db' in resultado
        assert 'T30' in resultado
        assert resultado['T30'] is not None
        assert abs(resultado['T30'] - 2.0) < 0.2  # tolerancia 10%

    def test_schroeder_edc_decae():
        fs = 44100
        t = np.arange(2 * fs) / fs
        h = np.random.randn(len(t)) * np.exp(-t / 0.1)
        resultado = integral_schroeder(h, fs)
        # EDC debe empezar en 0 dB y bajar
        assert resultado['edc_db'][0] > -0.1
        assert resultado['edc_db'][-1] < resultado['edc_db'][0]
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplo de implementacion (referencia del docente)

    Esta es una implementacion de referencia. Los alumnos deben llegar a algo similar usando IA:
    """)
    return


@app.cell
def _(np):
    def integral_schroeder(h, fs):
        """
        Calcula la integral de Schroeder y parametros acusticos.

        Parametros:
            h: respuesta al impulso (numpy array 1D)
            fs: frecuencia de muestreo (int)

        Retorna:
            dict con 'edc_db', 't', 'T30', 'EDT'
        """
        t = np.arange(len(h)) / fs

        # Integral de Schroeder (cumsum inverso de h^2)
        h2 = h ** 2
        edc = np.cumsum(h2[::-1])[::-1]
        edc_db = 10 * np.log10(edc / edc[0] + 1e-12)

        def _regresion(edc_db_arr, t_arr, db_inicio, db_fin):
            """Regresion lineal en un rango de dB."""
            mask = (edc_db_arr >= db_fin) & (edc_db_arr <= db_inicio)
            if np.sum(mask) < 2:
                return None
            m, _ = np.polyfit(t_arr[mask], edc_db_arr[mask], 1)
            if m >= 0:
                return None
            return -60.0 / m

        T30 = _regresion(edc_db, t, -5, -35)
        EDT = _regresion(edc_db, t, 0, -10)

        return {
            'edc_db': edc_db,
            't': t,
            'T30': T30,
            'EDT': EDT,
        }

    # Verificacion rapida
    fs_test = 44100
    t_test = np.arange(3 * fs_test) / fs_test
    tau_test = 2.0 / (6 * np.log(10))
    np.random.seed(42)
    h_test = np.random.randn(len(t_test)) * np.exp(-t_test / tau_test)

    res_test = integral_schroeder(h_test, fs_test)
    print(f"T30: {res_test['T30']:.2f} s (esperado: ~2.0 s)")
    print(f"EDT: {res_test['EDT']:.2f} s (esperado: ~2.0 s)")
    print(f"EDC empieza en: {res_test['edc_db'][0]:.1f} dB (esperado: 0.0)")
    print(f"Test pasado: {abs(res_test['T30'] - 2.0) < 0.2}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    | Tema | Punto clave |
    |------|------------|
    | Vibecoding | Espectro de niveles, no binario |
    | Cuando usar | Boilerplate si, algoritmos criticos no |
    | Riesgos | APIs falsas, bugs sutiles, confianza excesiva |
    | Patrones | Spec first, test first, review always |
    | Ruff | Linter + formateador rapido |
    | CI/CD | GitHub Actions para verificar automaticamente |
    | Workshop | Implementar con IA, verificar, comparar |

    ### Para la proxima clase
    Vamos a avanzar con el TP, aplicando todo lo aprendido sobre procesamiento de RI y herramientas de desarrollo.
    """)
    return


if __name__ == "__main__":
    app.run()
