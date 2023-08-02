import streamlit as st
import os
from pypercraft.pypercraft import Pypercraft

def main():
    st.title("Pypercraft Streamlit App")

    # User input
    query = st.text_input("Enter your query:", "Enter your query here...")
    topic = st.text_input("Enter the topic:", "Enter the topic here...")
    num_pages = st.number_input("Number of pages:", min_value=1, value=5, step=1)

    # Generate paper on button click
    if st.button("Generate Paper"):
        api_key = os.getenv("OPENAI_API_KEY")
        py_crft = Pypercraft(query, topic, num_pages, api_key)

        with st.spinner("Generating Paper..."):
            paper = py_crft.construct()

        st.subheader("Title")
        st.write(paper["title"])

        st.subheader("Introduction")
        st.write(paper["introduction"])

        st.subheader("Body")
        st.write(paper["body"])

        st.subheader("Conclusion")
        st.write(paper["conclusion"])


if __name__ == "__main__":
    main()
