import sys, json, itertools
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from val_paleta import *

N = {'tinta': '#170A33', 'noche': '#2E1466', 'rey': '#1F4FA8', 'papel': '#FFF8E6'}
V = {'sol': '#FFE42A', 'rosa': '#FAAED4', 'menta': '#47D59B', 'mango': '#FA9331', 'lila': '#A5A0F6'}
D = {'sol': '#7D6400', 'rosa': '#B02A6B', 'menta': '#0A7751', 'mango': '#A84B00', 'lila': '#5A4FC4'}
T = {'sol': '#FFF6C7', 'rosa': '#FFE7F2', 'menta': '#D6F7E8', 'mango': '#FFEADB', 'lila': '#ECEBFD'}
OLD = {'amarillo': '#F7F000', 'coral': '#DE4D74', 'jade': '#5BB68A', 'bermellón': '#C2381C', 'magenta': '#C8085D'}
PIL = {'sol': ('C', 'Conducción'), 'rosa': ('L', 'Lazos'), 'menta': ('A', 'Activos'), 'mango': ('V', 'Vía'), 'lila': ('E', 'Efecto')}
SIMS = [(None, 'Visión típica'), ('deuter', 'Deuteranopía'), ('protan', 'Protanopía'), ('tritan', 'Tritanopía')]

def tohex(rgb):
    return '#' + ''.join('%02X' % max(0, min(255, round(c * 255))) for c in rgb)

def simhex(h, s):
    r = sim(h, s)
    return r if isinstance(r, str) else tohex(r)

def f(x):
    return ('%.2f' % x).replace('.', ',')

def f1(x):
    return ('%.1f' % x).replace('.', ',')

def worst(P):
    m = (99, None, None)
    for (a, x), (b, y) in itertools.combinations(P.items(), 2):
        for s, _ in SIMS:
            d = de00(x, y) if s is None else de00(simhex(x, s), simhex(y, s))
            if d < m[0]:
                m = (d, a + '–' + b, s)
    return m

wn = worst(V); wo = worst(OLD)
simname = dict(SIMS)

# ---------- secciones ----------
def sw(name, hexv, role, fg):
    return f'<div class="sw" style="background:{hexv};color:{fg}"><b>{name}</b><code>{hexv}</code><span>{role}</span></div>'

neutros = ''.join([
    sw('tinta', N['tinta'], 'Texto y cromo', N['papel']),
    sw('noche', N['noche'], 'Tarjetas y láminas de acento', N['papel']),
    sw('rey', N['rey'], 'Fondo base (decisión Sync 1)', N['papel']),
    sw('papel', N['papel'], 'Fondo de documentos y tarjetas', N['tinta']),
])
vivos = ''.join(sw(k, V[k], f'{PIL[k][0]} · {PIL[k][1]}', N['tinta']) for k in V)
prof = ''.join(sw(k + '-d', D[k], 'Texto sobre papel', N['papel']) for k in D)
tint = ''.join(sw(k + '-t', T[k], 'Cajas y filas', N['tinta']) for k in T)

def cell(x, lim):
    cls = 'ok' if x >= lim else 'ko'
    return f'<td class="n {cls}">{f(x)}</td>'

rows_c = ''
for k in V:
    rows_c += (f'<tr><th scope="row"><i class="dot" style="background:{V[k]}"></i>{k}</th>'
               + cell(cr(V[k], N['rey']), 3) + cell(cr(V[k], N['noche']), 3) + cell(cr(N['tinta'], V[k]), 4.5)
               + cell(cr(D[k], N['papel']), 4.5) + cell(cr(D[k], T[k]), 4.5) + cell(cr(N['tinta'], T[k]), 4.5) + '</tr>')
neutral_rows = ''.join(
    f'<tr><td>{a} sobre {b}</td>{cell(cr(N[a], N[b]), 4.5)}</tr>'
    for a, b in [('papel', 'rey'), ('papel', 'noche'), ('papel', 'tinta'), ('tinta', 'papel')])
