from pathlib import Path
from html import escape


# ============================================================
# JSSSTU 24CS510 - COMPUTER NETWORKS
# UNIT 1, TOPIC 1
# STORE-AND-FORWARD PACKET SWITCHING
# ============================================================

OUTPUT_DIR = Path("output/unit1")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "01_store_and_forward.html"


# ------------------------------------------------------------
# HTML DOCUMENT
# ------------------------------------------------------------

html = r"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>
        Store-and-Forward Packet Switching |
        JSSSTU 24CS510
    </title>

    <style>

        :root {
            --background: #f4f7fb;
            --surface: #ffffff;
            --text: #172033;
            --muted: #5e6b82;
            --primary: #2457d6;
            --primary-light: #eaf0ff;
            --border: #dce3ee;
            --green: #15803d;
            --green-light: #ecfdf3;
            --orange: #b45309;
            --orange-light: #fff7ed;
            --red: #b91c1c;
            --red-light: #fef2f2;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background: var(--background);
            color: var(--text);
            font-family:
                "Segoe UI", Arial, sans-serif;
            line-height: 1.75;
        }

        .container {
            width: min(1050px, 92%);
            margin: 0 auto;
        }

        .hero {
            background: linear-gradient(
                135deg,
                #172554,
                #2457d6
            );

            color: white;
            padding: 55px 0;
        }

        .hero h1 {
            max-width: 850px;
            font-size: clamp(2rem, 5vw, 3.2rem);
            line-height: 1.2;
            margin: 15px 0;
        }

        .hero p {
            max-width: 750px;
            color: #e0e7ff;
        }

        .badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            background: #dbeafe;
            color: #1e40af;
        }

        main {
            padding: 28px 0 60px;
        }

        section {
            background: var(--surface);
            padding: 28px;
            margin: 22px 0;
            border: 1px solid var(--border);
            border-radius: 16px;
            box-shadow: 0 5px 18px
                        rgba(30, 50, 90, 0.04);
        }

        h2 {
            color: #193b8c;
            margin-top: 0;
            line-height: 1.35;
        }

        h3 {
            color: #244b9b;
        }

        .definition {
            border-left: 5px solid var(--primary);
            background: var(--primary-light);
            padding: 18px;
            border-radius: 8px;
        }

        .note {
            border-left: 5px solid var(--orange);
            background: var(--orange-light);
            padding: 16px;
            border-radius: 8px;
        }

        .success {
            border-left: 5px solid var(--green);
            background: var(--green-light);
            padding: 16px;
            border-radius: 8px;
        }

        .warning {
            border-left: 5px solid var(--red);
            background: var(--red-light);
            padding: 16px;
            border-radius: 8px;
        }

        .diagram {
            overflow-x: auto;
            margin: 24px 0;
            padding: 12px;
            background: #fbfdff;
            border: 1px solid var(--border);
            border-radius: 12px;
        }

        svg {
            display: block;
            width: 100%;
            height: auto;
            min-width: 500px;
        }

        .caption {
            text-align: center;
            color: var(--muted);
            font-size: 0.9rem;
        }

        .steps {
            counter-reset: step;
            list-style: none;
            padding: 0;
        }

        .steps li {
            counter-increment: step;
            position: relative;
            padding: 14px 15px 14px 55px;
            margin: 12px 0;
            border: 1px solid var(--border);
            border-radius: 10px;
            background: #fcfdff;
        }

        .steps li::before {
            content: counter(step);
            position: absolute;
            left: 14px;
            top: 13px;
            width: 27px;
            height: 27px;
            display: grid;
            place-items: center;
            border-radius: 50%;
            color: white;
            background: var(--primary);
            font-weight: bold;
        }

        .table-wrap {
            overflow-x: auto;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin: 18px 0;
        }

        th, td {
            padding: 13px;
            border: 1px solid var(--border);
            text-align: left;
            vertical-align: top;
        }

        th {
            background: var(--primary-light);
            color: #193b8c;
        }

        .answer {
            border: 1px solid #b9c9ee;
            background: #fbfcff;
            padding: 22px;
            border-radius: 12px;
            margin-top: 18px;
        }

        .marks {
            display: inline-block;
            background: #dbeafe;
            color: #1e40af;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: bold;
        }

        .revision li {
            margin: 8px 0;
        }

        .footer {
            text-align: center;
            color: var(--muted);
            padding: 25px 0;
        }

        @media print {
            body {
                background: white;
                font-size: 11pt;
            }

            .hero {
                background: white;
                color: black;
                padding: 20px 0;
            }

            .hero p {
                color: black;
            }

            section {
                box-shadow: none;
                break-inside: avoid;
                border: 1px solid #cccccc;
            }

            .container {
                width: 100%;
            }
        }

    </style>
