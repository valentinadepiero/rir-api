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
    # Clase 14: Ejercicios
    ## Pulido y Preparacion para el Demo Day

    Estos ejercicios son **practicos y de preparacion directa** para la entrega final. Cada uno produce un entregable concreto para el Demo Day.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 1: Abstract del informe

    Escriban el **Abstract** de su informe tecnico en **maximo 150 palabras**.

    Debe responder estas 4 preguntas:
    1. **Que** se hizo (objetivo del trabajo)
    2. **Como** se hizo (metodologia, en 1-2 oraciones)
    3. **Que** se obtuvo (resultado principal, con numeros)
    4. **Que** significa (conclusion principal)

    **Tips:**
    - No usar primera persona ("En este trabajo se desarrollo...")
    - Incluir al menos un dato numerico concreto
    - No incluir referencias ni acronimos sin definir
    - Escribirlo al final, despues de tener todos los resultados
    """)
    return


@app.cell
def _():
    # Ejercicio 1: Escriban su abstract aca

    abstract = """
    [Escribir su abstract aca - maximo 150 palabras]

    Se desarrollo una herramienta en Python para...
    La implementacion incluye...
    Los resultados muestran que...
    Se concluye que...
    """

    # Contar palabras
    palabras = len(abstract.split())
    print(f"Abstract ({palabras} palabras):")
    print(abstract)

    if palabras > 150:
        print(f"\nADVERTENCIA: Excede el limite de 150 palabras por {palabras - 150}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 2: Tabla de comparacion con REW

    Creen una **tabla de comparacion** entre los resultados de su herramienta y REW (Room EQ Wizard).

    Requisitos:
    - Al menos **2 respuestas al impulso** diferentes
    - Al menos **3 bandas de octava** por IR
    - Parametro principal: **T60**
    - Incluir: valor propio, valor REW, error absoluto, error porcentual

    **Pasos:**
    1. Cargar la misma IR en su herramienta y en REW
    2. Calcular T60 en las mismas bandas
    3. Anotar ambos valores
    4. Calcular los errores

    Si no tienen REW instalado, pueden usar valores de referencia de la literatura o generar IRs sinteticas con T60 conocido.
    """)
    return


@app.cell
def _():
    import numpy as np

    # Ejercicio 2: Tabla de comparacion
    # Completen con sus valores reales

    print("=" * 70)
    print("TABLA DE COMPARACION: AcoustiPy vs REW")
    print("=" * 70)

    # IR 1
    print("\nIR 1: [nombre del archivo]")
    print(f"{'Banda [Hz]':>10} | {'Propio [s]':>10} | {'REW [s]':>10} | {'Error [s]':>10} | {'Error [%]':>10}")
    print("-" * 60)

    # Valores de ejemplo (reemplacen con sus datos reales)
    bandas = [500, 1000, 2000]
    valores_propios_1 = [0.0, 0.0, 0.0]  # Completar
    valores_rew_1 = [0.0, 0.0, 0.0]      # Completar

    for i, banda in enumerate(bandas):
        propio = valores_propios_1[i]
        rew = valores_rew_1[i]
        error_abs = abs(propio - rew)
        error_pct = (error_abs / rew * 100) if rew > 0 else 0
        print(f"{banda:>10} | {propio:>10.3f} | {rew:>10.3f} | {error_abs:>10.3f} | {error_pct:>9.1f}%")

    # IR 2
    print("\nIR 2: [nombre del archivo]")
    print(f"{'Banda [Hz]':>10} | {'Propio [s]':>10} | {'REW [s]':>10} | {'Error [s]':>10} | {'Error [%]':>10}")
    print("-" * 60)

    valores_propios_2 = [0.0, 0.0, 0.0]  # Completar
    valores_rew_2 = [0.0, 0.0, 0.0]      # Completar

    for i, banda in enumerate(bandas):
        propio = valores_propios_2[i]
        rew = valores_rew_2[i]
        error_abs = abs(propio - rew)
        error_pct = (error_abs / rew * 100) if rew > 0 else 0
        print(f"{banda:>10} | {propio:>10.3f} | {rew:>10.3f} | {error_abs:>10.3f} | {error_pct:>9.1f}%")
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 3: Outline de la presentacion

    Creen el **outline** (esquema) de su presentacion de 20 minutos.

    Para cada slide, indiquen:
    - Numero de slide
    - Titulo
    - Contenido principal (2-3 bullets)
    - Tiempo estimado

    **Estructura sugerida:**
    - Slides 1-3: Introduccion (3 min)
    - Slides 4-8: Desarrollo tecnico (8 min)
    - Slides 9-12: Resultados (6 min)
    - Slides 13-14: Reflexiones y cierre (3 min)
    """)
    return


@app.cell
def _():
    # Ejercicio 3: Outline de la presentacion

    outline = """
    OUTLINE DE LA PRESENTACION (20 minutos)
    =========================================

    BLOQUE 1: INTRODUCCION (3 min)

    Slide 1 - Titulo (30 s)
      - Nombre del proyecto
      - Integrantes
      - Materia y fecha

    Slide 2 - Objetivos (1 min)
      - Que hace la herramienta
      - Que norma sigue
      - Que parametros calcula

    Slide 3 - Arquitectura general (1.5 min)
      - Diagrama de modulos
      - Flujo de datos
      - Tecnologias usadas

    BLOQUE 2: DESARROLLO TECNICO (8 min)

    Slide 4 - [Funcion clave 1] (2.5 min)
      - Mostrar codigo EN VIVO
      - Explicar la logica
      - Demo con datos reales

    Slide 5 - [Funcion clave 2] (2.5 min)
      - [completar]

    Slide 6 - [Funcion clave 3] (2 min)
      - [completar]

    Slide 7 - Testing y CI (1 min)
      - Tests unitarios
      - GitHub Actions

    BLOQUE 3: RESULTADOS (6 min)

    Slide 8 - Tabla de comparacion (2 min)
      - T60: nuestro vs REW
      - Error por banda

    Slide 9 - Graficos (2 min)
      - EDC por banda
      - Comparacion visual

    Slide 10 - Analisis de errores (2 min)
      - Donde hay mas error y por que
      - Limitaciones

    BLOQUE 4: REFLEXIONES (3 min)

    Slide 11 - Desafios y aprendizajes (1.5 min)
      - Que fue lo mas dificil
      - Que aprendimos

    Slide 12 - IA y cierre (1.5 min)
      - Como usamos IA
      - Que hariamos diferente
      - Preguntas
    """
    print(outline)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 4: Pipeline completo y graficos

    Ejecuten su **pipeline completo** de principio a fin con una IR real (o sintetica) y capturen todos los graficos.

    1. Cargar la IR
    2. Filtrar en bandas de octava
    3. Calcular integrales de Schroeder
    4. Calcular parametros
    5. Generar graficos:
       - EDC por banda (en dB vs tiempo)
       - T60 por banda (barras)
       - Comparacion con referencia (si tienen)

    Guarden los graficos en el directorio de figuras de su informe.
    """)
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt

    # Ejercicio 4: Pipeline completo con graficos
    # Este es un ejemplo con datos sinteticos.
    # Reemplacen con su pipeline real.

    fs = 44100
    bandas = [125, 250, 500, 1000, 2000, 4000]

    # Simular T60 por banda (decreciente con frecuencia)
    t60_por_banda = {
        125: 1.8, 250: 1.5, 500: 1.2,
        1000: 1.0, 2000: 0.85, 4000: 0.7
    }

    # Generar EDCs sinteticas
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle("Energy Decay Curves por Banda de Octava", fontsize=14)

    for idx, banda in enumerate(bandas):
        ax = axes[idx // 3, idx % 3]
        t60 = t60_por_banda[banda]
        t = np.arange(int(2.5 * fs)) / fs
        ir = np.exp(-6.908 * t / t60)
        edc = np.cumsum(ir[::-1]**2)[::-1]
        edc_db = 10 * np.log10(edc / edc[0] + 1e-12)

        ax.plot(t, edc_db, linewidth=1.5)
        ax.axhline(y=-60, color='red', linestyle='--', alpha=0.5, label='-60 dB')
        ax.set_xlabel("Tiempo [s]")
        ax.set_ylabel("Nivel [dB]")
        ax.set_title(f"{banda} Hz (T60={t60:.2f} s)")
        ax.set_ylim(-80, 5)
        ax.set_xlim(0, 2.5)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)

    plt.tight_layout()
    fig
    return (plt,)


