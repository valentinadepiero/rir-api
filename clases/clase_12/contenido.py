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
    ## Clase 12: Entrega 2 + Documentacion Moderna

    Hoy combinamos las presentaciones del **Milestone 2** con un tema fundamental para cualquier proyecto de software: la **documentacion**. Un proyecto sin documentacion es un proyecto que nadie puede usar, ni siquiera ustedes mismos en 6 meses.

    **Pilares**: P3 (principal), P2 (secundario)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Ecosistema de Documentacion Moderna

    La documentacion no es un unico documento: es un **ecosistema** con multiples niveles, cada uno con su proposito.

    ### La Piramide de Documentacion

    ```
                    /\
                   /  \
                  / UG  \        <- User Guides (guias de usuario)
                 /--------\
                / API Docs  \    <- Documentacion de API (auto-generada)
               /--------------\
              /     README      \  <- README del proyecto
             /--------------------\
            /     Docstrings       \  <- Docstrings en funciones/clases
           /--------------------------\
          /    Comentarios en codigo    \  <- Comentarios inline
         /------------------------------\
    ```

    ### Cuando usar cada nivel

    | Nivel | Que documenta | Audiencia | Ejemplo |
    |-------|--------------|-----------|---------|
    | Comentarios | El "por que" de decisiones no obvias | Desarrolladores del equipo | `# Usamos Butterworth por su respuesta plana en banda pasante` |
    | Docstrings | Que hace una funcion, parametros, retorno | Usuarios de la funcion | `'''Calcula el T60...'''` |
    | README | Vision general, instalacion, uso basico | Nuevos usuarios / evaluadores | Archivo en raiz del repo |
    | API Docs | Referencia completa de todas las funciones | Desarrolladores avanzados | Pagina web generada con pdoc |
    | User Guide | Tutoriales paso a paso, conceptos | Usuarios no tecnicos | Documentacion en GitHub Pages |

    ### Comentarios: comenten el POR QUE, no el QUE
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplos de comentarios buenos vs malos

    **MAL** - Comenta lo obvio:
    ```python
    # Incrementar i en 1
    i += 1

    # Calcular la media
    media = np.mean(datos)
    ```

    **BIEN** - Explica decisiones y contexto:
    ```python
    # Usamos filtro Butterworth orden 4 segun ISO 3382-1, seccion 5.3
    sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs, output='sos')

    # Truncamos la IR en -60 dB para evitar que el ruido de fondo
    # contamine el calculo de la integral de Schroeder
    idx_corte = np.argmax(edc_db < -60)
    ```

    **BIEN** - Documenta limitaciones conocidas:
    ```python
    # TODO: Esto falla para senales estereo, hay que agregar conversion a mono
    # Ver issue #23
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Docstrings en Practica

    Los docstrings son la forma estandar de documentar funciones, clases y modulos en Python. Nosotros usamos el estilo **NumPy**, que es el mas comun en el ecosistema cientifico.

    ### Anatomia de un docstring NumPy-style
    """)
    return


@app.cell
def _():
    import numpy as np

    def calcular_t60(edc, fs):
        """Calcula el tiempo de reverberacion T60 a partir de la EDC.

        El T60 se obtiene ajustando una recta por minimos cuadrados
        al rango de -5 dB a -35 dB de la curva de decaimiento
        energetico (metodo T30), y extrapolando a -60 dB.

        Parameters
        ----------
        edc : np.ndarray
            Curva de decaimiento energetico (Energy Decay Curve)
            en escala lineal. Debe estar normalizada (maximo = 1).
        fs : int
            Frecuencia de muestreo en Hz.

        Returns
        -------
        float
            Tiempo de reverberacion T60 en segundos.

        Raises
        ------
        ValueError
            Si la EDC no tiene suficiente rango dinamico (< 35 dB).

        Examples
        --------
        >>> import numpy as np
        >>> t = np.arange(44100) / 44100
        >>> h = np.exp(-6.908 * t)  # IR con T60 = 1 segundo
        >>> edc = np.cumsum(h[::-1]**2)[::-1]
        >>> edc = edc / edc[0]
        >>> t60 = calcular_t60(edc, 44100)
        >>> abs(t60 - 1.0) < 0.1
        True

        Notes
        -----
        Este metodo sigue la norma ISO 3382-1:2009, Anexo A.
        El T60 se calcula como T30 * 2, donde T30 es el tiempo
        que tarda la EDC en decaer de -5 dB a -35 dB.
        """
        edc_db = 10 * np.log10(edc / edc[0] + 1e-12)

        rango_dinamico = edc_db[0] - edc_db[-1]
        if rango_dinamico < 35:
            raise ValueError(
                f"Rango dinamico insuficiente: {rango_dinamico:.1f} dB. "
                f"Se necesitan al menos 35 dB para calcular T30."
            )

        idx_5 = np.argmax(edc_db < -5)
        idx_35 = np.argmax(edc_db < -35)

        t = np.arange(len(edc)) / fs
        coef = np.polyfit(t[idx_5:idx_35], edc_db[idx_5:idx_35], 1)

        t60 = -60 / coef[0]
        return t60

    # Demostrar el uso
    t_demo = np.arange(44100) / 44100
    h_demo = np.exp(-6.908 * t_demo)
    edc_demo = np.cumsum(h_demo[::-1]**2)[::-1]
    edc_demo = edc_demo / edc_demo[0]
    resultado = calcular_t60(edc_demo, 44100)
    f"T60 calculado: {resultado:.3f} s (esperado: ~1.0 s)"
    return (calcular_t60, edc_demo, np)


@app.cell
def _(mo):
    mo.md(r"""
    ### Secciones del docstring NumPy-style

    | Seccion | Obligatoria? | Contenido |
    |---------|-------------|-----------|
    | Descripcion corta | Si | Primera linea: que hace la funcion |
    | Descripcion larga | No | Detalles adicionales, contexto |
    | `Parameters` | Si (si hay params) | Nombre, tipo y descripcion de cada parametro |
    | `Returns` | Si (si retorna algo) | Tipo y descripcion del valor de retorno |
    | `Raises` | No | Excepciones que puede lanzar |
    | `Examples` | Recomendada | Ejemplos ejecutables (doctests) |
    | `Notes` | No | Referencias, formulas, detalles tecnicos |
    | `See Also` | No | Funciones relacionadas |

    ### Los docstrings se convierten en documentacion automaticamente

    ```python
    # En la terminal:
    # pdoc src/acoustipy/parametros.py
    # -> Genera una pagina HTML con toda la documentacion
    ```

    Herramientas como `pdoc`, `mkdocstrings` y `sphinx` leen los docstrings y generan documentacion web profesional.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. README como Documentacion

    El README.md es la **puerta de entrada** a su proyecto. Es lo primero que ve cualquier persona que visita el repositorio.

    ### Estructura recomendada para el TP
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```markdown
    # AcoustiPy - Analisis Acustico ISO 3382

    ![CI](https://github.com/usuario/acoustipy/actions/workflows/ci.yml/badge.svg)
    ![Python](https://img.shields.io/badge/python-3.10%2B-blue)
    ![License](https://img.shields.io/badge/license-MIT-green)

    Herramienta de analisis de parametros acusticos de salas a partir
    de respuestas al impulso, siguiendo la norma ISO 3382-1:2009.

    ## Caracteristicas

    - Carga y preprocesamiento de respuestas al impulso (.wav)
    - Filtrado en bandas de octava (125 Hz - 8 kHz)
    - Calculo de integral de Schroeder (EDC)
    - Parametros acusticos: EDT, T20, T30, T60, D50, C80
    - Visualizacion de resultados
    - Exportacion a JSON

    ## Instalacion

    ```bash
    git clone https://github.com/usuario/acoustipy.git
    cd acoustipy
    uv sync
    ```

    ## Uso rapido

    ```bash
    # Desde la linea de comandos
    acoustipy audio/sala_aula.wav --parametros T60 EDT C80

    # Desde Python
    from acoustipy import cargar_audio, calcular_parametros
    ir, fs = cargar_audio("audio/sala_aula.wav")
    resultados = calcular_parametros(ir, fs)
    ```

    ## Estructura del proyecto

    ```
    acoustipy/
    ├── src/acoustipy/
    │   ├── __init__.py
    │   ├── audio.py          # Carga y preprocesamiento
    │   ├── filtros.py         # Filtrado en bandas de octava
    │   ├── schroeder.py       # Integral de Schroeder
    │   ├── parametros.py      # Calculo de parametros acusticos
    │   ├── visualizacion.py   # Graficos
    │   └── main.py            # CLI y pipeline principal
    ├── tests/
    ├── docs/
    ├── pyproject.toml
    └── README.md
    ```

    ## API

    Ver la [documentacion completa](https://usuario.github.io/acoustipy/).

    ## Autores

    - Nombre Apellido - [GitHub](https://github.com/usuario)

    ## Licencia

    MIT License - ver [LICENSE](LICENSE)
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Badges (insignias)

    Las badges son indicadores visuales en la parte superior del README:

    - **CI Status**: muestra si los tests pasan (verde) o fallan (rojo)
    - **Python Version**: indica que versiones de Python son compatibles
    - **License**: tipo de licencia del proyecto
    - **Coverage**: porcentaje de codigo cubierto por tests

    Se generan con servicios como [shields.io](https://shields.io/) o directamente desde GitHub Actions.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Documentacion API Auto-generada

    ### pdoc: la opcion mas simple

    `pdoc` genera documentacion HTML a partir de los docstrings de su codigo. Es la forma mas rapida de tener documentacion profesional.

    ```bash
    # Instalar
    uv add pdoc

    # Generar documentacion
    pdoc src/acoustipy/ -o docs/api/

    # Vista previa en el navegador
    pdoc src/acoustipy/
    # -> Abre http://localhost:8080 con la documentacion
    ```

    ### mkdocs + mkdocstrings: mas personalizable

    Para proyectos mas grandes, `mkdocs` ofrece mas control sobre la estructura y el estilo.

    ```yaml
    # mkdocs.yml
    site_name: AcoustiPy
    theme:
      name: material  # tema profesional

    plugins:
      - search
      - mkdocstrings:
          handlers:
            python:
              options:
                docstring_style: numpy

    nav:
      - Inicio: index.md
      - Instalacion: instalacion.md
      - API:
        - Audio: api/audio.md
        - Filtros: api/filtros.md
        - Parametros: api/parametros.md
    ```

    ```markdown
    <!-- docs/api/parametros.md -->
    # Modulo parametros

    ::: acoustipy.parametros
    ```

    ```bash
    # Instalar
    uv add mkdocs mkdocs-material mkdocstrings[python]

    # Vista previa
    mkdocs serve

    # Construir
    mkdocs build  # genera sitio en site/
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. GitHub Pages

    GitHub Pages permite publicar documentacion web **gratis** directamente desde el repositorio.

    ### Opcion 1: Deploy manual

    ```bash
    # Construir la documentacion
    mkdocs build

    # Subir a la rama gh-pages
    mkdocs gh-deploy
    ```

    La documentacion estara disponible en: `https://usuario.github.io/acoustipy/`

    ### Opcion 2: Deploy automatico con GitHub Actions

    ```yaml
    # .github/workflows/docs.yml
    name: Deploy docs

    on:
      push:
        branches: [main]

    permissions:
      contents: write

    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4

          - name: Setup Python
            uses: actions/setup-python@v5
            with:
              python-version: "3.12"

          - name: Install dependencies
            run: |
              pip install mkdocs mkdocs-material mkdocstrings[python]

          - name: Build and deploy
            run: mkdocs gh-deploy --force
    ```

    Con este workflow, cada vez que hacen push a `main`, la documentacion se actualiza automaticamente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Quarto para Informes Tecnicos

    **Quarto** es una herramienta moderna para crear documentos tecnicos (informes, papers, presentaciones) que mezclan texto, codigo y resultados.

    ### Por que Quarto?

    - Combina Markdown + codigo ejecutable (Python, R, Julia)
    - Genera PDF, HTML, Word, presentaciones
    - Soporte nativo para ecuaciones LaTeX, figuras, tablas
    - Referencias bibliograficas automaticas
    - Mas moderno y simple que LaTeX puro

    ### Ejemplo basico

    ```markdown
    ---
    title: "Analisis Acustico de Sala"
    author: "Equipo 1"
    format: pdf
    bibliography: references.bib
    ---

    ## Introduccion

    Se analizo la respuesta al impulso de un aula utilizando
    la norma ISO 3382-1 [@iso3382].

    ## Resultados

    ```{python}
    import matplotlib.pyplot as plt
    # El codigo se ejecuta y la figura se incluye en el PDF
    plt.plot(t, edc_db)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Nivel [dB]")
    ```

    El T60 medido fue de $1.2 \pm 0.1$ s.
    ```

    Para mas detalles, consulten la guia completa en `guias/quarto_informe.md`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 7. IA para Documentacion (P2)

    La documentacion es una de las areas donde la IA puede ser **mas util**, porque es repetitiva y tiene patrones claros.

    ### Generar docstrings con IA

    **Prompt efectivo:**
    ```
    Genera un docstring en estilo NumPy para esta funcion Python.
    Incluye Parameters, Returns, Raises y Examples.
    El contexto es un proyecto de acustica de salas (ISO 3382).

    [pegar el codigo de la funcion]
    ```

    ### Generar README con IA

    **Prompt efectivo:**
    ```
    Genera un README.md para este proyecto Python.
    Es una herramienta de analisis acustico que calcula parametros
    de la norma ISO 3382 a partir de respuestas al impulso.
    Incluye: descripcion, instalacion, uso, estructura, licencia.
    La estructura del proyecto es:
    [pegar output de tree o ls]
    ```

    ### Advertencias importantes

    | Lo que la IA hace bien | Lo que la IA hace mal |
    |----------------------|---------------------|
    | Estructura y formato | Detalles tecnicos especificos |
    | Ejemplos genericos | Valores exactos y unidades |
    | Descripciones generales | Referencias a normas especificas |
    | Boilerplate repetitivo | Limitaciones y edge cases |

    **Regla de oro**: La IA genera el 80% del borrador, ustedes verifican y completan el 20% critico.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy aprendimos que la documentacion es un ecosistema con multiples niveles:

    1. **Comentarios**: explican el "por que" de decisiones no obvias
    2. **Docstrings**: documentan funciones con estilo NumPy
    3. **README**: puerta de entrada al proyecto
    4. **API Docs**: referencia auto-generada con pdoc o mkdocs
    5. **GitHub Pages**: publicacion gratuita de documentacion web
    6. **Quarto**: informes tecnicos profesionales
    7. **IA**: acelera la creacion de documentacion, pero requiere verificacion

    ### Para la proxima clase
    - Completar docstrings en todas las funciones del TP
    - Crear el README del proyecto
    - Generar documentacion API con pdoc
    """)
    return


if __name__ == "__main__":
    app.run()
