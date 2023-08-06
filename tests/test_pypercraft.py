import unittest
from unittest.mock import patch
from pypercraft.pypercraft import Pypercraft
import os
import datetime


def get_current_datetime():
    current_datetime = datetime.datetime.now()
    return current_datetime


class TestPypercraft(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_key = os.getenv("OPENAI_API_KEY")
        cls.query = "An article about deep learning applications on space ships in star wars movie series"
        cls.topic = "Deep Learning and Star Wars"
        cls.num_pages = 2
        cls.pypercraft = Pypercraft(cls.query, cls.topic, cls.num_pages, cls.api_key)

    def test_generate_title(self):
        title = self.pypercraft.generate_title()
        self.assertIsInstance(title, str)
        self.assertNotEqual(title, "")
        self.assertGreater(len(title), 10)

    def test_generate_introduction(self):
        introduction = self.pypercraft.generate_introduction()
        self.assertIsInstance(introduction, str)
        self.assertNotEqual(introduction, "")
        self.assertGreater(len(introduction), 10)

    def test_generate_body(self):
        body = self.pypercraft.generate_body()
        self.assertIsInstance(body, str)
        self.assertNotEqual(body, "")
        self.assertGreater(len(body), 10)

    def test_generate_conclusion(self):
        conclusion = self.pypercraft.generate_conclusion()
        self.assertIsInstance(conclusion, str)
        self.assertNotEqual(conclusion, "")
        self.assertGreater(len(conclusion), 10)

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
        self.assertGreater(len(paper["title"]), 10)
        self.assertGreater(len(paper["introduction"]), 10)
        self.assertGreater(len(paper["body"]), 10)
        self.assertGreater(len(paper["conclusion"]), 10)

    def test_construct_export(self):
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
        self.assertGreater(len(paper["title"]), 10)
        self.assertGreater(len(paper["introduction"]), 10)
        self.assertGreater(len(paper["body"]), 10)
        self.assertGreater(len(paper["conclusion"]), 10)
        self.pypercraft.export_docx(f"tmp/test_file_{get_current_datetime()}.docx")


if __name__ == "__main__":
    unittest.main()
