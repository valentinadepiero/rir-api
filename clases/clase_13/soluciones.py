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
    # Clase 13: Soluciones
    ## De Funciones a Producto

    Soluciones de referencia para los ejercicios de integracion.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 1: main.py con CLI

    Un main.py completo con CLI usando argparse:
    """)
    return


@app.cell
def _():
    codigo_main_completo = '''#!/usr/bin/env python
"""AcoustiPy - Punto de entrada principal.

Uso:
    acoustipy audio/sala.wav
    acoustipy audio/sala.wav --parametros T60 EDT --graficar
    acoustipy audio/sala.wav --config config.toml -v
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np


logger = logging.getLogger("acoustipy")


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
        "--parametros", nargs="+",
        default=["T60", "EDT", "D50", "C80"],
        help="Parametros a calcular (default: T60 EDT D50 C80)"
    )

    parser.add_argument(
        "--bandas", nargs="+", type=int,
        default=[125, 250, 500, 1000, 2000, 4000],
        help="Bandas de octava en Hz"
    )

    parser.add_argument(
        "--output", "-o", default="resultados.json",
        help="Archivo de salida (default: resultados.json)"
    )

    parser.add_argument(
        "--config", type=str, default=None,
        help="Archivo de configuracion TOML"
    )

    parser.add_argument(
        "--graficar", action="store_true",
        help="Generar graficos de los resultados"
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Mostrar informacion detallada"
    )

    return parser


def mostrar_info_audio(ruta, senal, fs):
    """Muestra informacion basica del archivo de audio.

    Parameters
    ----------
    ruta : str
        Ruta al archivo.
    senal : np.ndarray
        Senal de audio.
    fs : int
        Frecuencia de muestreo.
    """
    duracion = len(senal) / fs
    print(f"Archivo: {ruta}")
    print(f"Frecuencia de muestreo: {fs} Hz")
    print(f"Duracion: {duracion:.2f} s")
    print(f"Muestras: {len(senal)}")
    print(f"Valor maximo: {np.max(np.abs(senal)):.4f}")


def main():
    parser = crear_parser()
    args = parser.parse_args()

    # Configurar logging
    nivel = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=nivel,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # Verificar que el archivo existe
    ruta = Path(args.audio)
    if not ruta.exists():
        logger.error(f"Archivo no encontrado: {ruta}")
        sys.exit(1)

    if ruta.suffix.lower() != ".wav":
        logger.error(f"Formato no soportado: {ruta.suffix}")
        sys.exit(1)

    logger.info(f"Procesando: {args.audio}")
    logger.info(f"Parametros: {args.parametros}")
    logger.info(f"Bandas: {args.bandas}")

    # TODO: Completar con la logica real del pipeline
    # ir, fs = cargar_audio(args.audio)
    # mostrar_info_audio(args.audio, ir, fs)
    # ...

    logger.info(f"Resultados guardados en: {args.output}")


if __name__ == "__main__":
    main()
