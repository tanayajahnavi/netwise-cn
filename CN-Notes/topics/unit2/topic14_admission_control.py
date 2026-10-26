from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "unit2" / "14_admission_control.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root{--ink:#172033;--muted:#526078;--line:#dbe3ef;--paper:#f4f7fb;--blue:#1d4ed8;--pale:#eff6ff;--teal:#0f766e;--amber:#b45309}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.68 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
main{max-width:1050px;margin:auto;padding:28px 20px 64px}.hero{padding:34px 36px;border-radius:24px;background:linear-gradient(135deg,#e0f2fe,#eef2ff 60%,#f0fdfa);border:1px solid #cbdcf4;margin-bottom:22px}
.eyebrow{font-size:.78rem;letter-spacing:.14em;font-weight:800;color:var(--blue)}h1{font-size:clamp(2.1rem,5vw,3.3rem);line-height:1.1;margin:.2em 0}.lead{font-size:1.15rem;max-width:800px;color:#34435c}.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.chips span{padding:5px 11px;border:1px solid #bfdbfe;background:#fff;border-radius:999px;font-size:.83rem}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 30px;margin:18px 0;box-shadow:0 5px 18px #0f172a08}h2{font-size:1.55rem;margin-top:0;border-bottom:1px solid var(--line);padding-bottom:10px}h3{font-size:1.12rem;margin:1.25em 0 .35em}p{margin:.65em 0}li{margin:.38em 0}.diagram{margin:18px auto;max-width:780px;overflow-x:auto}.diagram svg{display:block;width:100%;height:auto;min-width:470px}.callout{background:var(--pale);border-left:4px solid var(--blue);padding:13px 16px;margin:18px 0;border-radius:8px}.warning{background:#fffbeb;border-left:4px solid #d97706;padding:13px 16px;margin:18px 0;border-radius:8px}.note{color:var(--muted);font-size:.92rem;background:#f8fafc;padding:11px 13px;border-radius:8px}.formula{font-family:ui-monospace,Consolas,monospace;background:#eff6ff;padding:14px;border-radius:10px;text-align:center;font-size:1.05rem;color:#1e40af}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.94rem}th,td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}th{background:#eff6ff}tr:nth-child(even) td{background:#fafcff}code{background:#eef2ff;padding:2px 5px;border-radius:4px}.exam{border-top:5px solid var(--teal)}details{border:1px solid var(--line);border-radius:10px;padding:12px 15px;margin:10px 0}summary{cursor:pointer;font-weight:700}.revision-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px}.revision-grid div{display:flex;flex-direction:column;gap:4px;padding:13px;border:1px solid var(--line);border-radius:10px;background:#fbfdff}.revision-grid span{color:var(--muted);font-size:.93rem}.source-note{background:#fbfdff}@media(max-width:650px){main{padding:12px}.hero,.card{padding:22px 18px}table{font-size:.85rem}th,td{padding:8px}}
"""

SVG = r"""
<svg viewBox="0 0 760 320" role="img" aria-label="Admission control checks resource availability before accepting a new flow">
 <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#64748b"/></marker></defs>
 <rect x="20" y="120" width="150" height="62" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
 <text x="95" y="146" text-anchor="middle" font-family="Arial" font-size="15" font-weight="bold" fill="#1e3a8a">New flow</text><text x="95" y="165" text-anchor="middle" font-family="Arial" font-size="12" fill="#1e3a8a">requests service</text>
 <path d="M170 151 H245" stroke="#64748b" stroke-width="2.5" marker-end="url(#arr)"/>
 <path d="M340 80 L435 151 L340 222 L245 151 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
 <text x="340" y="145" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#92400e">Enough</text><text x="340" y="163" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#92400e">resources?</text>
 <path d="M435 151 H515 V90 H570" stroke="#15803d" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
 <text x="493" y="137" font-family="Arial" font-size="13" fill="#166534">Yes</text>
 <rect x="580" y="60" width="160" height="60" rx="10" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
 <text x="660" y="85" text-anchor="middle" font-family="Arial" font-size="15" font-weight="bold" fill="#166534">Accept</text><text x="660" y="103" text-anchor="middle" font-family="Arial" font-size="12" fill="#166534">reserve resources</text>
 <path d="M435 151 H515 V230 H570" stroke="#dc2626" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
 <text x="493" y="174" font-family="Arial" font-size="13" fill="#b91c1c">No</text>
 <rect x="580" y="200" width="160" height="60" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
 <text x="660" y="225" text-anchor="middle" font-family="Arial" font-size="15" font-weight="bold" fill="#991b1b">Reject / defer</text><text x="660" y="243" text-anchor="middle" font-family="Arial" font-size="12" fill="#991b1b">protect existing flows</text>
 <text x="380" y="300" text-anchor="middle" font-family="Arial" font-size="13" fill="#475569">Conceptual flow: actual admission rules depend on the service and network</text>
</svg>
"""

content = r"""
<section class="hero">
 <p class="eyebrow">COMPUTER NETWORKS · UNIT 2 · TOPIC 14</p>
 <h1>Admission Control</h1>
 <p class="lead">A congestion-prevention mechanism that decides whether a new flow or connection can be accepted without violating the service requirements of existing traffic.</p>
 <div class="chips"><span>Congestion control</span><span>Resource reservation</span><span>QoS</span><span>Exam-ready notes</span></div>
</section>

<section class="card">
 <h2>1. What is admission control?</h2>
 <p><strong>Admission control</strong> is the process of deciding whether to accept a new flow, connection, or traffic request into a network or service domain. The decision is based on whether the network can accommodate the new request while continuing to meet the required performance or Quality of Service (QoS) commitments.</p>
 <div class="callout"><strong>Core idea:</strong> Do not accept more traffic with service guarantees than the network can support. Rejecting or deferring a new request can protect traffic that has already been admitted.</div>
 <p>Admission control is especially relevant when a service needs predictable resources, such as a requested bandwidth or delay bound. It can also be used with policy limits and capacity thresholds.</p>
</section>

<section class="card">
 <h2>2. Admission-control decision flow</h2>
 <div class="diagram">__SVG__</div>
 <ol>
  <li>A new application flow or connection requests service.</li>
  <li>The network estimates the resources that the request would require.</li>
  <li>The admission mechanism checks available capacity, existing commitments, and applicable policy.</li>
  <li>If the request can be supported, it is accepted and any required resources or state are reserved or recorded.</li>
  <li>If the request cannot be supported, it is rejected or deferred rather than overcommitting resources.</li>
 </ol>
 <p class="note">The exact admission test depends on the network architecture and service model. Some systems reserve resources explicitly; others use policy, capacity estimates, or configured thresholds.</p>
</section>

<section class="card">
 <h2>3. What does admission control check?</h2>
 <table><thead><tr><th>Consideration</th><th>Why it matters</th></tr></thead><tbody>
 <tr><td>Available bandwidth / capacity</td><td>Ensures that the new flow will not exceed the capacity budget for the relevant path or link.</td></tr>
 <tr><td>Existing reservations or commitments</td><td>Protects the guarantees already made to admitted flows.</td></tr>
 <tr><td>Delay or loss requirements</td><td>Checks whether the requested service level can plausibly be maintained.</td></tr>
 <tr><td>Buffer and processing resources</td><td>Some services or systems need capacity beyond raw link bandwidth.</td></tr>
 <tr><td>Administrative policy</td><td>Enforces priorities, service classes, user limits, or other configured rules.</td></tr>
 </tbody></table>
 <p class="note">Not every admission controller evaluates every item. Use the specific checks taught in your lecture slides if they prescribe a particular model.</p>
</section>

<section class="card">
 <h2>4. Simple bandwidth example</h2>
 <p>Consider a link with a capacity of <strong>10 Mb/s</strong>. Suppose the network's admission policy allows at most <strong>8 Mb/s</strong> to be committed to guaranteed flows, leaving 2 Mb/s as headroom.</p>
 <table><thead><tr><th>Request</th><th>Current committed rate</th><th>New request</th><th>Decision under this policy</th></tr></thead><tbody>
 <tr><td>Flow 1</td><td>0 Mb/s</td><td>3 Mb/s</td><td>Accept: total becomes 3 Mb/s</td></tr>
 <tr><td>Flow 2</td><td>3 Mb/s</td><td>4 Mb/s</td><td>Accept: total becomes 7 Mb/s</td></tr>
 <tr><td>Flow 3</td><td>7 Mb/s</td><td>2 Mb/s</td><td>Reject or defer: total would become 9 Mb/s, above the 8 Mb/s admission limit</td></tr>
 </tbody></table>
 <div class="formula">Accept if current commitments + requested resources ≤ admission limit</div>
 <p class="note">This is a simplified illustrative rule. Real networks may consider burstiness, overhead, statistical multiplexing, multiple links along a path, and QoS metrics beyond bandwidth.</p>
</section>

<section class="card">
 <h2>5. Admission control and congestion control</h2>
 <p>Admission control is one way to prevent congestion: it limits how much new traffic with specific service commitments is allowed into the system. It does not, by itself, remove all congestion from best-effort traffic or guarantee that network conditions will never change.</p>
 <table><thead><tr><th>Aspect</th><th>Admission control</th><th>Other congestion-control mechanisms</th></tr></thead><tbody>
 <tr><td>When it acts</td><td>When a new flow or service request is presented.</td><td>May act before, during, or after traffic is sent, depending on the mechanism.</td></tr>
 <tr><td>Main decision</td><td>Accept, reject, or defer a request.</td><td>May adjust sending rate, route, queue service, or packet handling.</td></tr>
 <tr><td>Primary goal</td><td>Avoid overcommitting resources and protect existing service commitments.</td><td>Reduce, prevent, or respond to network overload.</td></tr>
 </tbody></table>
</section>

<section class="card">
 <h2>6. Advantages</h2>
 <ul>
  <li>Helps prevent overcommitment of network resources.</li>
  <li>Can protect existing flows with QoS commitments.</li>
  <li>Supports predictable service when resource requirements can be estimated.</li>
  <li>Can make service admission decisions explicit and policy-based.</li>
 </ul>
 <h2>7. Limitations</h2>
 <ul>
  <li>New requests may be rejected even when users would accept best-effort service.</li>
  <li>Accurate decisions can be difficult when traffic is bursty or resource needs are uncertain.</li>
  <li>Network conditions can change after a flow is admitted.</li>
  <li>Admission checks across multiple links or domains can be complex.</li>
 </ul>
</section>

<section class="card exam">
 <h2>8. Exam-ready answers</h2>
 <h3>3-mark answer: Define admission control.</h3>
 <p>Admission control is a congestion-prevention mechanism that decides whether a new flow or connection should be accepted based on available network resources, existing commitments, and the requested service requirements. If the request cannot be supported, it may be rejected or deferred.</p>
 <h3>5-mark answer: Explain the working of admission control.</h3>
 <p>When a new flow requests service, the network estimates the resources it needs. The admission controller checks available capacity, existing reservations, service requirements, and relevant policies. If the request can be supported without violating existing commitments, it is accepted and resources or state may be reserved. Otherwise, the request is rejected or deferred. This helps avoid resource overcommitment and protect QoS.</p>
 <h3>8–10-mark answer: Explain admission control with a neat diagram and example.</h3>
 <p>Define admission control and explain its role in congestion prevention and QoS. Draw the request → resource check → accept/reject flowchart. Discuss bandwidth, existing commitments, delay/loss requirements, and policy checks. Use a small bandwidth example to demonstrate the accept/reject decision. Conclude with advantages such as resource protection and limitations such as rejection of new requests and uncertainty in traffic demand.</p>
</section>

<section class="card">
 <h2>9. Question bank</h2>
 <details open><summary>Short-answer questions</summary><ol>
  <li>Define admission control.</li><li>Why is admission control used in congestion management?</li><li>Name four factors that can affect an admission decision.</li><li>What may happen if a new request cannot be supported?</li>
 </ol></details>
 <details><summary>5-mark questions</summary><ol>
  <li>Explain the operation of admission control with a flowchart.</li><li>Explain the relationship between admission control and QoS.</li><li>Differentiate admission control from rate-based congestion control.</li>
 </ol></details>
 <details><summary>8–10-mark questions</summary><ol>
  <li>Explain admission control with a suitable diagram and numerical example.</li><li>Discuss the advantages and limitations of admission control as a congestion-prevention technique.</li>
 </ol></details>
</section>

<section class="card">
 <h2>10. Quick revision</h2>
 <div class="revision-grid">
  <div><strong>Trigger</strong><span>A new flow or connection requests service</span></div>
  <div><strong>Check</strong><span>Capacity, commitments, QoS needs, policy</span></div>
  <div><strong>Decision</strong><span>Accept, reject, or defer</span></div>
  <div><strong>Goal</strong><span>Avoid resource overcommitment</span></div>
  <div><strong>Benefit</strong><span>Protects admitted flows and service commitments</span></div>
  <div><strong>Limitation</strong><span>May reject new requests; estimates can be uncertain</span></div>
 </div>
 <h3>Self-check</h3>
 <ol><li>Can you define admission control in two sentences?</li><li>Can you draw the decision flow?</li><li>Can you explain the bandwidth example?</li><li>Can you name three advantages and two limitations?</li></ol>
</section>

<section class="card source-note">
 <h2>Source and scope note</h2>
 <p>This page covers admission control as a Unit 2 congestion-management concept. The bandwidth example and decision diagram are illustrative. The syllabus may mention admission control in more than one context; this page focuses on its role in controlling resource commitments and congestion. If the lecture PPT provides a specific algorithm or terminology, use that wording for the exam.</p>
</section>
"""

html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admission Control | Computer Networks Unit 2</title><style>""" + CSS + """</style></head>
<body><main>""" + content.replace("__SVG__", SVG) + """
<footer style="text-align:center;color:#64748b;padding:24px 0">Computer Networks · Unit 2 · Admission Control</footer>
</main></body></html>"""

OUT.write_text(html, encoding="utf-8")
print(f"Created: {OUT}")
print(f"HTML size: {OUT.stat().st_size:,} bytes")
