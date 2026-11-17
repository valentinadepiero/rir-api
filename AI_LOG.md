\# AI\_LOG.md



\# Log de desarrollo con Inteligencia Artificial



\## GENERAL



Durante el desarrollo del Trabajo Práctico de Señales y Sistemas se utilizaron herramientas de Inteligencia Artificial como apoyo para el aprendizaje, la resolución de problemas, la implementación de funcionalidades y la depuración del código.



Las respuestas obtenidas fueron utilizadas como orientación y debieron ser analizadas, verificadas y adaptadas al contexto del proyecto por los integrantes del grupo.



Este registro documenta las consultas realizadas, los resultados obtenidos y la evaluación del uso de estas herramientas en cada milestone.



\---



\## M0



\*Sección disponible para completar las consultas realizadas durante este milestone.\*



\## M1



\*Sección disponible para completar las consultas realizadas durante este milestone.\*



\## M2



\### Integrante: Lorenzo Carballo



\*\*Herramienta:\*\* ChatGPT (GPT-6)



\*\*Fecha:\*\* 04/11/2026



| Consulta realizada (resumida) | Uso | Resultado obtenido |

|---|---|---|

| Implementación de `logarithmic\_scale\_conversion(signal)`. | Comprender la conversión de amplitud lineal a escala logarítmica, su normalización y el tratamiento de valores nulos. | Se implementó la conversión mediante \\(20\\log\_{10}(|x|/\\max(|x|))\\), utilizando un piso de -120 dB para evitar el logaritmo de cero. |

| Revisión de `generate\_synthetic\_ir` y validación de frecuencias de corte. | Analizar la validación de Nyquist y la reutilización del servicio `filter\_single\_band`. | Se eliminó la validación manual y el recorte de la frecuencia superior, delegando la validación al servicio de filtrado. |

| Resolución de conflictos de integración con Git y GitHub. | Comprender la actualización de ramas, resolución de conflictos, uso de `cherry-pick` y creación de Pull Requests. | Se actualizó la rama con los cambios de `dev`, se separaron los cambios posteriores al merge anterior y se creó el PR #33. |



\*\*Evaluación y reflexión:\*\*



La herramienta resultó útil para comprender las funciones de procesamiento, analizar posibles errores y orientar el flujo de integración con Git.



Las sugerencias fueron revisadas y contrastadas mediante la inspección del código y la ejecución de pruebas automatizadas. Se obtuvieron 35 tests aprobados, 15 xfailed y un 92 % de cobertura.



El proceso permitió comprender mejor la conversión a escala logarítmica, la validación de frecuencias de corte y el manejo de ramas y Pull Requests.


### Integrante: Alexis Nievas
**Herramienta:** Claude (Anthropic)
**Fecha:** 04/11/2026

| Consulta realizada (resumida) | Uso | Resultado obtenido |
|---|---|---|
| Implementación de `get_impulse_response` (deconvolución) en `signal_utils.py`. | Comprender cómo obtener la respuesta al impulso a partir de la señal grabada y el sweep, y cómo estructurar la función. | Se implementó con `fftconvolve`, detección del pico, recorte con `PRE_PICO_MUESTRAS = 256`, normalización y `ValueError` para entradas inválidas. |
| Error `IndentationError` en la línea 92. |
| Limpieza de `ruff` y flujo de Git/GitHub (ramas desde `dev`, Conventional Commits, Pull Requests con base `dev`, reviews cruzadas). | 

**Evaluación y reflexión:**
La herramienta sirvió para entender el método de deconvolución y para ordenar el trabajo con Git paso a paso.
Las sugerencias se verificaron ejecutando `uv run pytest -v -k "impulse_response"` y con `ruff check` y `ruff format --check`; el test de correlación pasa.
Aprendí a distinguir errores de sangría de errores de lógica y a separar los commits de código de los de estilo.


\### Otros integrantes



\*Sección disponible para que los demás integrantes incorporen sus consultas y evaluaciones.\*



\---



\## M3

### Integrante: Alexis Nievas
**Herramienta:** Claude (Anthropic)
**Fecha:** 17/11/2026

| Consulta realizada (resumida) | Uso | Resultado obtenido |
|---|---|---|
| Implementación de `linear_regression(x, y)` (servicio 3). | Comprender las fórmulas de mínimos cuadrados (pendiente, ordenada y R²) y traducirlas a NumPy sin `np.polyfit`. | Se implementó la regresión con sumas explícitas, `ValueError` para entradas inválidas y `R² = 1.0` cuando todos los `y` son iguales. |


**Evaluación y reflexión:**
La herramienta ayudó a entender el método paso a paso.
Las sugerencias se verificaron con `uv run pytest -v -k "linear_regression"` (2 XPASS) y con `ruff check` y `ruff format --check`, ambos en verde.
Pude entender cada fórmula con un ejemplo a mano (`y = 2x + 1`) antes de pasarla a código.

\*Sección disponible para completar las consultas realizadas durante este milestone.\*

### Servicio 4: `calculate_parameters_from_ir`

**Fecha:** 17/11/2026
**Herramienta:** ChatGPT (GPT-6)

#### Consultas y utilización de IA

- Se utilizó ChatGPT para interpretar la especificación del servicio y organizar su implementación.
- Se consultó sobre el cálculo de EDT, T10, T20, T30, D50 y C80 a partir de respuestas al impulso filtradas por bandas de octava.
- Se utilizó como apoyo para integrar el servicio con las funciones existentes: `filter_single_band`, `apply_schroeder_integral` y `linear_regression`.
- Se consultó sobre la integración con FastAPI, el esquema de respuesta y el endpoint `/api/v1/acoustics/parameters`.
- Se utilizó para interpretar errores de Ruff, revisar el formato del código y orientar las pruebas.

#### Verificación y evaluación crítica

Se ejecutaron las pruebas unitarias y de API, además de una prueba manual mediante Swagger utilizando una respuesta al impulso sintética. También se verificó el código con Ruff y se comprobó que el endpoint devolviera correctamente los parámetros acústicos.

Las sugerencias de la IA fueron contrastadas con la especificación del proyecto, el código existente y los resultados de las pruebas. La IA funcionó como herramienta de apoyo, pero la implementación, las modificaciones y la verificación final se realizaron durante el desarrollo del proyecto.