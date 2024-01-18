# GenAI DLP Prompt Generator

GenAI DLP Prompt Generator is a Python tool designed to scrape DLP data and use it to generate GenAI prompt. It has three main modules:

* It fetches DLP test sample data from specified URLs, saves the data in text format, and then converts these text files into PDFs. 
* It uses an OpenAI Assistant to generate DLP mock data 
* It uses OpenAI Chat Completions to generate prompts for each DLP category


The output is suitable for benchmarking DLP systems or Generative AI Language Learning Models (GenAI LLMs).

## Features

- Web scraping from specified URLs.
- Data extraction and saving in text format.
- Conversion of text data to PDF format, ideal for benchmarking DLP systems or GenAI LLMs.

## Installing

To install DLP Data Scraper, clone the repository and install the required packages:

```bash
git clone https://github.com/BenderScript/DLPDataScraper.git
cd DLPDataScraper/dlp_data_scraper
pip3 install -r requirements.txt
```

## Usage

Make sure you have a OpenAI API key and set it as an environment variable:

```bash
export OPENAI_API_KEY=<your key here>
```

The file with DLP categories currently under `tests/dlp_categories.md`. Need to be copies to a new location 
and the path passed to the `OpenAIDLPAssistant` or `OpenAIChat` classes.

# To use the DLP Data Scraper:

The scraper access a URL with dynamic content, waits for it to load and extracts all DLP categories

```python
from dlp_data_scraper.umbrella import Umbrella
from file_utils.FileUtils import FileUtils

pdf_data = "umbrella/pdf_data"
text_data = "umbrella/text_data"
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
```

After the run is over, the generated data under the `umbrella/text_data` 
and `umbrella/pdf_data` directory. There will be one file for each DLP category.


# To use the OpenAI Assistant DLP generator:

```python
from dlp_data_gen.openai_dlp_assistant import OpenAIDLPAssistant

dlp_gen_assistant = OpenAIDLPAssistant(text_data="openai_dlp/text_data", pdf_data="openai_dlp/pdf_data",
                                           dlp_categories_file="dlp/dlp_categories.md")
dlp_gen_assistant.run()
```

After the run is over, the generated data will be under the `openai_dlp/text_data` 
and `openai_dlp/pdf_data` directory. There will be a single file with mock DLP data for
each category.

# To use the OpenAI DLP Prompt Generator 

```python
from prompt_gen.openai_chat import OpenAIChat

chat_gen = OpenAIChat(text_data="openai_chat_prompt/text_data",
                          pdf_data="openai_chat_prompt/pdf_data",
                          dlp_categories_file="dlp/dlp_categories.md")

chat_gen.run()
```

## Contributing

Contributions to DLP Data Scraper are welcome. Please feel free to submit pull requests or open issues to improve the project.

---

