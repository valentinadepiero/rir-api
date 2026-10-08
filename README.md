# RIR-API

API REST para procesamiento y analisis de respuestas al impulso segun la norma ISO 3382.
![CI](https://github.com/valentinadepiero/rir-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)

## Descripcion

RIR-API es el trabajo practico de Senales y Sistemas (UNTREF, 2C 2026): una API REST
(FastAPI) con la cadena completa de procesamiento acustico, desde la generacion de senales
de excitacion hasta el calculo de parametros acusticos (EDT, T20, T30, D50, C80) segun
ISO 3382-1.

- Consigna, especificaciones y ruta del TP: <https://maxiyommi.github.io/signal-systems/trabajo_practico/ruta/>
- API de referencia de la catedra (Swagger UI): <https://rir-api.onrender.com/docs>

## Integrantes

Valentina De Piero | Legajo 72221 | Responsable de generación de señales

## Requisitos previos

- Python 3.12 o superior
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes y entornos virtuales)
- git y una cuenta de GitHub

## Instalacion y ejecucion

```bash
# Crear el entorno e instalar dependencias (incluye las de desarrollo: pytest, ruff, ...)
uv sync

# Iniciar la API con hot-reload
uv run uvicorn app.main:app --reload

# Correr los tests
uv run pytest
```

La API queda disponible en `http://localhost:8000`. Documentacion interactiva:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Branching strategy
La idea es mantener la rama "main" protegida y sólo realizar commits a la misma cuando esté comprobada la funcionalidad y compatibilidad de los mergeos correspondentes. Sólo se realizarían cambios a main desde la rama "dev" como etapa previa. Luego, se crearán ramas por integrante que realicen commits a dev para unificarlas.


## Diagrama de estructura
```mermaid
flowchart TB
    C["Cliente<br/>Swagger · frontend · script"]
    subgraph API["RIR-API (FastAPI)"]
        direction TB
        subgraph R["app/routers/"]
            RH["health.py<br/>GET /health"]
            RS["signals.py<br/>POST /signals/pink-noise<br/>POST /signals/sine-sweep"]
            RM2["signals.py<br/>POST /signals/synthetic-ir<br/><br/>filters.py<br/>POST /filters/single-band"]
            RM3["utils.py<br/>POST /utils/smoothing<br/>POST /utils/schroeder<br/>POST /utils/lundeby<br/><br/>acoustics.py<br/>POST /acoustics/parameters"]
        end
        subgraph SC["app/schemas/"]
            SS["signals.py<br/>PinkNoiseRequest<br/>SineSweepRequest"]
            SM2["signals.py<br/>SyntheticIRRequest"]
            SM3["utils.py<br/>SmoothingRequest<br/>SchroederResponse<br/>LundebyResponse<br/><br/>responses.py<br/>BandAnalysisResponse"]
        end
        subgraph SV["app/services/"]
            PN["pink_noise.py<br/>generate_pink_noise"]
            SW["sine_sweep.py<br/>generate_sine_sweep_pair"]
            IO["audio_io.py<br/>play_and_record"]
            VM2["signal_utils.py<br/>load_audio<br/>generate_synthetic_ir<br/>get_impulse_response<br/>logarithmic_scale_conversion<br/><br/>filter.py<br/>filter_single_band"]
            VM3["acoustic_parameters.py<br/>apply_smoothing<br/>apply_schroeder_integral<br/>linear_regression<br/>calculate_parameters_from_ir<br/>apply_lundeby"]
        end
    end
    L["NumPy · SciPy · sounddevice"]
    L2["FastAPI "]
    L3["Pydantic"]
    C -->|"request HTTP + JSON"| RS
    C -->|"sube un WAV"| RM3
    RS -->|"valida con"| SS
    RM2 -->|"valida con"| SM2
    RM3 -->|"valida con"| SM3
    RS -->|"llama a"| PN
    SM2 -->|"llama a"| VM2
    SM3 -->|"llama a"| VM3
    RS -->|"llama a"| SW
    PN --> L
    SW --> L
    IO --> L
    RS --> L2
    RM2 --> L2
    RM3 --> L2
    SS --> L3
    SM2 --> L3
    SM3 --> L3
```

## Estructura del proyecto

```
rir-api/
├── app/
│   ├── __init__.py
│   ├── main.py                    # Punto de entrada FastAPI (/ y /health)
│   ├── settings.py                # Configuracion (pydantic-settings, variables RIR_*)
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py              # GET /health (M0)
│   │   └── audio_http.py          # wav_response y uploaded_file (ya resueltas)
│   ├── schemas/
│   │   └── __init__.py            # Modelos Pydantic de request/response (desde M1)
│   └── services/
│       ├── __init__.py
│       ├── pink_noise.py          # generate_pink_noise (M1)
│       ├── sine_sweep.py          # generate_sine_sweep_pair (M1)
│       ├── audio_io.py            # play_and_record (M1)
│       ├── signal_utils.py        # load_audio, generate_synthetic_ir, get_impulse_response,
│       │                          # logarithmic_scale_conversion (M2)
│       ├── filter.py              # filter_single_band (M2)
│       └── acoustic_parameters.py # apply_smoothing, apply_schroeder_integral, linear_regression,
│                                  # calculate_parameters_from_ir, apply_lundeby (M3)
├── tests/
│   ├── data/                      # WAV chicos de prueba (se versionan)
│   ├── test_placeholder.py        # Test trivial (M0)
│   ├── test_generacion.py         # Tests de M1
│   ├── test_procesamiento.py      # Tests de M2
│   ├── test_analisis.py           # Tests de M3 (services)
│   └── test_api.py                # Tests de endpoints, por milestone (M0 a M3)
├── data/                          # Mediciones y audios locales (ignorado por git)
├── docs/
│   └── README.md                  # Guia para la documentacion (graficas de validacion, etc.)
├── .github/workflows/ci.yml       # CI: ruff + pytest en cada push/PR
├── .gitignore
├── pyproject.toml                 # Dependencias y configuracion (ruff, pytest)
└── README.md
```

## Referencias

- ISO 3382-1:2009 — Acoustics — Measurement of room acoustic parameters.
- Farina, A. (2000). *Simultaneous measurement of impulse response and distortion with a
  swept-sine technique.* 108th AES Convention.
- Schroeder, M. R. (1965). *New method of measuring reverberation time.* JASA 37(3).
- [FastAPI](https://fastapi.tiangolo.com/) · [Pydantic](https://docs.pydantic.dev/) ·
  [uv](https://docs.astral.sh/uv/)
