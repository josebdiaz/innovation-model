# Historial de versiones — Modelo CLAVE

Todos los cambios relevantes del proyecto quedan aquí. El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y la numeración sigue [Versionado Semántico](https://semver.org/lang/es/) adaptado al modelo (ver [CONTRIBUTING.md](CONTRIBUTING.md#versiones)):

- **MAYOR** (`1.0.0`): cambia la estructura del modelo (pilares, factores o número de ítems).
- **MENOR** (`0.9.0`): cambia lo que se mide o cómo se presenta (ítems, escala, puntuación, entregables nuevos o rediseños).
- **PARCHE** (`0.9.1`): correcciones sin efecto en la medición (erratas, enlaces, ajustes visuales menores).

Cada versión publicada tiene una etiqueta `vX.Y.Z` en Git. Cuando un cambio nace de un hallazgo del equipo, la línea cita su código (por ejemplo, `H-001`).

## [Sin publicar]

### Cambiado
- Arquitectura del repositorio: carpetas por función (`Gestion/`, `Curso/`, `Contexto/`, `Herramientas/`, `Hallazgos/`, `Modelo/`), cada una con su README, y nombres de archivo en minúsculas sin espacios ni tildes.
- Este historial pasa de `Modelo/CHANGELOG.md` a la raíz y adopta el formato Keep a Changelog con versiones `X.Y.Z`.
- Los modelos de referencia pasan de `Herramientas/Markdown/` a `Herramientas/` con nombres `autor-tema.md`.
- El plan de acción del Sync 1 pasa a `Gestion/Reuniones/Sync-1/`; la dirección anterior redirige a la nueva.

### Añadido
- `CONTRIBUTING.md`: flujo de trabajo del equipo (ramas, pull requests, mensajes de commit, versiones y revisión).
- `.github/`: responsables de revisión (`CODEOWNERS`), plantilla de pull request con las reglas del profesor y formularios para tareas y errores.
- `Hallazgos/`: carpeta por integrante, plantilla y registro de integración con los tres hallazgos del Sync 1.
- `Gestion/decisiones.md`: registro de decisiones del proyecto.
- `.gitattributes` y `.editorconfig` para finales de línea y codificación uniformes.

## [0.9.0] — 2026-10-10 · paleta validada

### Cambiado
- Paleta recalculada con validación técnica: 4 neutros (tinta #170A33, noche #2E1466, rey #1F4FA8, papel #FFF8E6) y un vivo por pilar (C sol #FFE42A, L rosa #FAAED4, A menta #47D59B, V mango #FA9331, E lila #A5A0F6), cada uno con tono profundo para texto sobre papel y tinte para cajas.
- Deck: solo color. Tokens con nombre de rol (los nombres viejos quedan como alias), cero literales heredados del VHS, cada lámina de pilar con su color, texto y chispas tinta sobre fondos claros, y rampa de madurez rosa → mango → sol → menta. Sin cambios de estructura, texto ni animación.
- Documentos e índice: encabezados en azul rey, tintes derivados de la paleta, bandas de madurez con la misma rampa y blob del one-pager que ya no tapa el texto en pantallas angostas.

### Añadido
- `Modelo/V0/paleta-clave.html` (tokens, roles, contraste, daltonismo y QA visual) y `Modelo/V0/elementos/12-paleta/paleta-clave.json`.
- Validación: todos los vivos ≥ 3,27:1 sobre rey y tinta ≥ 7,9:1 sobre cada vivo; ΔE00 mínimo entre pilares de 12,2 en visión típica, deuteranopía, protanopía y tritanopía (antes 1,3).
- Páginas del equipo: `Contexto/contexto-consultor.html` y `Contexto/guia-conexion-equipo.html`.

## [0.8.0] — 2026-10-10

### Cambiado
- El fondo lavanda (#6E5F8F) se reemplaza por azul rey (#1F4FA8) en el deck, el índice y los documentos: más contraste con el amarillo (6,35:1) y el crema (7,21:1). Decisión del Sync 1 (`H-001`).
- Lilas pálidos de apoyo pasan a azul pálido (#E4ECFA, #DCE6F7) o crema.

### Eliminado
- Maricela Valencia sale de los documentos: ya no hace parte del Grupo 4.

## [0.7.0] — 2026-10-10 · versión congelada

### Añadido
- `ficha-tecnica.html` (descripción técnica y académica del modelo) y `plan-backend-dashboard.html` (arquitectura, consola interna vs. dashboard vivo, cronograma).
- Auditoría WCAG 2.2 AA general (texto y gráficos) en `auditoria-wcag.md`.
- Directorio de elementos separados en `Modelo/V0/elementos/`.

### Cambiado
- Deck: cierre con anillos en clave, etiquetas de la clave legibles, lámina 5 alineada en espejo, ritmo vertical fijo en las láminas de pilar, árbol 5 × 3 × 3 (columna = pilar, fila = factor, punto = pregunta) y diseño de la sesión de 120′ del taller.
- Etiqueta original `v0.7-congelado`; `v0.7.0` apunta al mismo commit.

## [0.6.0] — 2026-10-10

### Añadido
- Sonido real de clave (`clave.wav`, mono 48 kHz, 320 ms, pico −1 dBFS).
- One-pager del racional: `Modelo/V0/onepager-racional.html`.

### Cambiado
- Línea de tiempo de la clave continua (no salta de golpe en golpe), también en la lámina del taller.
- La lámina nueva aparece después de la máscara de blobs.
- Actos como recorrido de píldoras; lámina 5 con nombre de cada letra; lámina de IA sin códigos en cuadros; "Brecha" pasa a llamarse Desafine; foto y video explicados por la medición trimestral.

## [0.5.0] — 2026-10-10

### Cambiado
- La clave estructura la narrativa (5 actos en 3-2) pero ya no se dibuja en todas las láminas: solo en la metáfora, la clave cruzada, tensión/resolución, la ubicación del taller y el cierre.
- Estética recalculada desde el mapping "Los Sabanales": paleta extraída del video, Nunito + Kaushan Script, chispas que titilan, papel recortado con sombra, transición con blobs y palabras que entran con desenfoque. Sin VHS ni neón.

## [0.4.0] — 2026-10-09

### Cambiado
- Formato 16:9 fijo (container units): las láminas se ven igual en cualquier pantalla de presentación.
- Estética inspirada en el video lyric "Hit the road Jack": violeta, coral a magenta, verde neón, piso de cuadrícula, sol synthwave y grano VHS.
- Narrativa en clave 3-2: 5 actos (Por qué · Qué · Cómo | Qué veremos · Qué haremos) con rastreador de golpes.
- Reloj único a 107 BPM (tempo de "Chan Chan"); sonido de clave por síntesis modal, con soporte para un sample real `clave.wav`.
- Lámina 4: los pilares saltan en clave y la V a destiempo. Láminas de IA, de las 45 preguntas y de la regla 1 pregunta = 1 hecho rediseñadas. El taller se ubica en el golpe de Conducción (C1).

## [0.3.0] — 2026-10-09

### Cambiado
- Clave corregida a son clave 3-2: primero tres golpes (C, L, A), luego dos (V, E).
- Los compases se nombran por lo que provocan musicalmente: Tensión (lo que impulsa) y Resolución (lo que resuelve).
- "Cuadre" pasa a llamarse Desfase; la lámina del índice se lee con dos números (Índice CLAVE y Desfase).
- Cada lámina del deck lleva una "Idea clave".

## [0.2.0] — 2026-10-09 · deck animado

### Cambiado
- Se vuelve a la V0 como línea base: su redacción es menos sesgada que la V1.
- `Modelo/V0/modelo-clave-v0.html` pasa a ser un deck animado: tipografía grande, pocas palabras por lámina, movimiento en cada entrada, clave sonora (Web Audio), escala y batería interactivas y notas del presentador (tecla N).

### Eliminado
- La V1 queda archivada en `Modelo/_exploraciones/V1-vocabulario-show/` como exploración descartada.

## V1 (borrador, descartada) — 2026-10-09

- Taxonomía reubicada: Medición → Conducción; Comunicación + Reconocimiento → Visibilidad; Vía = Ideación · Ensayo · Estreno; Efecto = Escena · Público · Comunidad.
- 45 ítems reescritos con vocabulario de Delirio. Se descartó por estar más sesgada que la V0.

## [0.1.0] — 2026-10-09 · visual

### Cambiado
- Página `modelo-clave-v0.html` rediseñada con un sistema de diseño externo (Sintonía DS 3.0). Se descartó en 0.2.0. Contenido del modelo sin cambios.

## [0.0.0] — 2026-10-09 · primera versión

### Añadido
- Megamodelo: 5 pilares (Conducción, Lazos, Activos, Vía, Efecto) × 3 factores × 3 indicadores = 45 ítems.
- Escala Likert de 6 puntos sin punto medio ni "No sé"; bandas de madurez adaptadas de TLA.
- 7 ítems contemporáneos (IA y herramientas digitales) y variables matriciales D1–D4 (D1 provisional hasta T-03).
- Contexto de experiencia previa en Delirio (`Contexto/`).

[Sin publicar]: https://github.com/josebdiaz/innovation-model/compare/v0.9.0...HEAD
[0.9.0]: https://github.com/josebdiaz/innovation-model/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/josebdiaz/innovation-model/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/josebdiaz/innovation-model/releases/tag/v0.7.0
[0.6.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.5.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.4.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.3.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.2.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.1.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
[0.0.0]: https://github.com/josebdiaz/innovation-model/commit/2b6cd3d
