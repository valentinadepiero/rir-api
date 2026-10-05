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
    # Clase 12: Ejercicios
    ## Documentacion Moderna

    Estos ejercicios se enfocan en documentar su proyecto de forma profesional. La documentacion es tan importante como el codigo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 1: Docstrings NumPy-style

    Tomen **3 funciones** de su codigo del TP y escriban docstrings completos en estilo NumPy.

    Cada docstring debe incluir:
    - Descripcion corta (1 linea)
    - Descripcion larga (opcional, pero recomendada)
    - `Parameters`: nombre, tipo y descripcion de cada parametro
    - `Returns`: tipo y descripcion del valor de retorno
    - `Raises`: excepciones que puede lanzar
    - `Examples`: al menos un ejemplo ejecutable

    **Pista**: Empiecen por las funciones mas importantes de su proyecto (cargar_audio, calcular_t60, filtrar_banda_octava).
    """)
    return


@app.cell
def _():
    # Ejercicio 1: Espacio para escribir sus docstrings
    # Ejemplo de estructura (reemplacen con sus funciones reales):

    import numpy as np

    def mi_funcion_1():
        """[Escribir docstring completo aqui]

        Parameters
        ----------

        Returns
        -------

        Raises
        ------

        Examples
        --------
        """
        pass

    def mi_funcion_2():
        """[Escribir docstring completo aqui]"""
        pass

    def mi_funcion_3():
        """[Escribir docstring completo aqui]"""
        pass
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 2: README.md completo

    Escriban un **README.md completo** para su proyecto del TP siguiendo la estructura vista en clase:

    1. Titulo + badges (CI, Python version, license)
    2. Descripcion breve (2-3 oraciones)
    3. Caracteristicas principales (lista)
    4. Instalacion (paso a paso)
    5. Uso rapido (ejemplo de CLI y de Python)
    6. Estructura del proyecto (arbol de directorios)
    7. API (link a la documentacion o resumen)
    8. Autores
    9. Licencia

    **Pista**: Pueden escribirlo primero aca como texto y despues copiarlo a su repositorio.
    """)
    return


@app.cell
def _():
    # Ejercicio 2: Escriban el contenido de su README aca
    readme_contenido = """
    # [Nombre del Proyecto]

    ![CI](https://github.com/usuario/proyecto/actions/workflows/ci.yml/badge.svg)

    [Descripcion breve del proyecto]

    ## Caracteristicas
    - [caracteristica 1]
    - [caracteristica 2]

    ## Instalacion
    ```bash
    git clone https://github.com/usuario/proyecto.git
    cd proyecto
    uv sync
    ```

    ## Uso
    [ejemplos de uso]

    ## Estructura
    [arbol de directorios]

    ## Autores
    - [nombres]

    ## Licencia
    MIT
    """
    print(readme_contenido)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 3: Generar documentacion API con pdoc

    Generen documentacion API para su proyecto usando `pdoc`:

    1. Instalen pdoc: `uv add pdoc`
    2. Ejecuten: `pdoc src/nombre_proyecto/`
    3. Naveguen la documentacion generada en el navegador
    4. Tomen un screenshot del resultado

    **Preguntas para responder:**
    - Se generaron correctamente todas las funciones?
    - Los docstrings se ven bien formateados?
    - Falta documentar alguna funcion?
    """)
    return


@app.cell
def _():
    # Ejercicio 3: Anoten sus observaciones
    observaciones_pdoc = """
    Resultado de generar documentacion con pdoc:

    1. Funciones documentadas correctamente: [listar]
    2. Funciones sin docstring: [listar]
    3. Problemas encontrados: [describir]
    4. Mejoras necesarias: [describir]
    """
    print(observaciones_pdoc)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 4: IA para docstrings

    Pidan a una IA que genere docstrings para **una de sus funciones**.

    1. Copien el codigo de la funcion (sin docstring)
    2. Usen este prompt:
       ```
       Genera un docstring en estilo NumPy para esta funcion Python.
       Incluye Parameters, Returns, Raises y Examples.
       El contexto es analisis acustico de salas (ISO 3382).
       [pegar codigo]
       ```
    3. Comparen el docstring generado por IA con el que escribieron manualmente

    **Preguntas para responder:**
    - Que hizo bien la IA?
    - Que hizo mal o de forma incompleta?
    - Usarian el docstring generado directamente o lo modificarian?
    """)
    return


@app.cell
def _():
    # Ejercicio 4: Comparacion
    comparacion_ia = """
    Funcion analizada: [nombre]

    Docstring manual:
    [pegar su docstring]

    Docstring generado por IA:
    [pegar el docstring de la IA]

    Comparacion:
    - Lo que la IA hizo bien: [describir]
    - Lo que la IA hizo mal: [describir]
    - Conclusion: [usarian el de la IA? por que?]
    """
    print(comparacion_ia)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 5: Configuracion minima de mkdocs

    Configuren **mkdocs** para su proyecto:

    1. Instalen: `uv add mkdocs mkdocs-material mkdocstrings[python]`
    2. Creen el archivo `mkdocs.yml` en la raiz del proyecto
    3. Creen `docs/index.md` con una pagina de inicio
    4. Ejecuten: `mkdocs serve`
    5. Verifiquen que funciona en http://localhost:8000

    **Pista**: Usen la configuracion mostrada en clase como punto de partida.
    """)
    return


@app.cell
def _():
    # Ejercicio 5: Configuracion de mkdocs
    mkdocs_config = """
    # mkdocs.yml
    site_name: [Nombre del Proyecto]
    theme:
      name: material

    plugins:
      - search
      - mkdocstrings:
          handlers:
            python:
              options:
                docstring_style: numpy

    nav:
      - Inicio: index.md
      - API:
        - Audio: api/audio.md
        - Parametros: api/parametros.md
    """

    index_md = """
    # [Nombre del Proyecto]

    Bienvenidos a la documentacion de [nombre].

    ## Inicio rapido

    [instrucciones basicas]
    """

    print("mkdocs.yml:")
    print(mkdocs_config)
    print("\ndocs/index.md:")
    print(index_md)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 6: Diagrama de arquitectura con Mermaid

    Escriban la seccion "Arquitectura" de su README con un **diagrama Mermaid** que muestre como se conectan los modulos de su proyecto.

    **Ejemplo de sintaxis Mermaid:**

    ````markdown
    ```mermaid
    graph LR
        A[Audio .wav] --> B[Preprocesamiento]
        B --> C[Filtro Octava]
        C --> D[Integral Schroeder]
        D --> E[Parametros Acusticos]
        E --> F[JSON]
        E --> G[Graficos]
    ```
    ````

    GitHub renderiza Mermaid automaticamente en los archivos .md.

    **Pista**: Incluyan los modulos principales, las dependencias entre ellos, y los formatos de entrada/salida.
    """)
    return


@app.cell
def _():
    # Ejercicio 6: Escriban su diagrama Mermaid aca
    diagrama_mermaid = """
    ```mermaid
    graph LR
        A[...] --> B[...]
        B --> C[...]
        C --> D[...]
    ```
    """
    print("Diagrama Mermaid para el README:")
    print(diagrama_mermaid)
    return


if __name__ == "__main__":
    app.run()
