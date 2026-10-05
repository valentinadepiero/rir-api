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
    # Clase 12: Soluciones
    ## Documentacion Moderna

    Estas son soluciones de referencia para los ejercicios de documentacion. Adaptenlas a su proyecto especifico.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 1: Docstrings NumPy-style

    Tres funciones tipicas del TP con docstrings completos:
    """)
    return


@app.cell
def _():
    import numpy as np
    from scipy import signal

    def cargar_audio(ruta, fs_esperado=None):
        """Carga un archivo de audio WAV y retorna la senal y la frecuencia de muestreo.

        Lee un archivo WAV mono. Si el archivo es estereo, se convierte
        a mono promediando los canales. La senal se normaliza al rango [-1, 1].

        Parameters
        ----------
        ruta : str or pathlib.Path
            Ruta al archivo de audio WAV.
        fs_esperado : int, optional
            Frecuencia de muestreo esperada. Si el archivo tiene una
            frecuencia diferente, se emite una advertencia.

        Returns
        -------
        senal : np.ndarray
            Senal de audio normalizada, shape (N,).
        fs : int
            Frecuencia de muestreo en Hz.

        Raises
        ------
        FileNotFoundError
            Si el archivo no existe en la ruta especificada.
        ValueError
            Si el archivo no es un WAV valido o esta corrupto.

        Examples
        --------
        >>> senal, fs = cargar_audio("audio/sala_aula.wav")
        >>> print(f"Duracion: {len(senal)/fs:.2f} s")
        Duracion: 3.20 s
        >>> print(f"Frecuencia: {fs} Hz")
        Frecuencia: 44100 Hz

        Notes
        -----
        Se recomienda usar archivos WAV de 16 o 24 bits con frecuencia
        de muestreo de 44100 Hz o superior para analisis acustico.
        """
        # Implementacion simulada para el ejemplo
        fs = fs_esperado or 44100
        senal = np.random.randn(fs * 3)
        senal = senal / np.max(np.abs(senal))
        return senal, fs

    return (cargar_audio, np, signal)


@app.cell
def _(np, signal):
    def filtrar_banda_octava(senal, fs, frecuencia_central, orden=4):
        """Aplica un filtro pasa-banda de una octava centrado en la frecuencia dada.

        Implementa un filtro Butterworth pasa-banda con frecuencias de corte
        en f_central / sqrt(2) y f_central * sqrt(2), segun IEC 61260-1:2014.

        Parameters
        ----------
        senal : np.ndarray
            Senal de entrada, shape (N,).
        fs : int
            Frecuencia de muestreo en Hz.
        frecuencia_central : float
            Frecuencia central de la banda de octava en Hz.
            Valores tipicos: 125, 250, 500, 1000, 2000, 4000, 8000.
        orden : int, optional
            Orden del filtro Butterworth. Default: 4.

        Returns
        -------
        np.ndarray
            Senal filtrada, misma longitud que la entrada.

        Raises
        ------
        ValueError
            Si la frecuencia central es mayor que fs/2 (Nyquist).

        Examples
        --------
        >>> import numpy as np
        >>> fs = 44100
        >>> t = np.arange(fs) / fs
        >>> senal = np.sin(2 * np.pi * 1000 * t)  # tono de 1 kHz
        >>> filtrada = filtrar_banda_octava(senal, fs, 1000)
        >>> energia_in = np.sum(senal**2)
        >>> energia_out = np.sum(filtrada**2)
        >>> ratio = energia_out / energia_in
        >>> 0.8 < ratio < 1.0  # la mayor parte de la energia pasa
        True

        See Also
        --------
        scipy.signal.butter : Diseno de filtro Butterworth.
        scipy.signal.sosfilt : Filtrado con secciones de segundo orden.
        """
        f_nyquist = fs / 2
        if frecuencia_central >= f_nyquist:
            raise ValueError(
                f"Frecuencia central ({frecuencia_central} Hz) debe ser "
                f"menor que Nyquist ({f_nyquist} Hz)"
            )

        factor = np.sqrt(2)
        f_low = frecuencia_central / factor
        f_high = frecuencia_central * factor

        # Limitar al rango valido
        f_high = min(f_high, f_nyquist * 0.99)

        sos = signal.butter(orden, [f_low, f_high], btype='band', fs=fs, output='sos')
        return signal.sosfilt(sos, senal)

    # Demostrar
    fs_demo = 44100
    t_demo = np.arange(fs_demo) / fs_demo
    senal_demo = np.sin(2 * np.pi * 1000 * t_demo)
    filtrada_demo = filtrar_banda_octava(senal_demo, fs_demo, 1000)
    f"Energia original: {np.sum(senal_demo**2):.1f}, Filtrada: {np.sum(filtrada_demo**2):.1f}"
    return (filtrar_banda_octava,)


@app.cell
def _(np):
    def integral_schroeder(ir):
        """Calcula la integral de Schroeder (Energy Decay Curve) de una respuesta al impulso.

        La integral de Schroeder se calcula como la integral inversa
        acumulada de la energia de la respuesta al impulso:
        EDC(t) = integral desde t hasta infinito de h^2(tau) dtau.

        Parameters
        ----------
        ir : np.ndarray
            Respuesta al impulso, shape (N,).

        Returns
        -------
        np.ndarray
            Curva de decaimiento energetico (EDC) normalizada,
            misma longitud que la entrada. El valor maximo es 1.0.

        Examples
        --------
        >>> import numpy as np
        >>> t = np.arange(44100) / 44100
        >>> ir = np.exp(-6.908 * t)  # decaimiento exponencial
        >>> edc = integral_schroeder(ir)
        >>> edc[0]  # maximo al inicio
        1.0
        >>> edc[-1] < 0.01  # decae al final
        True

        Notes
        -----
        La EDC se calcula segun Schroeder (1965) como la integral
        retroacumulada del cuadrado de la respuesta al impulso.
        Es equivalente al promedio de infinitas curvas de decaimiento
        medidas con ruido interrumpido.

        References
        ----------
        .. [1] Schroeder, M.R. (1965). "New Method of Measuring
           Reverberation Time". J. Acoust. Soc. Am., 37, 409-412.
        """
        energia = ir ** 2
        edc = np.cumsum(energia[::-1])[::-1]
        edc = edc / edc[0]
        return edc

    # Demostrar
    t_demo2 = np.arange(44100) / 44100
    ir_demo = np.exp(-6.908 * t_demo2)
    edc_demo = integral_schroeder(ir_demo)
    f"EDC[0] = {edc_demo[0]:.3f}, EDC[-1] = {edc_demo[-1]:.6f}"
    return (integral_schroeder,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 2: README.md completo

    Template completo para el README del TP:
    """)
    return


