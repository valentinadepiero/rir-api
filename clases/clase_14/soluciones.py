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
    # Clase 14: Soluciones y Templates
    ## Pulido y Preparacion

    Estos son ejemplos y templates de referencia para los ejercicios de preparacion del Demo Day.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 1: Abstract de ejemplo

    Un abstract bien escrito para un TP tipico:
    """)
    return


@app.cell
def _():
    abstract_ejemplo = """
    Se desarrollo una herramienta de software en Python para el calculo de
    parametros acusticos de salas a partir de respuestas al impulso, de
    acuerdo con la norma ISO 3382-1:2009. La implementacion incluye carga
    y preprocesamiento de archivos WAV, filtrado en bandas de octava mediante
    filtros Butterworth de cuarto orden, calculo de la curva de decaimiento
    energetico (EDC) por el metodo de Schroeder, y extraccion de los
    parametros EDT, T20, T30, T60, D50 y C80. Se valido la herramienta
    comparando los resultados con el software de referencia REW (Room EQ
    Wizard) para tres respuestas al impulso de espacios con caracteristicas
    acusticas diferentes. La diferencia maxima observada fue de 0.15 s en
    T60 (4.6%) y 1.2 dB en C80, valores dentro de los margenes aceptables
    segun la norma. El proyecto se distribuye como paquete Python instalable
    con interfaz de linea de comandos, tests automatizados y documentacion
    generada automaticamente.
    """

    palabras = len(abstract_ejemplo.split())
    print(f"Abstract de ejemplo ({palabras} palabras):")
    print(abstract_ejemplo)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Analisis del abstract

    - **Que se hizo**: "Se desarrollo una herramienta de software en Python para el calculo de parametros acusticos..."
    - **Como se hizo**: "filtrado en bandas de octava mediante filtros Butterworth... metodo de Schroeder..."
    - **Que se obtuvo**: "diferencia maxima de 0.15 s en T60 (4.6%) y 1.2 dB en C80"
    - **Que significa**: "valores dentro de los margenes aceptables segun la norma"

    Notas:
    - No usa primera persona
    - Incluye datos numericos concretos
    - Menciona la norma de referencia
    - Describe brevemente la metodologia
    - Cierra con informacion sobre distribucion del software
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 2: Tabla de comparacion de ejemplo
    """)
    return


