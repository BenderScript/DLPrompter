import os
import platform

from fpdf import FPDF


class FileUtils:

    def __init__(self, font_path=None):
        if font_path is None:
            self.font_path = self.get_font_path()

    def get_font_path(self):
        """
        Get the font path depending on the operating system.
        """
        if platform.system() == 'Darwin':  # macOS
            return "/Library/Fonts/Arial Unicode.ttf"
        elif platform.system() == 'Windows':
            return "C:/Windows/Fonts/arialuni.ttf"  # Adjust if necessary
        elif platform.system() == 'Linux':
            return "/usr/share/fonts/truetype/freefont/FreeSans.ttf"  # Adjust if necessary
        else:
            raise OSError("Unsupported operating system")

    def convert_single_txt_to_pdf(self, filename: str, text_data, pdf_data):
        """
        Convert a single text file in the input directory to a PDF file in the output directory.
        """
        if not os.path.exists(pdf_data):
            os.makedirs(pdf_data)

        if filename.endswith('.txt'):
            input_file_path = os.path.join(text_data, filename)
            output_file_path = os.path.join(pdf_data, filename.replace('.txt', '.pdf'))

            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('CustomFont', '', self.font_path, uni=True)
            pdf.set_font('CustomFont', '', 12)

            with open(input_file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    cleaned_line = line.strip().replace('\r', '')
                    pdf.multi_cell(0, 10, txt=cleaned_line, align='L')

            pdf.output(output_file_path)

    def convert_txt_to_pdf(self, text_data, pdf_data):
        """
        Convert all text text_data in the input directory to PDF text_data in the output directory.
        """
        if not os.path.exists(pdf_data):
            os.makedirs(pdf_data)

        for filename in os.listdir(text_data):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(text_data, filename)
                output_file_path = os.path.join(pdf_data, filename.replace('.txt', '.pdf'))

                pdf = FPDF()
                pdf.add_page()
                pdf.add_font('CustomFont', '', self.font_path, uni=True)
                pdf.set_font('CustomFont', '', 12)

                with open(input_file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        cleaned_line = line.replace('\r', '').strip()  # Strips carriage return and trailing spaces
                        pdf.cell(200, 10, txt=cleaned_line, ln=True)

                pdf.output(output_file_path)

        print("Conversion completed.")

    @staticmethod
    def _get_filename_with_incrementing_suffix(base_file_name, data_folder):

        base_name, extension = os.path.splitext(base_file_name)
        counter = 1

        # Increment the suffix until an unused name is found
        while os.path.exists(os.path.join(data_folder, f"{base_name}_{counter}{extension}")):
            counter += 1
        new_file_path = os.path.join(data_folder, f"{base_name}_{counter}{extension}")
        return new_file_path

    def save_data_to_file(self, data: str, filename: str, data_folder: str):
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        filepath = self._get_filename_with_incrementing_suffix(filename, data_folder)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(data)
            file.close()
            return filepath