rows_old = ''.join(
    f'<tr><th scope="row"><i class="dot" style="background:{v}"></i>{k}</th>{cell(cr(v, N["rey"]), 3)}</tr>' for k, v in OLD.items())

rows_de = ''
for (a, x), (b, y) in itertools.combinations(V.items(), 2):
    tds = ''
    for s, _ in SIMS:
        d = de00(x, y) if s is None else de00(simhex(x, s), simhex(y, s))
        tds += f'<td class="n {"ok" if d >= 12 else "ko"}">{f1(d)}</td>'
    rows_de += f'<tr><th scope="row"><i class="dot" style="background:{x}"></i><i class="dot" style="background:{y}"></i>{a}–{b}</th>{tds}</tr>'

strips = ''
for s, lab in SIMS:
    cells_n = ''.join(f'<i style="background:{V[k] if s is None else simhex(V[k], s)}"><b>{PIL[k][0]}</b></i>' for k in V)
    cells_o = ''.join(f'<i style="background:{v if s is None else simhex(v, s)}"></i>' for v in OLD.values())
    strips += f'<div class="sim"><span>{lab}</span><div class="strip">{cells_n}</div><div class="strip old">{cells_o}</div></div>'

QA = [
    ('Alta', 'Deck', 'Tres rojos (coral, magenta y bermellón) competían entre sí. Bermellón y magenta quedan a ΔE00 1,3 en tritanopía: son el mismo color.', 'Un solo rosa. V pasa a mango y E a lila: cinco tonos separados en el círculo cromático.'),
    ('Alta', 'Deck', 'Coral (1,98:1), bermellón (1,41:1) y magenta (1,33:1) no llegaban a 3:1 sobre el azul rey. En V0.8 lo compensamos con anillos crema.', 'Los cinco vivos superan 3,27:1 sobre rey y 6,36:1 sobre noche. Los anillos se quedan como refuerzo.'),
    ('Alta', 'Deck', 'Los fondos de las láminas de pilar no coincidían con el color de su ficha: C en índigo, A en amarillo con ficha jade, V en jade con ficha bermellón.', 'Cada lámina de pilar usa su color: C sol, L rosa, A menta, V mango, E lila. Fichas, barras y árbol usan el mismo código.'),
    ('Media', 'Deck', 'Los nombres de los tokens contradecían su color: --pink era bermellón, --ice era crema, --neon era jade y --lav era azul.', 'Tokens con nombre de rol (--sol, --rosa, --rey, --papel…). Los nombres viejos quedan como alias para no tocar la estructura.'),
    ('Media', 'Deck', 'Quedaban literales de la etapa VHS: cian #9FF3FF, #7FDDF5 y #9FE8FF, violeta neón #8B3DFF, verde #109C3C y rosa #FFC2CC.', 'Ningún color fuera de la paleta. Las transparencias se derivan de tinta, papel, sol, rosa o lila.'),
    ('Media', 'Deck', 'En la lámina magenta el texto era lima. Las chispas solo cambiaban a tinta sobre amarillo, así que quedaban amarillas sobre fondos claros.', 'Todo fondo claro lleva texto y chispas tinta. Las chispas sol aparecen solo sobre rey y noche.'),
    ('Media', 'Deck', 'Las bandas de madurez no seguían una lógica de color: coral, bermellón, crema y amarillo.', 'Rampa cálida a fría (rosa → mango → sol → menta), la misma en el deck y en el one-pager.'),
    ('Media', 'Docs', 'Los encabezados de los documentos estaban en índigo, mientras el deck y el índice están en azul rey.', 'Todos los encabezados van en rey, con título sol (5,97:1) y texto papel (7,23:1).'),
    ('Media', 'Docs', 'Los pasteles de apoyo (#FBE0E8, #D9F0E3, #FDF6C4, #DCE6F7) no se derivaban de ningún vivo.', 'Cada vivo tiene un tinte (-t) y un tono profundo (-d). Tinta sobre cualquier tinte da ≥ 15,8:1.'),
    ('Baja', 'One-pager', 'En pantallas angostas, el blob del encabezado tapaba el subtítulo.', 'El blob es más pequeño bajo 1100 px y el texto queda por encima.'),
    ('Baja', 'Deck', 'La barra A (menta) del ejemplo "Dos números" se perdía sobre la lámina menta.', 'Las barras sobre menta llevan contorno tinta (WCAG 1.4.11).'),
    ('Baja', 'Deck', 'Rey contra noche da solo 1,95:1.', 'Noche se usa para tarjetas y láminas de acento, nunca para transmitir información frente a rey.'),
]
qa_rows = ''.join(f'<tr><td><span class="sev {s[0].lower()}">{s[0]}</span></td><td>{s[1]}</td><td>{s[2]}</td><td>{s[3]}</td></tr>' for s in QA)

