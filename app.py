import streamlit as st
import os
import pandas as pd
from io import BytesIO
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Page setup
st.set_page_config(page_title="Automated Report App", layout="wide")

st.title("📑 Automated Report Generator")

# File uploader
uploaded_file = st.file_uploader("Upload a file (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # --- Process DOCX ---
    if uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        st.subheader("📖 Document Preview (DOCX)")
        for para in doc.paragraphs[:5]:
            st.write(para.text)

    # --- Process PDF ---
    elif uploaded_file.name.endswith(".pdf"):
        st.subheader("📖 PDF file uploaded")
        st.info("PDF preview not implemented yet, but file is ready for processing.")

    # --- Generate a sample report ---
    st.subheader("📊 Generate Report")
    if st.button("Generate Report"):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"Report for file: {uploaded_file.name}")
        c.drawString(100, 720, "This is an auto-generated report placeholder.")
        c.save()

        buffer.seek(0)
        st.download_button(
            label="⬇️ Download Report (PDF)",
            data=buffer,
            file_name="generated_report.pdf",
            mime="application/pdf"
        )
