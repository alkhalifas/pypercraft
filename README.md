# Pypercraft
#### An Application of LLMs to Generate Documents

## Live Demo

A live demo of the Streamlit application can be seen [here](https://pypercraft-8c8dd60022df.herokuapp.com/)

## Quick Start Guide

#### Clone The Repo

    git clone git@github.com:alkhalifas/pypercraft.git

    pip install -r requirements.txt

    streamlit run ui.py

#### Install With Pip

    pip install pypercraft

    from pypercraft import pypercraft

    craft = pypercraft.Pypercraft(

            # Describe the paper you want to generate
            query= "A Scientific Paper about Deep Learning",

            # Select the topic of your paper
            topic= "Data Science",

            # Select number of pages
            num_pages= 3,

            # Select tone of the writer
            tone= "professional",

            # Enter API key
            api_key= os.getenv("OPENAI_API_KEY"))

    # Construct the paper
    paper = craft.construct()

    # Export final paper
    craft.export_docx('tmp/test.docx')
