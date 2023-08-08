"""
Main.py File to Start Applicaton
"""

import os
from pypercraft import pypercraft

if __name__ == '__main__':
    print('PyCharm')

    api_key = os.getenv("OPENAI_API_KEY")

    craft = pypercraft.Pypercraft(
        query="A Scientific Paper about Deep Learning",
        topic="Data Science",
        num_pages=3,
        tone="professional",
        api_key=api_key)

    paper = craft.construct()

    craft.export_docx('tmp/test.docx')

    print(paper)
