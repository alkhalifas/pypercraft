"""
Main.py File to Start Application
"""

import os
from pypercraft import pypercraft


def print_results(input_paper):
    """
    Simple function to print results
    """
    print(input_paper["title"])
    print(f"Len Intro: {len(input_paper['title'])}")
    print(f"Len Body: {len(input_paper['body'])}")
    print(f"Len Conclusion: {len(input_paper['conclusion'])}")


if __name__ == '__main__':

    api_key = os.getenv("OPENAI_API_KEY")

    craft = pypercraft.Pypercraft(
        query="A Scientific Paper about Deep Learning",
        topic="Data Science",
        num_pages=3,
        tone="professional",
        api_key=api_key)

    # Parallel True
    paper = craft.construct(parallel=True)
    craft.export_docx('tmp/test.docx')
    print_results(paper)

    # Parallel False
    paper = craft.construct(parallel=False)
    craft.export_docx('tmp/test.docx')
    print_results(paper)
