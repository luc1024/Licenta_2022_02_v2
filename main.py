import os
import shutil
from numpy import random as np_random

from prepare_items import get_items
from prepare_subiecte import make_subiecte
from write_docs import write_docs
from write_pdfs import write_pdfs
from write_zips import write_zips


# CONSTANTE
SHEET_ID = '1XSOBxM3CwXDD8xa_KY3e2qk6WYpAAI0EdbbONzLMf4k'  # 2021.06 - original
JSON_KEYFILE_NAME = 'licenta-317513-7b618b818287.json'

NR_COMISII = 6  # 6
NR_SUBIECTE_COMISIE = 32  # 32
NR_MATERII = 23

DICT_ZILE = {'M': 'Marti, 15.02.2022'}

SEED = 202202210

OUTPUT_FOLDER = os.getcwd() + os.sep + 'Subiecte_Comisii_' + str(SEED) + os.sep
DOC_FOLDER = OUTPUT_FOLDER + 'docs' + os.sep
PDF_FOLDER = OUTPUT_FOLDER + 'pdfs' + os.sep
PDF_FOLDER_2PAG = OUTPUT_FOLDER + '_pdfs_2_pages' + os.sep
ZIP_FOLDER = OUTPUT_FOLDER + 'zips' + os.sep


np_random.seed(SEED)

items = get_items(SHEET_ID, JSON_KEYFILE_NAME, from_local_file=True)
subiecte = make_subiecte(DICT_ZILE, NR_COMISII, NR_SUBIECTE_COMISIE, NR_MATERII, items, OUTPUT_FOLDER)

write_docs(subiecte, DOC_FOLDER, verificare=False)
write_pdfs(DOC_FOLDER, PDF_FOLDER, PDF_FOLDER_2PAG)
write_zips(PDF_FOLDER, ZIP_FOLDER, DICT_ZILE, NR_COMISII)

shutil.rmtree(DOC_FOLDER)
shutil.rmtree(PDF_FOLDER)

