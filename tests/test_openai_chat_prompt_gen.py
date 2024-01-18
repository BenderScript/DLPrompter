import unittest
from prompt_gen.openai_chat import OpenAIChat


class TestOpenAIPromptGen(unittest.TestCase):
    dlp_gen_assistant = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Assistant class
        cls.chat_gen = OpenAIChat(text_data="openai_chat_prompt/text_data",
                                  pdf_data="openai_chat_prompt/pdf_data",
                                  dlp_categories_file="dlp/dlp_categories.md")

    def test_chat_prompt_gen(self):
        self.chat_gen.run()


if __name__ == '__main__':
    unittest.main()
