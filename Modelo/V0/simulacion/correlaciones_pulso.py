"""Puntuación CLAVE + evaluación de correlaciones del Pulso (datos sintéticos)."""
import json, sys
import numpy as np, pandas as pd
from scipy import stats

src = sys.argv[1] if len(sys.argv) > 1 else "respuestas-sinteticas.csv"
outdir = sys.argv[2] if len(sys.argv) > 2 else "."
raw = pd.read_csv(src)
P = ["C", "L", "A", "V", "E"]
NOM = {"C": "Conducción", "L": "Lazos", "A": "Activos", "V": "Vía", "E": "Efecto"}
FACT = [p + str(f) for p in P for f in (1, 2, 3)]
ITEMS = [f + "." + str(k) for f in FACT for k in (1, 2, 3)]

# --- Limpieza (08-calidad) ---
linea = raw[ITEMS].nunique(axis=1) == 1
d = raw[raw.Q0 == 2].copy()
excl = raw[raw.Q0 != 2].resp_id.tolist()
n = len(d)

# --- Puntuación (06-puntuacion) ---
S = (d[ITEMS] - 1) * 20
F = pd.DataFrame({fa: S[[f"{fa}.{k}" for k in (1, 2, 3)]].apply(lambda r: r.mean() if r.notna().sum() >= 2 else np.nan, axis=1) for fa in FACT})
PIL = pd.DataFrame({p: F[[p + str(k) for k in (1, 2, 3)]].mean(axis=1) for p in P})
PIL["Índice"] = PIL[P].mean(axis=1)

def banda(v):
    return "Transformando" if v >= 85 else "Adaptando" if v >= 70 else "Emergiendo" if v >= 50 else "Entrando"

org = {p: round(PIL[p].mean(), 1) for p in P + ["Índice"]}
org["banda"] = banda(org["Índice"]); org["desfase"] = round(max(org[p] for p in P) - min(org[p] for p in P), 1)
niv = PIL.join(d[["D1", "D2"]]).groupby("D2")[P + ["Índice"]].agg(["mean", "count"])
por_nivel = {g: {p: round(niv.loc[g, (p, "mean")], 1) for p in P + ["Índice"]} | {"n": int(niv.loc[g, ("C", "count")])} for g in niv.index}
desafine = {p: round(por_nivel["Dirección"][p] - por_nivel["Asistencia, operación o staff"][p], 1) for p in P}
ar = PIL.join(d[["D1"]]).groupby("D1")[P].agg(["mean", "count"])
por_area = {g: {p: round(ar.loc[g, (p, "mean")], 1) for p in P} | {"n": int(ar.loc[g, ("C", "count")])} for g in ar.index}
areas_ok = [g for g in por_area if por_area[g]["n"] >= 5]
brecha_h = {p: round(max(por_area[g][p] for g in areas_ok) - min(por_area[g][p] for g in areas_ok), 1) for p in P}

# --- Correlaciones ---
def r_ci(r, n):
    z, se = np.arctanh(r), 1 / np.sqrt(n - 3)
    return float(np.tanh(z - 1.96 * se)), float(np.tanh(z + 1.96 * se))

pares = []
for i, a in enumerate(P):
    for b in P[i + 1:]:
        x = PIL[[a, b]].dropna()
        r, pv = stats.pearsonr(x[a], x[b]); rho, prho = stats.spearmanr(x[a], x[b])
        lo, hi = r_ci(r, len(x))
        pares.append({"a": a, "b": b, "r": round(r, 3), "p": float(pv), "ic95": [round(lo, 2), round(hi, 2)], "rho": round(rho, 3), "p_rho": float(prho)})
R_pil = PIL[P].corr(method="pearson").round(3)
R_fac = F.corr(method="spearman").round(3)
R_it = d[ITEMS].corr(method="spearman")

# promedios de r entre ítems: mismo factor / mismo pilar (otro factor) / otro pilar
def avg(mask):
    v = R_it.values[mask]; return round(float(np.nanmean(v)), 3)
pil_of = np.array([c[0] for c in ITEMS]); fac_of = np.array([c[:2] for c in ITEMS])
off = ~np.eye(len(ITEMS), dtype=bool)
same_f = (fac_of[:, None] == fac_of[None, :]) & off
same_p = (pil_of[:, None] == pil_of[None, :]) & ~(fac_of[:, None] == fac_of[None, :])
other_p = pil_of[:, None] != pil_of[None, :]
estructura = {"mismo_factor": avg(same_f), "mismo_pilar_otro_factor": avg(same_p), "otro_pilar": avg(other_p)}

# alfa de Cronbach y correlación ítem-resto por pilar
def alpha(X):
    X = X.dropna(); k = X.shape[1]
    return float(k / (k - 1) * (1 - X.var(ddof=1).sum() / X.sum(axis=1).var(ddof=1)))
