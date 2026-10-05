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
    # Clase 13: Ejercicios
    ## De Funciones a Producto

    Estos ejercicios los guian para transformar sus funciones individuales en una aplicacion integrada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 1: main.py con CLI basico

    Creen un archivo `main.py` para su TP que:

    1. Acepte la ruta a un archivo de audio como argumento
    2. Imprima informacion basica: duracion, canales, frecuencia de muestreo
    3. Use `argparse` para parsear los argumentos

    **Resultado esperado:**
    ```bash
    $ python main.py audio/sala.wav
    Archivo: audio/sala.wav
    Frecuencia de muestreo: 44100 Hz
    Duracion: 3.20 s
    Muestras: 141120
    ```
    """)
    return


@app.cell
def _():
    # Ejercicio 1: Escriban su main.py aca

    codigo_main = '''
    import argparse

    def crear_parser():
        parser = argparse.ArgumentParser(
            description="[Nombre del proyecto] - [descripcion]"
        )
        parser.add_argument("audio", help="Ruta al archivo de audio (.wav)")
        # Agregar mas argumentos segun necesiten
        return parser

    def main():
        parser = crear_parser()
        args = parser.parse_args()

        # TODO: Cargar el audio
        # TODO: Imprimir informacion basica
        print(f"Archivo: {args.audio}")

    if __name__ == "__main__":
        main()
    '''
    print(codigo_main)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 2: Configuracion TOML

    Creen un archivo `config.toml` para su TP con **todos** los parametros configurables:

    1. Frecuencia de muestreo
    2. Bandas de octava a analizar
    3. Orden del filtro
    4. Parametros acusticos a calcular
    5. Opciones de salida (formato, directorio)

    Luego, escriban una funcion que lo cargue con `tomllib`.
    """)
    return


@app.cell
def _():
    # Ejercicio 2: Escriban su configuracion y funcion de carga

    config_ejemplo = """
    # config.toml para el TP
    [general]
    fs = 44100

    [filtros]
    orden = 4
    bandas = [125, 250, 500, 1000, 2000, 4000]

    [analisis]
    parametros = ["T60", "EDT", "D50", "C80"]

    [salida]
    formato = "json"
    directorio = "resultados"
    """

    # Funcion para cargar:
    import tomllib

    config = tomllib.loads(config_ejemplo)
    print("Configuracion cargada:")
    for seccion, valores in config.items():
        print(f"\n[{seccion}]")
        for clave, valor in valores.items():
            print(f"  {clave} = {valor}")
    return (tomllib,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 3: Manejo de errores

    Agreguen manejo de errores robusto a su funcion `cargar_audio`:

    1. `FileNotFoundError`: el archivo no existe
    2. Formato no soportado: el archivo no es .wav
    3. Senal vacia: el archivo no tiene energia

    Definan **excepciones personalizadas** para su proyecto.
    """)
    return


@app.cell
def _():
    import numpy as np
    from pathlib import Path

    # Ejercicio 3: Definan sus excepciones y funcion con manejo de errores

    class AudioError(Exception):
        """Error base para operaciones de audio."""
        pass

    class ArchivoNoSoportado(AudioError):
        """El formato del archivo no es soportado."""
        pass

    class SenalVacia(AudioError):
        """La senal no tiene energia."""
        pass

    def cargar_audio_seguro(ruta):
        """Carga audio con manejo robusto de errores.

        Parameters
        ----------
        ruta : str
            Ruta al archivo de audio.

        Returns
        -------
        tuple
            (senal, fs)

        Raises
        ------
        FileNotFoundError
            Si el archivo no existe.
        ArchivoNoSoportado
            Si el formato no es .wav.
        SenalVacia
            Si la senal no tiene energia.
        """
        ruta = Path(ruta)

        # TODO: Implementar las 3 verificaciones
        # 1. Verificar que existe
        if not ruta.exists():
            raise FileNotFoundError(f"No se encontro: {ruta}")

        # 2. Verificar formato
        if ruta.suffix.lower() != ".wav":
            raise ArchivoNoSoportado(f"Formato no soportado: {ruta.suffix}")

        # 3. Cargar y verificar energia
        # senal, fs = sf.read(str(ruta))
        # if np.sum(senal**2) < 1e-10:
        #     raise SenalVacia(f"Senal sin energia en {ruta}")

        # Placeholder
        fs = 44100
        senal = np.random.randn(fs)
        return senal, fs

    # Probar el manejo de errores
    for ruta_test in ["no_existe.wav", "archivo.mp3"]:
        try:
            s, f = cargar_audio_seguro(ruta_test)
        except (FileNotFoundError, ArchivoNoSoportado) as e:
            print(f"Error capturado para '{ruta_test}': {type(e).__name__}: {e}")
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 4: Logging

    Agreguen logging basico a su pipeline principal:

    1. Configuren logging con formato que incluya timestamp
    2. Registren cada paso del pipeline: carga, filtrado, analisis
    3. Usen niveles apropiados: INFO para pasos normales, WARNING para situaciones inusuales
    """)
    return


