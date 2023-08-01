"""
Pypercraft Class
"""
import openai
from langchain import PromptTemplate


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

        template = """
                Generate an appropriate clever title for the paper concerning the following idea and topic:

                Idea: {idea}

                Topic: {topic}

                Return the result as a single string, and do not mention the fact that this is a title or a paper.
                """

        prompt = PromptTemplate.from_template(template).format(
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

        template = """
        Generate an appropriate introduction for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}
        
        Make sure the length of the introduction is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a introduction or a paper.
        """

        prompt = PromptTemplate.from_template(template).format(
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

        template = """
        Generate appropriate body paragraphs for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}

        Make sure the length of the body is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a body or a paper.
        """

        prompt = PromptTemplate.from_template(template).format(
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

        template = """
        Generate an appropriate conclusion for the paper concerning the following idea and topic:

        Idea: {idea}

        Topic: {topic}

        Make sure the length of the conclusion is appropriate for a paper that is {num_pages} pages long.

        Return the result as a single string, and do not mention the fact that this is a conclusion or a paper.
        """

        prompt = PromptTemplate.from_template(template).format(
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

        print("Reached construct")

        self.paper["title"] = self.generate_title()
        self.paper["introduction"] = self.generate_introduction()
        self.paper["body"] = self.generate_body()
        self.paper["conclusion"] = self.generate_conclusion()

        print("Done construct")

        return self.paper