tokens_css = (':root{\n'
              + ''.join(f'  --{k}:{v};\n' for k, v in N.items())
              + ''.join(f'  --{k}:{v};\n' for k, v in V.items())
              + ''.join(f'  --{k}-d:{v};\n' for k, v in D.items())
              + ''.join(f'  --{k}-t:{v};\n' for k, v in T.items()) + '}')

html = f'''<title>Paleta CLAVE V0.9</title>
<meta name="description" content="Paleta refinada del Modelo CLAVE: tokens, roles y validación técnica de contraste WCAG 2.2 y distinguibilidad bajo daltonismo (ΔE00).">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&family=Kaushan+Script&display=swap">
<style>
{tokens_css}
:root{{--line:#E6DCC4;--soft:#F7F1E1;--muted:#4B3F63;color-scheme:light dark}}
*{{box-sizing:border-box}}
body{{margin:0;background:#FFFDF6;color:var(--tinta);font:600 16px/1.55 "Nunito",system-ui,sans-serif;padding:0 16px 64px}}
.wrap{{max-width:1040px;margin:0 auto}}
.head{{background:var(--rey);color:var(--papel);margin:0 -16px 28px;padding:44px 16px 34px}}
.head .in{{max-width:1040px;margin:0 auto}}
.k{{font-weight:800;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--sol)}}
h1{{font-weight:900;font-size:clamp(2.2rem,6vw,3.4rem);line-height:1;margin:.6rem 0 .5rem;color:var(--sol)}}
h1 span{{font-family:"Kaushan Script",cursive;font-weight:400;font-size:.55em;color:var(--papel);margin-left:.2em}}
.head p{{max-width:68ch;margin:.4rem 0 0}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-top:20px}}
.kpi{{background:var(--noche);border-radius:16px;padding:14px 16px}}
.kpi b{{display:block;font-weight:900;font-size:1.7rem;color:var(--sol);line-height:1.1}}
.kpi small{{font-weight:700;font-size:.82rem}}
h2{{font-weight:900;font-size:1.45rem;margin:40px 0 6px}}
h2 small{{display:block;font-weight:700;font-size:.9rem;color:var(--muted);margin-top:2px}}
h3{{font-weight:900;font-size:1rem;margin:22px 0 8px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px}}
.sw{{border-radius:16px;padding:14px;min-height:110px;display:flex;flex-direction:column;gap:2px;box-shadow:inset 0 0 0 1.5px rgba(23,10,51,.12)}}
.sw b{{font-weight:900;font-size:1.1rem}}.sw code{{font:700 .85rem/1.2 ui-monospace,Menlo,monospace}}.sw span{{font-size:.82rem;font-weight:700;margin-top:auto}}
.tbl{{overflow-x:auto;margin:8px 0}}
table{{border-collapse:collapse;width:100%;font-size:.9rem;min-width:560px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
thead th{{background:var(--soft);font-weight:800;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
tbody th{{font-weight:800;white-space:nowrap}}
td.n{{font-variant-numeric:tabular-nums;font-weight:800;white-space:nowrap}}
td.ok::before{{content:"✓ ";color:var(--menta-d)}}td.ko{{color:var(--rosa-d)}}td.ko::before{{content:"✕ "}}
.dot{{display:inline-block;width:14px;height:14px;border-radius:50%;vertical-align:-2px;margin-right:6px;box-shadow:inset 0 0 0 1.5px rgba(23,10,51,.35)}}
.roles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}}
.card{{background:var(--papel);border-radius:18px;padding:16px 18px;box-shadow:inset 0 0 0 1.5px var(--line)}}
.card p{{margin:.3rem 0 0;font-size:.92rem}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}}
.chips span{{display:inline-flex;align-items:center;gap:6px;padding:6px 12px 6px 6px;border-radius:999px;font-weight:800;font-size:.85rem;background:#fff;box-shadow:inset 0 0 0 1.5px var(--line)}}
.chips i{{display:grid;place-items:center;width:26px;height:26px;border-radius:50%;font-style:normal;font-weight:900;color:var(--tinta);box-shadow:inset 0 0 0 2px var(--tinta)}}
.ramp{{display:grid;grid-template-columns:50fr 20fr 15fr 15fr;gap:4px;border-radius:999px;overflow:hidden;margin-top:10px;height:40px}}
.ramp div{{display:grid;place-items:center;font-weight:800;font-size:.72rem;color:var(--tinta);white-space:nowrap;overflow:hidden}}
.stage{{background:var(--rey);border-radius:20px;padding:18px;color:var(--papel)}}
.stage .row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.stage .pill{{padding:8px 14px;border-radius:999px;font-weight:900;color:var(--tinta)}}
.sims{{display:grid;gap:10px}}
.sim{{display:grid;grid-template-columns:120px 1fr 1fr;gap:10px;align-items:center;font-weight:800;font-size:.85rem}}
.strip{{display:grid;grid-template-columns:repeat(5,1fr);height:44px;border-radius:12px;overflow:hidden;background:var(--rey);gap:3px;padding:3px}}
.strip i{{border-radius:9px;display:grid;place-items:center}}.strip i b{{font-weight:900;color:var(--tinta)}}
.sim.h{{font-size:.74rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}}
.sev{{display:inline-block;font-weight:800;font-size:.72rem;padding:2px 8px;border-radius:999px;color:var(--tinta)}}
.sev.alta{{background:var(--rosa-t);box-shadow:inset 0 0 0 1.5px var(--rosa-d)}}.sev.media{{background:var(--sol-t);box-shadow:inset 0 0 0 1.5px var(--sol-d)}}.sev.baja{{background:var(--menta-t);box-shadow:inset 0 0 0 1.5px var(--menta-d)}}
pre{{background:var(--noche);color:var(--papel);border-radius:16px;padding:16px 18px;overflow-x:auto;font:700 .85rem/1.6 ui-monospace,Menlo,monospace}}
.note{{font-size:.88rem;color:var(--muted)}}
a{{color:var(--rey);font-weight:800}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--line:#3A2A66;--soft:#221247;--muted:#CFC6E8}}:root:not([data-theme="light"]) body{{background:var(--tinta);color:var(--papel)}}:root:not([data-theme="light"]) .card{{background:var(--noche);box-shadow:none}}:root:not([data-theme="light"]) .chips span{{background:var(--tinta);color:var(--papel)}}:root:not([data-theme="light"]) td.ok::before{{color:var(--menta)}}:root:not([data-theme="light"]) td.ko{{color:var(--rosa)}}:root:not([data-theme="light"]) a{{color:var(--sol)}}}}
:root[data-theme="dark"]{{--line:#3A2A66;--soft:#221247;--muted:#CFC6E8}}:root[data-theme="dark"] body{{background:var(--tinta);color:var(--papel)}}:root[data-theme="dark"] .card{{background:var(--noche);box-shadow:none}}:root[data-theme="dark"] .chips span{{background:var(--tinta);color:var(--papel)}}
@media (max-width:600px){{.sim{{grid-template-columns:1fr}}.sim.h{{display:none}}}}
</style>
<header class="head"><div class="in">
  <span class="k">Modelo CLAVE · Sistema de color V0.9</span>
  <h1>Paleta CLAVE <span>validada</span></h1>
  <p>Conserva el espíritu de "Los Sabanales" (azul rey plano y papeles de colores vivos) con un criterio técnico: cada color tiene un solo rol, todo texto cumple WCAG 2.2 AA y los cinco pilares se distinguen con cualquier tipo de daltonismo.</p>
  <div class="kpis">
    <div class="kpi"><b>{f1(wn[0])}</b><small>ΔE00 mínimo entre pilares, con cualquier visión. Antes: {f1(wo[0])}</small></div>
    <div class="kpi"><b>{f(min(cr(v, N["rey"]) for v in V.values()))}:1</b><small>Contraste mínimo de un vivo sobre rey. Antes: {f(min(cr(v, N["rey"]) for v in OLD.values()))}:1</small></div>
    <div class="kpi"><b>{f(min(cr(v, N["papel"]) for v in D.values()))}:1</b><small>Contraste mínimo de un tono profundo sobre papel</small></div>
    <div class="kpi"><b>0</b><small>Colores fuera de la paleta en el deck. Antes: 11</small></div>
  </div>
</div></header>
<main class="wrap">

<h2>1. Tokens<small>Cuatro neutros, cinco vivos (uno por pilar) y dos derivados de cada vivo.</small></h2>
<h3>Neutros</h3><div class="grid">{neutros}</div>
<h3>Vivos · rellenos sobre rey y noche, con texto tinta</h3><div class="grid">{vivos}</div>
<h3>Profundos (-d) · texto y bordes sobre papel</h3><div class="grid">{prof}</div>
<h3>Tintes (-t) · cajas, filas y etiquetas en documentos</h3><div class="grid">{tint}</div>

<h2>2. Roles<small>Un color, un significado, el mismo en el deck, los documentos y el dashboard.</small></h2>
<div class="roles">
  <div class="card"><b>Código de pilar</b><p>Cada pilar tiene su color y su lámina usa ese color de fondo. La letra siempre acompaña al color, porque el color nunca es la única pista.</p>
    <div class="chips">{''.join(f'<span><i style="background:{V[k]}">{PIL[k][0]}</i>{PIL[k][1]}</span>' for k in V)}</div></div>
  <div class="card"><b>Tensión y resolución</b><p>Los tres golpes que tensan van en rosa y los dos que resuelven en sol, igual que en las mitades de la lámina 5 y los golpes de la clave.</p>
    <div class="chips"><span><i style="background:var(--rosa)">3</i>Tensión</span><span><i style="background:var(--sol)">2</i>Resolución</span></div></div>
  <div class="card"><b>Rampa de madurez</b><p>Va de cálido a frío: rosa (Entrando), mango (Emergiendo), sol (Adaptando) y menta (Transformando).</p>
    <div class="ramp"><div style="background:var(--rosa)">Entrando</div><div style="background:var(--mango)">Emergiendo</div><div style="background:var(--sol)">Adaptando</div><div style="background:var(--menta)">Transformando</div></div></div>
  <div class="card"><b>Escenario</b><p>Rey es el fondo base. Noche se usa para tarjetas y láminas de acento. Papel es el fondo de lectura de los documentos. Tinta es el único color de texto sobre colores vivos.</p>
    <div class="stage" style="margin-top:10px"><div class="row">{''.join(f'<span class="pill" style="background:{V[k]}">{PIL[k][0]}</span>' for k in V)}<span style="font-weight:800">sobre rey</span></div></div></div>
</div>

<h2>3. Contraste WCAG 2.2<small>Mínimos: 3:1 para gráficos y texto grande (1.4.11, 1.4.3) y 4.5:1 para texto normal.</small></h2>
<div class="tbl"><table><thead><tr><th>Color</th><th>Vivo / rey</th><th>Vivo / noche</th><th>Tinta / vivo</th><th>-d / papel</th><th>-d / tinte</th><th>Tinta / tinte</th></tr></thead><tbody>{rows_c}</tbody></table></div>
<div class="roles" style="margin-top:10px">
  <div class="tbl"><table style="min-width:0"><thead><tr><th>Neutros</th><th>Ratio</th></tr></thead><tbody>{neutral_rows}</tbody></table></div>
  <div class="tbl"><table style="min-width:0"><thead><tr><th>Paleta V0.8 (antes)</th><th>Sobre rey</th></tr></thead><tbody>{rows_old}</tbody></table></div>
</div>

<h2>4. Distinguibilidad bajo daltonismo<small>ΔE00 (CIEDE2000) entre cada par de vivos, simulando deuteranopía, protanopía y tritanopía (Machado, Oliveira y Fernandes, 2009; severidad 1,0). Meta: ΔE00 ≥ 12.</small></h2>
<div class="tbl"><table><thead><tr><th>Par</th>{''.join(f'<th>{l}</th>' for _, l in SIMS)}</tr></thead><tbody>{rows_de}</tbody></table></div>
<p class="note">Par más cercano de la paleta nueva: {wn[1]} en {simname[wn[2]].lower()} (ΔE00 {f1(wn[0])}). Par más cercano de la paleta V0.8: {wo[1]} en {simname[wo[2]].lower()} (ΔE00 {f1(wo[0])}). Por debajo de 2, dos colores son prácticamente indistinguibles.</p>
<h3>Simulación sobre rey</h3>
<div class="sims">
  <div class="sim h"><span></span><span>Paleta V0.9 · C L A V E</span><span>Paleta V0.8</span></div>
  {strips}
</div>

<h2>5. QA visual de páginas y artefactos<small>Hallazgos de la revisión de color y lo que cambió en cada uno.</small></h2>
<div class="tbl"><table><thead><tr><th>Severidad</th><th>Dónde</th><th>Hallazgo</th><th>Corrección V0.9</th></tr></thead><tbody>{qa_rows}</tbody></table></div>
<p class="note">En el deck solo cambiaron colores: valores de los tokens, literales heredados, la clase de fondo de las láminas de pilar y el color de texto sobre fondos claros. No se tocó ninguna lámina, texto, orden ni animación.</p>

<h2>6. Tokens para copiar<small>Los mismos valores están en <code>Modelo/V0/elementos/12-paleta/paleta-clave.json</code>.</small></h2>
<pre>{tokens_css}</pre>
<p class="note">Método: los vivos se buscaron en OKLCH con una muestra aleatoria restringida (vivo ≥ 3,1:1 sobre rey, tinta ≥ 7:1 sobre el vivo) y se eligió la combinación de mayor croma con ΔE00 ≥ 12 en las cuatro visiones. Los profundos bajan la luminosidad OKLCH hasta ≥ 5,2:1 sobre papel. Grupo 4 · MGinn Universidad Icesi · octubre de 2026.</p>
</main>
'''
out = sys.argv[1]
open(out, 'w', encoding='utf-8').write(html)
json.dump({'version': 'V0.9', 'neutros': N, 'vivos': V, 'profundos': D, 'tintes': T,
           'pilares': {PIL[k][0]: {'nombre': PIL[k][1], 'vivo': V[k], 'profundo': D[k], 'tinte': T[k]} for k in V},
           'roles': {'tension': 'rosa', 'resolucion': 'sol', 'madurez': ['rosa', 'mango', 'sol', 'menta'], 'fondo': 'rey', 'tarjeta': 'noche', 'texto': 'tinta', 'lectura': 'papel'},
           'validacion': {'deltaE00_min': round(wn[0], 1), 'par_min': wn[1], 'vision_par_min': wn[2] or 'tipica', 'contraste_min_vivo_rey': round(min(cr(v, N['rey']) for v in V.values()), 2)}},
          open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('ok', len(html), wn, wo)
