import unittest
from unittest.mock import patch
from pypercraft.pypercraft import Pypercraft
import os

class TestPypercraft(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_key = os.getenv("OPENAI_API_KEY")
        cls.query = "An article about deep learning applications on space ships in star wars movie series"
        cls.topic = "Deep Learning and Star Wars"
        cls.num_pages = 5
        cls.pypercraft = Pypercraft(cls.query, cls.topic, cls.num_pages, cls.api_key)

    def test_generate_title(self):
        title = self.pypercraft.generate_title()
        self.assertIsInstance(title, str)
        self.assertNotEqual(title, "")
        # print("title:", title)

    def test_generate_introduction(self):
        introduction = self.pypercraft.generate_introduction()
        self.assertIsInstance(introduction, str)
        self.assertNotEqual(introduction, "")
        # print("introduction:", introduction)

    def test_generate_body(self):
        body = self.pypercraft.generate_body()
        self.assertIsInstance(body, str)
        self.assertNotEqual(body, "")
        # print("body:", body)

    def test_generate_conclusion(self):
        conclusion = self.pypercraft.generate_conclusion()
        self.assertIsInstance(conclusion, str)
        self.assertNotEqual(conclusion, "")
        # print("conclusion:", conclusion)

    def test_construct(self):

        paper = self.pypercraft.construct()

        self.assertIsInstance(paper, dict)
        self.assertIn("title", paper)
        self.assertIn("introduction", paper)
        self.assertIn("body", paper)
        self.assertIn("conclusion", paper)
        self.assertNotEqual(paper["title"], "")
        self.assertNotEqual(paper["introduction"], "")
        self.assertNotEqual(paper["body"], "")
        self.assertNotEqual(paper["conclusion"], "")


if __name__ == "__main__":
    unittest.main()