fiab = {}
item_rest = {}
for p in P:
    cols = [c for c in ITEMS if c[0] == p]; X = d[cols].dropna()
    fiab[p] = {"alfa": round(alpha(X), 3), "media_r_inter_item": round(float(X.corr().values[np.triu_indices(9, 1)].mean()), 3)}
    for c in cols:
        rest = X.drop(columns=c).sum(axis=1)
        item_rest[c] = {"r_item_resto": round(float(stats.pearsonr(X[c], rest)[0]), 3),
                        "alfa_si_se_elimina": round(alpha(X.drop(columns=c)), 3)}
alfa_total = round(alpha(d[ITEMS]), 3)
alfa_fac = {fa: round(alpha(d[[f"{fa}.{k}" for k in (1, 2, 3)]]), 3) for fa in FACT}

# correlación de pilares con jerarquía (ordinal) y antigüedad
ordn = {"Asistencia, operación o staff": 1, "Coordinación o jefatura": 2, "Dirección": 3}
ordt = {"Menos de 1 año": 1, "1 a 3 años": 2, "3 a 5 años": 3, "Más de 5 años": 4}
jer = {}
for p in P + ["Índice"]:
    rho, pv = stats.spearmanr(d.D2.map(ordn), PIL[p]); rt, pt = stats.spearmanr(d.D3.map(ordt), PIL[p])
    jer[p] = {"rho_nivel": round(rho, 3), "p_nivel": float(pv), "rho_antiguedad": round(rt, 3), "p_antiguedad": float(pt)}

# KMO y Bartlett (adecuación muestral) sobre los 45 ítems
Xc = d[ITEMS].dropna(); Rm = Xc.corr().values
try:
    inv = np.linalg.inv(Rm); Dg = np.diag(1 / np.sqrt(np.diag(inv))); Pc = -Dg @ inv @ Dg
    m = ~np.eye(45, dtype=bool); kmo = float((Rm[m] ** 2).sum() / ((Rm[m] ** 2).sum() + (Pc[m] ** 2).sum()))
except np.linalg.LinAlgError:
    kmo = None
sign, logdet = np.linalg.slogdet(Rm)
nb = len(Xc); chi2 = -(nb - 1 - (2 * 45 + 5) / 6) * logdet; dfb = 45 * 44 / 2
bart = {"chi2": round(float(chi2), 1), "gl": int(dfb), "p": float(stats.chi2.sf(chi2, dfb)), "det_R": float(np.exp(logdet)) if sign > 0 else 0.0,
        "rango_R": int(np.linalg.matrix_rank(Rm)), "n_validos_completos": nb}

# r crítico para p<.05 bilateral con n
tcrit = stats.t.ppf(0.975, n - 2); r_crit = float(tcrit / np.sqrt(n - 2 + tcrit ** 2))

top_pairs = []
iu = np.triu_indices(45, 1)
vals = R_it.values[iu]
for idx in np.argsort(-np.abs(vals))[:8]:
    top_pairs.append({"a": ITEMS[iu[0][idx]], "b": ITEMS[iu[1][idx]], "rho": round(float(vals[idx]), 3)})
ia = ["C3.3", "A1.3", "A3.1", "A3.3", "V2.3"]
r_ia = round(float(d[ia].corr(method="spearman").values[np.triu_indices(5, 1)].mean()), 3)

res = {"n_total": len(raw), "n_validos": n, "excluidos_Q0": excl, "linea_recta": raw[linea].resp_id.tolist(),
       "organizacion": org, "por_nivel": por_nivel, "desafine_dir_menos_operacion": desafine,
       "por_area": por_area, "brecha_horizontal": brecha_h, "r_critico_p05": round(r_crit, 3),
       "pilares_pares": pares, "matriz_pilares": R_pil.to_dict(), "estructura_inter_item": estructura,
       "fiabilidad_pilar": fiab, "alfa_total_45": alfa_total, "alfa_factor": alfa_fac, "item_resto": item_rest,
       "pilar_vs_perfil": jer, "kmo": None if kmo is None else round(kmo, 3), "bartlett": bart,
       "top_pares_items": top_pairs, "media_r_items_IA": r_ia,
       "matriz_factores_spearman": R_fac.to_dict(), "matriz_items_spearman": R_it.round(3).to_dict()}
json.dump(res, open(f"{outdir}/resultados-correlacion.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
R_pil.to_csv(f"{outdir}/matriz-pilares-pearson.csv"); R_fac.to_csv(f"{outdir}/matriz-factores-spearman.csv")
R_it.round(3).to_csv(f"{outdir}/matriz-items-spearman.csv")
PIL.round(1).join(d[["resp_id", "D1", "D2"]]).to_csv(f"{outdir}/puntajes-persona.csv", index=False)
print(json.dumps({k: res[k] for k in ["n_validos", "excluidos_Q0", "organizacion", "por_nivel", "desafine_dir_menos_operacion", "brecha_horizontal", "r_critico_p05", "pilares_pares", "estructura_inter_item", "fiabilidad_pilar", "alfa_total_45", "pilar_vs_perfil", "kmo", "bartlett", "top_pares_items", "media_r_items_IA"]}, ensure_ascii=False, indent=1))
print({c: v for c, v in item_rest.items() if v["r_item_resto"] < 0.30})
print(alfa_fac)
