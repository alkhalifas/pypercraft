"""
Pypercraft Class
"""
import openai
from langchain import PromptTemplate
from docx import Document
from pypercraft.prompts import GENERATE_TITLE_PROMPT, GENERATE_INTRODUCTION_PROMPT, \
    GENERATE_BODY_PROMPT, GENERATE_CONCLUSION_PROMPT


class Pypercraft:
    """
    Pypercraft class that constructs a full paper
    """
    def __init__(self, query, topic, num_pages, api_key):
        openai.api_key = api_key
        self.user_query = query
        self.topic = topic
        self.num_pages = num_pages
        self.paper = {
            "title": "",
            "introduction": "",
            "body": "",
            "conclusion": ""
        }
        self.system_role = """You are a helpful AI assistant that specializes in
        writing articles and papers."""

    def generate_title(self):
        """
        Generates the title of the document
        :return: str
        """

        prompt = PromptTemplate.from_template(GENERATE_TITLE_PROMPT).format(
            idea=self.user_query,
            topic=self.topic)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": self.system_role},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message['content']

    def generate_introduction(self):
        """
        Generates the introduction of the document
        :return: str
        """

        prompt = PromptTemplate.from_template(GENERATE_INTRODUCTION_PROMPT).format(
            idea=self.user_query,
            topic=self.topic,
            num_pages=self.num_pages)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": self.system_role},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message['content']

    def generate_body(self):
        """
        Generates the body of the document
        :return: str
        """

        prompt = PromptTemplate.from_template(GENERATE_BODY_PROMPT).format(
            idea=self.user_query,
            topic=self.topic,
            num_pages=self.num_pages)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": self.system_role},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message['content']

    def generate_conclusion(self):
        """
        Generates the conclusion of the document
        :return: str
        """

        prompt = PromptTemplate.from_template(GENERATE_CONCLUSION_PROMPT).format(
            idea=self.user_query,
            topic=self.topic,
            num_pages=self.num_pages)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": self.system_role},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message['content']

    def construct(self):
        """
        Queries the API to generate a document
        :return:
        """

        self.paper["title"] = self.generate_title()
        self.paper["introduction"] = self.generate_introduction()
        self.paper["body"] = self.generate_body()
        self.paper["conclusion"] = self.generate_conclusion()

        return self.paper

    def export_docx(self, file_path):
        """
        Exports file as docx
        """
        doc = Document()

        # Adding title, introduction, body, and conclusion to the DOCX document
        doc.add_heading(self.paper["title"], level=1)
        doc.add_paragraph(self.paper["introduction"])
        doc.add_paragraph(self.paper["body"])
        doc.add_paragraph(self.paper["conclusion"])

        # Save as DOCX
        doc.save(file_path)
