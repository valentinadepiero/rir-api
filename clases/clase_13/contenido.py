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
    ## Clase 13: De Funciones a Producto

    Hoy damos el paso de tener **funciones sueltas** a tener una **aplicacion integrada**. Vamos a crear una interfaz de linea de comandos, manejar configuracion, errores, y empaquetar nuestro proyecto como un paquete Python instalable.

    **Pilares**: P3 (principal), P2 (secundario), P1 (secundario)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 1. De Funciones a Aplicacion

    Hasta ahora tienen funciones individuales que hacen cosas utiles: cargar audio, filtrar, calcular parametros. Pero para que esto sea un **producto**, necesitan un **punto de entrada** que orqueste todo.

    ### El viaje de la integracion

    ```
    Funciones individuales     Modulos organizados      Aplicacion integrada
    ┌──────────────┐         ┌──────────────┐         ┌──────────────────┐
    │ calcular_t60 │         │ audio.py     │         │ main.py          │
    │ filtrar_banda│   -->   │ filtros.py   │   -->   │  ├─ CLI          │
    │ cargar_wav   │         │ parametros.py│         │  ├─ Config       │
    │ graficar     │         │ plots.py     │         │  ├─ Pipeline     │
    └──────────────┘         └──────────────┘         │  └─ Output       │
                                                       └──────────────────┘
    ```

    ### El patron main.py

    El archivo `main.py` es el **director de orquesta**: no calcula nada directamente, sino que llama a las funciones de cada modulo en el orden correcto.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Interfaz de linea de comandos con argparse

    `argparse` es la forma estandar de crear interfaces de linea de comandos en Python.
    """)
    return


@app.cell
def _():
    import argparse

    # Ejemplo de como se define un CLI para el TP
    # (no lo ejecutamos porque estamos en un notebook)

    codigo_cli = '''
    import argparse

    def crear_parser():
        """Crea el parser de argumentos de linea de comandos.

        Returns
        -------
        argparse.ArgumentParser
            Parser configurado con todos los argumentos.
        """
        parser = argparse.ArgumentParser(
            description="AcoustiPy - Analisis acustico ISO 3382",
            epilog="Ejemplo: acoustipy audio/sala.wav --parametros T60 EDT C80"
        )

        parser.add_argument(
            "audio",
            help="Ruta al archivo de audio (.wav)"
        )

        parser.add_argument(
            "--fs", type=int, default=44100,
            help="Frecuencia de muestreo en Hz (default: 44100)"
        )

        parser.add_argument(
            "--parametros", nargs="+",
            default=["T60", "EDT", "D50", "C80"],
            help="Parametros a calcular (default: T60 EDT D50 C80)"
        )

        parser.add_argument(
            "--bandas", nargs="+", type=int,
            default=[125, 250, 500, 1000, 2000, 4000],
            help="Bandas de octava a analizar en Hz"
        )

        parser.add_argument(
            "--output", "-o", default="resultados.json",
            help="Archivo de salida (default: resultados.json)"
        )

        parser.add_argument(
            "--graficar", action="store_true",
            help="Generar graficos de los resultados"
        )

        parser.add_argument(
            "--config", type=str, default=None,
            help="Archivo de configuracion TOML"
        )

        parser.add_argument(
            "--verbose", "-v", action="store_true",
            help="Mostrar informacion detallada"
        )

        return parser


    if __name__ == "__main__":
        parser = crear_parser()
        args = parser.parse_args()
        print(f"Audio: {args.audio}")
        print(f"Parametros: {args.parametros}")
    '''

    print(codigo_cli)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Uso del CLI

    ```bash
    # Uso basico
    acoustipy audio/sala_aula.wav

    # Especificar parametros
    acoustipy audio/sala_aula.wav --parametros T60 EDT

    # Con configuracion y graficos
    acoustipy audio/sala_aula.wav --config config.toml --graficar

    # Ver ayuda
    acoustipy --help
    ```

    La ventaja de `argparse` es que genera la ayuda automaticamente y valida los tipos de datos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 2. Gestion de Configuracion

    Los **valores hardcodeados** (escritos directamente en el codigo) son problematicos:

    - Dificiles de encontrar y cambiar
    - No se pueden ajustar sin modificar el codigo
    - Imposible tener configuraciones diferentes para diferentes situaciones

    ### Archivos TOML

    **TOML** (Tom's Obvious Minimal Language) es el formato estandar de configuracion en Python moderno. Es legible, simple y tiene soporte nativo desde Python 3.11.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Ejemplo de config.toml para el TP

    ```toml
    # config.toml - Configuracion de AcoustiPy

    [general]
    fs = 44100
    verbose = false

    [filtros]
    orden = 4
    tipo = "butterworth"
    bandas = [125, 250, 500, 1000, 2000, 4000, 8000]

    [analisis]
    parametros = ["EDT", "T20", "T30", "T60", "D50", "C80"]
    metodo_t60 = "T30"  # Metodo para calcular T60: "T20" o "T30"
    rango_dinamico_minimo = 35  # dB

    [salida]
    formato = "json"
    directorio = "resultados"
    generar_graficos = true
    formato_graficos = "png"
    dpi = 150
    ```
    """)
    return


