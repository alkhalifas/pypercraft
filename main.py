"""
Main.py File to Start Applicaton
"""
from pypercraft import pypercraft
import os

if __name__ == '__main__':
    print('PyCharm')

    api_key = os.getenv("OPENAI_API_KEY")

    craft = pypercraft.Pypercraft("A Scientific Paper about Deep Learning", "Data Science", 3, api_key)

    paper = craft.construct()

    craft.export_docx('tmp/test.docx')

    print(paper)