@app.cell
def _():
    readme_template = """# AcoustiPy - Analisis Acustico ISO 3382

![CI](https://github.com/usuario/acoustipy/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Herramienta de analisis de parametros acusticos de salas a partir
de respuestas al impulso, siguiendo la norma ISO 3382-1:2009.
Desarrollada como trabajo practico de la materia Senales y Sistemas
(UNTREF, 2026).

## Caracteristicas

- Carga y preprocesamiento de respuestas al impulso (.wav)
- Filtrado en bandas de octava (125 Hz - 8 kHz) con filtros Butterworth
- Calculo de integral de Schroeder (Energy Decay Curve)
- Parametros acusticos: EDT, T20, T30, T60, D50, C80
- Interfaz de linea de comandos (CLI)
- Visualizacion de resultados con Matplotlib
- Exportacion a JSON
- Tests automatizados con pytest + CI con GitHub Actions

## Instalacion

```bash
# Clonar el repositorio
git clone https://github.com/usuario/acoustipy.git
cd acoustipy

# Instalar dependencias
uv sync

# Instalar en modo desarrollo
uv pip install -e .
```

## Uso rapido

### Desde la linea de comandos

```bash
# Analisis basico
acoustipy audio/sala_aula.wav

# Especificar parametros y bandas
acoustipy audio/sala_aula.wav --parametros T60 EDT C80 --bandas 500 1000 2000

# Con configuracion personalizada y graficos
acoustipy audio/sala_aula.wav --config config.toml --graficar

# Ver ayuda
acoustipy --help
```

### Desde Python

```python
from acoustipy.audio import cargar_audio
from acoustipy.filtros import filtrar_bandas_octava
from acoustipy.schroeder import integral_schroeder
from acoustipy.parametros import calcular_t60, calcular_edt

# Cargar respuesta al impulso
ir, fs = cargar_audio("audio/sala_aula.wav")

# Filtrar en banda de 1 kHz
ir_1k = filtrar_bandas_octava(ir, fs, [1000])[1000]

# Calcular EDC e integral de Schroeder
edc = integral_schroeder(ir_1k)

# Calcular parametros
t60 = calcular_t60(edc, fs)
print(f"T60 a 1 kHz: {t60:.2f} s")
```

## Estructura del proyecto

```
acoustipy/
├── src/acoustipy/
│   ├── __init__.py          # Exports principales
│   ├── audio.py             # Carga y preprocesamiento de audio
│   ├── filtros.py           # Filtrado en bandas de octava
│   ├── schroeder.py         # Integral de Schroeder (EDC)
│   ├── parametros.py        # Calculo de parametros acusticos
│   ├── visualizacion.py     # Graficos y figuras
│   └── main.py              # CLI y pipeline principal
├── tests/
│   ├── test_audio.py
│   ├── test_filtros.py
│   ├── test_schroeder.py
│   └── test_parametros.py
├── audio/                   # Respuestas al impulso de ejemplo
├── docs/                    # Documentacion adicional
├── config.toml              # Configuracion por defecto
├── pyproject.toml           # Configuracion del paquete
└── README.md
```

## API

La documentacion completa de la API esta disponible en:
https://usuario.github.io/acoustipy/

### Modulos principales

- `acoustipy.audio`: Carga y preprocesamiento de archivos WAV
- `acoustipy.filtros`: Filtrado en bandas de octava (Butterworth)
- `acoustipy.schroeder`: Integral de Schroeder y EDC
- `acoustipy.parametros`: Calculo de EDT, T20, T30, T60, D50, C80

## Tests

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=acoustipy
```

## Autores

- Nombre Apellido 1 - [GitHub](https://github.com/usuario1)
- Nombre Apellido 2 - [GitHub](https://github.com/usuario2)

## Licencia

MIT License - ver [LICENSE](LICENSE) para mas detalles.

## Referencias

- ISO 3382-1:2009 - Measurement of room acoustic parameters
- Schroeder, M.R. (1965). "New Method of Measuring Reverberation Time"
"""
    print(readme_template)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 5: Configuracion minima de mkdocs

    Archivos necesarios para configurar mkdocs:
    """)
    return


@app.cell
def _():
    mkdocs_yml = """# mkdocs.yml