</head>

<body>

<header class="hero">
    <div class="container">

        <span class="badge">
            JSSSTU • 24CS510 • UNIT 1
        </span>

        <h1>
            Store-and-Forward Packet Switching
        </h1>

        <p>
            Network Layer Design Issues
            <br>
            Topic 01 | Computer Networks
        </p>

    </div>
</header>


<main class="container">

    <!-- SECTION 1: SYLLABUS STATUS -->

    <section>
        <h2>1. Syllabus and Source Status</h2>

        <div class="success">
            <strong>Syllabus status:</strong>
            Explicitly included in Unit 1 of the
            JSSSTU 24CS510 syllabus.
        </div>

        <p>
            <strong>Primary source:</strong>
            Unit-01 PPT, Store-and-Forward Packet
            Switching section.
        </p>

        <p>
            <strong>Supporting reference:</strong>
            Tanenbaum, Feamster and Wetherall,
            Computer Networks, Sixth Edition,
            Section 5.1.1.
        </p>

        <p>
            <strong>Self-learning exclusion:</strong>
            This is a regular Unit 1 syllabus topic,
            not one of the explicitly designated
            self-learning topics.
        </p>

        <p>
            <strong>Coverage assessment:</strong>
            The PPT directly explains the definition,
            network components, packet storage,
            checksum verification and forwarding.
            This topic is adequately introduced in
            the PPT. Additional timing details below
            are supplementary explanations.
        </p>
    </section>


    <!-- SECTION 2: DEFINITION -->

    <section>
        <h2>2. Definition</h2>

        <div class="definition">
            <strong>
                Store-and-forward packet switching
            </strong>
            is a packet-switching mechanism in which
            a router receives and stores an entire
            packet, performs the required processing,
            including checksum verification as
            described in the PPT, and then forwards
            the packet to the next router.
        </div>

        <p>
            A message is divided into packets before
            transmission through a packet-switched
            network. These packets travel through
            interconnected routers to reach the
            destination.
        </p>

        <p>
            Each intermediate router receives the
            packet over an incoming link, stores it
            temporarily and forwards it over an
            appropriate outgoing link.
        </p>
    </section>


    <!-- SECTION 3: NETWORK DIAGRAM -->

    <section>
        <h2>3. Network Architecture</h2>

        <p>
            The PPT illustrates a network containing
            customer equipment, ISP routers and
            transmission lines.
        </p>

        <div class="diagram">

            <svg viewBox="0 0 850 330"
                 xmlns="http://www.w3.org/2000/svg"
                 role="img"
                 aria-label="Store-and-forward packet
                 switching network">

                <defs>
                    <marker id="arrow"
                            markerWidth="10"
                            markerHeight="10"
                            refX="8"
                            refY="3"
                            orient="auto">

                        <path d="M0,0 L0,6 L9,3 z"
                              fill="#2457d6"/>
                    </marker>
                </defs>

                <!-- ISP NETWORK -->

                <rect x="175" y="35"
                      width="500" height="235"
                      rx="18"
                      fill="#eef3ff"
                      stroke="#2457d6"
                      stroke-width="2"
                      stroke-dasharray="7 5"/>

                <text x="425" y="60"
                      font-size="17"
                      text-anchor="middle"
                      fill="#193b8c"
                      font-weight="bold">
                    ISP NETWORK
                </text>

                <!-- HOST H1 -->

                <rect x="15" y="125"
                      width="100" height="60"
                      rx="10"
                      fill="#ffffff"
                      stroke="#64748b"
                      stroke-width="2"/>

                <text x="65" y="150"
                      font-size="15"
                      text-anchor="middle"
                      fill="#172033">
                    Host H1
                </text>

                <text x="65" y="170"
                      font-size="11"
                      text-anchor="middle"
                      fill="#5e6b82">
                    Source
                </text>

                <!-- ROUTER A -->

                <rect x="205" y="125"
                      width="100" height="60"
                      rx="10"
                      fill="#dbeafe"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="255" y="151"
                      font-size="16"
                      text-anchor="middle"
                      fill="#193b8c"
                      font-weight="bold">
                    Router A
                </text>

                <text x="255" y="170"
                      font-size="11"
                      text-anchor="middle"
                      fill="#193b8c">
                    Receive / Store
                </text>

                <!-- ROUTER B -->

                <rect x="385" y="125"
                      width="100" height="60"
                      rx="10"
                      fill="#dbeafe"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="435" y="151"
                      font-size="16"
                      text-anchor="middle"
                      fill="#193b8c"
                      font-weight="bold">
                    Router B
                </text>

                <text x="435" y="170"
                      font-size="11"
                      text-anchor="middle"
                      fill="#193b8c">
                    Process
                </text>

                <!-- ROUTER C -->

                <rect x="565" y="125"
                      width="100" height="60"
                      rx="10"
                      fill="#dbeafe"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="615" y="151"
                      font-size="16"
                      text-anchor="middle"
                      fill="#193b8c"
                      font-weight="bold">
                    Router C
                </text>

                <text x="615" y="170"
                      font-size="11"
                      text-anchor="middle"
                      fill="#193b8c">
                    Forward
                </text>

                <!-- DESTINATION -->

                <rect x="735" y="125"
                      width="100" height="60"
                      rx="10"
                      fill="#dcfce7"
                      stroke="#15803d"
                      stroke-width="2"/>

                <text x="785" y="150"
                      font-size="15"
                      text-anchor="middle"
                      fill="#166534">
                    Host H2
                </text>

                <text x="785" y="170"
                      font-size="11"
                      text-anchor="middle"
                      fill="#166534">
                    Destination
                </text>

                <!-- LINKS -->

                <path d="M115 155 H195"
                      stroke="#2457d6"
                      stroke-width="3"
                      marker-end="url(#arrow)"
                      fill="none"/>

                <path d="M305 155 H375"
                      stroke="#2457d6"
                      stroke-width="3"
                      marker-end="url(#arrow)"
                      fill="none"/>

                <path d="M485 155 H555"
                      stroke="#2457d6"
                      stroke-width="3"
                      marker-end="url(#arrow)"
                      fill="none"/>

                <path d="M665 155 H725"
                      stroke="#2457d6"
                      stroke-width="3"
                      marker-end="url(#arrow)"
                      fill="none"/>

                <!-- LEGEND -->

                <text x="425" y="225"
                      font-size="14"
                      text-anchor="middle"
                      fill="#334155">
                    Each router receives the complete
                    packet before forwarding it.
                </text>

                <text x="425" y="248"
                      font-size="12"
                      text-anchor="middle"
                      fill="#5e6b82">
                    Schematic illustration;
                    actual networks can have
                    alternative routes.
                </text>

            </svg>

        </div>

        <p class="caption">
            Figure 1: Simplified store-and-forward
            packet-switching path.
        </p>

        <div class="note">
            <strong>PPT terminology:</strong>
            Host H1, Router A and the ISP's
            equipment are introduced in the slides.
            Host H2 is connected through customer
            router F and a LAN. Router F is
            customer-owned, not ISP-owned.
        </div>
    </section>


    <!-- SECTION 4: COMPONENTS -->

    <section>
        <h2>4. Main Components</h2>

        <div class="table-wrap">

            <table>
                <thead>
                    <tr>
                        <th>Component</th>
                        <th>Function</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>Source host H1</td>
                        <td>
                            Generates packets that
                            must be delivered.
                        </td>
                    </tr>

                    <tr>
                        <td>Transmission line</td>
                        <td>
                            Carries packets between
                            connected network devices.
                        </td>
                    </tr>

                    <tr>
                        <td>Router</td>
                        <td>
                            Receives, stores and
                            processes packets before
                            forwarding them.
                        </td>
                    </tr>

                    <tr>
                        <td>ISP equipment</td>
                        <td>
                            Contains network equipment
                            such as routers connected
                            by transmission lines.
                        </td>
                    </tr>

                    <tr>
                        <td>Customer router F</td>
                        <td>
                            Connects a customer LAN
                            to the ISP network.
                        </td>
                    </tr>

                    <tr>
                        <td>Destination host H2</td>
                        <td>
                            Receives the delivered
                            packets.
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>
    </section>


    <!-- SECTION 5: WORKING -->

    <section>
        <h2>5. Working Principle</h2>

        <p>
            The operation follows a receive-store-
            process-forward sequence.
        </p>

        <ol class="steps">

            <li>
                <strong>Packet transmission:</strong>
                The source host transmits a packet
                to the nearest router.
            </li>

            <li>
                <strong>Complete reception:</strong>
                The router receives the entire
                packet before forwarding it.
            </li>

            <li>
                <strong>Temporary storage:</strong>
                The packet is stored in the router.
            </li>

            <li>
                <strong>Processing:</strong>
                The link's processing includes
                checksum verification, as stated
                in the PPT.
            </li>

            <li>
                <strong>Forwarding:</strong>
                The router forwards the packet
                to the next router along the path.
            </li>

            <li>
                <strong>Delivery:</strong>
                The packet continues through the
                network until it reaches the
                destination host.
            </li>

        </ol>
    </section>


    <!-- SECTION 6: FLOWCHART -->

    <section>
        <h2>6. Flowchart</h2>

        <div class="diagram">

            <svg viewBox="0 0 600 520"
                 xmlns="http://www.w3.org/2000/svg"
                 role="img"
                 aria-label="Store and forward
                 packet switching flowchart">

                <defs>
                    <marker id="flowArrow"
                            markerWidth="10"
                            markerHeight="10"
                            refX="8"
                            refY="3"
                            orient="auto">

                        <path d="M0,0 L0,6 L9,3 z"
                              fill="#2457d6"/>
                    </marker>
                </defs>

                <!-- START -->

                <rect x="190" y="15"
                      width="220" height="45"
                      rx="22"
                      fill="#dbeafe"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="300" y="43"
                      text-anchor="middle"
                      font-size="16"
                      fill="#193b8c">
                    Packet arrives
                </text>

                <!-- ARROW -->

                <path d="M300 60 V90"
                      stroke="#2457d6"
                      stroke-width="2"
                      marker-end="url(#flowArrow)"/>

                <!-- STORE -->

                <rect x="165" y="95"
                      width="270" height="55"
                      rx="8"
                      fill="#eef2ff"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="300" y="118"
                      text-anchor="middle"
                      font-size="15"
                      fill="#193b8c">
                    Store complete packet
                </text>

                <text x="300" y="137"
                      text-anchor="middle"
                      font-size="12"
                      fill="#334155">
                    in router memory
                </text>

                <!-- ARROW -->

                <path d="M300 150 V180"
                      stroke="#2457d6"
                      stroke-width="2"
                      marker-end="url(#flowArrow)"/>

                <!-- CHECK -->

                <rect x="165" y="185"
                      width="270" height="55"
                      rx="8"
                      fill="#eef2ff"
                      stroke="#2457d6"
                      stroke-width="2"/>

                <text x="300" y="208"
                      text-anchor="middle"
                      font-size="15"
                      fill="#193b8c">
                    Process packet
                </text>

                <text x="300" y="227"
                      text-anchor="middle"
                      font-size="12"
                      fill="#334155">
                    Verify checksum
                </text>

                <!-- ARROW -->

                <path d="M300 240 V270"
                      stroke="#2457d6"
                      stroke-width="2"
                      marker-end="url(#flowArrow)"/>

                <!-- FORWARD -->

                <rect x="165" y="275"
                      width="270" height="55"
                      rx="8"
                      fill="#dcfce7"
                      stroke="#15803d"
                      stroke-width="2"/>

                <text x="300" y="298"
                      text-anchor="middle"
                      font-size="15"
                      fill="#166534">
                    Forward packet
                </text>

                <text x="300" y="317"
                      text-anchor="middle"
                      font-size="12"
                      fill="#166534">
                    to next router
                </text>

                <!-- ARROW -->

                <path d="M300 330 V360"
                      stroke="#2457d6"
                      stroke-width="2"
                      marker-end="url(#flowArrow)"/>

                <!-- DECISION -->

                <path d="M300 365 L400 405
                         L300 445 L200 405 Z"
                      fill="#fff7ed"
                      stroke="#b45309"
                      stroke-width="2"/>

                <text x="300" y="401"
                      text-anchor="middle"
                      font-size="14"
                      fill="#92400e">
                    Destination
                </text>

                <text x="300" y="418"
                      text-anchor="middle"
                      font-size="14"
                      fill="#92400e">
                    reached?
                </text>

                <!-- YES -->

                <path d="M400 405 H520 V475"
                      fill="none"
                      stroke="#15803d"
                      stroke-width="2"
                      marker-end="url(#flowArrow)"/>

                <text x="450" y="392"
                      font-size="13"
                      fill="#15803d">
                    Yes
                </text>

                <rect x="410" y="475"
                      width="175" height="35"
                      rx="8"
                      fill="#dcfce7"
                      stroke="#15803d"
                      stroke-width="2"/>

                <text x="497" y="497"
                      text-anchor="middle"
                      font-size="13"
                      fill="#166534">
                    Deliver packet
                </text>

                <!-- NO / REPEAT -->

                <path d="M200 405 H80 V122 H155"
                      fill="none"
                      stroke="#2457d6"
                      stroke-width="2"
                      stroke-dasharray="6 4"
                      marker-end="url(#flowArrow)"/>

                <text x="90" y="392"
                      font-size="13"
                      fill="#2457d6">
                    No: next hop
                </text>

            </svg>

        </div>

        <p class="caption">
            Figure 2: The packet is stored and
            processed at each intermediate router.
        </p>
    </section>


    <!-- SECTION 7: EXAMPLE -->

    <section>
        <h2>7. Worked Example</h2>

        <p>
            Consider a packet travelling from Host
            H1 to Host H2 through three routers:
            A, B and C.
        </p>

        <div class="definition">
            Assume that the packet size is 1,000
            bytes and that each link has a
            transmission rate of 1 Mbps.
        </div>

        <h3>Step 1: Calculate transmission time</h3>

        <p>
            Packet size in bits:
        </p>

        <p>
            1,000 × 8 = 8,000 bits
        </p>

        <p>
            Transmission rate:
        </p>

        <p>
            1 Mbps = 1,000,000 bits/second
        </p>

        <p>
            Transmission time:
        </p>

        <p>
            <strong>
                T = Packet size / Transmission rate
            </strong>
        </p>

        <p>
            T = 8,000 / 1,000,000
        </p>

        <p>
            T = 0.008 seconds = 8 milliseconds
        </p>

        <div class="success">
            <strong>Result:</strong>
            One complete packet requires 8 ms
            of transmission time on a 1 Mbps link,
            excluding propagation, processing
            and queueing delays.
        </div>

        <h3>Step 2: Calculate idealized multi-hop delay</h3>

        <p>
            Suppose the packet traverses four
            equal-rate links. Assume store-and-
            forward operation, no queueing or
            processing delay, and a negligible
            propagation delay.
        </p>

        <p>
            Total transmission contribution:
        </p>

        <p>
            T = 4 × 8 ms = 32 ms
        </p>

        <div class="note">
            This is an idealized example.
            Real network delay also depends on
            propagation delay, queueing delay,
            router processing and the actual
            network path.
        </div>
    </section>


    <!-- SECTION 8: IMPORTANT CONCEPTS -->

    <section>
        <h2>8. Important Concepts</h2>

        <h3>8.1 Why is the complete packet stored?</h3>

        <p>
            Store-and-forward operation requires
            the complete packet to arrive at the
            router before it is forwarded to the
            next hop. The router can then perform
            the required processing before
            forwarding.
        </p>

        <h3>8.2 What is checksum verification?</h3>

        <p>
            A checksum is used to detect certain
            errors in data. Your PPT specifically
            mentions checksum verification during
            the packet's processing at the router.
        </p>

        <div class="warning">
            <strong>Technical distinction:</strong>
            Do not assume that every modern router
            verifies a checksum over the entire
            packet at every hop. The precise
            operation depends on the protocol
            and the type of checksum.
        </div>

        <h3>8.3 What causes additional delay?</h3>

        <ul>
            <li>
                <strong>Transmission delay:</strong>
                Time required to put all packet
                bits onto a link.
            </li>

            <li>
                <strong>Propagation delay:</strong>
                Time taken by the signal to travel
                through the medium.
            </li>

            <li>
                <strong>Processing delay:</strong>
                Time used by the router to
                process the packet.
            </li>

            <li>
                <strong>Queueing delay:</strong>
                Time the packet waits before
                being transmitted.
            </li>
        </ul>
    </section>


    <!-- SECTION 9: ADVANTAGES AND LIMITATIONS -->

    <section>
        <h2>9. Advantages and Limitations</h2>

        <div class="table-wrap">

            <table>
                <thead>
                    <tr>
                        <th>Advantages</th>
                        <th>Limitations</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>
                            Packets can be processed
                            at intermediate routers.
                        </td>

                        <td>
                            Each hop introduces
                            transmission and
                            processing delay.
                        </td>
                    </tr>

                    <tr>
                        <td>
                            Packets can be forwarded
                            through multiple routers
                            to reach distant hosts.
                        </td>

                        <td>
                            Queueing can increase
                            delay during congestion.
                        </td>
                    </tr>

                    <tr>
                        <td>
                            Packet switching allows
                            network links to be
                            shared by multiple flows.
                        </td>

                        <td>
                            Insufficient buffer space
                            can cause packet loss.
                        </td>
                    </tr>

                    <tr>
                        <td>
                            Routers can choose outgoing
                            links according to their
                            forwarding information.
                        </td>

                        <td>
                            The packet must be stored
                            until it has been received
                            completely.
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>

        <p>
            These advantages and limitations are
            supplementary explanatory points
            consistent with the packet-switching
            model. They are not presented as a
            verbatim list from your PPT.
        </p>
    </section>


    <!-- SECTION 10: FIVE-MARK ANSWER -->

    <section>
        <h2>
            10. Exam-Ready Answer
        </h2>

        <div class="answer">

            <span class="marks">5 MARKS</span>

            <h3>
                Explain Store-and-Forward
                Packet Switching.
            </h3>

            <p>
                Store-and-forward packet switching
                is a technique in which a router
                receives and stores an entire
                packet before forwarding it to
                the next router.
            </p>

            <p>
                The source host transmits the
                packet to the nearest router.
                The router stores the packet
                until it has fully arrived and
                performs the required processing,
                including checksum verification
                as described in the course PPT.
            </p>

            <p>
                After processing, the packet is
                forwarded to the next router
                along the path. This process is
                repeated until the packet reaches
                the destination host.
            </p>

            <p>
                The main stages are reception,
                temporary storage, processing,
                forwarding and destination
                delivery.
            </p>

            <p>
                Store-and-forward packet switching
                is an important mechanism used in
                packet-switched networks to move
                data across interconnected routers.
            </p>

        </div>
    </section>


    <!-- SECTION 11: TEN-MARK ANSWER -->

    <section>
        <h2>
            11. Exam-Ready Answer
        </h2>

        <div class="answer">

            <span class="marks">10 MARKS</span>

            <h3>
                Explain the architecture and
                operation of Store-and-Forward
                Packet Switching with a diagram.
            </h3>

            <h3>Definition</h3>

            <p>
                Store-and-forward packet switching
                is a mechanism in which an
                intermediate router receives and
                stores the complete packet before
                processing and forwarding it.
            </p>

            <h3>Architecture</h3>

            <p>
                A packet-switched network consists
                of hosts, routers and transmission
                lines. ISP equipment connects
                routers through transmission lines.
                Customer equipment can connect
                through a customer-owned router
                and a LAN.
            </p>

            <p>
                <strong>Diagram:</strong>
                Reproduce Figure 1, showing the
                source host, intermediate routers,
                transmission links and destination
                host.
            </p>

            <h3>Working</h3>

            <ol>
                <li>
                    The source host generates
                    and transmits a packet.
                </li>

                <li>
                    The packet reaches the
                    nearest router.
                </li>

                <li>
                    The router receives and
                    stores the entire packet.
                </li>

                <li>
                    The router performs the
                    required processing,
                    including checksum verification
                    as described in the PPT.
                </li>

                <li>
                    The packet is forwarded
                    over the appropriate outgoing
                    link to the next router.
                </li>

                <li>
                    The operation continues
                    across intermediate routers
                    until the destination host
                    receives the packet.
                </li>
            </ol>

            <h3>Delay</h3>

            <p>
                Packet delivery time depends on
                transmission delay, propagation
                delay, processing delay and
                queueing delay. Store-and-forward
                operation requires the entire
                packet to be received at each
                intermediate router before
                forwarding it.
            </p>

            <h3>Conclusion</h3>

            <p>
                Store-and-forward packet switching
                enables packets to travel through
                interconnected routers. The
                receive-store-process-forward
                sequence is its defining
                characteristic.
            </p>

        </div>

        <div class="note">
            <strong>Answer-writing tip:</strong>
            For a 10-mark question, include a
            labelled diagram, the complete
            sequence of operations, the role of
            routers and a brief explanation of
            delay. Adjust the length to the
            question wording.
        </div>
    </section>


    <!-- SECTION 12: QUICK REVISION -->

    <section>
        <h2>12. Quick Revision</h2>

        <ul class="revision">

            <li>
                <strong>Definition:</strong>
                Receive the entire packet,
                store it, process it and forward it.
            </li>

            <li>
                <strong>Core sequence:</strong>
                Receive → Store → Process →
                Forward → Deliver.
            </li>

            <li>
                <strong>Components:</strong>
                Hosts, routers and transmission lines.
            </li>

            <li>
                <strong>Checksum:</strong>
                Explicitly mentioned in the PPT's
                description of router processing.
            </li>

            <li>
                <strong>Delay:</strong>
                Transmission + propagation +
                processing + queueing.
            </li>

            <li>
                <strong>Diagram:</strong>
                Show source, intermediate routers,
                links and destination.
            </li>

            <li>
                <strong>Five-mark answer:</strong>
                Definition and working sequence.
            </li>

            <li>
                <strong>Ten-mark answer:</strong>
                Definition, architecture, labelled
                diagram, working and delay.
            </li>

        </ul>
    </section>


    <!-- SECTION 13: SELF-TEST -->

    <section>
        <h2>13. Self-Test</h2>

        <ol>
            <li>
                Define store-and-forward
                packet switching.
            </li>

            <li>
                Why must a packet be completely
                received before forwarding?
            </li>

            <li>
                State the main steps performed
                by a router.
            </li>

            <li>
                Explain the roles of the ISP
                router and customer router.
            </li>

            <li>
                Distinguish transmission delay
                from propagation delay.
            </li>
        </ol>

        <details>
            <summary>
                Show short answers
            </summary>

            <ol>
                <li>
                    A router stores the complete
                    packet before forwarding it.
                </li>

                <li>
                    Complete reception is a
                    defining requirement of the
                    store-and-forward mechanism.
                </li>

                <li>
                    Receive, store, process,
                    forward and deliver.
                </li>

                <li>
                    ISP routers form part of the
                    provider network; a customer
                    router connects customer
                    equipment to the ISP.
                </li>

                <li>
                    Transmission delay is the
                    time to place packet bits on
                    a link. Propagation delay is
                    the time for the signal to
                    travel through the medium.
                </li>
            </ol>
        </details>
    </section>



    <!-- SECTION 14: PREVIOUS-PAPER AND POSSIBLE QUESTIONS -->

    <section>
        <h2>14. Previous-Paper and Possible Questions</h2>

        <div class="note">
            <strong>Verified past-paper question:</strong>
            The uploaded JSSSTU Computer Networks paper, labelled
            20CS520, page 1, Part B, Question 6(b), asks:
            “Explain Store and Forward Packet Switching network
            environment with a neat diagram.” It carries 5 marks.
            This is a useful question-pattern reference for 24CS510;
            it is not a guarantee that the same question will recur.
        </div>

        <div class="answer">
            <span class="marks">PAST PAPER • 5 MARKS</span>
            <h3>Q1. Explain Store and Forward Packet Switching network environment with a neat diagram.</h3>

            <p><strong>Answer:</strong></p>
            <p>
                Store-and-forward packet switching is a mechanism in which
                an intermediate router receives and stores the entire packet
                before processing and forwarding it to the next router.
            </p>
            <p><strong>Working:</strong></p>
            <ol>
                <li>The source host sends a packet to the first router.</li>
                <li>The router receives and stores the complete packet in memory.</li>
                <li>The router performs the required processing, including the checksum verification described in the Unit-01 PPT.</li>
                <li>The router forwards the packet over the appropriate outgoing link to the next router.</li>
                <li>The same process is repeated at intermediate routers until the packet reaches the destination host.</li>
            </ol>
            <p>
                Draw a labelled diagram showing:
                <strong>Source Host → Router A → Router B → Destination Host</strong>.
                Inside each router, write “Receive complete packet → Store → Process → Forward”.
            </p>
            <p>
                Store-and-forward switching allows packets to travel through
                interconnected routers, but introduces transmission delay at
                each hop. Queueing and processing may add further delay.
            </p>
            <p><strong>Conclusion:</strong> A router receives the complete packet before forwarding it to the next hop.</p>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • 3–5 MARKS</span>
            <h3>Q2. Define store-and-forward packet switching and explain its operation.</h3>
            <p><strong>Answer:</strong> Store-and-forward packet switching is a technique in which each intermediate router receives and stores the entire packet before forwarding it. Its main steps are reception, temporary storage, packet processing, next-hop forwarding and eventual delivery to the destination. The sequence is repeated at every intermediate router.</p>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • 3 MARKS</span>
            <h3>Q3. Explain the role of a router in store-and-forward packet switching.</h3>
            <p><strong>Answer:</strong> A router receives the complete packet from an incoming link, stores it temporarily, examines relevant packet information, determines the outgoing link and forwards the packet. If the outgoing link is busy, the packet may wait in a queue.</p>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • 5 MARKS</span>
            <h3>Q4. State the advantages and limitations of store-and-forward packet switching.</h3>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr><th>Advantages</th><th>Limitations</th></tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Communication links can be shared by multiple packet flows.</td>
                            <td>Transmission delay is added at each hop.</td>
                        </tr>
                        <tr>
                            <td>Routers can temporarily buffer packets while an outgoing link is busy.</td>
                            <td>Buffers require memory and may fill up.</td>
                        </tr>
                        <tr>
                            <td>Routers can process packet information and choose an outgoing link.</td>
                            <td>Congestion can cause queueing delay and packet loss.</td>
                        </tr>
                        <tr>
                            <td>Packets can travel through multiple interconnected routers.</td>
                            <td>The complete packet must arrive before forwarding of that packet begins.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • NUMERICAL</span>
            <h3>Q5. A packet of 1,000 bytes travels over four 1 Mbps links. Find the total transmission time. Ignore propagation, processing and queueing delays.</h3>
            <p><strong>Step 1 — Convert bytes to bits:</strong></p>
            <p>Packet length = 1,000 × 8 = 8,000 bits.</p>
            <p><strong>Step 2 — Transmission time for one link:</strong></p>
            <p>T = L/R = 8,000 / 1,000,000 seconds = 0.008 seconds = 8 ms.</p>
            <p><strong>Step 3 — Four links:</strong></p>
            <p>Total transmission time = 4 × 8 ms = <strong>32 ms</strong>.</p>
            <div class="note">
                This answer assumes a single packet, equal-rate links and no overlap
                between its transmissions on successive links. If a question includes
                multiple packets or pipelining, calculate according to those conditions.
            </div>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • 2–3 MARKS</span>
            <h3>Q6. Why does store-and-forward switching introduce delay?</h3>
            <p><strong>Answer:</strong> A router must receive the complete packet before it can forward that packet on the next link. This introduces transmission delay at each hop. Processing, propagation and queueing can add further delay.</p>
        </div>

        <div class="answer">
            <span class="marks">PRACTICE • 3 MARKS</span>
            <h3>Q7. Differentiate transmission delay and propagation delay.</h3>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr><th>Transmission delay</th><th>Propagation delay</th></tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Time required to put all packet bits onto the link.</td>
                            <td>Time required for the signal to travel across the link.</td>
                        </tr>
                        <tr>
                            <td>Depends mainly on packet length and link rate: L/R.</td>
                            <td>Depends mainly on link distance and signal propagation speed.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="success">
            <strong>Revision priority:</strong> Prepare Q1 first because it directly
            matches the uploaded paper. Then practise the definition/working,
            advantages and limitations, and numerical question. Q2–Q7 are practice
            questions, not verified past-paper questions.
        </div>
    </section>


    <!-- SECTION 15: SOURCE TRACKING -->

    <section>
        <h2>14. Source and Accuracy Notes</h2>

        <ul>
            <li>
                <strong>Official syllabus:</strong>
                JSSSTU 24CS510, Unit 1.
            </li>

            <li>
                <strong>Primary lecture source:</strong>
                Uploaded Unit-01 PPT,
                Store-and-Forward Packet Switching
                slides.
            </li>

            <li>
                <strong>Reference:</strong>
                Tanenbaum, Feamster and Wetherall,
                Computer Networks, Sixth Edition,
                Section 5.1.1.
            </li>

            <li>
                <strong>Supplementary material:</strong>
                Delay calculation and explanatory
                advantages and limitations.
            </li>

            <li>
                <strong>Syllabus gap:</strong>
                No major gap identified for this
                topic based on the PPT's direct
                explanation of the mechanism.
            </li>
        </ul>

        <p>
            The diagram is a simplified redraw
            for studying. It is not an exact
            reproduction of the source slide.
        </p>
    </section>


</main>


<footer class="footer">
    <div class="container">
        JSSSTU • 24CS510 • Computer Networks
        <br>
        Unit 1 — Topic 1
    </div>
</footer>

</body>
</html>
"""


# ------------------------------------------------------------
# WRITE THE TOPIC PAGE
# ------------------------------------------------------------

OUTPUT_FILE.write_text(html, encoding="utf-8")

print("Topic page generated successfully!")
print(f"Output: {OUTPUT_FILE.resolve()}")
print()
print("Open the HTML file in your browser.")