@app.cell
def _(np, plt):
    # Grafico de T60 por banda
    bandas_plot = [125, 250, 500, 1000, 2000, 4000]
    t60_valores = [1.8, 1.5, 1.2, 1.0, 0.85, 0.7]

    fig2, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(bandas_plot))
    ax.bar(x, t60_valores, color="#2196F3", edgecolor="white", linewidth=0.5)

    ax.set_xlabel("Banda de octava [Hz]", fontsize=12)
    ax.set_ylabel("T60 [s]", fontsize=12)
    ax.set_title("Tiempo de Reverberacion por Banda de Octava", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels([str(b) for b in bandas_plot])
    ax.grid(axis="y", alpha=0.3)

    # Anotar valores
    for i, v in enumerate(t60_valores):
        ax.text(i, v + 0.03, f"{v:.2f}", ha='center', fontsize=10)

    plt.tight_layout()
    fig2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 5: Log de desarrollo con IA

    Escriban su **Log de Desarrollo con IA** (300-500 palabras).

    Sigan esta estructura:

    1. **Herramientas utilizadas** (50 palabras)
    2. **Interaccion destacada** (100 palabras): descripcion de un caso exitoso
    3. **Interaccion fallida** (100 palabras): descripcion de un caso donde la IA no ayudo
    4. **Reflexion general** (150-250 palabras): analisis de como la IA impacto su desarrollo

    **Preguntas guia para la reflexion:**
    - La IA los hizo mas productivos? En que tareas?
    - Confiaron demasiado en la IA en algun momento?
    - Que aprendieron sobre como formular prompts efectivos?
    - Usarian IA de la misma forma en su proximo proyecto?
    """)
    return


@app.cell
def _():
    # Ejercicio 5: Escriban su log de IA aca

    log_ia = """
    ## Log de Desarrollo con IA

    ### Herramientas utilizadas
    - [Herramienta 1]: para [tareas]
    - [Herramienta 2]: para [tareas]

    ### Interaccion destacada
    **Prompt**: [lo que le pidieron a la IA]
    **Respuesta**: [resumen de la respuesta]
    **Resultado**: [como lo usaron, si funciono]
    **Por que fue util**: [explicar]

    ### Interaccion fallida
    **Prompt**: [lo que le pidieron a la IA]
    **Problema**: [que salio mal]
    **Leccion aprendida**: [que aprendieron]

    ### Reflexion general
    [300-500 palabras sobre su experiencia con IA durante el desarrollo]
    [Incluir: productividad, confianza, prompts, futuro]
    """

    palabras = len(log_ia.split())
    print(f"Log de IA ({palabras} palabras):")
    print(log_ia)
    return


if __name__ == "__main__":
    app.run()
