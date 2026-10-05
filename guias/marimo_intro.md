# Guía de Marimo — Notebooks Interactivos

## ¿Qué es Marimo?

Marimo es un notebook reactivo para Python que reemplaza a Jupyter. Sus ventajas:

- **Reactivo**: al cambiar una celda, todas las celdas dependientes se actualizan automáticamente
- **Sin estado oculto**: no hay celdas "fantasma" — lo que ves es lo que hay
- **Archivos .py puros**: se pueden versionar con Git sin problemas (no es JSON como .ipynb)
- **Widgets nativos**: sliders, dropdowns, inputs interactivos integrados
- **Reproducible**: siempre da el mismo resultado al ejecutar

---

## Instalación

```bash
# Con uv (recomendado)
uv tool install marimo

# Con pip
pip install marimo
```

---

## Uso básico

```bash
# Crear/editar un notebook
marimo edit mi_notebook.py

# Ejecutar en modo solo lectura (para presentaciones)
marimo run mi_notebook.py

# Convertir un Jupyter notebook existente
marimo convert notebook.ipynb > notebook.py
```

Se abre automáticamente en el navegador.

---

## Estructura de un archivo Marimo

Un notebook Marimo es un archivo `.py` normal con esta estructura:

```python
import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    # Mi Título

    Este es un notebook de ejemplo con **Markdown**.

    Fórmulas LaTeX: $f(t) = A \sin(2\pi f t)$
    """)
    return


@app.cell
def _(np):
    # Generar una senoidal
    fs = 44100
    duracion = 1.0
    frecuencia = 440.0
    t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
    senoidal = np.sin(2 * np.pi * frecuencia * t)
    return fs, t, senoidal, frecuencia


@app.cell
def _(plt, t, senoidal):
    # Graficar (se muestra automáticamente)
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(t[:500], senoidal[:500])
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Amplitud")
    ax.set_title("Senoidal de 440 Hz")
    ax.grid(True)
    fig
    return


if __name__ == "__main__":
    app.run()
```

---

## Reglas importantes

### 1. Cada celda es una función
```python
@app.cell
def _(np, mo):   # Recibe las dependencias como parámetros
    x = np.array([1, 2, 3])
    return (x,)   # Retorna lo que define (tupla)
```

### 2. Las dependencias se pasan como parámetros
Si una celda necesita algo definido en otra celda, lo recibe como parámetro:

```python
@app.cell
def _():
    frecuencia = 440
    return (frecuencia,)

@app.cell
def _(frecuencia):   # ← recibe 'frecuencia' de la celda anterior
    periodo = 1 / frecuencia
    return (periodo,)
```

### 3. La última expresión se muestra
```python
@app.cell
def _(x):
    x * 2    # ← esto se muestra en el output de la celda
    return
```

### 4. Markdown con mo.md()
```python
@app.cell
def _(mo):
    mo.md(r"""
    ## Sección

    Texto con **negrita** y `código`.

    Fórmula: $E = mc^2$
    """)
    return
```

**Nota**: Usar `r"""` (raw string) para evitar problemas con backslashes en LaTeX.

---

## Widgets interactivos

### Slider
```python
@app.cell
def _(mo):
    slider_freq = mo.ui.slider(20, 20000, value=440, label="Frecuencia (Hz)")
    slider_freq
    return (slider_freq,)

@app.cell
def _(slider_freq, np):
    # slider_freq.value contiene el valor actual
    fs = 44100
    t = np.linspace(0, 0.01, int(fs * 0.01))
    senal = np.sin(2 * np.pi * slider_freq.value * t)
    return (senal, t)
```

### Número
```python
@app.cell
def _(mo):
    input_sr = mo.ui.number(value=44100, start=8000, stop=192000, step=100, label="Sample Rate")
    input_sr
    return (input_sr,)
```

### Dropdown
```python
@app.cell
def _(mo):
    selector = mo.ui.dropdown(
        options=["WAV", "FLAC", "MP3"],
        value="WAV",
        label="Formato de audio"
    )
    selector
    return (selector,)
```

### Checkbox
```python
@app.cell
def _(mo):
    mostrar_fase = mo.ui.checkbox(value=False, label="Mostrar fase")
    mostrar_fase
    return (mostrar_fase,)
```

### Text input
```python
@app.cell
def _(mo):
    nombre = mo.ui.text(value="mi_audio", label="Nombre del archivo")
    nombre
    return (nombre,)
```

---

## Gráficos

Matplotlib funciona naturalmente. La última expresión se renderiza:

```python
@app.cell
def _(plt, np, frecuencia):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    t = np.linspace(0, 0.01, 441)
    senal = np.sin(2 * np.pi * frecuencia * t)

    axes[0].plot(t, senal)
    axes[0].set_title("Dominio temporal")
    axes[0].set_xlabel("Tiempo [s]")

    freqs = np.fft.rfftfreq(len(senal), 1/44100)
    espectro = np.abs(np.fft.rfft(senal))
    axes[1].plot(freqs, espectro)
    axes[1].set_title("Espectro")
    axes[1].set_xlabel("Frecuencia [Hz]")

    plt.tight_layout()
    fig  # ← mostrar la figura
    return
```

---

## Tablas

```python
@app.cell
def _(mo):
    data = {
        "Nota": ["A4", "B4", "C5", "D5"],
        "Frecuencia (Hz)": [440, 494, 523, 587],
        "MIDI": [69, 71, 72, 74]
    }
    mo.ui.table(data)
    return
```

---

## Tips para la cursada

1. **Editar**: `marimo edit` para trabajar. **Ejecutar**: `marimo run` para ver sin modificar.
2. **Orden de celdas**: Marimo determina el orden automáticamente por dependencias. No importa en qué orden visual están.
3. **Errores**: Si una celda falla, las dependientes se marcan en rojo. Corregir la celda fuente arregla todo.
4. **Git**: Los archivos `.py` de Marimo se versionan perfectamente. Los diffs son legibles.
5. **No uses variables globales**: Cada celda recibe solo lo que necesita por parámetro.

---

## Comparación con Jupyter

| Aspecto | Jupyter | Marimo |
|---------|---------|--------|
| Formato | .ipynb (JSON) | .py (Python puro) |
| Git diffs | Ilegibles | Limpios y claros |
| Estado oculto | Sí (celdas ejecutadas fuera de orden) | No (reactivo) |
| Reproducibilidad | Depende del orden de ejecución | Siempre reproducible |
| Widgets | Requiere ipywidgets | Nativos e integrados |
| Curva de aprendizaje | Familiar | ~10 min de adaptación |
