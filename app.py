import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Republic Hall Fellow Application Portal | KNUST",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# SET THE SUBMISSION PHONE NUMBER HERE:
# ==========================================
SUBMISSION_PHONE_DISPLAY = "0506759271"   # Change to the Hall Tutor's actual number
SUBMISSION_PHONE_RAW = "233506759271"      # International format (233...) for the direct WhatsApp link

# Hide Streamlit default chrome
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Automatically load your uploaded crest image if present in the GitHub repo
logo_data_url = ""
for filename in ["image.jpg", "logo.jpg", "image.png", "logo.png"]:
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            mime = "image/png" if filename.endswith(".png") else "image/jpeg"
            logo_data_url = f"data:{mime};base64,{b64}"
        break

html_portal = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
            margin: 0;
            padding: 0;
        }}
        .a4-sheet {{
            background: #ffffff;
            width: 100%;
            max-width: 794px;
            min-height: 1020px;
            padding: 64px 72px;
            box-shadow: 0 4px 24px rgba(15, 23, 42, 0.08);
            border: 1px solid #e2e8f0;
            font-family: 'Times New Roman', Times, serif;
            color: #000000;
            font-size: 12pt;
            line-height: 1.65;
            letter-spacing: normal !important;
            word-spacing: normal !important;
            font-kerning: none;
            box-sizing: border-box;
            margin: 0 auto;
        }}
        @media (max-width: 640px) {{
            .a4-sheet {{
                padding: 32px 24px;
                font-size: 11pt;
                min-height: auto;
            }}
        }}
        @media print {{
            body * {{ visibility: hidden; }}
            #a4-document, #a4-document * {{ visibility: visible; }}
            #a4-document {{
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                box-shadow: none !important;
                border: none !important;
                padding: 20mm !important;
            }}
        }}
    </style>
