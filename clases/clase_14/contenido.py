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
    ## Clase 14: Pulido y Preparacion

    Esta es la **ultima clase antes del Demo Day**. Hoy nos enfocamos en tres cosas: escribir un informe tecnico profesional, preparar una presentacion efectiva, y validar los resultados de su proyecto.

    **Pilares**: P3 (principal), P2 (secundario)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. Escribir un Informe Tecnico

    El informe tecnico es la **documentacion formal** de su trabajo. No es un tutorial ni un manual: es un documento que explica **que hicieron, como lo hicieron, y que resultados obtuvieron**.

    ### Estructura del informe

    | Seccion | % del informe | Contenido |
    |---------|:------------:|-----------|
    | Abstract | 5% | Resumen completo en ~150 palabras |
    | Introduccion | 10% | Contexto, objetivos, alcance |
    | Marco teorico | 10% | Conceptos necesarios (breve, no copiar libros) |
    | Metodologia | 25% | Como se implemento: arquitectura, algoritmos, decisiones |
    | Resultados | 30% | Datos, tablas, graficos, comparaciones |
    | Conclusiones | 20% | Analisis critico, limitaciones, trabajo futuro |
    | Referencias | - | Normas, libros, papers citados |
    | Anexo: Log IA | - | Registro del uso de IA en el desarrollo |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### El Abstract

    El abstract es lo **mas importante** del informe porque es lo unico que muchas personas van a leer. Debe responder en 150 palabras:

    1. **Que** se hizo (objetivo)
    2. **Como** se hizo (metodologia, en una oracion)
    3. **Que** se obtuvo (resultado principal)
    4. **Que** significa (conclusion principal)

    **Ejemplo:**

    > Se desarrollo una herramienta en Python para el calculo de parametros acusticos
    > de salas a partir de respuestas al impulso, siguiendo la norma ISO 3382-1:2009.
    > La herramienta implementa filtrado en bandas de octava, calculo de la integral de
    > Schroeder, y extraccion de parametros EDT, T20, T30, T60, D50 y C80. Se valido
    > contra el software comercial REW utilizando tres respuestas al impulso de espacios
    > con diferentes caracteristicas acusticas. Los resultados muestran una diferencia
    > maxima de 0.15 s en T60 y 1.2 dB en C80 respecto a los valores de referencia,
    > dentro de los margenes aceptables segun la norma. El codigo fuente esta disponible
    > como paquete Python instalable con documentacion completa y tests automatizados.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Introduccion

    La introduccion debe:
    - Contextualizar el problema (por que importa la acustica de salas)
    - Definir el objetivo del trabajo
    - Describir el alcance (que se incluye y que no)
    - Mencionar brevemente la metodologia
    - Describir la estructura del informe

    **NO debe:**
    - Incluir resultados
    - Ser demasiado larga (1-2 paginas maximo)
    - Copiar texto de Wikipedia o libros
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Metodologia

    La seccion mas tecnica. Debe explicar **como** implementaron la solucion:

    1. **Arquitectura del software**: diagrama de modulos y sus relaciones
    2. **Algoritmos clave**: como calculan cada parametro (con ecuaciones)
    3. **Decisiones de diseno**: por que eligieron Butterworth y no Chebyshev, por que T30 y no T20, etc.
    4. **Herramientas utilizadas**: Python, NumPy, SciPy, pytest, etc.

    **Incluir diagramas:**

    ```
    ┌─────────┐    ┌──────────┐    ┌───────────┐    ┌────────────┐
    │  Audio   │───>│ Filtrado │───>│ Schroeder │───>│ Parametros │
    │  (.wav)  │    │ (Octava) │    │  (EDC)    │    │ (ISO 3382) │
    └─────────┘    └──────────┘    └───────────┘    └────────────┘
    ```

    **Incluir ecuaciones** (en LaTeX):

    $$EDC(t) = \int_t^{\infty} h^2(\tau) d\tau$$

    $$T_{60} = \frac{-60}{pendiente_{dB/s}}$$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Resultados

    La seccion de resultados debe ser **objetiva**: presentar datos, no opiniones.

    **Figuras profesionales:**
    - Ejes etiquetados con unidades
    - Leyenda cuando hay multiples curvas
    - Titulo descriptivo
    - Resolucion adecuada (minimo 150 dpi)
    - Referenciadas en el texto: "Como se observa en la Figura 3..."

    **Tablas de comparacion:**

    | Banda [Hz] | T60 propio [s] | T60 REW [s] | Error [s] | Error [%] |
    |:----------:|:--------------:|:----------:|:---------:|:---------:|
    | 125 | 1.45 | 1.52 | 0.07 | 4.6 |
    | 250 | 1.32 | 1.38 | 0.06 | 4.3 |
    | 500 | 1.18 | 1.21 | 0.03 | 2.5 |
    | 1000 | 1.05 | 1.08 | 0.03 | 2.8 |
    | 2000 | 0.92 | 0.95 | 0.03 | 3.2 |
    | 4000 | 0.78 | 0.81 | 0.03 | 3.7 |

    **Error aceptable**: segun la norma ISO 3382-1, diferencias menores a ±5% o ±0.05 s (el mayor) son aceptables para mediciones repetidas.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    # Ejemplo de figura profesional para el informe
    bandas = [125, 250, 500, 1000, 2000, 4000]
    t60_propio = [1.45, 1.32, 1.18, 1.05, 0.92, 0.78]
    t60_rew = [1.52, 1.38, 1.21, 1.08, 0.95, 0.81]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    # Grafico de barras comparativo
    x = np.arange(len(bandas))
    ancho = 0.35
    ax1.bar(x - ancho/2, t60_propio, ancho, label="AcoustiPy", color="#2196F3")
    ax1.bar(x + ancho/2, t60_rew, ancho, label="REW", color="#FF9800")
    ax1.set_xlabel("Banda de octava [Hz]")
    ax1.set_ylabel("T60 [s]")
    ax1.set_title("Comparacion T60: AcoustiPy vs REW")
    ax1.set_xticks(x)
    ax1.set_xticklabels([str(b) for b in bandas])
    ax1.legend()
    ax1.grid(axis="y", alpha=0.3)

    # Grafico de error
    errores = [abs(p - r) for p, r in zip(t60_propio, t60_rew)]
    ax2.bar(x, errores, color="#4CAF50")
    ax2.axhline(y=0.05, color="red", linestyle="--", label="Limite aceptable")
    ax2.set_xlabel("Banda de octava [Hz]")
    ax2.set_ylabel("Error absoluto [s]")
    ax2.set_title("Error absoluto por banda")
    ax2.set_xticks(x)
    ax2.set_xticklabels([str(b) for b in bandas])
    ax2.legend()
    ax2.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig
    return (fig, np, plt)


