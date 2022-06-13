import os
from dotenv import load_dotenv, dotenv_values


class Env:
    def __init__(self):
        load_dotenv()

        self.sheet_id = os.getenv('SHEET_ID')
        self.credentials_file = 'secret' + os.sep + os.getenv('GOOGLE_API_CREDENTIALS')

        self.exam_boards_count = int(os.getenv('EXAM_BOARDS_COUNT'))
        self.assignments_per_board = int(os.getenv('ASSIGNMENTS_PER_BOARD'))
        self.courses_count = int(os.getenv('COURSES_COUNT'))

        self.seed = int(os.getenv('SEED'))

        self.output_dir_name = os.getenv('OUTPUT_DIR_NAME')
        self.output_dir_path = os.getcwd() + os.sep + self.output_dir_name + os.sep + str(self.seed) + os.sep
        self.doc_folder = self.output_dir_path + 'docs' + os.sep
        self.pdf_folder = self.output_dir_path + 'pdfs' + os.sep
        self.pdf_folder_2pag = self.output_dir_path + '_pdfs_2_pages' + os.sep
        self.zip_folder = self.output_dir_path + 'zips' + os.sep

        self.get_from_local_file = (os.getenv('GET_FROM_LOCAL_FILE') == 'TRUE')
        self.fake_data = (os.getenv('FAKE_DATA') == 'TRUE')

        self.generate_liste_itemi = (os.getenv('GENERATE_LISTE_ITEMI') == 'TRUE')

        self.offset_row = int(os.getenv('OFFSET_ROW'))
        self.offset_col = int(os.getenv('OFFSET_COL'))
        self.answers_per_item = int(os.getenv('ANSWERS_PER_ITEM'))
        self.nr_paragraphs_per_item = self.answers_per_item + 1  # question + answers

        self.dict_exam_days = dotenv_values(".env-exam-days")
