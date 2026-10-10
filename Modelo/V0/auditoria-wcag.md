# Auditoría WCAG 2.2 AA — Modelo CLAVE V0

Fecha: 2026-10-10, actualizada el 2026-10-11 (V0.8, fondo azul rey) · Alcance: deck `modelo-clave-v0.html` (25 láminas, 16:9) y `onepager-racional.html`.
Método: inventario de cada texto y gráfico con significado por lámina, cálculo de contraste WCAG (incluye mezclas por transparencia) y revisión de teclado, movimiento, audio y semántica.

## Paleta y contrastes de texto (1.4.3)

| Texto | Fondo | Ratio | Uso | Estado |
|---|---|---|---|---|
| Amarillo #F7F000 | Azul rey #1F4FA8 | 6.35 | Títulos, cifras | Pasa |
| Crema #FFF8E1 | Azul rey | 7.21 | Texto corrido, etiquetas | Pasa |
| Crema / amarillo | Índigo #3F1F6E | 12.11 / 10.67 | Actos, C, madurez, cierre | Pasa |
| Tinta #1E0A3C | Amarillo | 14.97 | A, regla de oro, taller | Pasa |
| Tinta | Rosa #DE4D74 | 4.66 | Lazos, orquesta, golpes de tensión | Pasa |
| Crema | Rosa | 3.65 | Letra gigante L | Pasa (texto grande) |
| Amarillo | Magenta #C8085D | 4.77 | Efecto, foto/video | Pasa |
| Crema | Bermellón #C2381C | 5.10 | Fichas V, banda Emergiendo, barra 55 | Pasa |
| Tinta / índigo | Jade #5BB68A | 7.31 / 5.21 | Vía, dos números | Pasa |
| Magenta | Crema | 5.42 | Etiqueta "Idea clave" | Pasa |
| Rosa | Tinta | 4.66 | "clave cruzada" en el veredicto | Pasa |
| Crema sobre píldora tinta #1E0A3C | Azul rey | 16.98 | Leyenda de la lámina IA | Pasa |
| Crema al 72 % | Índigo | 6.96 | Actos pendientes | Pasa |

## Gráficos con significado (1.4.11, mínimo 3:1)

| Elemento | Antes | Ahora |
|---|---|---|
| Celdas y puntos "Trabajo digital" (bermellón sobre lavanda) | 1.05–1.38 · falla | Crema rayado / anillo crema: 7.21, y forma distinta a IA (sólido amarillo) |
| ✕ de "sin punto medio" (bermellón sobre lavanda) | 1.33 · falla | Amarillo 6.35 |
| ✓ de las preguntas correctas (verde sobre crema) | 3.38 | Tinta 15.2 |
| Letras CLAVE del cierre sobre el anillo rosa | 3.21 (rozando) | Anillos movidos y reducidos: ya no se superponen |
| Barra de progreso | 7.21 / 14.97 | Pasa |
| Fichas, botones 1–3 y bola V en rosa, magenta o bermellón sobre azul rey | 1.33–1.98 · falla | Anillo crema 7.21 alrededor de cada elemento |
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
