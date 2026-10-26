from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "unit2" / "13_traffic_aware_routing.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root{--ink:#172033;--muted:#526078;--line:#dbe3ef;--paper:#f4f7fb;--blue:#1d4ed8;--pale:#eff6ff;--teal:#0f766e;--amber:#b45309}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.68 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
main{max-width:1050px;margin:auto;padding:28px 20px 64px}.hero{padding:34px 36px;border-radius:24px;background:linear-gradient(135deg,#e0f2fe,#eef2ff 60%,#f0fdfa);border:1px solid #cbdcf4;margin-bottom:22px}
.eyebrow{font-size:.78rem;letter-spacing:.14em;font-weight:800;color:var(--blue)}h1{font-size:clamp(2.1rem,5vw,3.3rem);line-height:1.1;margin:.2em 0}.lead{font-size:1.15rem;max-width:800px;color:#34435c}.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.chips span{padding:5px 11px;border:1px solid #bfdbfe;background:#fff;border-radius:999px;font-size:.83rem}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 30px;margin:18px 0;box-shadow:0 5px 18px #0f172a08}h2{font-size:1.55rem;margin-top:0;border-bottom:1px solid var(--line);padding-bottom:10px}h3{font-size:1.12rem;margin:1.25em 0 .35em}p{margin:.65em 0}li{margin:.38em 0}.diagram{margin:18px auto;max-width:780px;overflow-x:auto}.diagram svg{display:block;width:100%;height:auto;min-width:470px}.callout{background:var(--pale);border-left:4px solid var(--blue);padding:13px 16px;margin:18px 0;border-radius:8px}.warning{background:#fffbeb;border-left:4px solid #d97706;padding:13px 16px;margin:18px 0;border-radius:8px}.note{color:var(--muted);font-size:.92rem;background:#f8fafc;padding:11px 13px;border-radius:8px}.formula{font-family:ui-monospace,Consolas,monospace;background:#eff6ff;padding:14px;border-radius:10px;text-align:center;font-size:1.1rem;color:#1e40af}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.94rem}th,td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}th{background:#eff6ff}tr:nth-child(even) td{background:#fafcff}code{background:#eef2ff;padding:2px 5px;border-radius:4px}.exam{border-top:5px solid var(--teal)}details{border:1px solid var(--line);border-radius:10px;padding:12px 15px;margin:10px 0}summary{cursor:pointer;font-weight:700}.revision-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px}.revision-grid div{display:flex;flex-direction:column;gap:4px;padding:13px;border:1px solid var(--line);border-radius:10px;background:#fbfdff}.revision-grid span{color:var(--muted);font-size:.93rem}.source-note{background:#fbfdff}@media(max-width:650px){main{padding:12px}.hero,.card{padding:22px 18px}table{font-size:.85rem}th,td{padding:8px}}
"""

SVG = r"""
<svg viewBox="0 0 760 310" role="img" aria-label="Two paths between a source and destination, with traffic levels influencing route selection">
 <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#64748b"/></marker></defs>
 <circle cx="65" cy="150" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/><text x="65" y="156" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#1e3a8a">S</text>
 <circle cx="250" cy="70" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/><text x="250" y="76" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#1e3a8a">A</text>
 <circle cx="250" cy="230" r="28" fill="#dcfce7" stroke="#15803d" stroke-width="2"/><text x="250" y="236" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#166534">B</text>
 <circle cx="510" cy="70" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/><text x="510" y="76" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#1e3a8a">C</text>
 <circle cx="510" cy="230" r="28" fill="#dcfce7" stroke="#15803d" stroke-width="2"/><text x="510" y="236" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#166534">D</text>
 <circle cx="695" cy="150" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/><text x="695" y="156" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="16" fill="#1e3a8a">T</text>
 <path d="M90 136 L225 84 M90 164 L225 216 M278 70 H482 M278 230 H482 M538 84 L670 136 M538 216 L670 164" stroke="#64748b" stroke-width="3" fill="none" marker-end="url(#arr)"/>
 <text x="155" y="95" font-family="Arial" font-size="13" fill="#334155">Path 1</text><text x="155" y="211" font-family="Arial" font-size="13" fill="#334155">Path 2</text>
 <rect x="335" y="35" width="92" height="25" rx="6" fill="#fee2e2" stroke="#dc2626"/><text x="381" y="52" text-anchor="middle" font-family="Arial" font-size="12" fill="#991b1b">Busy link</text>
 <rect x="335" y="245" width="92" height="25" rx="6" fill="#dcfce7" stroke="#15803d"/><text x="381" y="262" text-anchor="middle" font-family="Arial" font-size="12" fill="#166534">Less loaded</text>
 <text x="380" y="300" text-anchor="middle" font-family="Arial" font-size="13" fill="#475569">Conceptual: route choice can account for current traffic load</text>
</svg>
"""

content = r"""
<section class="hero">
 <p class="eyebrow">COMPUTER NETWORKS · UNIT 2 · TOPIC 13</p>
 <h1>Traffic-Aware Routing</h1>
 <p class="lead">Routing that considers traffic load or congestion conditions—not just static link costs—when selecting paths through a network.</p>
 <div class="chips"><span>Congestion management</span><span>Traffic load</span><span>Route selection</span><span>Exam-ready notes</span></div>
</section>

<section class="card">
 <h2>1. What is traffic-aware routing?</h2>
 <p><strong>Traffic-aware routing</strong> is a routing approach in which path selection takes account of current or estimated traffic conditions, such as link utilization, queue length, delay, or congestion, in addition to—or instead of—static measures such as hop count.</p>
 <p>In ordinary shortest-path routing, a route may be selected using a fixed link metric. If many flows choose the same apparently cheapest path, that path can become congested even while alternative paths have spare capacity. Traffic-aware routing attempts to account for such conditions.</p>
 <div class="callout"><strong>Core idea:</strong> Choose a route using both connectivity/cost and information about how busy the network is.</div>
</section>

<section class="card">
 <h2>2. Visual example</h2>
 <div class="diagram">__SVG__</div>
 <p>Suppose Path 1 has a lower static cost but its central link is heavily loaded. Path 2 is a little longer but has less traffic. A traffic-aware algorithm may choose Path 2 if its measured or estimated total cost is lower under the chosen metric.</p>
 <p class="note">This diagram is illustrative. It does not represent a specific topology or exact example from the course PPT.</p>
</section>

<section class="card">
 <h2>3. What traffic information can be considered?</h2>
 <table><thead><tr><th>Metric</th><th>What it indicates</th><th>Possible routing implication</th></tr></thead><tbody>
 <tr><td>Link utilization</td><td>How much of a link's capacity is being used.</td><td>A highly utilized link may receive a higher cost.</td></tr>
 <tr><td>Queue length</td><td>How many packets are waiting to be forwarded.</td><td>A long queue may indicate a bottleneck.</td></tr>
 <tr><td>Delay</td><td>Time taken by packets, potentially including queueing and transmission.</td><td>Delay-sensitive traffic may prefer a lower-delay route.</td></tr>
 <tr><td>Packet loss</td><td>Packets being dropped along a link or path.</td><td>A route with high loss may be avoided where alternatives exist.</td></tr>
 <tr><td>Available capacity</td><td>Estimated spare capacity on a link or path.</td><td>Traffic may be steered toward links with more headroom.</td></tr>
 </tbody></table>
 <p class="note">A particular routing protocol may use only some of these metrics. Do not claim every protocol uses every metric.</p>
</section>

<section class="card">
 <h2>4. General operation</h2>
 <ol>
  <li><strong>Collect measurements:</strong> routers or a controller obtain information such as utilization, delay, queue lengths, or link state.</li>
  <li><strong>Represent traffic conditions:</strong> measured values are converted into a cost, weight, constraint, or policy input.</li>
  <li><strong>Evaluate available paths:</strong> the routing process compares feasible routes using the selected metric or objective.</li>
  <li><strong>Select a route:</strong> traffic is assigned or steered to the chosen next hop/path.</li>
  <li><strong>Monitor and update:</strong> as traffic conditions change, measurements and route decisions may be updated.</li>
 </ol>
 <div class="formula">Illustrative path cost = base link cost + traffic-load penalty</div>
 <p>The expression above is a conceptual model, not a universal formula. Real protocols and algorithms define their own metrics and constraints.</p>
</section>

<section class="card">
 <h2>5. Why not always choose the currently least-loaded path?</h2>
 <p>Traffic-aware routing must be designed carefully. If many routers simultaneously observe that one path is lightly loaded and move traffic to it, the path may become overloaded. A later measurement may then send traffic back to the first path. This can cause repeated route changes known as <strong>route oscillation</strong>.</p>
 <p>Other challenges include:</p>
 <ul>
  <li><strong>Measurement delay:</strong> traffic information may already be out of date when used.</li>
  <li><strong>Control overhead:</strong> collecting and distributing measurements consumes resources.</li>
  <li><strong>Metric design:</strong> combining delay, utilization, loss, and administrative preferences is not always straightforward.</li>
  <li><strong>Stability:</strong> route changes should not create new congestion or oscillations.</li>
  <li><strong>Fairness:</strong> moving traffic for one flow can affect other flows sharing the network.</li>
 </ul>
</section>

<section class="card">
 <h2>6. Static shortest-path routing vs. traffic-aware routing</h2>
 <table><thead><tr><th>Feature</th><th>Static-metric shortest path</th><th>Traffic-aware routing</th></tr></thead><tbody>
 <tr><td>Primary input</td><td>Configured or relatively stable link costs.</td><td>Traffic measurements or estimates may influence costs or path choice.</td></tr>
 <tr><td>Response to load</td><td>May not react directly to current utilization or queueing.</td><td>Can adapt to congestion or traffic distribution.</td></tr>
 <tr><td>Potential benefit</td><td>Predictable and comparatively simple route computation.</td><td>May distribute traffic more effectively and avoid busy paths.</td></tr>
 <tr><td>Potential risk</td><td>A low-cost path can become overloaded when many flows use it.</td><td>Stale measurements or aggressive adaptation can cause oscillation and overhead.</td></tr>
 </tbody></table>
 <p class="note">This is a conceptual comparison; some shortest-path protocols allow metrics to be configured or updated based on traffic, and real implementations vary.</p>
</section>

<section class="card">
 <h2>7. Benefits and limitations</h2>
 <h3>Benefits</h3>
 <ul><li>Can avoid heavily loaded links when suitable alternatives exist.</li><li>May reduce congestion-related delay and packet loss.</li><li>Can improve use of available network capacity.</li><li>May help distribute traffic across multiple paths.</li></ul>
 <h3>Limitations</h3>
 <ul><li>Needs reliable, timely traffic information.</li><li>Measurement and route updates add overhead.</li><li>Route decisions can oscillate if feedback is poorly designed.</li><li>A traffic-aware path is not necessarily the globally best path for every performance goal.</li></ul>
</section>

<section class="card exam">
 <h2>8. Exam-ready answers</h2>
 <h3>3-mark answer: Define traffic-aware routing.</h3>
 <p>Traffic-aware routing is a routing approach that considers current or estimated traffic conditions—such as link utilization, queue length, delay, or congestion—when selecting paths. Its purpose is to avoid overloaded paths and use network resources more effectively.</p>
 <h3>5-mark answer: Explain the working of traffic-aware routing.</h3>
 <p>First, the network collects traffic measurements such as utilization, delay, queue length, or packet loss. These measurements are represented as link costs, penalties, or constraints. The routing process evaluates available paths and selects one according to the defined objective. Routers or controllers continue monitoring traffic and may update route choices when conditions change. Care is needed because stale measurements and frequent route changes can cause overhead or route oscillation.</p>
 <h3>8–10-mark answer: Explain traffic-aware routing with a diagram.</h3>
 <p>Define traffic-aware routing and explain why a shortest path based only on static costs may become congested. Draw two paths between a source and destination, showing one path with a busy link and another with spare capacity. Explain the possible metrics—utilization, queue length, delay, loss, and available capacity—then describe measurement, metric calculation, path evaluation, route selection, and monitoring. Conclude with benefits and limitations, including measurement overhead and route oscillation.</p>
</section>

<section class="card">
 <h2>9. Question bank</h2>
 <details open><summary>Short-answer questions</summary><ol>
  <li>Define traffic-aware routing.</li><li>Name four traffic metrics that can influence routing.</li><li>Why can a static shortest path become congested?</li><li>What is route oscillation?</li>
 </ol></details>
 <details><summary>5-mark questions</summary><ol>
  <li>Explain the operation of traffic-aware routing.</li><li>Compare static shortest-path routing and traffic-aware routing.</li><li>List the advantages and limitations of traffic-aware routing.</li>
 </ol></details>
 <details><summary>8–10-mark questions</summary><ol>
  <li>Explain traffic-aware routing with a suitable diagram.</li><li>Discuss how traffic measurements affect route selection and explain the stability challenges.</li>
 </ol></details>
</section>

<section class="card">
 <h2>10. Quick revision</h2>
 <div class="revision-grid">
  <div><strong>Inputs</strong><span>Utilization, queue length, delay, loss, available capacity</span></div>
  <div><strong>Process</strong><span>Measure → evaluate → select route → monitor</span></div>
  <div><strong>Goal</strong><span>Avoid overloaded paths and use resources efficiently</span></div>
  <div><strong>Risk</strong><span>Stale measurements and route oscillation</span></div>
  <div><strong>Key contrast</strong><span>Static link metric vs. metric influenced by traffic conditions</span></div>
  <div><strong>Exam keywords</strong><span>Load, link cost, delay, utilization, stability</span></div>
 </div>
 <h3>Self-check</h3>
 <ol><li>Can you define traffic-aware routing in two sentences?</li><li>Can you list and explain four traffic metrics?</li><li>Can you describe the operation in five steps?</li><li>Can you explain route oscillation and why it is undesirable?</li></ol>
</section>

<section class="card source-note">
 <h2>Source and scope note</h2>
 <p>This page explains the general concept of traffic-aware routing as a Unit 2 congestion-management topic. The diagram, illustrative path-cost expression, and examples are teaching illustrations rather than claims about exact content in the lecture PPT. Follow the course slides for any specific algorithm, formula, or terminology prescribed by the lecturer.</p>
</section>
"""

html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Traffic-Aware Routing | Computer Networks Unit 2</title><style>""" + CSS + """</style></head>
<body><main>""" + content.replace("__SVG__", SVG) + """
<footer style="text-align:center;color:#64748b;padding:24px 0">Computer Networks · Unit 2 · Traffic-Aware Routing</footer>
</main></body></html>"""

OUT.write_text(html, encoding="utf-8")
print(f"Created: {OUT}")
print(f"HTML size: {OUT.stat().st_size:,} bytes")
