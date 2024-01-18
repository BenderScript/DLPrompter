import openai
import os
import time
from colorama import Fore, Style
from openai import OpenAI
from file_utils.FileUtils import FileUtils


class OpenAIChat:
    def __init__(self, dlp_categories_file="dlp/dlp_categories.md", text_data="./text_data", pdf_data="./pdf_data"):
        self.text_data = text_data
        self.pdf_data = pdf_data
        self.dlp_categories_file = dlp_categories_file
        self.file_utils = FileUtils()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_mock_data(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",  # Use the GPT-4 model
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.8
        )
        return response.choices[0].message.content

    def run(self):
        print(f"{Fore.BLUE}Starting Prompt Data Generation {Style.RESET_ALL}\n")

        # Start time
        start_time = time.time()

        base_prompt = (
            "Create a chat prompt for the DLP category below. Each prompt should be two or more sentences, "
            "mimicking a human conversing with chatGPT. Ensure that the prompts are realistic and human-like. "
            "Include mock data that is structurally valid and accurately represents the specific DLP category. "
            "Do not add any extraneous commentary or chatGPT's answer. Focus solely on generating a single "
            "chat prompt that includes the required mock data. "
            "Prompts for countries with native languages other than English should use their language and"
            " character set, therefore the response should be in UTF-8.\n\n"
            "The category is:\n\n"
        )

        with open(self.dlp_categories_file, 'r') as file:
            for line in file:
                category_description = line.strip()
                full_prompt = base_prompt + category_description
                mock_data = self.generate_mock_data(full_prompt)
                print(category_description)
                # print(mock_data)
                filepath = self.file_utils.save_data_to_file(mock_data, "prompt_data.txt", self.text_data)
                self.file_utils.convert_single_txt_to_pdf(os.path.basename(filepath), self.text_data, self.pdf_data)

        # End time
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{Fore.BLUE}Elapsed time: {elapsed_time} seconds{Style.RESET_ALL}\n")