@app.cell
def _(mo):
    mo.md(r"""
    ### Conclusiones

    Las conclusiones deben:

    1. **Resumir los resultados principales** (sin repetir las tablas)
    2. **Analizar criticamente**: que funciono bien y que no
    3. **Identificar limitaciones**: que no cubre su implementacion
    4. **Proponer trabajo futuro**: que mejorarian con mas tiempo

    **Ejemplo de conclusiones:**

    > La herramienta desarrollada calcula los parametros acusticos con una precision
    > aceptable segun la norma ISO 3382-1, con errores maximos de 4.6% en T60.
    > Las mayores diferencias se observaron en la banda de 125 Hz, posiblemente
    > debido a la sensibilidad del filtro Butterworth en frecuencias bajas.
    >
    > **Limitaciones:**
    > - Solo soporta archivos WAV mono
    > - No implementa correccion por ruido de fondo
    > - El metodo de truncamiento de la IR es basico
    >
    > **Trabajo futuro:**
    > - Implementar correccion de Lundeby para truncamiento
    > - Agregar soporte para mediciones multicanal
    > - Implementar parametros laterales (JLF, JLFC)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### El Anexo: Log de Desarrollo con IA

    Este anexo es **obligatorio** para el informe. Documenta como usaron IA durante el desarrollo.

    **Estructura sugerida:**

    1. **Herramientas utilizadas**: Claude, ChatGPT, Copilot, etc.
    2. **Tareas asistidas por IA**: para que la usaron
    3. **Ejemplo de interaccion exitosa**: prompt + respuesta + resultado
    4. **Ejemplo de interaccion fallida**: prompt + respuesta + por que fallo
    5. **Reflexion**: como cambio su flujo de trabajo
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Quarto vs LaTeX

    Pueden escribir el informe en **Quarto** o en **LaTeX**. Ambos son validos.

    | Aspecto | Quarto | LaTeX |
    |---------|--------|-------|
    | Curva de aprendizaje | Baja | Alta |
    | Codigo ejecutable | Si (incluye graficos automaticamente) | No (hay que exportar figuras) |
    | Control tipografico | Medio | Total |
    | Templates UNTREF | No (pero se puede personalizar) | Si (template existente) |
    | Formato de entrada | Markdown | LaTeX |
    | Salida | PDF, HTML, Word | PDF |
    | Ecuaciones | LaTeX (igual) | LaTeX (nativo) |
    | Bibliografia | Si (CSL/BibTeX) | Si (BibTeX) |

    ### Recomendacion

    - Si nunca usaron LaTeX: **Quarto**
    - Si ya conocen LaTeX: **LaTeX** con el template de UNTREF
    - En ambos casos: enfoquense en el **contenido**, no en el formato

    Para detalles sobre Quarto, consulten `guias/quarto_informe.md`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Habilidades de Presentacion para Ingenieros

    La presentacion final dura **20 minutos** + 5 minutos de preguntas. Hay que usar el tiempo sabiamente.

    ### Estructura recomendada (20 minutos)

    | Bloque | Tiempo | Contenido |
    |--------|:------:|-----------|
    | Introduccion | 3 min | Equipo, objetivos, arquitectura general |
    | Desarrollo tecnico | 8 min | 2-3 funciones clave EN VIVO, decisiones de diseno |
    | Resultados | 6 min | Tablas comparativas, graficos, validacion |
    | Reflexiones | 3 min | Desafios, aprendizajes, que harian diferente |

    ### Desarrollo tecnico: mostrar codigo EN VIVO

    No muestren TODO el codigo. Elijan **2-3 funciones clave** y expliquen:
    - Que hace la funcion
    - Por que la implementaron asi
    - Que alternativas consideraron
    - Como la testearon

    **Ejemplo**: mostrar `calcular_t60()` ejecutandose en un notebook con una IR real, y comparar el resultado con REW.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Tips para demos en vivo

    1. **SIEMPRE tengan backups pre-computados**
       - Screenshots de la terminal funcionando
       - Graficos ya generados como imagenes
       - Un video corto de la demo (por si todo falla)

    2. **Testeen la demo 3 veces antes de presentar**
       - En la misma computadora que van a usar
       - Con el proyector conectado (la resolucion cambia)
       - Con todos los paquetes instalados

    3. **Tengan a alguien listo para switchear al backup**
       - Si la demo falla, no pierdan tiempo debuggeando en vivo
       - "Tuvimos un problema tecnico, pero aca estan los resultados"

    4. **Asignen roles claros**
       - Quien presenta cada seccion
       - Quien maneja la computadora
       - Quien responde preguntas de cada area
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Errores comunes en presentaciones

    | Error | Por que es malo | Solucion |
    |-------|----------------|----------|
    | Leer las slides | El publico puede leer solo | Usar bullets como guia, hablar con sus palabras |
    | Mucha teoria | Los evaluadores ya la conocen | Enfocarse en implementacion y resultados |
    | No ensayar | Se pasan de tiempo, se traban | Ensayar minimo 2 veces cronometrados |
    | Ignorar el tiempo | No llegan a los resultados | Usar un timer visible, tener alguien que avise |
    | Slides con mucho texto | Nadie las lee | Maximo 6 bullets por slide, usar figuras |
    | No preparar preguntas | Se ponen nerviosos | Anticipar 5 preguntas probables y preparar respuestas |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Metodologia de Validacion

    ### Comparacion con REW

    [REW (Room EQ Wizard)](https://www.roomeqwizard.com/) es el software de referencia gratuito para acustica de salas. Para validar sus resultados:

    1. **Cargar la misma IR** en REW y en su herramienta
    2. **Calcular los mismos parametros** con las mismas bandas de octava
    3. **Comparar** los resultados en una tabla
    4. **Analizar las diferencias**: si hay diferencias grandes, investigar por que

    ### Crear la tabla de comparacion

    Para cada respuesta al impulso, crear una tabla como esta:

    ```
    IR: sala_aula.wav (fs=44100 Hz, duracion=3.2 s)

    Parametro | Banda | AcoustiPy | REW    | Error abs | Error %
    ----------|-------|-----------|--------|-----------|--------
    T60       | 500   | 1.18 s    | 1.21 s | 0.03 s    | 2.5%
    T60       | 1000  | 1.05 s    | 1.08 s | 0.03 s    | 2.8%
    EDT       | 500   | 1.02 s    | 1.05 s | 0.03 s    | 2.9%
    EDT       | 1000  | 0.95 s    | 0.97 s | 0.02 s    | 2.1%
    D50       | 500   | 0.42      | 0.44   | 0.02      | 4.5%
    C80       | 1000  | 1.8 dB    | 2.0 dB | 0.2 dB    | -
    ```

    ### Criterios de aceptacion

    - **T60, EDT**: error < 5% o < 0.05 s (el mayor)
    - **D50**: error absoluto < 0.05
    - **C80**: error absoluto < 0.5 dB

    Si usan **multiples IRs**, reporten media ± desviacion estandar.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Checklist Final

    Usen esta lista para verificar que tienen todo listo para el Demo Day.

    ### Codigo
    - [ ] Todas las funciones implementadas (cargar, filtrar, Schroeder, parametros)
    - [ ] Tests unitarios pasando (`pytest` en verde)
    - [ ] CI configurado y verde en GitHub
    - [ ] Manejo de errores robusto
    - [ ] CLI funcional (`acoustipy --help`)

    ### Documentacion
    - [ ] README completo (descripcion, instalacion, uso, estructura)
    - [ ] Docstrings NumPy-style en todas las funciones publicas
    - [ ] Documentacion API generada (pdoc o mkdocs)

    ### Informe
    - [ ] Abstract (150 palabras)
    - [ ] Introduccion, marco teorico, metodologia
    - [ ] Resultados con tablas y figuras
    - [ ] Conclusiones con analisis critico
    - [ ] Referencias bibliograficas
    - [ ] Anexo: Log de desarrollo con IA

    ### Presentacion
    - [ ] Slides listas (20 minutos)
    - [ ] Demo probada (3 veces minimo)
    - [ ] Backup de la demo (screenshots, video)
    - [ ] Roles asignados

    ### Repositorio
    - [ ] Tag `v1.0.0` creado
    - [ ] Historial de commits limpio
    - [ ] `.gitignore` adecuado
    - [ ] Sin archivos innecesarios (no subir data/, __pycache__, .env)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. Reflexion sobre IA (P2)

    Antes del Demo Day, deben escribir su **Log de Desarrollo con IA** (300-500 palabras). Estas preguntas los ayudan a reflexionar:

    ### Preguntas guia

    1. **Herramientas**: Que herramientas de IA usaron? (Claude, ChatGPT, Copilot, etc.)

    2. **Tareas**: Para que tareas usaron IA?
       - Generar codigo inicial
       - Debuggear errores
       - Escribir tests
       - Crear documentacion
       - Refactorizar
       - Explicar conceptos

    3. **Interaccion mas util**: Cual fue la interaccion con IA que mas les sirvio? Describan el prompt, la respuesta, y por que fue util.

    4. **Interaccion menos util**: Cual fue la interaccion que menos les sirvio o que los llevo por un camino equivocado? Que aprendieron de esa experiencia?

    5. **Impacto en el flujo de trabajo**: Como cambio la IA su forma de programar? Programan mas rapido? Mejor? Diferente?

    6. **Pensamiento critico**: En que momentos fue importante NO seguir la sugerencia de la IA? Por que?

    7. **Futuro**: Usarian IA de la misma forma en su proximo proyecto? Que cambiarian?

    ### Formato del log

    ```markdown
    ## Log de Desarrollo con IA

    ### Herramientas utilizadas
    - [herramienta 1]: para [tarea]
    - [herramienta 2]: para [tarea]

    ### Interaccion destacada
    **Prompt**: [lo que le pidieron]
    **Respuesta**: [resumen de lo que respondio]
    **Resultado**: [como lo usaron, si funciono]

    ### Interaccion fallida
    **Prompt**: [lo que le pidieron]
    **Problema**: [por que la respuesta no sirvio]
    **Leccion**: [que aprendieron]

    ### Reflexion general
    [300-500 palabras sobre su experiencia]
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy preparamos todo para el Demo Day:

    1. **Informe tecnico**: estructura clara, figuras profesionales, analisis critico
    2. **Quarto vs LaTeX**: elijan la herramienta que les resulte mas comoda
    3. **Presentacion**: 20 minutos bien distribuidos, demo con backup
    4. **Validacion**: comparacion sistematica con REW
    5. **Checklist**: verifiquen que tienen todo listo
    6. **Reflexion IA**: escriban su log de desarrollo

    ### Proxima clase: DEMO DAY (7 de julio)
    - Presentaciones finales: 20 min + 5 min Q&A por grupo
    - Entregables: codigo (tag v1.0.0), informe (PDF), slides
    - Evaluacion: tecnico (40%), comunicacion (35%), analisis critico (25%)
    """)
    return


if __name__ == "__main__":
    app.run()
