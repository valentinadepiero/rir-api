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
    ## Clase 15: Demo Day

    Bienvenidos al **Demo Day**! Hoy es el dia de mostrar todo lo que construyeron durante el cuatrimestre.

    **Pilares**: P3 (principal)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Agenda

    | Horario | Actividad |
    |---------|-----------|
    | 15:00 - 17:30 | Presentaciones finales (20 min + 5 min Q&A por grupo) |
    | 17:30 - 18:00 | Retrospectiva del curso y cierre |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Criterios de Evaluacion

    | Criterio | Peso | Que se evalua |
    |----------|:----:|---------------|
    | **Aspectos tecnicos** | 40% | Correctitud de los parametros, calidad del codigo, tests, CI, manejo de errores |
    | **Comunicacion** | 35% | Claridad de la presentacion, calidad del informe, documentacion, README |
    | **Analisis critico** | 25% | Validacion contra REW, analisis de errores, reflexion IA, conclusiones |

    ### Aspectos tecnicos (40%)
    - Los parametros acusticos se calculan correctamente?
    - El codigo esta bien organizado y es legible?
    - Hay tests y pasan?
    - El CI esta configurado?
    - Se manejan los errores adecuadamente?

    ### Comunicacion (35%)
    - La presentacion es clara y bien estructurada?
    - El informe tiene todas las secciones requeridas?
    - La documentacion (README, docstrings, API) es completa?
    - Las figuras y tablas son profesionales?

    ### Analisis critico (25%)
    - Se comparo con software de referencia (REW)?
    - Se analizaron las diferencias y sus posibles causas?
    - El log de IA muestra reflexion genuina?
    - Las conclusiones identifican limitaciones y trabajo futuro?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Retrospectiva del Curso

    Despues de las presentaciones, hagamos una retrospectiva grupal.

    ### Preguntas para reflexionar

    **Sobre el proyecto:**
    - Que fue lo mas valioso que aprendieron desarrollando el TP?
    - Que fue lo mas dificil?
    - Que harian diferente si empezaran de nuevo?

    **Sobre los 3 pilares:**
    - **P1 (Senales y Sistemas)**: Que conceptos de la teoria les resultaron mas utiles en la practica?
    - **P2 (IA como herramienta)**: Como cambio la IA su forma de programar? La seguirian usando?
    - **P3 (Ingenieria de software)**: Que practica de ingenieria de software les parece mas valiosa? (Git, testing, CI, documentacion, etc.)

    **Sobre la carrera:**
    - Como aplicarian lo aprendido en su carrera profesional?
    - Que habilidades sienten que desarrollaron mas alla de lo tecnico?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Feedback del Curso

    Su opinion nos ayuda a mejorar el curso para el proximo cuatrimestre.

    ### Preguntas para el feedback anonimo

    1. **Contenido**: Que temas fueron los mas utiles? Cuales fueron los menos utiles? Que temas agregarian?

    2. **Formato**: Las clases practicas con notebooks fueron efectivas? Que mejorarian del formato?

    3. **TP integrador**: El proyecto grupal fue una buena forma de aprender? La dificultad fue adecuada?

    4. **Herramientas**: Fue util aprender Git, pytest, CI/CD? Que otras herramientas les gustaria aprender?

    5. **IA**: El enfoque de usar IA como herramienta fue apropiado? Que cambiarian?

    6. **Ritmo**: El ritmo del curso fue adecuado? Muy rapido? Muy lento?

    7. **General**: Que nota le pondrian al curso (1-10)? Por que?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Recursos para Seguir Aprendiendo

    El curso termina, pero el aprendizaje no. Aca tienen recursos para profundizar en cada area.

    ### Senales y Sistemas
    - **Libro**: Oppenheim & Willsky - "Signals and Systems" (el clasico)
    - **Libro**: Steven W. Smith - "The Scientist and Engineer's Guide to DSP" (gratuito online)
    - **Online**: [scipy-lectures.org](https://scipy-lectures.org/) - Tutoriales de Python cientifico
    - **Curso**: MIT OpenCourseWare 6.003 - Signals and Systems

    ### Python Cientifico
    - **Online**: [Real Python](https://realpython.com/) - Tutoriales de Python de alta calidad
    - **Libro**: Jake VanderPlas - "Python Data Science Handbook" (gratuito online)
    - **Documentacion**: [NumPy](https://numpy.org/doc/), [SciPy](https://docs.scipy.org/), [Matplotlib](https://matplotlib.org/stable/)

    ### Ingenieria de Software
    - **Libro**: "Clean Code" de Robert C. Martin
    - **Online**: [git-scm.com/book](https://git-scm.com/book/) - Pro Git (gratuito)
    - **Practica**: Contribuir a proyectos open source en GitHub

    ### Audio y Acustica
    - **Software**: [REW](https://www.roomeqwizard.com/), [Audacity](https://www.audacityteam.org/)
    - **Norma**: ISO 3382-1:2009 (medir parametros acusticos)
    - **Comunidad**: Audio Engineering Society (AES)

    ### Proximos pasos sugeridos
    1. Seguir usando **Git** en todos sus proyectos (no solo los de la facultad)
    2. Escribir **tests** para su codigo (es un habito que se aprende practicando)
    3. Usar **IA** como herramienta, pero siempre verificar y entender el codigo
    4. Documentar sus proyectos (su yo del futuro se lo va a agradecer)
    5. Explorar **DSP** y **audio programming** si les intereso la tematica
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Cierre

    Gracias por su participacion y esfuerzo durante todo el cuatrimestre.

    Recuerden: lo mas valioso que se llevan no es solo el conocimiento tecnico, sino la **metodologia de trabajo** y el **pensamiento critico** que desarrollaron.

    **Exitos en lo que viene!**
    """)
    return


if __name__ == "__main__":
    app.run()