@app.cell
def _():
    import logging

    # Ejercicio 4: Configurar logging para el pipeline

    # Configuracion
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )

    logger = logging.getLogger("mi_proyecto")

    # Simular pipeline con logging
    def pipeline_con_logging(ruta_audio):
        """Ejecuta el pipeline completo con logging."""
        logger.info(f"Inicio del analisis: {ruta_audio}")

        # Paso 1: Cargar audio
        logger.info("Cargando archivo de audio...")
        # ir, fs = cargar_audio(ruta_audio)
        logger.info("Audio cargado: 44100 Hz, 3.2 s")

        # Paso 2: Filtrar
        bandas = [500, 1000, 2000]
        logger.info(f"Filtrando en bandas: {bandas}")
        for banda in bandas:
            logger.info(f"  Procesando banda {banda} Hz")

        # Paso 3: Analisis
        logger.info("Calculando parametros acusticos...")
        logger.warning("Banda 125 Hz: rango dinamico bajo (28 dB)")
        logger.info("Parametros calculados: T60, EDT, D50, C80")

        # Paso 4: Guardar
        logger.info("Guardando resultados en resultados.json")
        logger.info("Analisis completado exitosamente")

    pipeline_con_logging("audio/sala_aula.wav")
    return (logging,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 5: pyproject.toml con entry point

    Configuren su `pyproject.toml` para crear un CLI instalable:

    1. Definan el entry point en `[project.scripts]`
    2. Instalen con `uv pip install -e .`
    3. Verifiquen que `nombre_proyecto --help` funciona

    **Pista**: El entry point apunta a la funcion `main()` de su `main.py`.
    """)
    return


@app.cell
def _():
    # Ejercicio 5: pyproject.toml

    pyproject_contenido = """
    [project]
    name = "acoustipy"
    version = "1.0.0"
    description = "Analisis acustico de salas segun ISO 3382"
    readme = "README.md"
    requires-python = ">=3.10"
    dependencies = [
        "numpy>=1.24",
        "scipy>=1.10",
        "matplotlib>=3.7",
    ]

    [project.optional-dependencies]
    dev = [
        "pytest>=7.0",
        "ruff>=0.1",
    ]

    [project.scripts]
    acoustipy = "acoustipy.main:main"

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.hatch.build.targets.wheel]
    packages = ["src/acoustipy"]
    """

    print("Contenido de pyproject.toml:")
    print(pyproject_contenido)
    print("\nComandos para instalar y probar:")
    print("  uv pip install -e .")
    print("  acoustipy --help")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Ejercicio 6: Test de integracion

    Creen un test que ejecute el **pipeline completo** con una IR sintetica y verifique que los resultados son correctos.

    El test debe:
    1. Generar una IR sintetica con T60 conocido
    2. Ejecutar todo el pipeline (filtrar, Schroeder, parametros)
    3. Verificar que el T60 calculado esta dentro del rango esperado
    """)
    return


@app.cell
def _(np):
    # Ejercicio 6: Test de integracion

    def test_pipeline_completo():
        """Test de integracion del pipeline completo.

        Genera una IR sintetica con T60 = 1.0 s y verifica que
        el pipeline calcula un T60 cercano al valor esperado.
        """
        # 1. Generar IR sintetica con T60 conocido
        fs = 44100
        t60_esperado = 1.0
        duracion = 2.0  # segundos
        t = np.arange(int(duracion * fs)) / fs

        # IR = exponencial decreciente (T60 = 1.0 s)
        # La constante de decaimiento para T60 es: -60 dB en T60 segundos
        # -> factor = 6.908 / T60 (porque 20*log10(exp(-6.908)) ≈ -60)
        ir = np.exp(-6.908 * t / t60_esperado)

        # Agregar un poco de ruido
        ir = ir + np.random.randn(len(ir)) * 0.001

        # 2. Calcular EDC (integral de Schroeder)
        edc = np.cumsum(ir[::-1]**2)[::-1]
        edc = edc / edc[0]

        # 3. Calcular T60
        edc_db = 10 * np.log10(edc + 1e-12)
        idx_5 = np.argmax(edc_db < -5)
        idx_35 = np.argmax(edc_db < -35)

        t_vector = np.arange(len(edc)) / fs
        coef = np.polyfit(t_vector[idx_5:idx_35], edc_db[idx_5:idx_35], 1)
        t60_calculado = -60 / coef[0]

        # 4. Verificar
        error = abs(t60_calculado - t60_esperado)
        tolerancia = 0.1  # 100 ms de tolerancia

        print(f"T60 esperado: {t60_esperado:.3f} s")
        print(f"T60 calculado: {t60_calculado:.3f} s")
        print(f"Error: {error:.3f} s")
        print(f"Tolerancia: {tolerancia:.3f} s")

        assert error < tolerancia, (
            f"T60 fuera de tolerancia: {t60_calculado:.3f} s "
            f"(esperado: {t60_esperado:.3f} ± {tolerancia:.3f} s)"
        )
        print("TEST PASADO: T60 dentro de la tolerancia")

    test_pipeline_completo()
    return


if __name__ == "__main__":
    app.run()
