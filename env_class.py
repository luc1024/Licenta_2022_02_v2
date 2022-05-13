import os
from dotenv import load_dotenv, dotenv_values


class Env:
    def __init__(self):
        load_dotenv()

        self.sheet_id = os.getenv('SHEET_ID')
        self.credentials_file = 'secret' + os.sep + os.getenv('GOOGLE_API_CREDENTIALS')

        self.nr_comisii = int(os.getenv('NR_COMISII'))
        self.nr_subiecte_comisie = int(os.getenv('NR_SUBIECTE_COMISIE'))
        self.nr_materii = int(os.getenv('NR_MATERII'))

        self.seed = int(os.getenv('SEED'))

        self.output_dir_path = os.getcwd() + os.sep + os.getenv('OUTPUT_DIR_NAME') + os.sep + str(self.seed) + os.sep
        self.doc_folder = self.output_dir_path + 'docs' + os.sep
        self.pdf_folder = self.output_dir_path + 'pdfs' + os.sep
        self.pdf_folder_2pag = self.output_dir_path + '_pdfs_2_pages' + os.sep
        self.zip_folder = self.output_dir_path + 'zips' + os.sep

        self.get_from_local_file = (os.getenv('GET_FROM_LOCAL_FILE') == 'TRUE')

        self.generate_liste_itemi = (os.getenv('GENERATE_LISTE_ITEMI') == 'TRUE')

        self.offset_row = int(os.getenv('OFFSET_ROW'))  # headerul
        self.offset_col = int(os.getenv('OFFSET_COL'))  # timestamp, email, categoria, materia
        self.nr_variante_raspuns = int(os.getenv('NR_VARIANTE_RASPUNS'))
        self.nr_paragraphs_per_item = self.nr_variante_raspuns + 1  # intrebarea + variantele de raspuns

        self.dict_zile = dotenv_values(".env-zile")
