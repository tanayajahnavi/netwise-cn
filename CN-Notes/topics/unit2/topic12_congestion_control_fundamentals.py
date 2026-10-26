from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "unit2" / "12_congestion_control_fundamentals.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root{--ink:#172033;--muted:#526078;--line:#dbe3ef;--paper:#f4f7fb;--blue:#1d4ed8;--pale:#eff6ff;--teal:#0f766e;--amber:#b45309}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.68 system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
main{max-width:1050px;margin:auto;padding:28px 20px 64px}.hero{padding:34px 36px;border-radius:24px;background:linear-gradient(135deg,#e0f2fe,#eef2ff 60%,#f0fdfa);border:1px solid #cbdcf4;margin-bottom:22px}
.eyebrow{font-size:.78rem;letter-spacing:.14em;font-weight:800;color:var(--blue)}h1{font-size:clamp(2.1rem,5vw,3.3rem);line-height:1.1;margin:.2em 0}.lead{font-size:1.15rem;max-width:800px;color:#34435c}.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.chips span{padding:5px 11px;border:1px solid #bfdbfe;background:#fff;border-radius:999px;font-size:.83rem}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 30px;margin:18px 0;box-shadow:0 5px 18px #0f172a08}h2{font-size:1.55rem;margin-top:0;border-bottom:1px solid var(--line);padding-bottom:10px}h3{font-size:1.12rem;margin:1.25em 0 .35em}p{margin:.65em 0}li{margin:.38em 0}.diagram{margin:18px auto;max-width:780px;overflow-x:auto}.diagram svg{display:block;width:100%;height:auto;min-width:460px}.callout{background:var(--pale);border-left:4px solid var(--blue);padding:13px 16px;margin:18px 0;border-radius:8px}.warning{background:#fffbeb;border-left:4px solid #d97706;padding:13px 16px;margin:18px 0;border-radius:8px}.note{color:var(--muted);font-size:.92rem;background:#f8fafc;padding:11px 13px;border-radius:8px}.formula{font-family:ui-monospace,Consolas,monospace;background:#eff6ff;padding:14px;border-radius:10px;text-align:center;font-size:1.1rem;color:#1e40af}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.94rem}th,td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}th{background:#eff6ff}tr:nth-child(even) td{background:#fafcff}code{background:#eef2ff;padding:2px 5px;border-radius:4px}.exam{border-top:5px solid var(--teal)}details{border:1px solid var(--line);border-radius:10px;padding:12px 15px;margin:10px 0}summary{cursor:pointer;font-weight:700}.revision-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px}.revision-grid div{display:flex;flex-direction:column;gap:4px;padding:13px;border:1px solid var(--line);border-radius:10px;background:#fbfdff}.revision-grid span{color:var(--muted);font-size:.93rem}.source-note{background:#fbfdff}@media(max-width:650px){main{padding:12px}.hero,.card{padding:22px 18px}table{font-size:.85rem}th,td{padding:8px}}
"""

SVG = r"""
<svg viewBox="0 0 760 310" role="img" aria-label="Congestion forms when incoming traffic exceeds available network capacity">
 <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#64748b"/></marker></defs>
 <rect x="20" y="95" width="155" height="82" rx="12" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
 <text x="97" y="127" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#1e3a8a">Many senders</text><text x="97" y="151" text-anchor="middle" font-family="Arial" font-size="13" fill="#1e3a8a">Packets arrive</text>
 <path d="M175 136 H270" stroke="#64748b" stroke-width="3" marker-end="url(#arrow)"/>
 <rect x="280" y="82" width="190" height="108" rx="12" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
 <text x="375" y="115" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#92400e">Router queue</text>
 <rect x="312" y="130" width="126" height="28" rx="5" fill="#fde68a" stroke="#d97706"/><text x="375" y="149" text-anchor="middle" font-family="Arial" font-size="13" fill="#92400e">Queue builds up</text>
 <path d="M470 136 H565" stroke="#64748b" stroke-width="3" marker-end="url(#arrow)"/>
 <rect x="575" y="95" width="165" height="82" rx="12" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
 <text x="657" y="127" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#166534">Output link</text><text x="657" y="151" text-anchor="middle" font-family="Arial" font-size="13" fill="#166534">Limited capacity</text>
 <path d="M375 190 V230 H235" stroke="#dc2626" stroke-width="2.5" fill="none"/><path d="M235 230 l10 -6 v12 z" fill="#dc2626"/>
 <text x="225" y="254" text-anchor="middle" font-family="Arial" font-size="14" fill="#b91c1c">Excess queueing delay</text>
 <path d="M375 190 V276 H520" stroke="#dc2626" stroke-width="2.5" fill="none"/><path d="M520 276 l-10 -6 v12 z" fill="#dc2626"/>
 <text x="540" y="281" text-anchor="start" font-family="Arial" font-size="14" fill="#b91c1c">Buffer overflow → drops</text>
</svg>
"""

content = r"""
<section class="hero">
 <p class="eyebrow">COMPUTER NETWORKS · UNIT 2 · TOPIC 12</p>
 <h1>Congestion Control: Fundamentals & Approaches</h1>
 <p class="lead">Understand what congestion is, why it occurs, how it affects network performance, and the broad approaches used to control it.</p>
 <div class="chips"><span>Congestion</span><span>Queueing and packet loss</span><span>Open-loop / closed-loop</span><span>Exam-ready notes</span></div>
</section>

<section class="card">
 <h2>1. What is network congestion?</h2>
 <p><strong>Congestion</strong> occurs when the amount of traffic offered to a network or part of it exceeds the resources available to carry that traffic. Resources may include link bandwidth, router processing capacity, and buffer space.</p>
 <div class="diagram">__SVG__</div>
 <p>When packets arrive at a router faster than they can be transmitted on an outgoing link, they wait in a queue. As the queue grows, delay increases. If the buffer becomes full, newly arriving packets—or packets already queued, depending on the policy—may be dropped.</p>
 <div class="callout"><strong>Exam definition:</strong> Congestion is a condition in which excessive traffic overloads network resources, causing increased delay, packet loss, and reduced effective throughput.</div>
</section>

<section class="card">
 <h2>2. Causes of congestion</h2>
 <ul>
  <li><strong>Traffic bursts:</strong> many packets arrive within a short interval.</li>
  <li><strong>Insufficient bandwidth:</strong> the output link cannot transmit packets as quickly as they arrive.</li>
  <li><strong>Limited buffer space:</strong> queues fill up and packets are dropped.</li>
  <li><strong>Slow router processing:</strong> packets wait for processing or forwarding decisions.</li>
  <li><strong>Traffic concentration:</strong> multiple flows compete for the same bottleneck link or router.</li>
  <li><strong>Inefficient routing or resource use:</strong> traffic may be directed through already busy network sections.</li>
 </ul>
</section>

<section class="card">
 <h2>3. Effects of congestion</h2>
 <table><thead><tr><th>Effect</th><th>Explanation</th></tr></thead><tbody>
 <tr><td>Increased delay</td><td>Packets spend more time waiting in router queues.</td></tr>
 <tr><td>Packet loss</td><td>Full buffers force routers to discard packets.</td></tr>
 <tr><td>Retransmissions</td><td>Lost packets may be retransmitted, adding more traffic.</td></tr>
 <tr><td>Lower goodput</td><td>A larger fraction of network capacity may be spent carrying retransmissions or traffic that does not contribute to useful application delivery.</td></tr>
 <tr><td>Unstable performance</td><td>Delay and throughput can fluctuate as queues and traffic loads change.</td></tr>
 </tbody></table>
 <div class="warning"><strong>Congestion vs. flow control:</strong> Flow control prevents a sender from overwhelming a particular receiver. Congestion control addresses overload of network resources shared by many flows. They are related, but they are not the same problem.</div>
</section>

<section class="card">
 <h2>4. Congestion control: broad approaches</h2>
 <p>Congestion-control techniques are commonly grouped into two broad categories: <strong>open-loop</strong> and <strong>closed-loop</strong>. These categories describe whether the approach relies on prevention policies or on feedback about the network's current condition.</p>
 <table><thead><tr><th>Approach</th><th>Basic idea</th><th>Typical mechanisms / examples</th></tr></thead><tbody>
 <tr><td>Open-loop congestion control</td><td>Try to prevent congestion before it occurs, without depending on feedback that congestion has already developed.</td><td>Retransmission policy, window policy, acknowledgement policy, discarding policy, admission policy.</td></tr>
 <tr><td>Closed-loop congestion control</td><td>Detect congestion or its symptoms, communicate information about it, and adjust system behaviour in response.</td><td>Backpressure, choke packets, implicit signalling, explicit signalling.</td></tr>
 </tbody></table>
 <p class="note">These are broad textbook classifications. Specific protocols can combine prevention, detection, feedback, and rate adaptation.</p>
</section>

<section class="card">
 <h2>5. Open-loop congestion control</h2>
 <p>Open-loop methods use policies intended to reduce the chance that congestion will arise. The policies are selected in advance rather than being triggered only after a congestion signal is received.</p>
 <h3>Common policies</h3>
 <ul>
  <li><strong>Retransmission policy:</strong> use appropriate timers and retransmission rules so unnecessary retransmissions do not add avoidable load.</li>
  <li><strong>Window policy:</strong> choose a retransmission/window strategy that avoids sending needless duplicate traffic. The effect depends on the protocol and its window design.</li>
  <li><strong>Acknowledgement policy:</strong> reduce unnecessary acknowledgement traffic when the protocol permits it.</li>
  <li><strong>Discarding policy:</strong> where appropriate, discard less useful packets or packets according to a defined policy when resources are constrained.</li>
  <li><strong>Admission policy:</strong> do not accept a new flow or virtual circuit if sufficient resources cannot be supported under the service requirements.</li>
 </ul>
 <div class="callout"><strong>Remember:</strong> Open-loop = prevention through design and policy.</div>
</section>

<section class="card">
 <h2>6. Closed-loop congestion control</h2>
 <p>Closed-loop methods use information about the network's state. A basic feedback process is:</p>
 <ol>
  <li>Monitor the network or detect a symptom such as a growing queue, packet loss, or high delay.</li>
  <li>Indicate congestion to the sender or relevant routers, explicitly or implicitly.</li>
  <li>Adjust the sending rate, route, admission decisions, or resource use.</li>
  <li>Continue monitoring and adapt as conditions change.</li>
 </ol>
 <h3>Common feedback mechanisms</h3>
 <ul>
  <li><strong>Backpressure:</strong> a congested node signals an upstream node to reduce or pause traffic; the signal may propagate backward along the path.</li>
  <li><strong>Choke packet:</strong> a router sends a control message to the source asking it to reduce its sending rate.</li>
  <li><strong>Implicit signalling:</strong> the sender infers congestion from symptoms such as packet loss or increased delay.</li>
  <li><strong>Explicit signalling:</strong> network devices directly mark or communicate congestion information. The exact method depends on the protocol.</li>
 </ul>
 <div class="callout"><strong>Remember:</strong> Closed-loop = detect, signal, and respond.</div>
</section>

<section class="card">
 <h2>7. Open-loop vs. closed-loop</h2>
 <table><thead><tr><th>Feature</th><th>Open-loop</th><th>Closed-loop</th></tr></thead><tbody>
 <tr><td>Main purpose</td><td>Prevent congestion through policies.</td><td>React to congestion information or symptoms.</td></tr>
 <tr><td>Feedback</td><td>Does not rely on feedback that congestion has occurred.</td><td>Uses feedback or inferred congestion signals.</td></tr>
 <tr><td>Timing</td><td>Policies are designed and applied in advance.</td><td>Actions adapt to observed network conditions.</td></tr>
 <tr><td>Examples</td><td>Retransmission, window, acknowledgement, discarding, admission policies.</td><td>Backpressure, choke packets, implicit and explicit signalling.</td></tr>
 </tbody></table>
</section>

<section class="card">
 <h2>8. Congestion control vs. congestion management</h2>
 <p>In broad usage, <strong>congestion management</strong> describes the wider set of design and operational techniques used to avoid, monitor, respond to, and mitigate congestion. <strong>Congestion control</strong> often refers more specifically to mechanisms that regulate traffic offered to the network. Course materials may use these terms differently, so retain your lecturer's wording when it is explicitly defined.</p>
</section>

<section class="card exam">
 <h2>9. Exam-ready answers</h2>
 <h3>3-mark answer: Define congestion and state its effects.</h3>
 <p>Congestion occurs when offered traffic exceeds available network resources such as bandwidth, processing capacity, or buffer space. It causes increased queueing delay and packet loss, and may lead to retransmissions and reduced effective throughput.</p>
 <h3>5-mark answer: Differentiate open-loop and closed-loop congestion control.</h3>
 <p>Open-loop congestion control attempts to prevent congestion using policies selected in advance and does not depend on feedback that congestion has occurred. Examples include retransmission, window, acknowledgement, discarding, and admission policies. Closed-loop congestion control detects congestion or its symptoms, communicates information through feedback or signalling, and adjusts network behaviour. Examples include backpressure, choke packets, implicit signalling, and explicit signalling.</p>
 <h3>8–10-mark answer: Explain congestion and the approaches to congestion control.</h3>
 <p>Define congestion and explain its causes: bursts of traffic, limited bandwidth, buffers, processing capacity, and traffic concentration. Describe its effects—queueing delay, packet loss, retransmissions, and lower goodput. Explain open-loop prevention policies with examples, then closed-loop feedback mechanisms such as backpressure, choke packets, implicit signalling, and explicit signalling. Conclude by distinguishing congestion control from receiver-oriented flow control.</p>
</section>

<section class="card">
 <h2>10. Question bank</h2>
 <details open><summary>Short-answer questions</summary><ol>
  <li>Define congestion in a computer network.</li><li>List any four effects of congestion.</li><li>Differentiate flow control and congestion control.</li><li>What is open-loop congestion control?</li><li>What is closed-loop congestion control?</li>
 </ol></details>
 <details><summary>5-mark questions</summary><ol>
  <li>Explain the causes and effects of network congestion.</li><li>Compare open-loop and closed-loop congestion control.</li><li>Explain any four open-loop policies.</li><li>Explain backpressure and choke packets.</li>
 </ol></details>
 <details><summary>8–10-mark questions</summary><ol>
  <li>Explain congestion control approaches with examples.</li><li>Discuss open-loop and closed-loop congestion control in detail.</li><li>Explain why congestion control is different from flow control.</li>
 </ol></details>
</section>

<section class="card">
 <h2>11. Quick revision</h2>
 <div class="revision-grid">
  <div><strong>Congestion</strong><span>Traffic demand exceeds available network resources</span></div>
  <div><strong>Symptoms</strong><span>Long queues, delay, packet drops</span></div>
  <div><strong>Open-loop</strong><span>Prevention using policies</span></div>
  <div><strong>Closed-loop</strong><span>Detect, signal, respond</span></div>
  <div><strong>Open-loop examples</strong><span>Retransmission, window, acknowledgement, discarding, admission</span></div>
  <div><strong>Closed-loop examples</strong><span>Backpressure, choke packets, implicit and explicit signalling</span></div>
 </div>
 <h3>Self-check</h3>
 <ol><li>Can you define congestion in one or two sentences?</li><li>Can you explain why queues and buffers matter?</li><li>Can you list five open-loop policies?</li><li>Can you explain four closed-loop mechanisms?</li><li>Can you distinguish congestion control from flow control?</li></ol>
</section>

<section class="card source-note">
 <h2>Source and scope note</h2>
 <p>This is the first Unit 2 overview page in the visual-notes series. It introduces congestion and the broad open-loop/closed-loop classification. The next pages will cover individual syllabus topics such as traffic-aware routing, admission control, traffic throttling, load shedding, traffic shaping, packet scheduling, QoS, integrated services, differentiated services, tunneling, and packet fragmentation. ISP backbone traffic, edge computing and congestion management, and QoS challenges in IoT remain separate self-learning/term-work topics according to the syllabus notes.</p>
</section>
"""

html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Congestion Control Fundamentals | Computer Networks Unit 2</title><style>""" + CSS + """</style></head>
<body><main>""" + content.replace("__SVG__", SVG) + """
<footer style="text-align:center;color:#64748b;padding:24px 0">Computer Networks · Unit 2 · Congestion Control Fundamentals</footer>
</main></body></html>"""

OUT.write_text(html, encoding="utf-8")
print(f"Created: {OUT}")
print(f"HTML size: {OUT.stat().st_size:,} bytes")