'''
    print(codigo_main_completo)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 2: Configuracion TOML completa
    """)
    return


@app.cell
def _():
    import tomllib

    config_toml_completo = """
    # config.toml - Configuracion de AcoustiPy
    # Todos los parametros son opcionales; si no se especifican,
    # se usan los valores por defecto del codigo.

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
    formato_graficos = "png"
    dpi = 150
    """

    def cargar_config(ruta_config=None):
        """Carga configuracion desde archivo TOML con valores por defecto.

        Parameters
        ----------
        ruta_config : str or None
            Ruta al archivo TOML. Si es None, retorna defaults.

        Returns
        -------
        dict
            Configuracion completa.
        """
        defaults = {
            "general": {"fs": 44100, "verbose": False},
            "filtros": {
                "orden": 4,
                "tipo": "butterworth",
                "bandas": [125, 250, 500, 1000, 2000, 4000],
            },
            "analisis": {
                "parametros": ["T60", "EDT", "D50", "C80"],
                "metodo_t60": "T30",
                "rango_dinamico_minimo": 35,
            },
            "salida": {
                "formato": "json",
                "directorio": "resultados",
                "generar_graficos": False,
                "dpi": 150,
            },
        }

        if ruta_config is None:
            return defaults

        from pathlib import Path
        ruta = Path(ruta_config)
        if not ruta.exists():
            raise FileNotFoundError(f"Config no encontrada: {ruta}")

        with open(ruta, "rb") as f:
            archivo = tomllib.load(f)

        # Merge: archivo sobreescribe defaults
        for seccion, valores in archivo.items():
            if seccion in defaults and isinstance(defaults[seccion], dict):
                defaults[seccion].update(valores)
            else:
                defaults[seccion] = valores

        return defaults

    # Demostrar carga desde string
    config = tomllib.loads(config_toml_completo)
    print("Configuracion cargada:")
    for seccion, valores in config.items():
        print(f"\n[{seccion}]")
        for k, v in valores.items():
            print(f"  {k} = {v}")
    return (cargar_config, tomllib)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 3: Manejo de errores completo
    """)
    return


@app.cell
def _():
    import numpy as np
    from pathlib import Path

    # Excepciones personalizadas
    class AudioError(Exception):
        """Error base para operaciones de audio."""
        pass

    class ArchivoNoSoportado(AudioError):
        """Formato de archivo no soportado."""
        pass

    class SenalVacia(AudioError):
        """Senal sin energia detectada."""
        pass

    class RangoDinamicoInsuficiente(AudioError):
        """Rango dinamico insuficiente para el analisis."""
        pass

    def cargar_audio_robusto(ruta, fs_esperado=None):
        """Carga audio con manejo completo de errores.

        Parameters
        ----------
        ruta : str or Path
            Ruta al archivo de audio.
        fs_esperado : int, optional
            Frecuencia de muestreo esperada.

        Returns
        -------
        tuple
            (senal, fs)

        Raises
        ------
        FileNotFoundError
            Si el archivo no existe.
        ArchivoNoSoportado
            Si el formato no es WAV.
        SenalVacia
            Si la senal no tiene energia.
        """
        ruta = Path(ruta)

        # 1. Verificar existencia
        if not ruta.exists():
            raise FileNotFoundError(
                f"Archivo no encontrado: {ruta}\n"
                f"Directorio actual: {Path.cwd()}\n"
                f"Verifique la ruta e intente nuevamente."
            )

        # 2. Verificar formato
        formatos_validos = {".wav"}
        if ruta.suffix.lower() not in formatos_validos:
            raise ArchivoNoSoportado(
                f"Formato '{ruta.suffix}' no soportado.\n"
                f"Formatos validos: {formatos_validos}\n"
                f"Convierta el archivo a WAV e intente nuevamente."
            )

        # 3. Cargar (simulado)
        try:
            # En la practica:
            # import soundfile as sf
            # senal, fs = sf.read(str(ruta))
            fs = fs_esperado or 44100
            senal = np.random.randn(fs * 2)
        except Exception as e:
            raise AudioError(f"Error al leer {ruta}: {e}")

        # 4. Verificar energia
        energia = np.sum(senal**2)
        if energia < 1e-10:
            raise SenalVacia(
                f"Senal sin energia en {ruta}\n"
                f"Energia total: {energia:.2e}\n"
                f"El archivo puede estar corrupto o contener silencio."
            )

        # 5. Advertencia si fs no coincide
        if fs_esperado and fs != fs_esperado:
            import warnings
            warnings.warn(
                f"Frecuencia de muestreo ({fs} Hz) diferente "
                f"a la esperada ({fs_esperado} Hz)"
            )

        return senal, fs

    # Demostrar cada tipo de error
    print("=== Test de manejo de errores ===\n")

    tests = [
        ("no_existe.wav", "FileNotFoundError"),
        ("archivo.mp3", "ArchivoNoSoportado"),
    ]

    for ruta_test, error_esperado in tests:
        try:
            s, f = cargar_audio_robusto(ruta_test)
            print(f"  {ruta_test}: OK (inesperado)")
        except (FileNotFoundError, ArchivoNoSoportado, SenalVacia) as e:
            print(f"  {ruta_test}: {type(e).__name__}")
            print(f"    Mensaje: {str(e).split(chr(10))[0]}")
            print()
    return (np,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 4: Pipeline con logging
    """)
    return


@app.cell
def _(np):
    import logging
    import time

    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        force=True  # Forzar reconfiguracion
    )

    logger = logging.getLogger("acoustipy")

    def pipeline_completo(ruta_audio, config=None):
        """Ejecuta el pipeline de analisis acustico con logging.

        Parameters
        ----------
        ruta_audio : str
            Ruta al archivo de audio.
        config : dict, optional
            Configuracion del analisis.
        """
        logger.info("=" * 50)
        logger.info("INICIO DEL ANALISIS ACUSTICO")
        logger.info("=" * 50)

        config = config or {
            "filtros": {"bandas": [500, 1000, 2000], "orden": 4},
            "analisis": {"parametros": ["T60", "EDT"]},
        }

        # Paso 1: Cargar audio
        logger.info(f"Paso 1/5: Cargando audio desde {ruta_audio}")
        fs = 44100
        duracion = 3.2
        logger.info(f"  -> Audio cargado: {fs} Hz, {duracion:.1f} s")

        # Paso 2: Filtrar
        bandas = config["filtros"]["bandas"]
        logger.info(f"Paso 2/5: Filtrando en {len(bandas)} bandas de octava")
        for banda in bandas:
            logger.debug(f"  -> Filtrando banda {banda} Hz")
        logger.info(f"  -> Filtrado completado")

        # Paso 3: Integral de Schroeder
        logger.info("Paso 3/5: Calculando integrales de Schroeder")
        for banda in bandas:
            rango_dinamico = np.random.uniform(25, 50)
            if rango_dinamico < 35:
                logger.warning(
                    f"  Banda {banda} Hz: rango dinamico bajo "
                    f"({rango_dinamico:.0f} dB < 35 dB)"
                )
            else:
                logger.debug(f"  Banda {banda} Hz: {rango_dinamico:.0f} dB OK")

        # Paso 4: Parametros
        parametros = config["analisis"]["parametros"]
        logger.info(f"Paso 4/5: Calculando parametros: {parametros}")
        for param in parametros:
            for banda in bandas:
                valor = np.random.uniform(0.5, 2.0)
                logger.debug(f"  {param} @ {banda} Hz = {valor:.3f}")

        # Paso 5: Guardar
        logger.info("Paso 5/5: Guardando resultados")
        logger.info("  -> Resultados: resultados.json")
        logger.info("  -> Graficos: resultados/figuras/")

        logger.info("=" * 50)
        logger.info("ANALISIS COMPLETADO EXITOSAMENTE")
        logger.info("=" * 50)

    pipeline_completo("audio/sala_aula.wav")
    return (logging,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 6: Test de integracion completo
    """)
    return


@app.cell
def _(np):
    from scipy import signal

    def test_integracion_pipeline():
        """Test de integracion: pipeline completo con IR sintetica.

        Genera una IR con T60 conocido, ejecuta todo el pipeline,
        y verifica que los resultados estan dentro de la tolerancia.
        """
        # Configuracion
        fs = 44100
        t60_esperado = 1.0
        duracion = 2.5  # segundos (> T60 para tener suficiente decaimiento)
        tolerancia_t60 = 0.1  # ± 100 ms

        print(f"=== Test de Integracion ===")
        print(f"T60 esperado: {t60_esperado} s")
        print(f"Tolerancia: ±{tolerancia_t60} s")
        print()

        # 1. Generar IR sintetica
        t = np.arange(int(duracion * fs)) / fs
        ir = np.exp(-6.908 * t / t60_esperado)
        ir = ir * np.random.choice([-1, 1], size=len(ir))  # signo aleatorio
        print(f"IR generada: {len(ir)} muestras, {duracion} s")

        # 2. Filtrar en banda de 1 kHz
        f_central = 1000
        f_low = f_central / np.sqrt(2)
        f_high = f_central * np.sqrt(2)
        sos = signal.butter(4, [f_low, f_high], btype='band', fs=fs, output='sos')
        ir_filtrada = signal.sosfilt(sos, ir)
        print(f"Filtrado en banda de {f_central} Hz: OK")

        # 3. Integral de Schroeder
        edc = np.cumsum(ir_filtrada[::-1]**2)[::-1]
        edc = edc / edc[0]
        print(f"Integral de Schroeder: OK")

        # 4. Calcular T60 (metodo T30)
        edc_db = 10 * np.log10(edc + 1e-12)
        idx_5 = np.argmax(edc_db < -5)
        idx_35 = np.argmax(edc_db < -35)

        if idx_35 <= idx_5:
            print("ERROR: Rango dinamico insuficiente")
            return

        t_vec = np.arange(len(edc)) / fs
        coef = np.polyfit(t_vec[idx_5:idx_35], edc_db[idx_5:idx_35], 1)
        t60_calculado = -60 / coef[0]

        # 5. Verificar resultado
        error = abs(t60_calculado - t60_esperado)
        print(f"\nResultado:")
        print(f"  T60 calculado: {t60_calculado:.3f} s")
        print(f"  Error: {error:.3f} s ({error/t60_esperado*100:.1f}%)")

        if error < tolerancia_t60:
            print(f"  RESULTADO: PASS")
        else:
            print(f"  RESULTADO: FAIL")

    test_integracion_pipeline()
    return


if __name__ == "__main__":
    app.run()
