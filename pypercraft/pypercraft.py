import openai


class Pypercraft:
    def __init__(self, query, topics, pages, references):
        self.user_query = query
        self.topics = topics
        self.pages = pages
        self.references = references

    def generate(self):
        """
        Generates the full text document as a JSON
        :return: JSON file
        """
    def construct(self):
        """
        Queries the API to generate a document
        :return:
        """

    def initial_prompt_generator(self):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature=0.7,
            messages=[
                {"role": "user", "content": self.user_query}
            ]
        )
        return response.choices[0]["message"]["content"]