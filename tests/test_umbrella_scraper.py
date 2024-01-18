import os
import unittest

from dlp_data_scraper.umbrella import Umbrella
from file_utils.FileUtils import FileUtils


class UmbrellaScraper(unittest.TestCase):
    def test_umbrella_scrape(self):
        pdf_data = "umbrella_dlp/pdf_data"
        text_data = "umbrella_dlp/text_data"
        file_utils = FileUtils()
        url = (
            'https://support.umbrella.com/hc/en-us/articles/4402023980692-Data-Loss-Prevention-DLP-Test-Sample-Data-for'
            '-Built-In-Data-Identifiers')
        scraper = Umbrella(url=url, text_data=text_data, pdf_data=pdf_data)
        html_content = scraper.initialize_browser()
        scraped_data = scraper.scrape_data()
        scraper.save_data_to_files()
        file_utils.convert_txt_to_pdf(text_data, pdf_data)
        print("Scraping and conversion to PDF completed.")
        # Check if the directories are not empty
        text_files = os.listdir(text_data)
        pdf_files = os.listdir(pdf_data)

        self.assertTrue(text_files, "No text text_data found in the text_data directory.")
        self.assertTrue(pdf_files, "No PDF text_data found in the pdf_data directory.")

        # Check if for every .txt file in text_data, there is a corresponding .pdf in pdf_data
        text_files_without_extension = {file.split('.')[0] for file in text_files if file.endswith('.txt')}
        pdf_files_without_extension = {file.split('.')[0] for file in pdf_files if file.endswith('.pdf')}

        self.assertEqual(text_files_without_extension, pdf_files_without_extension)
        # Cleanup: Remove pdf_data and text_data folders if they exist
        # for folder in [pdf_data, text_data]:
        #     if os.path.exists(folder):
        #         shutil.rmtree(folder)


if __name__ == '__main__':
    unittest.main()