site_name: AcoustiPy - Documentacion
site_description: Analisis acustico de salas segun ISO 3382
repo_url: https://github.com/usuario/acoustipy

theme:
  name: material
  palette:
    primary: blue
    accent: orange
  features:
    - navigation.sections
    - search.highlight

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: numpy
            show_source: true

nav:
  - Inicio: index.md
  - Instalacion: instalacion.md
  - Uso: uso.md
  - API:
    - audio: api/audio.md
    - filtros: api/filtros.md
    - schroeder: api/schroeder.md
    - parametros: api/parametros.md
  - Contribuir: contribuir.md
"""

    docs_index = """# AcoustiPy

Herramienta de analisis de parametros acusticos de salas
a partir de respuestas al impulso (ISO 3382-1:2009).

## Inicio rapido

```bash
uv pip install -e .
acoustipy audio/sala.wav --parametros T60 EDT C80
```

## Contenido

- [Instalacion](instalacion.md): como instalar el proyecto
- [Uso](uso.md): ejemplos de uso desde CLI y Python
- [API](api/audio.md): referencia completa de funciones
"""

    api_parametros = """# Modulo parametros

Funciones para calcular parametros acusticos segun ISO 3382-1.

::: acoustipy.parametros
"""

    print("=== mkdocs.yml ===")
    print(mkdocs_yml)
    print("\n=== docs/index.md ===")
    print(docs_index)
    print("\n=== docs/api/parametros.md ===")
    print(api_parametros)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Solucion Ejercicio 6: Diagrama Mermaid

    Ejemplo de diagrama de arquitectura para el README:

    ````markdown
    ## Arquitectura

    ```mermaid
    graph TD
        A[archivo.wav] -->|cargar_audio| B[Senal IR]
        B -->|filtrar_bandas_octava| C[Senales filtradas por banda]
        C -->|integral_schroeder| D[EDC por banda]
        D -->|calcular_parametros| E[Resultados]
        E -->|json.dump| F[resultados.json]
        E -->|graficar_resultados| G[Figuras PNG]

        H[config.toml] -->|tomllib.load| I[Configuracion]
        I --> B
        I --> C
        I --> D

        J[CLI argparse] --> I
        J --> A
    ```
    ````

    Este diagrama muestra el flujo de datos desde el archivo de audio hasta los resultados, incluyendo la configuracion y el CLI.
    """)
    return


if __name__ == "__main__":
    app.run()