@app.cell
def _():
    # Cargar configuracion TOML con tomllib
    # Disponible nativamente desde Python 3.11
    import tomllib
    from pathlib import Path

    # Simulamos un archivo TOML como string
    config_toml = """
    [general]
    fs = 44100
    verbose = false

    [filtros]
    orden = 4
    tipo = "butterworth"
    bandas = [125, 250, 500, 1000, 2000, 4000, 8000]

    [analisis]
    parametros = ["EDT", "T20", "T30", "T60", "D50", "C80"]
    metodo_t60 = "T30"
    rango_dinamico_minimo = 35

    [salida]
    formato = "json"
    directorio = "resultados"
    generar_graficos = true
    dpi = 150
    """

    # Cargar desde string (en la practica, se carga desde archivo)
    config = tomllib.loads(config_toml)

    # Acceder a la configuracion
    print(f"Frecuencia de muestreo: {config['general']['fs']} Hz")
    print(f"Bandas de octava: {config['filtros']['bandas']}")
    print(f"Parametros a calcular: {config['analisis']['parametros']}")
    print(f"Orden del filtro: {config['filtros']['orden']}")
    return (Path, config, tomllib)


@app.cell
def _(mo):
    mo.md(r"""
    ### Funcion para cargar configuracion

    ```python
    import tomllib
    from pathlib import Path

    def cargar_config(ruta_config=None):
        '''Carga la configuracion desde un archivo TOML.

        Si no se especifica ruta, usa valores por defecto.

        Parameters
        ----------
        ruta_config : str or Path, optional
            Ruta al archivo de configuracion TOML.

        Returns
        -------
        dict
            Diccionario con la configuracion.
        '''
        config_default = {
            "general": {"fs": 44100, "verbose": False},
            "filtros": {"orden": 4, "bandas": [125, 250, 500, 1000, 2000, 4000]},
            "analisis": {"parametros": ["T60", "EDT", "D50", "C80"]},
            "salida": {"formato": "json", "directorio": "resultados"},
        }

        if ruta_config is None:
            return config_default

        ruta = Path(ruta_config)
        if not ruta.exists():
            raise FileNotFoundError(f"Archivo de configuracion no encontrado: {ruta}")

        with open(ruta, "rb") as f:
            config_archivo = tomllib.load(f)

        # Merge: valores del archivo sobreescriben los defaults
        for seccion, valores in config_archivo.items():
            if seccion in config_default:
                config_default[seccion].update(valores)
            else:
                config_default[seccion] = valores

        return config_default
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 3. Manejo de Errores

    Un programa robusto **no se rompe** cuando algo sale mal: informa al usuario que paso y como solucionarlo.

    ### Errores comunes en procesamiento de audio

    | Error | Causa | Solucion |
    |-------|-------|----------|
    | `FileNotFoundError` | Ruta incorrecta | Verificar que el archivo existe |
    | Formato no soportado | Archivo no es .wav | Validar extension y contenido |
    | Senal vacia | Archivo corrupto o silencio | Verificar que la senal tiene energia |
    | Rango dinamico bajo | Ruido de fondo alto | Advertir al usuario, no calcular |
    | Frecuencia de muestreo baja | Archivo de baja calidad | Advertir que las bandas altas no son validas |
    """)
    return


