# Auditoría WCAG 2.2 AA — Modelo CLAVE V0

Fecha: 2026-10-10, actualizada el 2026-10-10 (V0.8, fondo azul rey; V0.9, paleta validada) · Alcance: deck `modelo-clave-v0.html` (25 láminas, 16:9) y `onepager-racional.html`.
Método: inventario de cada texto y gráfico con significado por lámina, cálculo de contraste WCAG (incluye mezclas por transparencia) y revisión de teclado, movimiento, audio y semántica.

## Paleta y contrastes de texto (1.4.3)

Paleta V0.9 (2026-10-10). Detalle, tokens y validación bajo daltonismo en `paleta-clave.html` y `elementos/12-paleta/paleta-clave.json`.

| Texto | Fondo | Ratio | Uso | Estado |
|---|---|---|---|---|
| Sol #FFE42A | Rey #1F4FA8 | 5.97 | Títulos, cifras | Pasa |
| Papel #FFF8E6 | Rey | 7.23 | Texto corrido, etiquetas | Pasa |
| Papel / sol | Noche #2E1466 | 14.08 / 11.63 | Actos, La clave, Madurez, Cierre, tarjetas "Idea clave" | Pasa |
| Tinta #170A33 | Sol | 14.53 | Lámina C, regla de oro, taller | Pasa |
| Tinta / noche | Rosa #FAAED4 | 10.70 / 8.57 | Lámina L, orquesta, golpes de tensión | Pasa |
| Tinta / noche | Menta #47D59B | 9.98 / 8.00 | Lámina A, dos números | Pasa |
| Tinta / noche | Mango #FA9331 | 8.23 / 6.59 | Lámina V, banda Emergiendo | Pasa |
| Tinta / noche | Lila #A5A0F6 | 7.94 / 6.36 | Lámina E, foto y video | Pasa |
| Rosa profundo #B02A6B | Papel | 5.85 | Etiqueta "Idea clave" sobre papel, bloque de medición del taller | Pasa |
| Rosa | Tinta | 10.70 | "clave cruzada" en el veredicto | Pasa |
| Papel sobre píldora tinta | Rey | 17.58 | Leyenda de la lámina IA, cromo | Pasa |
| Papel al 72 % | Noche | 7.80 | Actos pendientes | Pasa |

Regla V0.9: todo fondo claro (sol, rosa, menta, mango, lila, papel) lleva texto tinta o noche; los vivos solo se usan como texto sobre rey, noche o tinta; sobre papel se usa su tono profundo (-d, ≥ 5.26:1).

## Gráficos con significado (1.4.11, mínimo 3:1)

| Elemento | Antes | Ahora |
|---|---|---|
| Celdas y puntos "Trabajo digital" (bermellón sobre lavanda) | 1.05–1.38 · falla | Crema rayado / anillo crema: 7.21, y forma distinta a IA (sólido amarillo) |
| ✕ de "sin punto medio" (bermellón sobre lavanda) | 1.33 · falla | Amarillo 6.35 |
| ✓ de las preguntas correctas (verde sobre crema) | 3.38 | Tinta 15.2 |
| Letras CLAVE del cierre sobre el anillo rosa | 3.21 (rozando) | Anillos movidos y reducidos: ya no se superponen |
| Barra de progreso | 7.21 / 14.97 | Pasa |
| Fichas, botones 1–3 y bola V en rosa, magenta o bermellón sobre azul rey | 1.33–1.98 · falla | V0.9: los cinco vivos dan 3.27–5.97 sobre rey por sí solos; el anillo papel se mantiene como refuerzo |
| Barra A (menta) sobre la lámina menta "Dos números" | 1.0 · falla | Contorno tinta 9.98 |
| Cinco pilares bajo daltonismo (ΔE00 entre pares) | Mínimo 1.3 (bermellón–magenta, tritanopía) | Mínimo 12.2 (sol–mango, deuteranopía); la letra acompaña siempre al color (1.4.1) |
| Foco: contorno tinta + halo amarillo | 3.18 / 4.71 | Pasa sobre todos los fondos |
| Nombres bajo los golpes de la clave (lámina 3) | Tinta sobre índigo ≈ 1.3 · falla (heredaban el color del círculo) | Crema sobre índigo 12.11; tinta sobre fondos claros |

## Menú y controles

- Barra de control y etiqueta de acto con fondo propio (tinta + crema 15.2): legibles sobre cualquier lámina.
- Estado activo de Sonido / Pausa / Notas: amarillo con texto tinta.
- Botones de 44 px de alto mínimo; fichas de las 45 ≥ 24 px (2.5.8).

## Movimiento, audio y semántica

- Botón Pausa (tecla P) detiene todas las animaciones en bucle (2.2.2); `prefers-reduced-motion` las desactiva y quita la transición de manchas.
- Sonido solo por acción del usuario, con control (1.4.2).
- Idioma español (3.1.1); anunciador "Lámina N de 25: título"; láminas ocultas con `inert` (4.1.2).
- Navegación completa por teclado: flechas, Inicio/Fin, N, S, P.
- Las categorías nunca dependen solo del color (1.4.1): IA y digital se distinguen también por forma; los pilares llevan letra y nombre.

## One-pager

Todos los textos pasan AA: el más bajo es magenta sobre el recuadro de límites (4.64).

## Pendiente de verificar en dispositivo

- Recorrido con VoiceOver.
- Zoom al 200 % del navegador (1.4.4).
