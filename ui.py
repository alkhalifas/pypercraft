import streamlit as st
import os
from pypercraft.pypercraft import Pypercraft
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def main():
    st.title("Pypercraft Streamlit App")

    # User input
    query = st.text_input("Enter your query:", "Enter your query here...")
    topic = st.text_input("Enter the topic:", "Enter the topic here...")
    num_pages = st.number_input("Number of pages:", min_value=1, value=5, step=1)

    # Generate paper on button click
    if st.button("Generate Paper"):
        api_key = os.getenv("OPENAI_API_KEY")
        pypercraft = Pypercraft(query, topic, num_pages, api_key)

        with st.spinner("Generating Paper..."):
            paper = pypercraft.construct()

        st.subheader("Title")
        st.write(paper["title"])

        st.subheader("Introduction")
        st.write(paper["introduction"])

        st.subheader("Body")
        st.write(paper["body"])

        st.subheader("Conclusion")
        st.write(paper["conclusion"])

    # Export to DOCX and PDF on button click
    if st.button("Export as DOCX and PDF"):
        export_document(paper)


def export_document(paper):
    doc = Document()

    # Adding title, introduction, body, and conclusion to the DOCX document
    doc.add_heading(paper["title"], level=1)
    doc.add_paragraph(paper["introduction"])
    doc.add_paragraph(paper["body"])
    doc.add_paragraph(paper["conclusion"])

    # Save as DOCX
    doc_filename = "generated_paper.docx"
    doc.save(doc_filename)
    st.success(f"DOCX file generated: {doc_filename}")

    # Save as PDF
    pdf_filename = "generated_paper.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(72, 800, paper["title"])
    c.drawString(72, 750, paper["introduction"])
    c.drawString(72, 700, paper["body"])
    c.drawString(72, 650, paper["conclusion"])
    c.save()
    st.success(f"PDF file generated: {pdf_filename}")


if __name__ == "__main__":
    main()