</head>
<body class="min-h-screen pb-12">

    <!-- Top Branding Bar -->
    <header class="bg-[#0b6623] border-b-4 border-[#d4af37] text-white px-6 py-4 shadow-md">
        <div class="max-w-7xl mx-auto flex items-center justify-between flex-wrap gap-4">
            <div class="flex items-center gap-3.5">
                <img id="nav-crest" src="{logo_data_url}" class="h-12 w-12 rounded-full bg-white p-0.5 object-contain {'hidden' if not logo_data_url else ''}" alt="Crest" />
                <div>
                    <h1 class="text-lg md:text-xl font-bold tracking-tight">REPUBLIC HALL FELLOW APPLICATION PORTAL</h1>
                    <p class="text-xs text-[#fde047] font-semibold uppercase tracking-wider">Kwame Nkrumah University of Science and Technology (KNUST) — Set The Pace</p>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Split Layout -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 pt-6 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">

        <!-- LEFT COLUMN: Form Controls -->
        <section class="lg:col-span-5 bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-5">

            <!-- Full Name & Academic Title -->
            <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-slate-800 mb-1.5">
                    FULL NAME & ACADEMIC TITLE / RANK <span class="text-red-600">*</span>
                </label>
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                    </span>
                    <input id="inp-name" type="text" placeholder="e.g., Dr. John Mensah, Senior Lecturer"
                        class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-slate-300 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-[#0b6623] transition" />
                </div>
                <p class="text-xs text-slate-400 mt-1">Include honorary title, prefix (e.g., Prof., Dr., Mr., Mrs.), and university rank.</p>
            </div>

            <!-- College / Faculty / Department / Office / Center -->
            <div>
                <label class="block text-xs font-bold uppercase tracking-wider text-slate-800 mb-1.5">
                    COLLEGE / FACULTY / DEPARTMENT / OFFICE / CENTER <span class="text-red-600">*</span>
                </label>
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                    </span>
                    <input id="inp-unit" type="text" placeholder="e.g., College of Engineering / Dept. of Mechanical Engineering"
                        class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-slate-300 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-[#0b6623] transition" />
                </div>
                <p class="text-xs text-slate-400 mt-1">State your primary academic college, faculty, institute, or university unit.</p>
            </div>

            <!-- Phone & Email Row -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-800 mb-1.5">
                        PHONE NUMBER <span class="text-red-600">*</span>
                    </label>
                    <div class="relative">
                        <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                        </span>
                        <input id="inp-phone" type="tel" placeholder="e.g., 0240000000"
                            class="w-full pl-10 pr-3 py-2.5 rounded-lg border border-slate-300 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-[#0b6623] transition" />
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-800 mb-1.5">
                        EMAIL ADDRESS <span class="text-red-600">*</span>
                    </label>
                    <div class="relative">
                        <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        </span>
                        <input id="inp-email" type="email" placeholder="e.g., jmensah@knust.edu.gh"
                            class="w-full pl-10 pr-3 py-2.5 rounded-lg border border-slate-300 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-[#0b6623] transition" />
                    </div>
                </div>
            </div>

            <!-- Application Date -->
            <div>
                <div class="flex items-center justify-between mb-1.5">
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-800">
                        APPLICATION DATE <span class="text-red-600">*</span>
                    </label>
                    <button type="button" id="btn-today" class="text-xs font-semibold text-[#0b6623] hover:underline">
                        Set Today's Date
                    </button>
                </div>
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                    </span>
                    <input id="inp-date" type="text" placeholder="e.g., November 11, 2026"
                        class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-slate-300 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-[#0b6623] transition" />
                </div>
                <p class="text-xs text-slate-400 mt-1">Standard format: Month DD, YYYY (e.g. November 11, 2026)</p>
            </div>

            <!-- Electronic Signature Section -->
            <div class="pt-2 border-t border-slate-100">
                <div class="flex items-center justify-between mb-2.5">
                    <label class="text-sm font-bold text-slate-800">
                        Electronic Signature <span class="text-red-600">*</span>
                    </label>
                    <span id="sig-badge" class="hidden inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
                        ✓ Signature Attached
                    </span>
                </div>

                <!-- Tabs -->
                <div class="grid grid-cols-2 bg-slate-100 p-1 rounded-xl mb-3">
                    <button type="button" id="tab-draw" class="py-2 text-xs font-bold rounded-lg bg-white text-[#0b6623] shadow-sm transition">
                        ✒️ Tab 1: Draw Signature
                    </button>
                    <button type="button" id="tab-upload" class="py-2 text-xs font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition">
                        ⬆️ Tab 2: Upload Signature
                    </button>
                </div>

                <!-- Draw Panel -->
                <div id="panel-draw" class="space-y-2.5">
                    <div class="flex items-center justify-between flex-wrap gap-2">
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-slate-600 font-medium">Ink Color:</span>
                            <button type="button" id="ink-blue" class="px-3 py-1 rounded-lg text-xs font-semibold border-2 border-[#000080] bg-blue-50 text-[#000080] flex items-center gap-1.5">
                                <span class="w-2.5 h-2.5 rounded-full bg-[#000080]"></span> Blue Ink (#000080)
                            </button>
                            <button type="button" id="ink-black" class="px-3 py-1 rounded-lg text-xs font-semibold border border-slate-300 bg-white text-slate-800 flex items-center gap-1.5">
                                <span class="w-2.5 h-2.5 rounded-full bg-[#111111]"></span> Black Ink (#111111)
                            </button>
                        </div>
                        <button type="button" id="btn-clear-sig" class="px-3 py-1 rounded-lg text-xs font-semibold border border-rose-200 text-rose-600 hover:bg-rose-50 transition">
                            ↻ Clear Signature
                        </button>
                    </div>

                    <div class="relative rounded-xl border-2 border-dashed border-slate-300 bg-white overflow-hidden">
                        <canvas id="sig-canvas" width="460" height="150" class="w-full h-[150px] cursor-crosshair touch-none"></canvas>
                        <div class="pointer-events-none absolute bottom-3 left-5 right-5 border-b border-slate-200 flex justify-between text-[10px] text-slate-300 pb-0.5">
                            <span>Sign above this line</span>
                            <span>Kwame Nkrumah University of Science and Technology</span>
                        </div>
                    </div>
                </div>

                <!-- Upload Panel -->
                <div id="panel-upload" class="hidden">
                    <label class="flex flex-col items-center justify-center border-2 border-dashed border-slate-300 rounded-xl p-6 cursor-pointer hover:bg-slate-50 transition">
                        <span class="text-xs font-semibold text-[#0b6623] mb-1">Click to upload signature image (PNG or JPG)</span>
                        <span class="text-[11px] text-slate-400">Transparent PNG or white background recommended</span>
                        <input id="inp-sig-file" type="file" accept="image/png,image/jpeg" class="hidden" />
                    </label>
                </div>
            </div>

            <!-- Validation Notice -->
            <div id="validation-banner" class="rounded-xl bg-amber-50 border border-amber-200 px-4 py-3 text-xs font-medium text-amber-800">
                ⚠️ Please sign inside the signature box (or upload a signature) and ensure all compulsory (*) fields are filled to unlock your PDF download.
            </div>

        </section>

        <!-- RIGHT COLUMN: Actions + Highlighted Number + Live A4 Preview -->
        <section class="lg:col-span-7 space-y-4">

            <!-- Highlighted Submission Phone Callout Banner -->
            <div class="bg-amber-50/90 border-2 border-[#d4af37] rounded-2xl p-4 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                <div>
                    <span class="inline-block text-[11px] font-bold uppercase tracking-wider bg-[#0b6623] text-white px-2.5 py-0.5 rounded-md mb-1">
                        Step 2: Where to Send Your Downloaded PDF
                    </span>
                    <p class="text-xs text-slate-700">
                        After downloading your signed PDF below, send it via WhatsApp to the <strong>Hall Tutor</strong>:
                    </p>
                    <div class="mt-1 flex items-center gap-2 flex-wrap">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-600">Hall Tutor:</span>
                        <span id="sub-phone-text" class="text-base sm:text-lg font-extrabold text-[#0b6623] bg-white px-3 py-1 rounded-lg border border-emerald-200 tracking-wide select-all">
                            {SUBMISSION_PHONE_DISPLAY}
                        </span>
                    </div>
                </div>
                <div class="flex items-center gap-2.5 w-full sm:w-auto">
                    <button type="button" id="btn-copy-phone"
                        class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-bold bg-white text-slate-800 border border-slate-300 hover:bg-slate-100 shadow-sm transition">
                        📋 <span id="copy-btn-label">Copy Number</span>
                    </button>
                    <a href="https://wa.me/{SUBMISSION_PHONE_RAW}" target="_blank" rel="noopener noreferrer"
                        class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-bold bg-[#0b6623] text-white hover:bg-[#09521c] shadow-sm transition">
                        💬 Send to Hall Tutor on WhatsApp
                    </a>
                </div>
            </div>

            <!-- Action Buttons Row -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                <button type="button" id="btn-download-pdf" disabled
                    class="w-full py-3.5 px-5 rounded-xl font-bold text-sm text-white bg-[#0b6623] hover:bg-[#09521c] disabled:opacity-50 disabled:cursor-not-allowed shadow-sm flex items-center justify-center gap-2 transition">
                    ⬇️ Download Completed Application (PDF)
                </button>
                <button type="button" id="btn-print"
                    class="w-full py-3.5 px-5 rounded-xl font-bold text-sm text-slate-800 bg-white border border-slate-300 hover:bg-slate-50 shadow-sm flex items-center justify-center gap-2 transition">
                    🖨️ Print / Save as PDF
                </button>
            </div>

            <!-- Live A4 Document Sheet -->
            <div id="a4-document" class="a4-sheet">

                <!-- Optional Crest Header if logo exists in repo -->
                <div id="doc-crest-wrap" class="text-center mb-5 {'hidden' if not logo_data_url else ''}">
                    <img id="doc-crest" src="{logo_data_url}" class="h-16 mx-auto object-contain" alt="Republic Hall Crest" />
                </div>

                <!-- Memo Metadata Table starting directly with Date -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px; font-size: 12pt;">
                    <tr>
                        <td style="width: 85px; font-weight: bold; padding-bottom: 6px; vertical-align: top;">Date:</td>
                        <td id="out-date" style="padding-bottom: 6px; vertical-align: top;">[Application Date]</td>
                    </tr>
                    <tr>
                        <td style="font-weight: bold; padding-bottom: 6px; vertical-align: top;">To:</td>
                        <td style="padding-bottom: 6px; vertical-align: top;">Hall Warden, Republic Hall</td>
                    </tr>
                    <tr>
                        <td style="font-weight: bold; vertical-align: top;">From:</td>
                        <td style="vertical-align: top;">
                            <div id="out-name">[Full Name & Academic Title]</div>
                            <div><span id="out-unit">[College/Faculty/Department/Office/Center]</span>, KNUST</div>
                        </td>
                    </tr>
                </table>

                <!-- Salutation -->
                <div style="margin-bottom: 16px;">Dear Hall Master/Warden,</div>

                <!-- Bold Underlined Subject Line -->
                <div style="font-weight: bold; text-decoration: underline; margin-bottom: 18px;">
                    Application To Become A Fellow of Republic Hall, KNUST
                </div>

                <!-- Body Paragraphs -->
                <p style="margin-bottom: 14px; text-align: left; line-height: 1.75;">
                    I write to formally express my interest in being a fellow of Republic Hall, KNUST.
                </p>
                <p style="margin-bottom: 14px; text-align: left; line-height: 1.75;">
                    I am eager to join this family and collaborate with colleague fellows in advancing the traditions of the hall and providing mentorship to junior members.
                </p>
                <p style="margin-bottom: 28px; text-align: left; line-height: 1.75;">
                    I thank you for your kind consideration and look forward to hearing favorably from you soon
                </p>

                <!-- Sign-off -->
                <div style="margin-bottom: 8px;">Yours faithfully,</div>

                <!-- Signature Image Container -->
                <div style="height: 60px; margin: 6px 0 10px 0; display: flex; align-items: center;">
                    <img id="out-sig-img" src="" alt="Signature" style="max-height: 56px; max-width: 210px; object-fit: contain; display: none;" />
                    <span id="out-sig-empty" style="font-size: 10pt; color: #94a3b8; font-style: italic;">[Electronic Signature Pending]</span>
                </div>

                <!-- Signatory Block -->
                <div id="out-sign-name" style="font-weight: bold;">[Full Name & Academic Title]</div>
                <div><span id="out-sign-unit">[College/Faculty/Department/Office/Center]</span>, KNUST</div>
                <div style="font-size: 11pt; color: #334155; margin-top: 2px;">
                    Contact: <span id="out-phone">[Phone Number]</span> / <span id="out-email">[Email Address]</span>
                </div>

            </div>
        </section>
    </main>

    <script>
        // Elements
        const inpName = document.getElementById('inp-name');
        const inpUnit = document.getElementById('inp-unit');
        const inpPhone = document.getElementById('inp-phone');
        const inpEmail = document.getElementById('inp-email');
        const inpDate = document.getElementById('inp-date');

        const outDate = document.getElementById('out-date');
        const outName = document.getElementById('out-name');
        const outUnit = document.getElementById('out-unit');
        const outSignName = document.getElementById('out-sign-name');
        const outSignUnit = document.getElementById('out-sign-unit');
        const outPhone = document.getElementById('out-phone');
        const outEmail = document.getElementById('out-email');

        const outSigImg = document.getElementById('out-sig-img');
        const outSigEmpty = document.getElementById('out-sig-empty');
        const sigBadge = document.getElementById('sig-badge');
        const validationBanner = document.getElementById('validation-banner');
        const btnDownload = document.getElementById('btn-download-pdf');

        let signatureDataUrl = '';

        // Copy Phone Number button
        document.getElementById('btn-copy-phone').addEventListener('click', () => {{
            const rawPhone = document.getElementById('sub-phone-text').innerText.trim();
            navigator.clipboard.writeText(rawPhone);
            const lbl = document.getElementById('copy-btn-label');
            lbl.innerText = '✓ Copied!';
            setTimeout(() => {{ lbl.innerText = 'Copy Number'; }}, 2000);
        }});

        // Set Today's Date
        document.getElementById('btn-today').addEventListener('click', () => {{
            const now = new Date();
            const formatted = now.toLocaleDateString('en-US', {{ month: 'long', day: 'numeric', year: 'numeric' }});
            inpDate.value = formatted;
            syncPreview();
        }});

        // Signature Canvas Setup
        const canvas = document.getElementById('sig-canvas');
        const ctx = canvas.getContext('2d');
        let drawing = false;
        let strokeColor = '#000080';

        function configureCtx() {{
            ctx.strokeStyle = strokeColor;
            ctx.lineWidth = 2.2;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
        }}
        configureCtx();

        function getPos(e) {{
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return {{
                x: (clientX - rect.left) * scaleX,
                y: (clientY - rect.top) * scaleY
            }};
        }}

        function startDraw(e) {{
            e.preventDefault();
            drawing = true;
            configureCtx();
            const pos = getPos(e);
            ctx.beginPath();
            ctx.moveTo(pos.x, pos.y);
        }}

        function moveDraw(e) {{
            if (!drawing) return;
            e.preventDefault();
            const pos = getPos(e);
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
        }}

        function endDraw(e) {{
            if (!drawing) return;
            e.preventDefault();
            drawing = false;
            signatureDataUrl = canvas.toDataURL('image/png');
            syncPreview();
        }}

        canvas.addEventListener('mousedown', startDraw);
        canvas.addEventListener('mousemove', moveDraw);
        window.addEventListener('mouseup', endDraw);
        canvas.addEventListener('touchstart', startDraw, {{ passive: false }});
        canvas.addEventListener('touchmove', moveDraw, {{ passive: false }});
        canvas.addEventListener('touchend', endDraw, {{ passive: false }});

        // Ink color switchers
        const btnBlue = document.getElementById('ink-blue');
        const btnBlack = document.getElementById('ink-black');
        btnBlue.addEventListener('click', () => {{
            strokeColor = '#000080';
            btnBlue.className = 'px-3 py-1 rounded-lg text-xs font-semibold border-2 border-[#000080] bg-blue-50 text-[#000080] flex items-center gap-1.5';
            btnBlack.className = 'px-3 py-1 rounded-lg text-xs font-semibold border border-slate-300 bg-white text-slate-800 flex items-center gap-1.5';
        }});
        btnBlack.addEventListener('click', () => {{
            strokeColor = '#111111';
            btnBlack.className = 'px-3 py-1 rounded-lg text-xs font-semibold border-2 border-slate-900 bg-slate-100 text-slate-900 flex items-center gap-1.5';
            btnBlue.className = 'px-3 py-1 rounded-lg text-xs font-semibold border border-slate-300 bg-white text-slate-700 flex items-center gap-1.5';
        }});

        // Clear Signature
        document.getElementById('btn-clear-sig').addEventListener('click', () => {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            signatureDataUrl = '';
            syncPreview();
        }});

        // Tabs for Draw vs Upload Signature
        const tabDraw = document.getElementById('tab-draw');
        const tabUpload = document.getElementById('tab-upload');
        const panelDraw = document.getElementById('panel-draw');
        const panelUpload = document.getElementById('panel-upload');

        tabDraw.addEventListener('click', () => {{
            panelDraw.classList.remove('hidden');
            panelUpload.classList.add('hidden');
            tabDraw.className = 'py-2 text-xs font-bold rounded-lg bg-white text-[#0b6623] shadow-sm transition';
            tabUpload.className = 'py-2 text-xs font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition';
        }});
        tabUpload.addEventListener('click', () => {{
            panelUpload.classList.remove('hidden');
            panelDraw.classList.add('hidden');
            tabUpload.className = 'py-2 text-xs font-bold rounded-lg bg-white text-[#0b6623] shadow-sm transition';
            tabDraw.className = 'py-2 text-xs font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition';
        }});

        // Upload Signature File
        document.getElementById('inp-sig-file').addEventListener('change', (e) => {{
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (ev) => {{
                signatureDataUrl = ev.target.result;
                syncPreview();
            }};
            reader.readAsDataURL(file);
        }});

        // Live Sync
        function syncPreview() {{
            const vName = inpName.value.trim();
            const vUnit = inpUnit.value.trim();
            const vPhone = inpPhone.value.trim();
            const vEmail = inpEmail.value.trim();
            const vDate = inpDate.value.trim();

            outDate.textContent = vDate || '[Application Date]';
            outName.textContent = vName || '[Full Name & Academic Title]';
            outUnit.textContent = vUnit || '[College/Faculty/Department/Office/Center]';
            outSignName.textContent = vName || '[Full Name & Academic Title]';
            outSignUnit.textContent = vUnit || '[College/Faculty/Department/Office/Center]';
            outPhone.textContent = vPhone || '[Phone Number]';
            outEmail.textContent = vEmail || '[Email Address]';

            if (signatureDataUrl) {{
                outSigImg.src = signatureDataUrl;
                outSigImg.style.display = 'block';
                outSigEmpty.style.display = 'none';
                sigBadge.classList.remove('hidden');
            }} else {{
                outSigImg.style.display = 'none';
                outSigEmpty.style.display = 'inline';
                sigBadge.classList.add('hidden');
            }}

            const allComplete = vName && vUnit && vPhone && vEmail && vDate && signatureDataUrl;
            btnDownload.disabled = !allComplete;
            validationBanner.style.display = allComplete ? 'none' : 'block';
        }}

        [inpName, inpUnit, inpPhone, inpEmail, inpDate].forEach(el => el.addEventListener('input', syncPreview));
        syncPreview();

        // Print Button
        document.getElementById('btn-print').addEventListener('click', () => window.print());

        // Crisp A4 PDF Download
        btnDownload.addEventListener('click', async () => {{
            const originalText = btnDownload.innerHTML;
            btnDownload.innerHTML = '⏳ Generating Official PDF...';
            btnDownload.disabled = true;

            const element = document.getElementById('a4-document');
            const canvasImg = await html2canvas(element, {{
                scale: 2,
                useCORS: true,
                backgroundColor: '#ffffff',
                windowWidth: 1200
            }});

            const imgData = canvasImg.toDataURL('image/png');
            const {{ jsPDF }} = window.jspdf;
            const pdf = new jsPDF('p', 'mm', 'a4');
            const pdfWidth = pdf.internal.pageSize.getWidth();
            const pdfHeight = (canvasImg.height * pdfWidth) / canvasImg.width;

            pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
            const cleanName = (inpName.value.trim() || 'Applicant').replace(/[^a-zA-Z0-9]/g, '_');
            pdf.save(`Republic_Hall_Fellow_Application_${{cleanName}}.pdf`);

            btnDownload.innerHTML = originalText;
            btnDownload.disabled = false;
        }});
    </script>
</body>
</html>
"""

components.html(html_portal, height=1350, scrolling=True)
