"""Grafica 3 de M3: T30 por banda, RIR-API vs REW, con la tolerancia de +-10 %.

Uso, desde la raiz del repositorio (PowerShell):
    uv run python docs/m3/grafica_validacion_m3.py

Lee de docs/m3/ los JSON de /acoustics/parameters y los .txt exportados de REW,
y guarda docs/m3/validacion_t30.png.
"""

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/m3")
BANDAS = [125, 250, 500, 1000, 2000, 4000]

# Ajustar estos nombres si los archivos se guardaron con otro nombre.
CASOS = [
    ("RI sintética (T60 = 2 s)", "resultado_sintetica.json", "ri_sintetica_REW.txt"),
    ("RI real (con 5 ms de ceros al inicio)", "resultado_real_pad.json", "ri_larga_real_pad_REW.txt"),
]


def leer_rew(ruta: Path) -> dict[int, float]:
    """Devuelve {banda: T30} de las filas de octava del .txt de REW."""
    t30 = {}
    for linea in ruta.read_text(encoding="latin-1").splitlines():
        p = linea.split()
        if len(p) >= 18 and p[1] == "1/1" and p[0].isdigit() and int(p[0]) in BANDAS:
            t30[int(p[0])] = float(p[6])
    return t30


def leer_api(ruta: Path) -> dict[int, float]:
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return {int(float(k)): v for k, v in datos["parameters"]["T30"].items()}


def main() -> None:
    faltan = [n for _, j, r in CASOS for n in (j, r) if not (BASE / n).exists()]
    if faltan:
        disponibles = sorted(p.name for p in BASE.iterdir())
        raise SystemExit(f"Faltan archivos en {BASE}: {faltan}\nHay: {disponibles}")

    fig, ejes = plt.subplots(1, len(CASOS), figsize=(11, 4.2), sharey=True)
    x = range(len(BANDAS))
    for ax, (titulo, json_name, rew_name) in zip(ejes, CASOS):
        api = leer_api(BASE / json_name)
        ref = leer_rew(BASE / rew_name)
        y_api = [api[b] for b in BANDAS]
        y_ref = [ref[b] for b in BANDAS]
        ax.fill_between(
            x,
            [0.9 * v for v in y_ref],
            [1.1 * v for v in y_ref],
            color="#9ecae1",
            alpha=0.5,
            label="Tolerancia ±10 % de REW",
        )
        ax.plot(x, y_ref, "o-", color="#08519c", label="REW (referencia)")
        ax.plot(x, y_api, "s--", color="#d94801", label="RIR-API")
        ax.set_xticks(list(x), [str(b) for b in BANDAS])
        ax.set_title(titulo)
        ax.set_xlabel("Banda de octava (Hz)")
        ax.grid(alpha=0.3)
    ejes[0].set_ylabel("T30 (s)")
    ejes[0].legend(loc="lower left", fontsize=8)
    fig.suptitle("T30 por banda de octava: RIR-API vs REW")
    fig.tight_layout()
    salida = BASE / "validacion_t30.png"
    fig.savefig(salida, dpi=150)
    print(f"Guardado: {salida}")


if __name__ == "__main__":
    main()
