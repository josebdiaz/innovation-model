# Modelo CLAVE · Diagnóstico de innovación para Fundación Delirio

Modelo propio para medir el sistema y la cultura de innovación de Fundación Delirio (Cali): 5 pilares, 15 factores y 45 preguntas en una escala de 6 puntos sin punto medio, contado con la metáfora de la son clave 3-2.

Proyecto del **Grupo 4** del módulo "Haciéndolo Posible", Maestría en Gestión de la Innovación, Universidad Icesi. Profesor: Andrés Felipe Naranjo. Equipo: Jose Bolaños, Katherine Castro, María del Mar Espinel, Paola Giraldo y Jorge Mario Murillo.

**Sitio publicado:** https://josebdiaz.github.io/innovation-model/ · **Versión vigente:** [0.9.0](CHANGELOG.md)

## Empieza aquí

| Si quieres… | Ve a |
|---|---|
| Ver los entregables | [Índice publicado](https://josebdiaz.github.io/innovation-model/) |
| Conectar tu IA y publicar hallazgos | [Guía de conexión](https://josebdiaz.github.io/innovation-model/Contexto/guia-conexion-equipo.html) |
| Saber qué tareas hay y quién las tiene | [Documento Ancla](Gestion/documento-ancla.md) |
| Proponer un cambio | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Ver qué cambió y cuándo | [CHANGELOG.md](CHANGELOG.md) |

## Estructura

```
innovation-model/
├── index.html            Portada de GitHub Pages
├── README.md             Este archivo
├── CONTRIBUTING.md       Cómo trabajamos: ramas, pull requests, commits, versiones
├── CHANGELOG.md          Historial de versiones del modelo
├── Gestion/              Cómo se gestiona el proyecto
│   ├── documento-ancla.md    Hoja de ruta y tareas T-01 a T-15
│   ├── decisiones.md         Registro de decisiones
│   └── Reuniones/            Un plan de acción por reunión (Sync-1, Sync-2…)
├── Modelo/               El producto
│   ├── V0/                   Deck, documentos, batería, paleta y elementos separados
│   └── _exploraciones/       Variantes descartadas
├── Hallazgos/            Aportes del equipo: una carpeta por integrante y el registro
├── Contexto/             Contexto para el equipo y sus IA: guía de conexión, contexto del consultor, prompt
├── Herramientas/         Los 10 modelos de referencia en Markdown
├── Curso/                Logs y transcripciones de las sesiones de clase
└── .github/              Responsables de revisión y plantillas de pull request e issues
```

Cada carpeta tiene su propio `README.md` con el detalle.

## Cómo colaborar, en corto

1. Nada entra a `main` sin pull request y revisión de Jose (máximo 48 horas).
2. Una rama por cambio: `hallazgo/`, `modelo/`, `docs/`, `diseno/`, `fix/` o `chore/`.
3. Mensajes de commit con [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/): `feat(modelo): agrega ítem de licencias de IA en A3`.
4. Versiones `X.Y.Z` con etiqueta de Git y nota en el CHANGELOG.

El detalle está en [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

[GPL-3.0](LICENSE).