@app.cell
def _():
    import numpy as np

    # Datos de ejemplo para la comparacion
    print("=" * 72)
    print("TABLA DE COMPARACION: AcoustiPy vs REW")
    print("=" * 72)

    # IR 1: Aula
    print("\nIR 1: aula_untref.wav (fs=44100 Hz, duracion=3.2 s)")
    print("-" * 72)
    print(f"{'Banda [Hz]':>10} | {'AcoustiPy [s]':>13} | {'REW [s]':>10} | {'Error [s]':>10} | {'Error [%]':>10}")
    print("-" * 72)

    datos_ir1 = [
        (500, 1.18, 1.21),
        (1000, 1.05, 1.08),
        (2000, 0.92, 0.95),
    ]

    for banda, propio, rew in datos_ir1:
        error = abs(propio - rew)
        error_pct = error / rew * 100
        print(f"{banda:>10} | {propio:>13.2f} | {rew:>10.2f} | {error:>10.3f} | {error_pct:>9.1f}%")

    # IR 2: Auditorio
    print(f"\nIR 2: auditorio.wav (fs=48000 Hz, duracion=5.1 s)")
    print("-" * 72)
    print(f"{'Banda [Hz]':>10} | {'AcoustiPy [s]':>13} | {'REW [s]':>10} | {'Error [s]':>10} | {'Error [%]':>10}")
    print("-" * 72)

    datos_ir2 = [
        (500, 2.35, 2.41),
        (1000, 2.10, 2.15),
        (2000, 1.78, 1.82),
    ]

    for banda, propio, rew in datos_ir2:
        error = abs(propio - rew)
        error_pct = error / rew * 100
        print(f"{banda:>10} | {propio:>13.2f} | {rew:>10.2f} | {error:>10.3f} | {error_pct:>9.1f}%")

    # Resumen
    todos_errores = [abs(p - r) for _, p, r in datos_ir1 + datos_ir2]
    todos_errores_pct = [abs(p - r) / r * 100 for _, p, r in datos_ir1 + datos_ir2]

    print(f"\nRESUMEN")
    print("-" * 40)
    print(f"Error absoluto maximo: {max(todos_errores):.3f} s")
    print(f"Error absoluto medio:  {np.mean(todos_errores):.3f} s")
    print(f"Error porcentual max:  {max(todos_errores_pct):.1f}%")
    print(f"Error porcentual medio: {np.mean(todos_errores_pct):.1f}%")
    print(f"\nCriterio ISO (<5% o <0.05 s): CUMPLE")
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 3: Outline de presentacion de ejemplo
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```
    PRESENTACION FINAL - AcoustiPy
    Equipo: [nombres]
    Duracion: 20 minutos + 5 min Q&A

    ═══════════════════════════════════════════

    BLOQUE 1: INTRODUCCION (3 min)
    Presentador: [nombre]

    Slide 1 - Portada (20 s)
      • Titulo: "AcoustiPy: Analisis Acustico ISO 3382 en Python"
      • Nombres del equipo
      • Logo/imagen del proyecto

    Slide 2 - Contexto y objetivo (1.5 min)
      • Por que es importante medir parametros acusticos
      • Objetivo: herramienta que calcula EDT, T60, D50, C80
      • Norma ISO 3382-1:2009

    Slide 3 - Arquitectura (1 min)
      • Diagrama de modulos (audio → filtros → Schroeder → parametros)
      • Stack tecnologico: Python, NumPy, SciPy, pytest, GitHub Actions
      • Estructura del repositorio

    ═══════════════════════════════════════════

    BLOQUE 2: DESARROLLO TECNICO (8 min)
    Presentador: [nombre]

    Slide 4-5 - Filtrado en bandas de octava (2.5 min)
      • Codigo de filtrar_banda_octava() EN VIVO
      • Por que Butterworth orden 4
      • Demo: filtrar una IR real, mostrar espectro

    Slide 6-7 - Integral de Schroeder y T60 (3 min)
      • Ecuacion de la integral de Schroeder
      • Codigo de calcular_t60() EN VIVO
      • Demo: EDC de una sala real, ajuste lineal

    Slide 8 - Testing y CI (1.5 min)
      • Ejemplo de test con IR sintetica
      • Screenshot de GitHub Actions en verde
      • Cobertura de tests

    Slide 9 - CLI y empaquetado (1 min)
      • Demo: acoustipy audio/sala.wav --parametros T60 EDT
      • Screenshot de la salida

    ═══════════════════════════════════════════

    BLOQUE 3: RESULTADOS (6 min)
    Presentador: [nombre]

    Slide 10 - Tabla de comparacion (2 min)
      • T60 por banda: AcoustiPy vs REW
      • Dos IRs diferentes
      • Error maximo: X.XX s (X.X%)

    Slide 11 - Graficos (2 min)
      • EDC por banda (figura)
      • T60 por banda (barras comparativas)
      • Graficos de error

    Slide 12 - Analisis de errores (2 min)
      • Donde hay mas error y por que
      • Efecto del orden del filtro
      • Limitaciones: ruido de fondo, truncamiento

    ═══════════════════════════════════════════

    BLOQUE 4: REFLEXIONES (3 min)
    Presentador: [nombre]

    Slide 13 - Desafios y aprendizajes (1.5 min)
      • Mayor desafio: [descripcion]
      • Aprendizaje mas valioso: [descripcion]
      • Uso de IA: que funciono y que no

    Slide 14 - Cierre (1.5 min)
      • Trabajo futuro: correccion Lundeby, soporte multicanal
      • Link al repositorio
      • Preguntas?
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 4: Graficos profesionales para el informe
    """)
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt

    # Generar graficos profesionales de ejemplo

    # --- Grafico 1: EDC por banda ---
    fig1, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig1.suptitle("Curvas de Decaimiento Energetico (EDC) por Banda de Octava",
                   fontsize=14, fontweight='bold')

    bandas = [125, 250, 500, 1000, 2000, 4000]
    t60_vals = [1.8, 1.5, 1.2, 1.0, 0.85, 0.7]
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    for idx, (banda, t60, color) in enumerate(zip(bandas, t60_vals, colores)):
        ax = axes[idx // 3, idx % 3]
        fs = 44100
        t = np.arange(int(2.5 * fs)) / fs
        ir = np.exp(-6.908 * t / t60)
        edc = np.cumsum(ir[::-1]**2)[::-1]
        edc_db = 10 * np.log10(edc / edc[0] + 1e-12)

        ax.plot(t, edc_db, color=color, linewidth=1.5)
        ax.axhline(y=-5, color='gray', linestyle=':', alpha=0.5)
        ax.axhline(y=-35, color='gray', linestyle=':', alpha=0.5)
        ax.axhline(y=-60, color='red', linestyle='--', alpha=0.5)

        # Marcar rango de ajuste
        ax.axvspan(0, t60 * 5/60, alpha=0.05, color='green')

        ax.set_xlabel("Tiempo [s]", fontsize=9)
        ax.set_ylabel("Nivel [dB]", fontsize=9)
        ax.set_title(f"{banda} Hz | T60 = {t60:.2f} s", fontsize=11)
        ax.set_ylim(-80, 5)
        ax.set_xlim(0, 2.5)
        ax.grid(True, alpha=0.2)

    plt.tight_layout()
    fig1
    return (plt,)


@app.cell
def _(np, plt):
    # --- Grafico 2: Comparacion T60 ---
    bandas_comp = [125, 250, 500, 1000, 2000, 4000]
    t60_propio = [1.82, 1.48, 1.18, 1.05, 0.88, 0.72]
    t60_rew = [1.89, 1.52, 1.21, 1.08, 0.91, 0.74]

    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    fig2.suptitle("Validacion: AcoustiPy vs REW", fontsize=14, fontweight='bold')

    x = np.arange(len(bandas_comp))
    ancho = 0.35

    # Barras comparativas
    bars1 = ax1.bar(x - ancho/2, t60_propio, ancho,
                     label="AcoustiPy", color="#2196F3", edgecolor="white")
    bars2 = ax1.bar(x + ancho/2, t60_rew, ancho,
                     label="REW", color="#FF9800", edgecolor="white")

    ax1.set_xlabel("Banda de octava [Hz]", fontsize=11)
    ax1.set_ylabel("T60 [s]", fontsize=11)
    ax1.set_title("Comparacion de T60 por banda")
    ax1.set_xticks(x)
    ax1.set_xticklabels([str(b) for b in bandas_comp])
    ax1.legend(fontsize=10)
    ax1.grid(axis="y", alpha=0.3)

    # Error absoluto
    errores = [abs(p - r) for p, r in zip(t60_propio, t60_rew)]
    colores_error = ['#4CAF50' if e < 0.05 else '#FFC107' for e in errores]
    ax2.bar(x, errores, color=colores_error, edgecolor="white")
    ax2.axhline(y=0.05, color="red", linestyle="--", linewidth=1.5,
                label="Limite aceptable (0.05 s)")

    ax2.set_xlabel("Banda de octava [Hz]", fontsize=11)
    ax2.set_ylabel("Error absoluto [s]", fontsize=11)
    ax2.set_title("Error absoluto por banda")
    ax2.set_xticks(x)
    ax2.set_xticklabels([str(b) for b in bandas_comp])
    ax2.legend(fontsize=10)
    ax2.grid(axis="y", alpha=0.3)

    # Anotar errores
    for i, e in enumerate(errores):
        ax2.text(i, e + 0.002, f"{e:.3f}", ha='center', fontsize=9)

    plt.tight_layout()
    fig2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 5: Log de IA de ejemplo
    """)
    return


@app.cell
def _():
    log_ia_ejemplo = """
    ## Log de Desarrollo con IA

    ### Herramientas utilizadas
    - Claude (Anthropic): generacion de codigo, debugging, explicacion de conceptos
    - GitHub Copilot: autocompletado de codigo, sugerencias en el editor

    ### Interaccion destacada
    **Prompt**: "Implementa una funcion en Python que calcule el T60 a partir
    de la EDC usando el metodo T30 segun ISO 3382. Usa NumPy."

    **Respuesta**: Claude genero una funcion completa con ajuste lineal por
    minimos cuadrados en el rango de -5 a -35 dB, incluyendo validacion
    del rango dinamico y docstring.

    **Resultado**: La funcion funciono correctamente con pequenas modificaciones.
    Tuvimos que ajustar el manejo del caso donde el rango dinamico es insuficiente
    (la IA usaba un return None en vez de una excepcion, que era mas apropiado
    para nuestro pipeline).

    **Por que fue util**: Nos ahorro ~30 minutos de implementacion y nos dio
    una estructura solida sobre la cual iterar.

    ### Interaccion fallida
    **Prompt**: "Genera tests unitarios completos para el modulo de filtros"

    **Problema**: Los tests generados eran superficiales (solo verificaban que
    la funcion no lanzara excepciones) y no testeaban propiedades importantes
    como la atenuacion fuera de banda o la respuesta en frecuencia central.
    Ademas, usaba valores magicos sin explicar de donde salian.

    **Leccion aprendida**: Para tests, es mejor definir nosotros QUE queremos
    testear y pedirle a la IA que implemente esos tests especificos, en vez de
    pedirle "genera tests" de forma abierta.

    ### Reflexion general
    La IA fue una herramienta valiosa que acelero significativamente nuestro
    desarrollo, especialmente en tareas repetitivas como escribir docstrings,
    generar boilerplate de configuracion, y crear estructuras iniciales de
    funciones. Estimamos que nos ahorro entre un 20-30% del tiempo total
    de desarrollo.

    Sin embargo, aprendimos que la IA no reemplaza el entendimiento profundo
    del dominio. En varias ocasiones, el codigo generado era sintacticamente
    correcto pero conceptualmente incorrecto (por ejemplo, aplicar la ventana
    de Hanning a la IR antes de calcular la EDC, lo cual es erroneo segun
    la norma ISO).

    El mayor aprendizaje fue sobre como formular prompts efectivos. Los prompts
    mas utiles fueron los que incluian contexto especifico (la norma ISO, el
    formato de datos, las restricciones del proyecto) en vez de pedidos genericos.

    Para el proximo proyecto, usariamos la IA de forma mas estrategica:
    como generador de borradores que siempre revisamos criticamente, y como
    herramienta de debugging cuando estamos trabados. Pero nunca como reemplazo
    del diseno y la toma de decisiones arquitecturales.
    """

    palabras = len(log_ia_ejemplo.split())
    print(f"Log de IA de ejemplo ({palabras} palabras):")
    print(log_ia_ejemplo)
    return


if __name__ == "__main__":
    app.run()
