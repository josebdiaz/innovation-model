# Cómo trabajamos en este repositorio

Guía de colaboración del Grupo 4 para el Modelo CLAVE. Si es tu primera vez, empieza por la [guía de conexión](https://josebdiaz.github.io/innovation-model/Contexto/guia-conexion-equipo.html): explica lo mismo sin tecnicismos.

## Roles

| Rol | Quién | Qué hace |
|---|---|---|
| Responsable del repositorio | Jose Bolaños (`@josebdiaz`) | Revisa y aprueba todo cambio a `main`, integra hallazgos al modelo, publica versiones |
| Integrantes | Katherine Castro, María del Mar Espinel, Paola Giraldo, Jorge Mario Murillo | Leen todo, publican hallazgos en su carpeta y proponen cambios por pull request |

## Reglas de oro

1. **`main` siempre está lista para mostrar.** Es lo que publica GitHub Pages. Nadie sube cambios directo a `main`: todo entra por pull request.
2. **Un cambio, una rama, un pull request.** Si mezclas dos temas, se revisan y se deshacen peor.
3. **Nada se borra para "limpiar".** Lo descartado se mueve a una carpeta de archivo (`Modelo/_exploraciones/`) y se anota en el [historial](CHANGELOG.md).
4. **Las reglas del profesor aplican a todo cambio del modelo:** una sola idea por pregunta, simetría 5 × 3 × 3, hechos observables, escala sin punto medio y comparación matricial.

## Flujo de trabajo (GitHub Flow)

```
main ──●────────────●────────────●──  (protegida, publicada)
        \          / \          /
         ●──●──●──●   ●──●──●──●      rama corta → pull request → revisión → fusión
```

1. Crea una rama desde `main` con el nombre `tipo/tema-corto`:

   | Prefijo | Para qué | Ejemplo |
   |---|---|---|
   | `hallazgo/` | Un hallazgo nuevo en `Hallazgos/<tu-carpeta>/` | `hallazgo/paola-indice-andi` |
   | `modelo/` | Cambios a ítems, factores, escala o puntuación | `modelo/c1-redaccion` |
   | `docs/` | Documentos, guías, README | `docs/guia-gemini` |
   | `diseno/` | Cambios visuales de páginas o deck | `diseno/menu-navegacion` |
   | `fix/` | Errores: enlaces rotos, erratas | `fix/enlace-ficha` |
   | `chore/` | Orden del repositorio, configuración | `chore/arquitectura-repo` |

   Si subes un archivo desde el navegador, GitHub crea la rama solo (`usuario-patch-1`). Está bien así.
2. Haz tus cambios y guárdalos con mensajes claros (ver abajo).
3. Abre un pull request hacia `main`. La plantilla te pide revisar las reglas del profesor.
4. Jose revisa en máximo **48 horas**. Puede aprobar, pedir ajustes o explicar por qué no entra.
5. Se fusiona con **Squash and merge** (un solo commit por pull request en `main`) y se borra la rama.

## Mensajes de commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) en español:

```
tipo(alcance): qué cambió, en presente y en menos de 72 caracteres

Por qué cambió, si no es obvio. Cita hallazgos (H-004) o tareas (T-07).
```

- **Tipos:** `feat` (algo nuevo), `fix` (corrección), `docs` (documentación), `style` (solo visual), `refactor` (reorganizar sin cambiar el resultado), `chore` (mantenimiento).
- **Alcances:** `modelo`, `deck`, `docs`, `hallazgos`, `gestion`, `curso`, `repo`.
- **Ejemplos:** `feat(modelo): agrega ítem de licencias de IA en A3` · `fix(deck): corrige contraste de la lámina E` · `docs(hallazgos): registra H-004 índice ANDI`.

## Versiones

El modelo usa [Versionado Semántico](https://semver.org/lang/es/) adaptado:

| Cambio | Sube | Ejemplo |
|---|---|---|
| Estructura del modelo: pilares, factores o número de ítems | **Mayor** | `0.9.0` → `1.0.0` |
| Lo que se mide o cómo se presenta: ítems, escala, puntuación, entregables nuevos | **Menor** | `0.9.0` → `0.10.0` |
| Correcciones sin efecto en la medición | **Parche** | `0.9.0` → `0.9.1` |

Mientras la versión empiece por `0.`, el modelo está en construcción. La `1.0.0` es la versión que se aplica en Delirio.

**Para publicar una versión** (solo Jose):

1. Mueve lo que está en `[Sin publicar]` del [CHANGELOG](CHANGELOG.md) a una sección con el número y la fecha.
2. Fusiona ese cambio a `main`.
3. Crea la etiqueta y súbela:
   ```bash
   git tag -a v0.10.0 -m "Modelo CLAVE 0.10.0: resumen corto"
   git push origin v0.10.0
   ```
4. En GitHub: **Releases → Draft a new release**, elige la etiqueta y pega las notas del CHANGELOG. Las versiones presentadas al profesor se marcan como "congeladas" en el título.

## Hallazgos

Cada integrante publica en `Hallazgos/<su-carpeta>/` con la [plantilla](Hallazgos/_plantilla.md). Jose asigna un código (`H-001`, `H-002`…) y una decisión en el [registro](Hallazgos/registro.md): **integrado**, **parcial**, **en espera** o **descartado**, siempre con la razón. Si un hallazgo cambia el modelo, el CHANGELOG lo cita.

## Nombres y carpetas

- Archivos en minúsculas, con guiones, sin espacios, tildes ni ñ: `plan-accion-sync1.html`, no `Plan de Acción Sync 1.html`.
- Cada carpeta tiene un `README.md` que dice qué contiene.
- Las páginas publicadas no cambian de dirección. Si hay que moverlas, la dirección vieja se deja como redirección.
- Videos, audios de referencia y PDF pesados no se suben: quedan en `Referencias/` (excluida en `.gitignore`) o en Drive.

## Configuración de GitHub (una sola vez, Jose)

- **Settings → Collaborators:** invitar a cada integrante con permiso **Write**.
- **Settings → Branches → Add branch ruleset** (o *branch protection rule*) para `main`: exigir pull request con 1 aprobación, exigir revisión de *Code Owners*, bloquear *force push* y borrado. Dejar a los administradores como excepción para emergencias.
- **Settings → General → Pull Requests:** dejar solo **Allow squash merging** y activar **Automatically delete head branches**.
- **Settings → Pages:** rama `main`, carpeta `/ (root)`.
