"""
Republic Hall Fellow Application Portal - Streamlit Edition
Kwame Nkrumah University of Science and Technology (KNUST)

Run with:
    streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components
from datetime import date

# Configure Streamlit page
st.set_page_config(
    page_title="Republic Hall Fellow Application Portal - KNUST",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Republic Hall CSS styling for Streamlit container
st.markdown(
    """<style>
    :root {
        --republic-green: #0b6623;
        --republic-gold: #d4af37;
    }
    
    .stApp {
        background-color: #f8fafc;
    }

    header[data-testid="stHeader"] {
        display: none;
    }

    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1350px;
    }
    </style>""",
    unsafe_allow_html=True,
)

# Build full client-side interactive component with live signature drawing canvas,
# real-time live A4 letter sheet preview, and one-click crisp PDF download
today_str = date.today().strftime("%B %d, %Y")

portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Republic Hall Fellow Application Portal - KNUST</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #f8fafc;
    color: #1e293b;
    padding: 12px;
  }}

  /* Top Navigation Banner */
  .portal-header {{
    background-color: #0b6623;
    color: #ffffff;
    border-radius: 12px;
    border-bottom: 4px solid #d4af37;
    padding: 16px 20px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  }}

  .header-left {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  .crest-svg {{
    width: 60px;
    height: 60px;
    flex-shrink: 0;
  }}

  .header-title-box .sub {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #d4af37;
    text-transform: uppercase;
  }}

  .header-title-box h1 {{
    font-size: 22px;
    font-weight: 900;
    letter-spacing: -0.5px;
    margin: 2px 0;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .motto-badge {{
    font-size: 10px;
    font-weight: 800;
    background: #d4af37;
    color: #084c1a;
    padding: 2px 8px;
    border-radius: 9999px;
    text-transform: uppercase;
  }}

  .header-subtitle {{
    font-size: 12px;
    color: #d1fae5;
  }}

  /* Split Screen Grid */
  .grid-layout {{
    display: grid;
    grid-template-columns: 460px 1fr;
    gap: 24px;
    align-items: start;
  }}

  @media (max-width: 1024px) {{
    .grid-layout {{
      grid-template-columns: 1fr;
    }}
  }}

  /* Left Form Card */
  .form-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}

  .form-title {{
    font-size: 16px;
    font-weight: 800;
    color: #0b6623;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
  }}

  .compulsory-pill {{
    font-size: 11px;
    font-weight: 700;
    background: #fef3c7;
    color: #92400e;
    padding: 2px 8px;
    border-radius: 9999px;
    border: 1px solid #fde68a;
  }}

  .form-desc {{
    font-size: 12px;
    color: #64748b;
    margin-bottom: 16px;
  }}

  .form-group {{
    margin-bottom: 14px;
  }}

  .form-group label {{
    display: block;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #334155;
    margin-bottom: 4px;
  }}

  .form-group label span.req {{
    color: #dc2626;
  }}

  .form-input {{
    width: 100%;
    padding: 9px 12px;
    font-size: 13px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    outline: none;
    transition: border-color 0.15s;
  }}

  .form-input:focus {{
    border-color: #0b6623;
    box-shadow: 0 0 0 2px rgba(11, 102, 35, 0.15);
  }}

  .two-cols {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}

  /* Live Signature Canvas */
  .sig-section {{
    margin-top: 18px;
    padding-top: 14px;
    border-top: 1px solid #f1f5f9;
  }}

  .sig-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }}

  .sig-badge {{
    font-size: 11px;
    font-weight: 600;
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    padding: 2px 8px;
    border-radius: 9999px;
  }}

  .sig-controls {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
    font-size: 12px;
  }}

  .ink-group {{
    display: flex;
    gap: 6px;
    align-items: center;
  }}

  .ink-btn {{
    font-size: 11px;
    font-weight: 600;
    padding: 4px 8px;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}

  .ink-btn.active {{
    border-color: #000080;
    background: #eff6ff;
    color: #000080;
    box-shadow: 0 0 0 1px #000080;
  }}

  .ink-btn.black.active {{
    border-color: #111111;
    background: #f1f5f9;
    color: #111111;
    box-shadow: 0 0 0 1px #111111;
  }}

  .btn-clear {{
    background: #ffffff;
    border: 1px solid #fecdd3;
    color: #be123c;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 8px;
    border-radius: 6px;
    cursor: pointer;
  }}

  .btn-clear:hover {{
    background: #ffe4e6;
  }}

  .canvas-wrapper {{
    position: relative;
    border: 2px dashed #cbd5e1;
    border-radius: 8px;
    background: #ffffff;
    overflow: hidden;
  }}

  canvas#sig-pad {{
    width: 100%;
    height: 120px;
    display: block;
    cursor: crosshair;
    touch-action: none;
  }}

  .sig-guide {{
    position: absolute;
    bottom: 12px;
    left: 16px;
    right: 16px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    color: #94a3b8;
    pointer-events: none;
  }}

  .quick-btns {{
    display: flex;
    gap: 8px;
    margin-bottom: 14px;
  }}

  .btn-small {{
    font-size: 11px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid #cbd5e1;
    background: #f8fafc;
  }}

  .btn-small.green {{
    background: #ecfdf5;
    border-color: #a7f3d0;
    color: #065f46;
  }}

  /* Right Action Buttons */
  .action-bar {{
    margin-bottom: 14px;
  }}

  .action-buttons {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 10px;
  }}

  .btn-download {{
    background-color: #0b6623;
    color: #ffffff;
    border: none;
    padding: 12px 16px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 6px -1px rgba(11, 102, 35, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: background-color 0.15s;
  }}

  .btn-download:hover {{
    background-color: #084c1a;
  }}

  .btn-download:disabled {{
    background-color: #cbd5e1;
    cursor: not-allowed;
    box-shadow: none;
  }}

  .btn-print {{
    background-color: #ffffff;
    color: #1e293b;
    border: 2px solid #cbd5e1;
    padding: 12px 16px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }}

  .btn-print:hover {{
    background-color: #f1f5f9;
  }}

  .reminder-box {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 11px;
    color: #92400e;
    margin-bottom: 10px;
    display: none;
  }}

  .success-box {{
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 11px;
    color: #065f46;
    margin-bottom: 10px;
    display: none;
  }}

  /* Live A4 Letter Preview Sheet */
  .a4-container {{
    display: flex;
    justify-content: center;
    background: transparent;
  }}

  #a4-letter-sheet {{
    width: 794px;
    min-height: 1123px;
    background-color: #ffffff;
    color: #111111;
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 11.5pt;
    line-height: 1.65;
    padding: 76px 72px 80px 72px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    box-sizing: border-box;
    text-align: left;
  }}

  .memo-line {{
    display: flex;
    margin-bottom: 4px;
  }}

  .memo-label {{
    width: 80px;
    font-weight: bold;
  }}

  .subject-line {{
    font-weight: bold;
    text-decoration: underline;
    margin: 16px 0;
    display: block;
    letter-spacing: 0.2px;
  }}

  .letter-body {{
    margin: 16px 0 24px 0;
    text-align: left;
    line-height: 1.65;
  }}

  .sig-img-container {{
    height: 60px;
    display: flex;
    align-items: flex-end;
    margin: 10px 0;
  }}

  .sig-img-container img {{
    max-height: 55px;
    max-width: 260px;
    object-fit: contain;
  }}

  .sig-empty-placeholder {{
    height: 45px;
    width: 200px;
    border: 1px dashed #cbd5e1;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10pt;
    color: #94a3b8;
    font-style: italic;
  }}

  @media print {{
    body {{
      background: #ffffff !important;
      padding: 0 !important;
    }}
    .no-print, .portal-header, .form-card, .action-bar {{
      display: none !important;
    }}
    #a4-letter-sheet {{
      border: none !important;
      box-shadow: none !important;
      margin: 0 !important;
      padding: 24mm 22mm !important;
      width: 210mm !important;
    }}
  }}
</style>
</head>
<body>

<!-- Header -->
<div class="portal-header no-print">
  <div class="header-left">
    <!-- Republic Hall Crest SVG -->
    <svg class="crest-svg" viewBox="0 0 200 200" role="img" aria-label="Republic Hall KNUST Crest">
      <defs>
        <linearGradient id="crestGreen" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0b6623"/>
          <stop offset="100%" stop-color="#074417"/>
        </linearGradient>
        <linearGradient id="crestGold" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f7e07c"/>
          <stop offset="40%" stop-color="#d4af37"/>
          <stop offset="100%" stop-color="#9a7b1c"/>
        </linearGradient>
        <path id="crestTop" d="M 28 100 A 72 72 0 1 1 172 100" fill="none"/>
        <path id="crestBot" d="M 172 100 A 72 72 0 0 1 28 100" fill="none"/>
      </defs>
      <circle cx="100" cy="100" r="98" fill="url(#crestGold)" stroke="#785e13" stroke-width="1.5"/>
      <circle cx="100" cy="100" r="92" fill="url(#crestGreen)" stroke="url(#crestGold)" stroke-width="2"/>
      <circle cx="100" cy="100" r="66" fill="#fcfbf7" stroke="url(#crestGold)" stroke-width="3"/>
      <text fill="#ffffff" font-size="13" font-weight="800" letter-spacing="2.5" font-family="sans-serif">
        <textPath href="#crestTop" startOffset="50%" text-anchor="middle">REPUBLIC HALL</textPath>
      </text>
      <text fill="#ffffff" font-size="7.8" font-weight="700" letter-spacing="0.8" font-family="sans-serif">
        <textPath href="#crestBot" startOffset="50%" text-anchor="middle">KWAME NKRUMAH UNIV. OF SCI. & TECH.</textPath>
      </text>
      <path d="M 68 62 L 132 62 C 132 94 122 114 100 128 C 78 114 68 94 68 62 Z" fill="#0b6623" stroke="url(#crestGold)" stroke-width="2.5"/>
      <!-- Torch -->
      <g transform="translate(100, 72) scale(0.65)">
        <path d="M 0 -22 C -6 -12 -8 -4 0 4 C 8 -4 6 -12 0 -22 Z" fill="#e65100"/>
        <path d="M 0 -18 C -3 -11 -4 -5 0 1 C 4 -5 3 -11 0 -18 Z" fill="#ffb300"/>
        <path d="M -12 4 L 12 4 L 6 16 L -6 16 Z" fill="url(#crestGold)"/>
        <path d="M -4 16 L 4 16 L 2 34 L -2 34 Z" fill="url(#crestGold)"/>
      </g>
      <!-- Book -->
      <g transform="translate(100, 106) scale(0.68)">
        <path d="M 0 -2 C -12 -10 -28 -8 -32 -2 L -32 16 C -28 10 -12 8 0 16 C 12 8 28 10 32 16 L 32 -2 C 28 -8 12 -10 0 -2 Z" fill="#ffffff" stroke="#0b6623" stroke-width="1.5"/>
        <line x1="0" y1="-2" x2="0" y2="16" stroke="#0b6623" stroke-width="2"/>
      </g>
      <!-- Banner -->
      <g transform="translate(100, 150)">
        <path d="M -68 0 L -60 -10 L -46 -5 L 46 -5 L 60 -10 L 68 0 L 56 12 L -56 12 Z" fill="#d4af37" stroke="#785e13" stroke-width="1.2"/>
        <text x="0" y="7" fill="#084c1a" font-size="9.5" font-weight="900" letter-spacing="1.8" text-anchor="middle" font-family="sans-serif">SET THE PACE</text>
      </g>
    </svg>
    <div class="header-title-box">
      <div class="sub">KWAME NKRUMAH UNIVERSITY OF SCIENCE &amp; TECHNOLOGY, KUMASI</div>
      <h1>REPUBLIC HALL <span class="motto-badge">SET THE PACE</span></h1>
      <div class="header-subtitle">Fellow Application Portal &bull; Official Secretariat Generator</div>
    </div>
  </div>
</div>

<!-- Main Split Screen Grid -->
<div class="grid-layout">
  <!-- Left Column: Form & Live Signature Canvas -->
  <div class="form-card no-print">
    <div class="form-title">
      <span>Applicant Information</span>
      <span class="compulsory-pill">Compulsory (*)</span>
    </div>
    <div class="form-desc">Complete all fields and draw your signature below.</div>

    <div class="quick-btns">
      <button type="button" class="btn-small green" id="btn-sample">Reset Sample Data</button>
      <button type="button" class="btn-small" id="btn-clear-all">Clear All</button>
    </div>

    <!-- Inputs -->
    <div class="form-group">
      <label>Full Name &amp; Academic Title/Rank <span class="req">*</span></label>
      <input type="text" id="inp-name" class="form-input" value="Dr. John Mensah, Senior Lecturer" placeholder="e.g. Dr. John Mensah, Senior Lecturer">
    </div>

    <div class="form-group">
      <label>College / Faculty / Department / Office <span class="req">*</span></label>
      <input type="text" id="inp-dept" class="form-input" value="College of Engineering / Dept. of Mechanical Engineering" placeholder="e.g. College of Engineering / Dept. of Mechanical Engineering">
    </div>

    <div class="two-cols">
      <div class="form-group">
        <label>Phone Number <span class="req">*</span></label>
        <input type="tel" id="inp-phone" class="form-input" value="0240000000" placeholder="0240000000">
      </div>
      <div class="form-group">
        <label>Email Address <span class="req">*</span></label>
        <input type="email" id="inp-email" class="form-input" value="jmensah@knust.edu.gh" placeholder="jmensah@knust.edu.gh">
      </div>
    </div>

    <div class="form-group">
      <label>Application Date <span class="req">*</span></label>
      <input type="text" id="inp-date" class="form-input" value="{today_str}" placeholder="e.g. {today_str}">
    </div>

    <!-- Live Implemented Drawing Signature Pad -->
    <div class="sig-section">
      <div class="sig-header">
        <label style="font-weight: 800; font-size: 12px; color: #0b6623;">
          ✍️ Live Electronic Signature <span class="req">*</span>
        </label>
        <span class="sig-badge" id="sig-status">Live Signature Active</span>
      </div>

      <div class="sig-controls">
        <div class="ink-group">
          <span style="font-size: 11px; font-weight: 700; color: #475569;">Ink:</span>
          <button type="button" class="ink-btn active" id="btn-ink-blue">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#000080;"></span>
            Blue Ink (#000080)
          </button>
          <button type="button" class="ink-btn black" id="btn-ink-black">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#111111;"></span>
            Black Ink (#111111)
          </button>
        </div>
        <button type="button" class="btn-clear" id="btn-clear-sig">Clear Signature</button>
      </div>

      <div class="canvas-wrapper">
        <canvas id="sig-pad" width="420" height="120"></canvas>
        <div class="sig-guide">
          <span>Sign above this line (Mouse or Touch)</span>
          <span>Republic Hall, KNUST</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Right Column: Action Buttons & Live A4 Letter Preview -->
  <div>
    <!-- Action Bar -->
    <div class="action-bar no-print">
      <div class="action-buttons">
        <button type="button" class="btn-download" id="btn-download-pdf">
          <span>📥 Download Completed Application (PDF)</span>
        </button>
        <button type="button" class="btn-print" onclick="window.print()">
          <span>🖨️ Print / Save as PDF</span>
        </button>
      </div>
      <div class="reminder-box" id="reminder-msg">
        ⚠️ Please complete all compulsory fields (*) and draw your signature to download.
      </div>
      <div class="success-box" id="success-msg">
        ✅ Application PDF generated successfully!
      </div>
    </div>

    <!-- Live A4 Sheet Preview -->
    <div class="a4-container">
      <div id="a4-letter-sheet">
        <!-- Date Block -->
        <div class="memo-line">
          <div class="memo-label">Date:</div>
          <div id="prev-date">{today_str}</div>
        </div>
        <div class="memo-line">
          <div class="memo-label">To:</div>
          <div>Hall Warden, Republic Hall</div>
        </div>
        <div class="memo-line" style="align-items: flex-start; margin-bottom: 18px;">
          <div class="memo-label">From:</div>
          <div>
            <div id="prev-name">Dr. John Mensah, Senior Lecturer</div>
            <div><span id="prev-dept">College of Engineering / Dept. of Mechanical Engineering</span>, KNUST</div>
          </div>
        </div>

        <div>Dear Hall Master/Warden,</div>

        <div class="subject-line">APPLICATION FOR FELLOWSHIP OF REPUBLIC HALL, KNUST</div>

        <div class="letter-body">
          <p>
            I write to formally express my interest in serving as a Fellow of Republic Hall, KNUST. I am eager to actively network and collaborate with other Fellows and past students (alumni) to advance the rich traditions, mentorship networks, and continuous development of the Hall. Furthermore, I am deeply committed to promoting student welfare, academic excellence, and a supportive residential community in close partnership with Hall Management. I thank you for your kind consideration and look forward to hearing favorably from you soon.
          </p>
        </div>

        <div style="margin-top: 24px;">Yours faithfully,</div>

        <!-- Rendered Live Signature -->
        <div class="sig-img-container" id="prev-sig-box">
          <img id="prev-sig-img" src="" alt="Electronic Signature" style="display:none;" />
          <div id="prev-sig-none" class="sig-empty-placeholder">[Signature Required]</div>
        </div>

        <div style="line-height: 1.4; margin-top: 6px;">
          <div style="font-weight: bold;" id="prev-name-footer">Dr. John Mensah, Senior Lecturer</div>
          <div><span id="prev-dept-footer">College of Engineering / Dept. of Mechanical Engineering</span>, KNUST</div>
          <div style="font-size: 10.5pt; color: #334155; margin-top: 2px;">
            Contact: <span id="prev-phone">0240000000</span> / <span id="prev-email">jmensah@knust.edu.gh</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // DOM Elements
  const inpName = document.getElementById('inp-name');
  const inpDept = document.getElementById('inp-dept');
  const inpPhone = document.getElementById('inp-phone');
  const inpEmail = document.getElementById('inp-email');
  const inpDate = document.getElementById('inp-date');

  const prevName = document.getElementById('prev-name');
  const prevNameFooter = document.getElementById('prev-name-footer');
  const prevDept = document.getElementById('prev-dept');
  const prevDeptFooter = document.getElementById('prev-dept-footer');
  const prevPhone = document.getElementById('prev-phone');
  const prevEmail = document.getElementById('prev-email');
  const prevDate = document.getElementById('prev-date');

  const prevSigBox = document.getElementById('prev-sig-box');
  const prevSigImg = document.getElementById('prev-sig-img');
  const prevSigNone = document.getElementById('prev-sig-none');

  const btnDownload = document.getElementById('btn-download-pdf');
  const reminderMsg = document.getElementById('reminder-msg');
  const successMsg = document.getElementById('success-msg');

  const btnBlue = document.getElementById('btn-ink-blue');
  const btnBlack = document.getElementById('btn-ink-black');
  const btnClearSig = document.getElementById('btn-clear-sig');
  const btnSample = document.getElementById('btn-sample');
  const btnClearAll = document.getElementById('btn-clear-all');
  const sigStatus = document.getElementById('sig-status');

  // Canvas Setup
  const canvas = document.getElementById('sig-pad');
  const ctx = canvas.getContext('2d');
  let isDrawing = false;
  let hasDrawn = false;
  let inkColor = '#000080';

  function initCanvas() {{
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * 2;
    canvas.height = rect.height * 2;
    ctx.scale(2, 2);
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = 2.2;
    ctx.strokeStyle = inkColor;
    drawSampleSignature();
  }}

  // Draw default sample signature
  function drawSampleSignature() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = inkColor;
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    ctx.moveTo(30, 60);
    ctx.bezierCurveTo(70, 20, 110, 80, 160, 45);
    ctx.bezierCurveTo(190, 25, 220, 75, 270, 50);
    ctx.bezierCurveTo(300, 35, 330, 80, 370, 55);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(80, 75);
    ctx.bezierCurveTo(150, 85, 260, 80, 350, 70);
    ctx.stroke();

    hasDrawn = true;
    updateSigPreview();
  }}

  function updateSigPreview() {{
    if (hasDrawn) {{
      const dataUrl = canvas.toDataURL('image/png');
      prevSigImg.src = dataUrl;
      prevSigImg.style.display = 'block';
      prevSigNone.style.display = 'none';
      sigStatus.textContent = 'Live Signature Active';
      sigStatus.style.background = '#ecfdf5';
      sigStatus.style.color = '#065f46';
    }} else {{
      prevSigImg.src = '';
      prevSigImg.style.display = 'none';
      prevSigNone.style.display = 'flex';
      sigStatus.textContent = 'Signature Required';
      sigStatus.style.background = '#fef2f2';
      sigStatus.style.color = '#991b1b';
    }}
    validate();
  }}

  // Drawing Event Listeners
  function getPos(e) {{
    const rect = canvas.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;
    return {{
      x: clientX - rect.left,
      y: clientY - rect.top
    }};
  }}

  function startDraw(e) {{
    if (e.touches) e.preventDefault();
    isDrawing = true;
    const pos = getPos(e);
    ctx.beginPath();
    ctx.moveTo(pos.x, pos.y);
  }}

  function drawMove(e) {{
    if (!isDrawing) return;
    if (e.touches) e.preventDefault();
    const pos = getPos(e);
    ctx.strokeStyle = inkColor;
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
    hasDrawn = true;
    updateSigPreview();
  }}

  function stopDraw() {{
    if (!isDrawing) return;
    isDrawing = false;
    updateSigPreview();
  }}

  canvas.addEventListener('mousedown', startDraw);
  canvas.addEventListener('mousemove', drawMove);
  canvas.addEventListener('mouseup', stopDraw);
  canvas.addEventListener('mouseleave', stopDraw);

  canvas.addEventListener('touchstart', startDraw, {{ passive: false }});
  canvas.addEventListener('touchmove', drawMove, {{ passive: false }});
  canvas.addEventListener('touchend', stopDraw);

  // Ink Controls
  btnBlue.onclick = () => {{
    inkColor = '#000080';
    btnBlue.classList.add('active');
    btnBlack.classList.remove('active');
  }};

  btnBlack.onclick = () => {{
    inkColor = '#111111';
    btnBlack.classList.add('active');
    btnBlue.classList.remove('active');
  }};

  btnClearSig.onclick = () => {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    hasDrawn = false;
    updateSigPreview();
  }};

  // Live Sync Inputs to Preview
  function updateText() {{
    const name = inpName.value.trim() || '[Full Name & Academic Title/Rank]';
    const dept = inpDept.value.trim() || '[College/Faculty/Department/Office]';
    const phone = inpPhone.value.trim() || '[Phone Number]';
    const email = inpEmail.value.trim() || '[Email Address]';
    const dateVal = inpDate.value.trim() || '[Application Date]';

    prevName.textContent = name;
    prevNameFooter.textContent = name;
    prevDept.textContent = dept;
    prevDeptFooter.textContent = dept;
    prevPhone.textContent = phone;
    prevEmail.textContent = email;
    prevDate.textContent = dateVal;

    validate();
  }}

  [inpName, inpDept, inpPhone, inpEmail, inpDate].forEach(el => {{
    el.addEventListener('input', updateText);
  }});

  // Validation
  function validate() {{
    const isValid = inpName.value.trim() &&
                    inpDept.value.trim() &&
                    inpPhone.value.trim() &&
                    inpEmail.value.trim() &&
                    inpDate.value.trim() &&
                    hasDrawn;

    if (isValid) {{
      btnDownload.disabled = false;
      reminderMsg.style.display = 'none';
    }} else {{
      btnDownload.disabled = true;
      reminderMsg.style.display = 'block';
    }}
    return isValid;
  }}

  // Reset Sample
  btnSample.onclick = () => {{
    inpName.value = 'Dr. John Mensah, Senior Lecturer';
    inpDept.value = 'College of Engineering / Dept. of Mechanical Engineering';
    inpPhone.value = '0240000000';
    inpEmail.value = 'jmensah@knust.edu.gh';
    inpDate.value = '{today_str}';
    drawSampleSignature();
    updateText();
  }};

  // Clear All
  btnClearAll.onclick = () => {{
    inpName.value = '';
    inpDept.value = '';
    inpPhone.value = '';
    inpEmail.value = '';
    inpDate.value = '';
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    hasDrawn = false;
    updateSigPreview();
    updateText();
  }};

  // PDF Download using html2canvas & jsPDF
  btnDownload.onclick = async () => {{
    if (!validate()) return;
    try {{
      btnDownload.innerText = 'Generating Crisp PDF...';
      btnDownload.disabled = true;

      const sheet = document.getElementById('a4-letter-sheet');
      
      const canvasCaptured = await html2canvas(sheet, {{
        scale: 2,
        useCORS: true,
        backgroundColor: '#ffffff',
        width: 794,
        windowWidth: 794
      }});

      const {{ jsPDF }} = window.jspdf;
      const pdf = new jsPDF('portrait', 'mm', 'a4');
      const imgData = canvasCaptured.toDataURL('image/png', 1.0);
      pdf.addImage(imgData, 'PNG', 0, 0, 210, 297, undefined, 'FAST');

      const cleanName = (inpName.value || 'Applicant').trim().replace(/[^\\w\\s-]/g, '').replace(/\\s+/g, '_');
      pdf.save(`Republic_Hall_Fellow_Application_${{cleanName}}.pdf`);

      successMsg.style.display = 'block';
      setTimeout(() => {{ successMsg.style.display = 'none'; }}, 4000);
    }} catch (err) {{
      alert('Error generating PDF: ' + err.message);
    }} finally {{
      btnDownload.innerHTML = '<span>📥 Download Completed Application (PDF)</span>';
      validate();
    }}
  }};

  // Initialize
  window.addEventListener('load', () => {{
    initCanvas();
    updateText();
  }});
  setTimeout(initCanvas, 100);
</script>
</body>
</html>
"""

# Render the application component in Streamlit with full height
components.html(portal_html, height=1280, scrolling=True)
