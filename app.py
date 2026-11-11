"""
Republic Hall Fellow Application Portal - Streamlit Edition
Kwame Nkrumah University of Science and Technology (KNUST)

Run with:
    streamlit run app.py
"""

import io
import datetime
from datetime import date
import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Republic Hall Fellow Application Portal - KNUST",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Republic Hall CSS styling
st.markdown(
    """
    <style>
    :root {
        --republic-green: #0b6623;
        --republic-gold: #d4af37;
    }
    
    .main-header {
        background-color: #0b6623;
        color: white;
        padding: 18px 24px;
        border-radius: 12px;
        border-bottom: 4px solid #d4af37;
        margin-bottom: 24px;
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 26px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .main-header .sub {
        color: #d4af37;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .a4-sheet {
        background: #ffffff;
        color: #111111;
        font-family: 'Times New Roman', Times, Georgia, serif;
        font-size: 11.5pt;
        line-height: 1.65;
        padding: 48px 44px;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        text-align: left;
    }
    
    .a4-sheet .memo-header {
        font-size: 11.5pt;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    .a4-sheet .subject {
        font-weight: bold;
        text-decoration: underline;
        margin: 16px 0;
        display: block;
    }

    .signature-box {
        max-height: 55px;
        margin: 12px 0 8px 0;
    }
    
    div[data-testid="stButton"] > button[kind="primary"] {
        background-color: #0b6623 !important;
        border-color: #0b6623 !important;
        color: white !important;
        font-weight: bold !important;
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background-color: #084c1a !important;
        border-color: #084c1a !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
    <div class="main-header">
        <div class="sub">Kwame Nkrumah University of Science and Technology, Kumasi</div>
        <h1>REPUBLIC HALL &bull; FELLOW APPLICATION PORTAL</h1>
        <div style="font-size: 13px; color: #e2e8f0; margin-top: 4px;">
            Motto: <strong>"Set The Pace"</strong> &bull; Hall Warden's Secretariat
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State
if "full_name" not in st.session_state:
    st.session_state.full_name = "Dr. John Mensah, Senior Lecturer"
if "college_dept" not in st.session_state:
    st.session_state.college_dept = "College of Engineering / Dept. of Mechanical Engineering"
if "phone_number" not in st.session_state:
    st.session_state.phone_number = "0240000000"
if "email" not in st.session_state:
    st.session_state.email = "jmensah@knust.edu.gh"
if "app_date" not in st.session_state:
    st.session_state.app_date = date.today().strftime("%B %d, %Y")

# Two-column layout
col_form, col_preview = st.columns([1, 1], gap="large")

with col_form:
    st.subheader("Applicant Details (Compulsory *)")
    st.caption("All fields marked with an asterisk are required to generate and download the application.")

    full_name = st.text_input(
        "Full Name & Academic Title/Rank *",
        value=st.session_state.full_name,
        placeholder="e.g. Dr. John Mensah, Senior Lecturer",
    )

    college_dept = st.text_input(
        "College / Faculty / Department / Office / Center *",
        value=st.session_state.college_dept,
        placeholder="e.g. College of Engineering / Dept. of Mechanical Engineering",
    )

    c_phone, c_email = st.columns(2)
    with c_phone:
        phone_number = st.text_input(
            "Phone Number *",
            value=st.session_state.phone_number,
            placeholder="0240000000",
        )
    with c_email:
        email = st.text_input(
            "Email Address *",
            value=st.session_state.email,
            placeholder="jmensah@knust.edu.gh",
        )

    app_date = st.text_input(
        "Application Date *",
        value=st.session_state.app_date,
        placeholder="e.g. November 11, 2026",
    )

    st.markdown("---")
    st.subheader("Electronic Signature *")
    st.caption("Upload your electronic signature image (PNG or JPG).")
    uploaded_sig = st.file_uploader(
        "Signature Image (PNG / JPG)",
        type=["png", "jpg", "jpeg"],
        label_visibility="collapsed",
    )

    # Validation check
    has_name = bool(full_name.strip())
    has_dept = bool(college_dept.strip())
    has_phone = bool(phone_number.strip())
    has_email = bool(email.strip())
    has_date = bool(app_date.strip())
    has_signature = uploaded_sig is not None

    all_valid = has_name and has_dept and has_phone and has_email and has_date and has_signature

    if not all_valid:
        missing = []
        if not has_name: missing.append("Full Name")
        if not has_dept: missing.append("College/Department")
        if not has_phone: missing.append("Phone Number")
        if not has_email: missing.append("Email Address")
        if not has_date: missing.append("Application Date")
        if not has_signature: missing.append("Electronic Signature")
        st.warning(f"⚠️ Please complete compulsory fields: {', '.join(missing)}")

with col_preview:
    st.subheader("Live A4 Letter Preview")

    # Generate PDF helper function using ReportLab if installed or fallback
    def generate_pdf_bytes():
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch, mm
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
            
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=22*mm,
                leftMargin=22*mm,
                topMargin=24*mm,
                bottomMargin=24*mm,
            )
            story = []
            styles = getSampleStyleSheet()
            
            # Custom Times New Roman-like styles
            normal_style = ParagraphStyle(
                'FormalBody',
                parent=styles['Normal'],
                fontName='Times-Roman',
                fontSize=11.5,
                leading=19,
                textColor='#111111',
            )
            bold_style = ParagraphStyle(
                'FormalBold',
                parent=normal_style,
                fontName='Times-Bold',
            )
            subject_style = ParagraphStyle(
                'FormalSubject',
                parent=normal_style,
                fontName='Times-Bold',
                fontSize=11.5,
                leading=19,
            )

            # Date, To, From block
            story.append(Paragraph(f"<b>Date:</b> &nbsp;&nbsp;&nbsp;&nbsp;{app_date.strip()}", normal_style))
            story.append(Paragraph("<b>To:</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hall Warden, Republic Hall", normal_style))
            story.append(Paragraph(f"<b>From:</b> &nbsp;&nbsp;&nbsp;{full_name.strip()}", normal_style))
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{college_dept.strip()}, KNUST", normal_style))
            story.append(Spacer(1, 16))

            # Salutation
            story.append(Paragraph("Dear Hall Master/Warden,", normal_style))
            story.append(Spacer(1, 10))

            # Subject
            story.append(Paragraph("<u><b>APPLICATION FOR FELLOWSHIP OF REPUBLIC HALL, KNUST</b></u>", subject_style))
            story.append(Spacer(1, 12))

            # Body Paragraph
            body_text = (
                "I write to formally express my interest in serving as a Fellow of Republic Hall, KNUST. "
                "I am eager to actively network and collaborate with other Fellows and past students (alumni) "
                "to advance the rich traditions, mentorship networks, and continuous development of the Hall. "
                "Furthermore, I am deeply committed to promoting student welfare, academic excellence, and a supportive "
                "residential community in close partnership with Hall Management. I thank you for your kind consideration "
                "and look forward to hearing favorably from you soon."
            )
            story.append(Paragraph(body_text, normal_style))
            story.append(Spacer(1, 18))

            # Sign off
            story.append(Paragraph("Yours faithfully,", normal_style))
            story.append(Spacer(1, 8))

            # Signature
            if uploaded_sig is not None:
                uploaded_sig.seek(0)
                img_data = io.BytesIO(uploaded_sig.read())
                story.append(Image(img_data, width=150, height=45))
                uploaded_sig.seek(0)
            else:
                story.append(Spacer(1, 30))

            story.append(Spacer(1, 8))
            story.append(Paragraph(f"<b>{full_name.strip()}</b>", normal_style))
            story.append(Paragraph(f"{college_dept.strip()}, KNUST", normal_style))
            story.append(Paragraph(f"Contact: {phone_number.strip()} / {email.strip()}", normal_style))

            doc.build(story)
            buffer.seek(0)
            return buffer.getvalue()
        except ImportError:
            # Fallback if reportlab is not installed
            return None

    # Render A4 Letter sheet
    sig_img_html = ""
    if uploaded_sig is not None:
        import base64
        uploaded_sig.seek(0)
        encoded_sig = base64.b64encode(uploaded_sig.read()).decode()
        uploaded_sig.seek(0)
        sig_img_html = f'<img src="data:image/png;base64,{encoded_sig}" class="signature-box" />'
    else:
        sig_img_html = '<div style="height: 45px; width: 180px; border: 1px dashed #cbd5e1; display: flex; align-items: center; justify-content: center; font-size: 10pt; color: #94a3b8; margin: 10px 0;">[Signature Required]</div>'

    clean_file_name = (
        f"Republic_Hall_Fellow_Application_{full_name.strip().replace(' ', '_')}.pdf"
        if full_name.strip()
        else "Republic_Hall_Fellow_Application_Applicant.pdf"
    )

    pdf_data = generate_pdf_bytes() if all_valid else None

    if pdf_data:
        st.download_button(
            label="📥 Download Completed Application (PDF)",
            data=pdf_data,
            file_name=clean_file_name,
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )
    else:
        st.button(
            "📥 Download Completed Application (PDF)",
            disabled=True,
            help="Please fill out all compulsory fields (*) and upload a signature to download.",
            use_container_width=True,
        )

    # Sheet Preview HTML
    memo_html = f"""
    <div class="a4-sheet">
        <div class="memo-header">
            <div><strong>Date:</strong> &nbsp;&nbsp;&nbsp;{app_date or '[Application Date]'}</div>
            <div><strong>To:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hall Warden, Republic Hall</div>
            <div><strong>From:</strong> &nbsp;&nbsp;{full_name or '[Full Name & Academic Title/Rank]'}</div>
            <div style="margin-left: 56px;">{college_dept or '[College/Faculty/Department/Office/Center/etc.]'}, KNUST</div>
        </div>
        
        <div>Dear Hall Master/Warden,</div>
        
        <div class="subject">APPLICATION FOR FELLOWSHIP OF REPUBLIC HALL, KNUST</div>
        
        <p>
            I write to formally express my interest in serving as a Fellow of Republic Hall, KNUST. I am eager to actively network and collaborate with other Fellows and past students (alumni) to advance the rich traditions, mentorship networks, and continuous development of the Hall. Furthermore, I am deeply committed to promoting student welfare, academic excellence, and a supportive residential community in close partnership with Hall Management. I thank you for your kind consideration and look forward to hearing favorably from you soon.
        </p>
        
        <div style="margin-top: 24px;">Yours faithfully,</div>
        
        {sig_img_html}
        
        <div style="margin-top: 10px;">
            <div style="font-weight: bold;">{full_name or '[Full Name & Academic Title/Rank]'}</div>
            <div>{college_dept or '[College/Faculty/Department/Office/Center/etc.]'}, KNUST</div>
            <div style="font-size: 10.5pt; color: #475569;">Contact: {phone_number or '[Phone Number]'} / {email or '[Email Address]'}</div>
        </div>
    </div>
    """
    st.markdown(memo_html, unsafe_allow_html=True)
