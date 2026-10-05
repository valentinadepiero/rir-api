# Análisis Básico de Señales Sinusoidales

Este proyecto genera y analiza señales sinusoidales simples. Permite calcular estadísticas básicas, la energía de la señal y generar señales compuestas.

## Estructura del Proyecto

```
signal-analysis-project
├── src
│   ├── code_res.py                # Archivo principal que ejecuta el análisis
│   ├── utils                      # Módulo con funciones auxiliares
│   │   ├── __init__.py            # Archivo para inicializar el módulo
│   │   ├── generar_senoidal.py    # Función para generar señales sinusoidales
│   │   ├── calcular_estadisticas.py # Función para calcular estadísticas
│   │   ├── calcular_energia.py    # Función para calcular la energía de una señal
│   │   └── generar_señal_compuesta.py # Función para generar señales compuestas
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Documentación del proyecto
```

## Instalación

Para configurar el proyecto, necesitas tener Python instalado en tu máquina. Luego, puedes instalar las dependencias necesarias utilizando `pip`.

1. Clona el repositorio:
   ```bash
   git clone <repository-url>
   cd signal-analysis-project
   ```

2. Instala los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar el análisis de señales, ejecuta el script principal:

```bash
python src/code_res.py
```

Puedes modificar los parámetros en `code_res.py` para cambiar la frecuencia, amplitud y duración de las señales que se analizan.

## Funcionalidades

- **Generar señales sinusoidales**: Usa la función `generar_senoidal` para crear señales con parámetros personalizados.
- **Calcular estadísticas**: Obtén el valor máximo, mínimo, medio y la desviación estándar de la señal.
- **Calcular energía**: Calcula la energía total de la señal como la suma de los cuadrados de sus valores.
- **Generar señales compuestas**: Combina dos señales sinusoidales para crear una señal más compleja.

## Contribuciones

Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.