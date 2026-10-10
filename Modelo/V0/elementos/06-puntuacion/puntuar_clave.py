"""Puntuación del Modelo CLAVE V0.

Uso:
    python puntuar_clave.py respuestas.csv [salida.json]

respuestas.csv: una fila por persona, columnas resp_id, D1, D2, D3, D4, Q0 y los 45
códigos de ítem (C1.1 ... E3.3) con valores 1-6 (vacío = faltante).
Solo usa la biblioteca estándar de Python.
"""
import csv
import json
import statistics as st
import sys

PILARES = ["C", "L", "A", "V", "E"]
FACTORES = [p + str(f) for p in PILARES for f in (1, 2, 3)]
ITEMS = [f + "." + str(k) for f in FACTORES for k in (1, 2, 3)]
N_MIN = 5
UMBRAL_DESFASE, UMBRAL_DESAFINE, UMBRAL_SILO = 20, 15, 15
BANDAS = [(85, "Transformando"), (70, "Adaptando"), (50, "Emergiendo"), (0, "Entrando")]


def banda(v):
    return next(nombre for corte, nombre in BANDAS if v >= corte)


def media_valida(vals, minimo=2):
    vals = [v for v in vals if v is not None]
    return st.mean(vals) if len(vals) >= minimo else None


def puntuar_persona(fila):
    s = {}
    for it in ITEMS:
        x = (fila.get(it) or "").strip()
        s[it] = 20 * (int(x) - 1) if x else None
    f = {fa: media_valida([s[fa + "." + str(k)] for k in (1, 2, 3)]) for fa in FACTORES}
    p = {pi: media_valida([f[pi + str(k)] for k in (1, 2, 3)]) for pi in PILARES}
    ps = [v for v in p.values() if v is not None]
    indice = st.mean(ps) if len(ps) == 5 else None
    return s, f, p, indice


def resumen(personas, etiqueta):
    n = len(personas)
    if n < N_MIN:
        return {"grupo": etiqueta, "n": n, "suprimido": True}
    out = {"grupo": etiqueta, "n": n, "suprimido": False, "pilares": {}, "factores": {}}
    for pi in PILARES:
        vals = [x["p"][pi] for x in personas if x["p"][pi] is not None]
        out["pilares"][pi] = round(st.mean(vals), 1) if vals else None
    for fa in FACTORES:
        vals = [x["f"][fa] for x in personas if x["f"][fa] is not None]
        ev = [x["s"][it] for x in personas for it in ITEMS
              if it.startswith(fa + ".") and x["s"][it] is not None]
        out["factores"][fa] = {
            "puntaje": round(st.mean(vals), 1) if vals else None,
            "evidencia_pct": round(100 * sum(1 for v in ev if v >= 80) / len(ev), 1) if ev else None,
        }
    pv = [v for v in out["pilares"].values() if v is not None]
    if len(pv) == 5:
        out["indice_clave"] = round(st.mean(pv), 1)
        out["banda"] = banda(out["indice_clave"])
        out["desfase"] = round(max(pv) - min(pv), 1)
        out["clave_cruzada"] = out["desfase"] > UMBRAL_DESFASE
    return out


def main(entrada, salida=None):
    filas = list(csv.DictReader(open(entrada, encoding="utf-8")))
    personas = []
    for fila in filas:
        if (fila.get("Q0") or "").strip() != "2":  # control de atención: "En desacuerdo"
            continue
        s, f, p, i = puntuar_persona(fila)
        personas.append({"perfil": {k: fila.get(k, "") for k in ("D1", "D2", "D3", "D4")},
                         "s": s, "f": f, "p": p, "i": i})
    res = {"organizacion": resumen(personas, "Delirio"), "por_area": [], "por_nivel": [], "desafine": {}}
    for var, clave in (("D1", "por_area"), ("D2", "por_nivel")):
        for g in sorted({x["perfil"][var] for x in personas}):
            res[clave].append(resumen([x for x in personas if x["perfil"][var] == g], g))
    niveles = {r["grupo"]: r for r in res["por_nivel"] if not r["suprimido"]}
    if "Dirección" in niveles and "Operación" in niveles:
        for pi in PILARES:
            d, o = niveles["Dirección"]["pilares"][pi], niveles["Operación"]["pilares"][pi]
            if d is not None and o is not None:
                res["desafine"][pi] = {"valor": round(d - o, 1), "alerta": abs(d - o) > UMBRAL_DESAFINE}
    areas = [r for r in res["por_area"] if not r["suprimido"]]
    if len(areas) >= 2:
        res["brecha_horizontal"] = {}
        for pi in PILARES:
            v = [a["pilares"][pi] for a in areas if a["pilares"][pi] is not None]
            if len(v) >= 2:
                res["brecha_horizontal"][pi] = {"valor": round(max(v) - min(v), 1),
                                                "silo": max(v) - min(v) > UMBRAL_SILO}
    res["excluidos_por_control"] = len(filas) - len(personas)
    texto = json.dumps(res, ensure_ascii=False, indent=2)
    if salida:
        open(salida, "w", encoding="utf-8").write(texto)
    else:
        print(texto)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
