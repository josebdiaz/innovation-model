"""Simulación sintética del Pulso de innovación (Modelo CLAVE V0) — 50 personas.

Modelo generador jerárquico (latentes normales estandarizadas):
    g            ~ N(0,1)                      percepción general de innovación
    Pilar_p      = 0.70 g + 0.71 u_p            (r latente entre pilares ≈ 0.49)
    Factor_f     = 0.80 Pilar + 0.60 w_f
    Ítem_k       = 0.80 Factor + 0.60 e_k
    Respuesta    = redondeo( media_ítem + efecto_nivel + efecto_área + estilo + 1.05·Ítem ), acotado 1–6
Se incluyen 2 casos que fallan el control Q0 (uno en línea recta) para probar la limpieza.
Semilla fija: 2026.
"""
import csv, sys
import numpy as np

rng = np.random.default_rng(2026)
OUT = sys.argv[1] if len(sys.argv) > 1 else "respuestas-sinteticas.csv"

P = ["C", "L", "A", "V", "E"]
FACT = [p + str(f) for p in P for f in (1, 2, 3)]
ITEMS = [f + "." + str(k) for f in FACT for k in (1, 2, 3)]

# Perfil base plausible para Delirio (media 1–6 por ítem). Fuerte en escena y aliados; débil en IA, registro y medición.
MU = {
 "C1.1":2.2,"C1.2":3.0,"C1.3":2.6,"C2.1":3.6,"C2.2":4.0,"C2.3":2.9,"C3.1":2.7,"C3.2":3.5,"C3.3":1.9,
 "L1.1":3.7,"L1.2":3.4,"L1.3":3.0,"L2.1":4.1,"L2.2":3.2,"L2.3":4.5,"L3.1":3.6,"L3.2":2.0,"L3.3":3.3,
 "A1.1":2.4,"A1.2":4.0,"A1.3":2.0,"A2.1":2.1,"A2.2":2.6,"A2.3":4.6,"A3.1":1.8,"A3.2":3.8,"A3.3":3.0,
 "V1.1":2.5,"V1.2":2.1,"V1.3":3.6,"V2.1":3.2,"V2.2":2.8,"V2.3":2.6,"V3.1":2.4,"V3.2":2.4,"V3.3":2.6,
 "E1.1":4.9,"E1.2":4.2,"E1.3":4.3,"E2.1":3.4,"E2.2":3.0,"E2.3":4.2,"E3.1":2.6,"E3.2":2.7,"E3.3":3.1,
}

AREAS = ["Dirección General","Producción artística","Producción técnica y logística","Comercial y mercadeo",
         "Administrativa y financiera","Proyectos sociales y formación","Otra"]
N_AREA = [4, 14, 11, 7, 6, 6, 2]
NIV = ["Dirección", "Coordinación o jefatura", "Asistencia, operación o staff"]

# Efecto del nivel jerárquico por pilar (puntos de la escala 1–6): la cabeza ve más que la base.
EF_NIVEL = {
 "Dirección":                     {"C":0.9,"L":0.5,"A":0.5,"V":0.8,"E":0.6},
 "Coordinación o jefatura":       {"C":0.35,"L":0.2,"A":0.2,"V":0.3,"E":0.25},
 "Asistencia, operación o staff": {"C":0,"L":0,"A":0,"V":0,"E":0},
}
# Efectos de área (sobre factores concretos).
EF_AREA = {
 "Producción artística": {"L1":0.4,"L2":0.3,"V3":-0.4,"E1":0.3},
 "Producción técnica y logística": {"L1":-0.3,"C3":-0.4,"A2":-0.3,"E2":0.2},
 "Comercial y mercadeo": {"E1":0.4,"E2":0.4,"A3":0.4,"V1":0.2},
 "Administrativa y financiera": {"A1":0.4,"E1":-0.4,"L2":-0.4,"E3":0.3},
 "Proyectos sociales y formación": {"L2":0.6,"E2":0.4,"A1":0.3,"A2":0.3},
}

# Construir perfiles: Dirección = 4 de Dirección General + 1 en Comercial; jefaturas repartidas.
perfil = []
for a, n in zip(AREAS, N_AREA):
    for j in range(n):
        if a == "Dirección General":
            niv = "Dirección"
        elif a == "Comercial y mercadeo" and j == 0:
            niv = "Dirección"
        elif j < (3 if n >= 10 else 2 if n >= 6 else 0):
            niv = "Coordinación o jefatura"
        else:
            niv = "Asistencia, operación o staff"
        perfil.append([a, niv])
# Ajuste a 13 jefaturas: subir una en "Otra"? no; promover 2 en las áreas grandes
for idx in (10, 24):
    perfil[idx][1] = "Coordinación o jefatura"
rng.shuffle(perfil)

D3 = ["Menos de 1 año", "1 a 3 años", "3 a 5 años", "Más de 5 años"]
D4 = ["Contrato laboral", "Prestación de servicios", "Otro"]

filas = []
for i, (area, niv) in enumerate(perfil):
    d3 = rng.choice(D3, p=[0.18, 0.34, 0.22, 0.26]) if niv != "Dirección" else rng.choice(D3[2:])
    d4 = rng.choice(D4, p=[0.45, 0.48, 0.07]) if niv == "Asistencia, operación o staff" else "Contrato laboral"
    g = rng.normal()
    estilo = rng.normal(0, 0.2)  # aquiescencia individual leve
    r = {"resp_id": f"S{i+1:03d}", "D1": area, "D2": niv, "D3": d3, "D4": d4}
    for p in P:
        lp = 0.70 * g + 0.714 * rng.normal()
        for f in (1, 2, 3):
            fa = p + str(f)
            lf = 0.80 * lp + 0.60 * rng.normal()
            for k in (1, 2, 3):
                it = f"{fa}.{k}"
                y = 0.80 * lf + 0.60 * rng.normal()
                x = MU[it] + EF_NIVEL[niv][p] + EF_AREA.get(area, {}).get(fa, 0) + estilo + 1.05 * y
                r[it] = int(np.clip(np.rint(x), 1, 6))
    r["Q0"] = 2
    filas.append(r)

# Casos de control: S017 responde en línea recta (todo 5) y falla Q0; S041 responde al azar y falla Q0.
for it in ITEMS:
    filas[16][it] = 5
filas[16]["Q0"] = 5
for it in ITEMS:
    filas[40][it] = int(rng.integers(1, 7))
filas[40]["Q0"] = 4
# Un faltante aislado (no invalida el factor: quedan 2 de 3 ítems)
filas[7]["V1.2"] = ""

cols = ["resp_id", "D1", "D2", "D3", "D4", "Q0"] + ITEMS
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(filas)
print("ok", OUT, len(filas))
