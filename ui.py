import streamlit as st
import os
from pypercraft.pypercraft import Pypercraft
from docx import Document


def main():

    st.title("Pypercraft Paper Generator")

    # User input
    query = st.text_input("Enter your query:", placeholder="Enter your query here...")
    topic = st.text_input("Enter the topic:", placeholder="Enter the topic here...")

    col1, col2 = st.columns(2)

    with col1:
        num_pages = st.number_input("Number of pages:", min_value=1, value=2, step=1)
    with col2:
        tone = st.selectbox("Select Tone", ["Professional", "Cute", "Artistic", "Moderate"])

    # Generate paper on button click
    if st.button("Generate Paper"):
        api_key = os.getenv("OPENAI_API_KEY")
        pypercraft = Pypercraft(query, topic, num_pages, api_key)

        with st.spinner("Generating Paper..."):
            paper = pypercraft.construct()
            st.session_state.paper = paper

        st.subheader("Title")
        st.write(paper["title"])

        st.subheader("Introduction")
        st.write(paper["introduction"])

        st.subheader("Body")
        st.write(paper["body"])

        st.subheader("Conclusion")
        st.write(paper["conclusion"])
        export_document(st.session_state.paper)


def export_document(paper):
    doc = Document()

    # Adding title, introduction, body, and conclusion to the DOCX document
    doc.add_heading(paper["title"], level=1)
    doc.add_paragraph(paper["introduction"])
    doc.add_paragraph(paper["body"])
    doc.add_paragraph(paper["conclusion"])

    # Save as DOCX
    doc_filename = "tmp/generated_paper.docx"
    doc.save(doc_filename)
    st.success(f"DOCX file generated: {doc_filename}")

    # Read the content of the temporary file
    with open(doc_filename, "rb") as file:
        data = file.read()

    # Display a download button with the file content
    st.download_button(
        label="Download docx",
        data=data,
        file_name="pypercraft_paper.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


if __name__ == "__main__":
    main()