@app.cell
def _():
    # Excepciones personalizadas para el proyecto

    class AudioError(Exception):
        """Error base para operaciones de audio."""
        pass

    class ArchivoNoSoportado(AudioError):
        """El archivo de audio no tiene un formato soportado."""
        pass

    class SenalVacia(AudioError):
        """La senal de audio no tiene energia (esta vacia o es silencio)."""
        pass

    class RangoDinamicoInsuficiente(AudioError):
        """La senal no tiene suficiente rango dinamico para el analisis."""
        pass

    class FrecuenciaMuestreoInvalida(AudioError):
        """La frecuencia de muestreo no es valida para el analisis solicitado."""
        pass

    # Ejemplo de uso
    print("Excepciones personalizadas definidas:")
    print(f"  - AudioError (base)")
    print(f"  - ArchivoNoSoportado")
    print(f"  - SenalVacia")
    print(f"  - RangoDinamicoInsuficiente")
    print(f"  - FrecuenciaMuestreoInvalida")
    return (ArchivoNoSoportado, AudioError, FrecuenciaMuestreoInvalida, RangoDinamicoInsuficiente, SenalVacia)


@app.cell
def _(ArchivoNoSoportado, SenalVacia):
    import numpy as np
    from pathlib import Path as PathLib

    def cargar_audio_robusto(ruta, fs_esperado=None):
        """Carga un archivo de audio con manejo robusto de errores.

        Parameters
        ----------
        ruta : str or Path
            Ruta al archivo de audio.
        fs_esperado : int, optional
            Frecuencia de muestreo esperada. Si el archivo tiene
            otra frecuencia, se lanza una advertencia.

        Returns
        -------
        tuple
            (senal, fs) donde senal es np.ndarray y fs es int.

        Raises
        ------
        FileNotFoundError
            Si el archivo no existe.
        ArchivoNoSoportado
            Si el formato no es .wav.
        SenalVacia
            Si la senal no tiene energia.
        """
        ruta = PathLib(ruta)

        # Verificar que el archivo existe
        if not ruta.exists():
            raise FileNotFoundError(
                f"Archivo no encontrado: {ruta}\n"
                f"Verifique que la ruta es correcta."
            )

        # Verificar formato
        extensiones_validas = {".wav", ".WAV"}
        if ruta.suffix not in extensiones_validas:
            raise ArchivoNoSoportado(
                f"Formato no soportado: {ruta.suffix}\n"
                f"Formatos validos: {extensiones_validas}"
            )

        # Simular carga (en la practica, usar scipy.io.wavfile o soundfile)
        # import soundfile as sf
        # senal, fs = sf.read(str(ruta))

        # Para el ejemplo, generamos datos sinteticos
        fs = fs_esperado or 44100
        senal = np.random.randn(fs)  # 1 segundo de ruido

        # Verificar que la senal no esta vacia
        energia = np.sum(senal**2)
        if energia < 1e-10:
            raise SenalVacia(
                f"La senal en {ruta} no tiene energia.\n"
                f"Energia total: {energia:.2e}\n"
                f"Posible archivo corrupto o silencio."
            )

        return senal, fs

    # Demostrar manejo de errores
    try:
        senal, fs = cargar_audio_robusto("archivo_inexistente.wav")
    except FileNotFoundError as e:
        print(f"Error capturado: {e}")

    try:
        senal, fs = cargar_audio_robusto("archivo.mp3")
    except ArchivoNoSoportado as e:
        print(f"\nError capturado: {e}")
    return (cargar_audio_robusto, np)


@app.cell
def _(mo):
    mo.md(r"""
    ### Logging: registrar lo que pasa

    `logging` es mejor que `print` porque:
    - Se puede configurar el nivel (DEBUG, INFO, WARNING, ERROR)
    - Se puede redirigir a archivos
    - Incluye timestamps automaticamente
    - Se puede desactivar sin borrar las lineas de codigo
    """)
    return


