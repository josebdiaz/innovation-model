# 06 · Algoritmo de puntuación

```
Ítem              s = 20 × (x − 1)                      x ∈ {1..6} → 0 a 100
Factor            F = media de sus 3 ítems              válido con ≥ 2 de 3
Pilar             P = media de sus 3 factores           válido con ≥ 2 de 3
Índice CLAVE      I = Σ 0,20 × P                        promedio de los 5 pilares
Evidencia         E = % de respuestas ≥ 5               por ítem, factor o pilar
Desfase           D = máx(P̄) − mín(P̄)                   > 20 = clave cruzada
Desafine          Δ = P̄ Dirección − P̄ Operación         por pilar · > 15 = alerta
Brecha horizontal H = máx área − mín área               por pilar · > 15 = silo
```

- Agregado organizacional: media de los encuestados válidos, con desviación estándar e intervalo bootstrap al 95 % (cálculo fuera de línea).
- Se excluyen los casos que fallan el control de atención (Q0 distinto de 2).
- Ningún grupo con n < 5 se publica.
- Pesos iguales *a priori*; se recalibran tras la primera medición. Bandas y umbrales son convenciones interpretativas sujetas a calibración (ver `ficha-tecnica.html`).

Implementación de referencia: `puntuar_clave.py` (solo biblioteca estándar de Python).
