from pathlib import Path
from html import escape

# Topic 1: Store-and-Forward Packet Switching
# Run from the CN-Notes project root:
#   python topics/unit1/topic01_store_forward.py
# Output:
#   output/unit1/01_store_and_forward.html

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "output" / "unit1"
OUTPUT_FILE = OUTPUT_DIR / "01_store_and_forward.html"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Topic 1 — Store-and-Forward Packet Switching | CN Notes</title>
<style>
:root {
  --ink: #182230;
  --muted: #526174;
  --paper: #f4f7fb;
  --card: #ffffff;
  --line: #dce4ee;
  --blue: #2457c5;
  --blue-soft: #eaf1ff;
  --teal: #087f8c;
  --teal-soft: #e6f7f7;
  --amber: #9a5b00;
  --amber-soft: #fff4d9;
  --green: #176b45;
  --green-soft: #e6f6ed;
  --red: #a33a3a;
  --red-soft: #fff0f0;
  --shadow: 0 10px 28px rgba(24, 34, 48, .07);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: Inter, "Segoe UI", Arial, sans-serif; line-height: 1.65;
}
header {
  background: linear-gradient(130deg, #132d62, #2457c5 65%, #087f8c);
  color: white; padding: 42px 22px 36px;
}
.hero, main { max-width: 1120px; margin: auto; }
.eyebrow { text-transform: uppercase; letter-spacing: .13em; font-size: .78rem; opacity: .85; font-weight: 700; }
h1 { font-size: clamp(2rem, 4vw, 3.15rem); line-height: 1.12; margin: 10px 0 14px; }
header p { max-width: 780px; margin: 0; font-size: 1.06rem; opacity: .95; }
.meta { display: flex; gap: 9px; flex-wrap: wrap; margin-top: 20px; }
.pill { display: inline-block; padding: 5px 10px; border-radius: 99px; font-size: .82rem; font-weight: 700; }
header .pill { background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.25); }
main { padding: 24px 18px 60px; }
nav.toc {
  background: var(--card); border: 1px solid var(--line); border-radius: 16px;
  padding: 18px 22px; box-shadow: var(--shadow); margin: -2px 0 24px;
}
nav.toc strong { display: block; margin-bottom: 8px; }
nav.toc a { color: var(--blue); text-decoration: none; margin: 0 14px 5px 0; display: inline-block; }
nav.toc a:hover { text-decoration: underline; }
section.card {
  background: var(--card); border: 1px solid var(--line); border-radius: 16px;
  padding: clamp(18px, 3vw, 28px); margin: 20px 0; box-shadow: var(--shadow);
  scroll-margin-top: 16px;
}
h2 { font-size: 1.55rem; margin: 0 0 14px; line-height: 1.3; }
h3 { font-size: 1.12rem; margin: 22px 0 8px; }
p { margin: 9px 0 12px; }
.lead { font-size: 1.08rem; }
.callout { border-left: 4px solid var(--blue); background: var(--blue-soft); padding: 13px 16px; border-radius: 8px; margin: 14px 0; }
.callout.teal { border-color: var(--teal); background: var(--teal-soft); }
.callout.amber { border-color: #e2a126; background: var(--amber-soft); }
.callout.green { border-color: #2e9b68; background: var(--green-soft); }
.callout.red { border-color: #d55b5b; background: var(--red-soft); }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
.mini { background: #fbfcfe; border: 1px solid var(--line); border-radius: 12px; padding: 15px; }
.mini h3 { margin-top: 0; }
.diagram { overflow-x: auto; padding: 8px 0; }
.diagram svg { display: block; width: 100%; min-width: 620px; height: auto; }
figcaption { color: var(--muted); font-size: .88rem; margin-top: 7px; }
table { width: 100%; border-collapse: collapse; margin: 12px 0 6px; font-size: .95rem; }
th, td { border: 1px solid var(--line); text-align: left; vertical-align: top; padding: 11px 12px; }
th { background: #edf2f9; }
tr:nth-child(even) td { background: #fbfcfe; }
.steps { counter-reset: step; list-style: none; padding: 0; }
.steps li { counter-increment: step; position: relative; padding: 4px 0 14px 46px; }
.steps li::before {
  content: counter(step); position: absolute; left: 0; top: 2px; width: 30px; height: 30px;
  border-radius: 50%; display: grid; place-items: center; background: var(--blue); color: white; font-weight: 800;
}
.formula { background: #17243a; color: white; padding: 16px; border-radius: 12px; font-family: "Consolas", monospace; overflow-x: auto; }
.question { border: 1px solid var(--line); border-radius: 12px; padding: 17px; margin: 14px 0; }
.question h3 { margin: 0 0 8px; }
.badge { font-size: .76rem; padding: 4px 8px; border-radius: 6px; display: inline-block; margin-right: 7px; font-weight: 800; vertical-align: 2px; }
.badge.past { color: #7c2d12; background: #ffedd5; }
.badge.practice { color: #1746a2; background: #eaf1ff; }
.badge.numerical { color: #176b45; background: #e6f6ed; }
.answer-label { color: var(--teal); font-weight: 800; margin-top: 12px; display: block; }
ul, ol { padding-left: 24px; }
li { margin: 5px 0; }
.small { color: var(--muted); font-size: .9rem; }
.checklist li { list-style: "☐  "; padding-left: 4px; }
footer { color: var(--muted); text-align: center; font-size: .88rem; padding: 20px; }
@media print {
  body { background: white; }
  header { padding: 22px; }
  section.card, nav.toc { box-shadow: none; break-inside: avoid; }
  nav.toc { margin-top: 12px; }
  a { color: inherit !important; }
}
</style>
</head>
<body>
<header>
  <div class="hero">
    <div class="eyebrow">24CS510 · Computer Networks · Unit 1</div>
    <h1>Store-and-Forward<br>Packet Switching</h1>
    <p>Visual notes with a network diagram, working sequence, transmission-time example, exam-ready answer, and a question bank informed by the uploaded JSSSTU question paper.</p>
    <div class="meta">
      <span class="pill">Core concept</span>
      <span class="pill">5-mark answer</span>
      <span class="pill">Diagram + numerical</span>
      <span class="pill">Question bank</span>
    </div>
  </div>
</header>

<main>
<nav class="toc">
  <strong>On this page</strong>
  <a href="#definition">Definition</a>
  <a href="#environment">Network environment</a>
  <a href="#working">Working</a>
  <a href="#numerical">Numerical</a>
  <a href="#exam-answer">5-mark answer</a>
  <a href="#questions">Questions & answers</a>
  <a href="#revision">Quick revision</a>
</nav>

<section class="card" id="definition">
  <h2>1. Definition and core idea</h2>
  <p class="lead"><strong>Store-and-forward packet switching</strong> is a packet-switching technique in which an intermediate router receives the <strong>entire packet</strong>, stores it temporarily, and then forwards it to the next router or destination.</p>
  <div class="callout">
    <strong>Remember:</strong> The router waits for the complete packet to arrive before starting to forward that packet on the outgoing link.
  </div>
  <div class="grid">
    <div class="mini"><h3>📥 Store</h3><p>The complete incoming packet is held temporarily in a router buffer.</p></div>
    <div class="mini"><h3>🔎 Check and inspect</h3><p>The router examines packet/header information and may perform error-related checks as supported by the relevant protocol.</p></div>
    <div class="mini"><h3>➡️ Forward</h3><p>The router selects the outgoing interface/next hop and transmits the packet when the link is available.</p></div>
  </div>
</section>

<section class="card" id="environment">
  <h2>2. Store-and-forward network environment</h2>
  <p>A packet may travel through multiple routers between the source and destination. Every intermediate router repeats the receive–store–forward process.</p>
  <figure class="diagram">
    <svg viewBox="0 0 940 280" role="img" aria-label="Source host connected through Router A and Router B to a destination host">
      <defs>
        <marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2457c5"/></marker>
      </defs>
      <rect x="22" y="70" width="150" height="90" rx="14" fill="#eaf1ff" stroke="#2457c5" stroke-width="2"/>
      <text x="97" y="105" text-anchor="middle" font-size="18" font-weight="700" fill="#182230">Source Host</text>
      <text x="97" y="130" text-anchor="middle" font-size="13" fill="#526174">Creates packet</text>
      <rect x="245" y="55" width="170" height="120" rx="14" fill="#e6f7f7" stroke="#087f8c" stroke-width="2"/>
      <text x="330" y="85" text-anchor="middle" font-size="18" font-weight="700" fill="#182230">Router A</text>
      <text x="330" y="111" text-anchor="middle" font-size="14" fill="#182230">Receive complete</text>
      <text x="330" y="131" text-anchor="middle" font-size="14" fill="#182230">packet → store</text>
      <text x="330" y="151" text-anchor="middle" font-size="14" fill="#182230">→ forward</text>
      <rect x="525" y="55" width="170" height="120" rx="14" fill="#e6f7f7" stroke="#087f8c" stroke-width="2"/>
      <text x="610" y="85" text-anchor="middle" font-size="18" font-weight="700" fill="#182230">Router B</text>
      <text x="610" y="111" text-anchor="middle" font-size="14" fill="#182230">Receive complete</text>
      <text x="610" y="131" text-anchor="middle" font-size="14" fill="#182230">packet → store</text>
      <text x="610" y="151" text-anchor="middle" font-size="14" fill="#182230">→ forward</text>
      <rect x="768" y="70" width="150" height="90" rx="14" fill="#e6f6ed" stroke="#176b45" stroke-width="2"/>
      <text x="843" y="105" text-anchor="middle" font-size="18" font-weight="700" fill="#182230">Destination</text>
      <text x="843" y="130" text-anchor="middle" font-size="13" fill="#526174">Receives packet</text>
      <line x1="172" y1="115" x2="238" y2="115" stroke="#2457c5" stroke-width="3" marker-end="url(#arrow)"/>
      <line x1="415" y1="115" x2="518" y2="115" stroke="#2457c5" stroke-width="3" marker-end="url(#arrow)"/>
      <line x1="695" y1="115" x2="761" y2="115" stroke="#2457c5" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="205" y="99" text-anchor="middle" font-size="12" fill="#526174">Link 1</text>
      <text x="466" y="99" text-anchor="middle" font-size="12" fill="#526174">Link 2</text>
      <text x="728" y="99" text-anchor="middle" font-size="12" fill="#526174">Link 3</text>
      <rect x="230" y="208" width="480" height="42" rx="10" fill="#fff4d9" stroke="#e2a126"/>
      <text x="470" y="234" text-anchor="middle" font-size="15" font-weight="700" fill="#7c4a03">Each router stores the complete packet before forwarding it</text>
    </svg>
    <figcaption>Conceptual diagram: packet travels hop by hop through routers. The real path can contain more or fewer routers.</figcaption>
  </figure>
  <h3>Elements and their roles</h3>
  <table>
    <thead><tr><th>Element</th><th>Role</th></tr></thead>
    <tbody>
      <tr><td>Source host</td><td>Creates and sends packets into the network.</td></tr>
      <tr><td>Communication link</td><td>Transfers packet bits between adjacent network devices.</td></tr>
      <tr><td>Router</td><td>Receives a complete packet, stores it, examines relevant information and forwards it.</td></tr>
      <tr><td>Buffer / queue</td><td>Temporarily holds packets while they wait for processing or an outgoing link.</td></tr>
      <tr><td>Destination host</td><td>Receives the packet after it crosses the network.</td></tr>
    </tbody>
  </table>
</section>

<section class="card" id="working">
  <h2>3. Working sequence</h2>
  <ol class="steps">
    <li><strong>Packet creation:</strong> The source host prepares a packet for transmission.</li>
    <li><strong>Reception:</strong> The first router receives all bits of the packet.</li>
    <li><strong>Storage:</strong> The router temporarily stores the complete packet in its buffer.</li>
    <li><strong>Inspection:</strong> The router reads relevant header information and performs applicable checks.</li>
    <li><strong>Next-hop selection:</strong> The forwarding decision determines the outgoing interface.</li>
    <li><strong>Transmission:</strong> The complete packet is sent over the outgoing link when it is available.</li>
    <li><strong>Repeat:</strong> Intermediate routers repeat the process until the packet reaches its destination.</li>
  </ol>
  <figure class="diagram">
    <svg viewBox="0 0 940 150" role="img" aria-label="Flowchart: receive packet, store complete packet, inspect header, choose next hop, forward packet">
      <defs><marker id="flowArrow" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2457c5"/></marker></defs>
      <rect x="10" y="38" width="145" height="64" rx="10" fill="#eaf1ff" stroke="#2457c5" stroke-width="2"/>
      <rect x="202" y="38" width="145" height="64" rx="10" fill="#e6f7f7" stroke="#087f8c" stroke-width="2"/>
      <rect x="394" y="38" width="145" height="64" rx="10" fill="#fff4d9" stroke="#e2a126" stroke-width="2"/>
      <rect x="586" y="38" width="145" height="64" rx="10" fill="#eaf1ff" stroke="#2457c5" stroke-width="2"/>
      <rect x="778" y="38" width="150" height="64" rx="10" fill="#e6f6ed" stroke="#176b45" stroke-width="2"/>
      <g fill="#182230" font-size="14" font-weight="700" text-anchor="middle">
        <text x="82" y="65">Receive full</text><text x="82" y="84">packet</text>
        <text x="274" y="65">Store in</text><text x="274" y="84">buffer</text>
        <text x="466" y="65">Inspect</text><text x="466" y="84">packet/header</text>
        <text x="658" y="65">Select</text><text x="658" y="84">next hop</text>
        <text x="853" y="65">Forward</text><text x="853" y="84">packet</text>
      </g>
      <g stroke="#2457c5" stroke-width="2.5" marker-end="url(#flowArrow)">
        <line x1="155" y1="70" x2="195" y2="70"/><line x1="347" y1="70" x2="387" y2="70"/>
        <line x1="539" y1="70" x2="579" y2="70"/><line x1="731" y1="70" x2="771" y2="70"/>
      </g>
      <text x="470" y="132" text-anchor="middle" fill="#526174" font-size="13">The same sequence is repeated at each intermediate router.</text>
    </svg>
  </figure>
</section>

<section class="card" id="numerical">
  <h2>4. Worked numerical example</h2>
  <p><strong>Question:</strong> A packet of 1,000 bytes travels over four equal-rate links of 1 Mbps each. Find the total transmission time under store-and-forward operation. Ignore propagation, processing and queueing delays.</p>
  <h3>Step 1 — Convert packet size into bits</h3>
  <div class="formula">L = 1000 bytes × 8 = 8000 bits</div>
  <h3>Step 2 — Calculate transmission time on one link</h3>
  <div class="formula">t = L / R = 8000 / 1,000,000 seconds = 0.008 s = 8 ms</div>
  <h3>Step 3 — Calculate for four links</h3>
  <div class="formula">T = 4 × 8 ms = 32 ms</div>
  <div class="callout green"><strong>Final answer: 32 ms.</strong> This assumes one packet and no overlap between its transmissions on successive links. Propagation, processing and queueing delays are excluded.</div>
  <div class="callout amber"><strong>Exam caution:</strong> Do not automatically multiply by the number of links if the question includes multiple packets, unequal rates, or pipelined transmission. Read the assumptions carefully.</div>
</section>

<section class="card" id="exam-answer">
  <h2>5. Exam-ready answer — 5 marks</h2>
  <div class="callout amber"><strong>Past-paper match · 5 marks</strong><br>Uploaded JSSSTU paper, page 1, Part B, Q6(b): “Explain Store and Forward Packet Switching network environment with a neat diagram.” The paper is labelled 20CS520; use it as a question-pattern reference for current course 24CS510.</div>
  <p><strong>Answer:</strong></p>
  <p>Store-and-forward packet switching is a technique in which a router receives the entire packet, stores it temporarily in memory, and then forwards it to the next router or destination.</p>
  <p><strong>Working:</strong></p>
  <ol>
    <li>The source host sends a packet into the network.</li>
    <li>The first router receives the complete packet and stores it in a buffer.</li>
    <li>The router examines relevant packet-header information and performs applicable checks.</li>
    <li>It selects the next hop and forwards the packet when the outgoing link is available.</li>
    <li>Every intermediate router repeats this process until the packet reaches the destination.</li>
  </ol>
  <p><strong>Advantages:</strong> Efficient sharing of communication links, buffering during temporary congestion, and the ability to make forwarding decisions at each router.</p>
  <p><strong>Limitations:</strong> Each hop introduces transmission delay; routers need buffer memory; congestion may cause queueing or packet loss.</p>
  <p><strong>Conclusion:</strong> In store-and-forward packet switching, a router must receive the complete packet before forwarding it on the next link.</p>
  <div class="callout teal"><strong>Diagram tip:</strong> Draw Source Host → Router A → Router B → Destination Host. Inside each router, label “Receive complete packet → Store → Inspect → Forward”.</div>
</section>

<section class="card" id="questions">
  <h2>6. Previous-paper and possible questions with answers</h2>
  <p class="small">Only the first question below is directly found in the uploaded paper. The remaining questions are practice questions based on this concept, not confirmed past-paper questions.</p>

  <article class="question">
    <h3><span class="badge past">PAST PAPER</span>Q1. Explain Store-and-Forward Packet Switching network environment with a neat diagram. (5 marks)</h3>
    <span class="answer-label">Answer outline</span>
    <p>Define store-and-forward switching, draw the source–router–router–destination diagram, explain full-packet reception, buffering, inspection, next-hop selection and forwarding, and list key advantages and limitations. Use the complete 5-mark answer in the previous section.</p>
  </article>

  <article class="question">
    <h3><span class="badge practice">PRACTICE</span>Q2. Define store-and-forward packet switching and explain its operation. (3–5 marks)</h3>
    <span class="answer-label">Answer</span>
    <p>It is a packet-switching method in which each intermediate router receives and stores the complete packet before forwarding it. The router receives the packet, buffers it, examines relevant header information, selects the next hop, and transmits it over the outgoing link. The process repeats at each intermediate router.</p>
  </article>

  <article class="question">
    <h3><span class="badge practice">PRACTICE</span>Q3. Explain the role of a router in store-and-forward packet switching. (3 marks)</h3>
    <span class="answer-label">Answer</span>
    <p>A router receives the complete packet, stores it temporarily in a buffer, examines relevant header information, selects an outgoing interface using its forwarding information, and sends the packet over the selected link. If the outgoing link is busy, the packet may wait in a queue.</p>
  </article>

  <article class="question">
    <h3><span class="badge numerical">NUMERICAL</span>Q4. A packet contains 1,000 bytes and is transmitted over four 1 Mbps links. Find the total transmission time under store-and-forward operation. Assume one packet and ignore propagation, processing and queueing delays. (5 marks)</h3>
    <span class="answer-label">Answer</span>
    <p>Packet length, L = 1,000 × 8 = 8,000 bits. Link rate, R = 1,000,000 bits/s.</p>
    <p>Transmission time per link = L/R = 8,000/1,000,000 = 0.008 s = 8 ms.</p>
    <p>For four links, total transmission time = 4 × 8 = <strong>32 ms</strong>.</p>
  </article>

  <article class="question">
    <h3><span class="badge practice">PRACTICE</span>Q5. State the advantages and limitations of store-and-forward packet switching. (5 marks)</h3>
    <span class="answer-label">Answer</span>
    <table>
      <thead><tr><th>Advantages</th><th>Limitations</th></tr></thead>
      <tbody>
        <tr><td>Communication links can be shared by many packets.</td><td>Transmission delay is added at each hop.</td></tr>
        <tr><td>Routers can buffer packets while an outgoing link is busy.</td><td>Buffers require memory and can fill up.</td></tr>
        <tr><td>Each router can make a forwarding decision.</td><td>Congestion can cause queueing and packet loss.</td></tr>
        <tr><td>Relevant packet information can be checked before forwarding.</td><td>A packet must be received completely before its forwarding transmission begins.</td></tr>
      </tbody>
    </table>
  </article>

  <article class="question">
    <h3><span class="badge practice">PRACTICE</span>Q6. Why does store-and-forward switching introduce delay? (2–3 marks)</h3>
    <span class="answer-label">Answer</span>
    <p>The router must receive all bits of a packet before forwarding that packet over the next link. This adds a transmission delay at every hop. Processing, propagation and queueing can add further delay.</p>
  </article>

  <article class="question">
    <h3><span class="badge practice">PRACTICE</span>Q7. Differentiate transmission delay and propagation delay. (3 marks)</h3>
    <span class="answer-label">Answer</span>
    <table>
      <thead><tr><th>Transmission delay</th><th>Propagation delay</th></tr></thead>
      <tbody>
        <tr><td>Time required to place all packet bits onto the link.</td><td>Time required for a signal to travel across the link.</td></tr>
        <tr><td>Depends mainly on packet length and link data rate: <strong>L/R</strong>.</td><td>Depends mainly on link distance and signal propagation speed.</td></tr>
      </tbody>
    </table>
  </article>
</section>

<section class="card" id="revision">
  <h2>7. Quick revision</h2>
  <div class="grid">
    <div class="mini"><h3>One-line definition</h3><p>Receive the complete packet, store it, then forward it.</p></div>
    <div class="mini"><h3>Router sequence</h3><p>Receive → Store → Inspect → Choose next hop → Forward.</p></div>
    <div class="mini"><h3>Numerical formula</h3><p>Transmission delay per link = packet length in bits ÷ link rate in bits/s.</p></div>
  </div>
  <h3>Exam checklist</h3>
  <ul class="checklist">
    <li>Definition and working principle</li>
    <li>Neat network-environment diagram</li>
    <li>Router operation and buffering</li>
    <li>Advantages and limitations</li>
    <li>Transmission-time numerical with units</li>
    <li>Previous-paper question practised</li>
  </ul>
  <div class="callout red"><strong>Scope note:</strong> This page covers Store-and-Forward Packet Switching only. It does not replace the other examinable Unit 1 topics in the 24CS510 syllabus.</div>
</section>

<footer>
  CN Notes · 24CS510 · Unit 1 · Topic 1<br>
  Prepared from the topic notes context and the uploaded JSSSTU 20CS520 question paper; practice questions are labelled separately from the actual paper question.
</footer>
</main>
</body>
</html>
"""

OUTPUT_FILE.write_text(PAGE, encoding="utf-8")
print(f"Created: {OUTPUT_FILE}")
print("Open the HTML file in your browser to view the updated visual notes.")