@app.cell
def _():
    import logging

    # Configuracion basica del logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    logger = logging.getLogger("acoustipy")

    # Ejemplo de uso en el pipeline
    logger.info("Iniciando analisis acustico")
    logger.info("Cargando archivo de audio: sala_aula.wav")
    logger.info("Frecuencia de muestreo: 44100 Hz")
    logger.info("Duracion: 3.2 s")
    logger.info("Aplicando filtro de banda: 1000 Hz")
    logger.warning("Rango dinamico bajo en banda 125 Hz: 28 dB")
    logger.info("Calculando parametros: T60, EDT, D50, C80")
    logger.info("Resultados guardados en: resultados.json")
    logger.info("Analisis completado exitosamente")
    return (logger, logging)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 4. Empaquetado Python

    Para que su proyecto se pueda **instalar** como un paquete Python, necesitan un `pyproject.toml`.

    ### pyproject.toml: la forma moderna
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```toml
    # pyproject.toml
    [project]
    name = "acoustipy"
    version = "1.0.0"
    description = "Analisis acustico de salas segun ISO 3382"
    readme = "README.md"
    license = {text = "MIT"}
    requires-python = ">=3.10"
    authors = [
        {name = "Equipo 1", email = "equipo1@untref.edu.ar"},
    ]

    dependencies = [
        "numpy>=1.24",
        "scipy>=1.10",
        "matplotlib>=3.7",
        "soundfile>=0.12",
    ]

    [project.optional-dependencies]
    dev = [
        "pytest>=7.0",
        "pytest-cov>=4.0",
        "ruff>=0.1",
    ]
    docs = [
        "pdoc>=14.0",
        "mkdocs>=1.5",
        "mkdocs-material>=9.0",
    ]

    # Entry point: esto crea el comando 'acoustipy'
    [project.scripts]
    acoustipy = "acoustipy.main:main"

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.hatch.build.targets.wheel]
    packages = ["src/acoustipy"]

    [tool.pytest.ini_options]
    testpaths = ["tests"]

    [tool.ruff]
    line-length = 88
    ```

    ### Comandos para empaquetar

    ```bash
    # Instalar en modo desarrollo (editable)
    uv pip install -e .

    # Ahora pueden usar el CLI
    acoustipy --help

    # Construir el paquete (genera .whl y .tar.gz)
    uv build

    # Instalar dependencias de desarrollo
    uv pip install -e ".[dev]"
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Que es un entry point?

    Cuando definen:
    ```toml
    [project.scripts]
    acoustipy = "acoustipy.main:main"
    ```

    Python crea un comando ejecutable `acoustipy` que llama a la funcion `main()` del modulo `acoustipy.main`. Es decir:

    ```bash
    acoustipy audio/sala.wav --parametros T60
    ```

    Es equivalente a:

    ```python
    from acoustipy.main import main
    import sys
    sys.argv = ["acoustipy", "audio/sala.wav", "--parametros", "T60"]
    main()
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 5. Ejemplo de Integracion Completa

    Asi se ve un `main.py` que integra todo lo que vimos:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```python
    # src/acoustipy/main.py
    '''Punto de entrada principal de AcoustiPy.'''

    import argparse
    import json
    import logging
    import sys
    import tomllib
    from pathlib import Path

    import numpy as np

    from acoustipy.audio import cargar_audio
    from acoustipy.filtros import filtrar_bandas_octava
    from acoustipy.schroeder import integral_schroeder
    from acoustipy.parametros import calcular_parametros
    from acoustipy.visualizacion import graficar_resultados

    logger = logging.getLogger("acoustipy")


    def crear_parser():
        parser = argparse.ArgumentParser(
            description="AcoustiPy - Analisis acustico ISO 3382"
        )
        parser.add_argument("audio", help="Ruta al archivo de audio (.wav)")
        parser.add_argument("--config", help="Archivo de configuracion TOML")
        parser.add_argument("--parametros", nargs="+",
                            default=["T60", "EDT", "D50", "C80"])
        parser.add_argument("--output", "-o", default="resultados.json")
        parser.add_argument("--graficar", action="store_true")
        parser.add_argument("--verbose", "-v", action="store_true")
        return parser


    def cargar_config(ruta_config):
        if ruta_config is None:
            return {}
        with open(ruta_config, "rb") as f:
            return tomllib.load(f)


    def main():
        parser = crear_parser()
        args = parser.parse_args()

        # Configurar logging
        nivel = logging.DEBUG if args.verbose else logging.INFO
        logging.basicConfig(
            level=nivel,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )

        try:
            # 1. Cargar configuracion
            config = cargar_config(args.config)
            logger.info("Configuracion cargada")

            # 2. Cargar audio
            logger.info(f"Cargando: {args.audio}")
            ir, fs = cargar_audio(args.audio)
            logger.info(f"Audio: {len(ir)/fs:.2f}s, {fs} Hz")

            # 3. Filtrar en bandas de octava
            bandas = config.get("filtros", {}).get(
                "bandas", [125, 250, 500, 1000, 2000, 4000]
            )
            logger.info(f"Filtrando en bandas: {bandas}")
            senales_filtradas = filtrar_bandas_octava(ir, fs, bandas)

            # 4. Integral de Schroeder por banda
            edcs = {}
            for banda, senal in senales_filtradas.items():
                edcs[banda] = integral_schroeder(senal)
            logger.info("Integrales de Schroeder calculadas")

            # 5. Calcular parametros por banda
            resultados = {}
            for banda, edc in edcs.items():
                resultados[banda] = calcular_parametros(
                    edc, fs, args.parametros
                )
            logger.info(f"Parametros calculados: {args.parametros}")

            # 6. Guardar resultados
            with open(args.output, "w") as f:
                json.dump(resultados, f, indent=2, default=str)
            logger.info(f"Resultados guardados en: {args.output}")

            # 7. Graficar (opcional)
            if args.graficar:
                graficar_resultados(resultados, edcs, bandas)
                logger.info("Graficos generados")

            logger.info("Analisis completado exitosamente")

        except FileNotFoundError as e:
            logger.error(f"Archivo no encontrado: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error inesperado: {e}")
            sys.exit(1)


    if __name__ == "__main__":
        main()
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Diagrama del pipeline

    ```
    ┌────────────┐    ┌──────────┐    ┌───────────┐    ┌───────────┐
    │  CLI Args  │--->│  Config  │--->│   Audio   │--->│  Filtros  │
    │  argparse  │    │  TOML    │    │  .wav     │    │  Octava   │
    └────────────┘    └──────────┘    └───────────┘    └───────────┘
                                                             │
                                                             v
    ┌────────────┐    ┌──────────┐    ┌───────────┐    ┌───────────┐
    │  Graficos  │<---│  JSON    │<---│ Parametros│<---│ Schroeder │
    │  matplotlib│    │  Output  │    │ T60,EDT.. │    │  EDC      │
    └────────────┘    └──────────┘    └───────────┘    └───────────┘
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 6. IA para Refactoring (P2)

    La IA puede ayudar a **mejorar codigo existente** identificando problemas y sugiriendo mejoras.

    ### Prompts utiles para refactoring

    **Encontrar code smells:**
    ```
    Revisa este codigo Python y lista los "code smells"
    (problemas de diseno) que encuentres. Para cada uno,
    explica por que es un problema y como solucionarlo.

    [pegar codigo]
    ```

    **Mejorar estructura:**
    ```
    Este modulo tiene funciones muy largas. Sugiere como
    dividirlas en funciones mas pequenas y cohesivas.
    Manten la misma funcionalidad.

    [pegar codigo]
    ```

    **Consistencia:**
    ```
    Revisa estos 3 modulos y verifica que usen convenciones
    consistentes: nombres de variables, manejo de errores,
    estilo de docstrings, tipos de retorno.

    [pegar codigo de los modulos]
    ```

    ### Advertencia

    La IA puede sugerir cambios que **rompen funcionalidad**. Siempre:
    1. Entiendan **por que** sugiere cada cambio
    2. Apliquen los cambios **uno por uno**
    3. Corran los **tests** despues de cada cambio
    4. Usen **git** para poder revertir si algo se rompe
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Resumen

    Hoy pasamos de funciones individuales a una aplicacion integrada:

    1. **CLI con argparse**: interfaz de usuario profesional
    2. **Configuracion TOML**: parametros externalizados y flexibles
    3. **Manejo de errores**: excepciones personalizadas y mensajes utiles
    4. **Logging**: registro de operaciones para debugging
    5. **Empaquetado**: pyproject.toml con entry points
    6. **Integracion**: main.py que orquesta todo el pipeline
    7. **IA para refactoring**: mejorar codigo existente con asistencia

    ### Para la proxima clase
    - Tener el main.py funcionando con CLI
    - Configuracion TOML creada
    - Pipeline completo: audio -> filtros -> Schroeder -> parametros -> JSON
    - Preparar el informe tecnico y la presentacion
    """)
    return


if __name__ == "__main__":
    app.run()
