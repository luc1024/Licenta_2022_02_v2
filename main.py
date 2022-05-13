import os
import shutil
from numpy import random as np_random
from dotenv import dotenv_values


from prepare_items import get_items
from prepare_subiecte import make_subiecte
from write_docs import write_docs
from write_pdfs import write_pdfs
from write_zips import write_zips


# CONSTANTE
# load_dotenv()

sheet_id = os.getenv('SHEET_ID')
credentials_file = os.getenv('GOOGLE_API_CREDENTIALS')

nr_comisii = int(os.getenv('NR_COMISII'))
nr_subiecte_comisie = int(os.getenv('NR_SUBIECTE_COMISIE'))
nr_materii = int(os.getenv('NR_MATERII'))

dict_zile = dotenv_values(".env-zile")

seed = int(os.getenv('SEED'))

output_dir_path = os.getcwd() + os.sep + os.getenv('OUTPUT_DIR_NAME') + os.sep + str(seed) + os.sep
doc_folder = output_dir_path + 'docs' + os.sep
pdf_folder = output_dir_path + 'pdfs' + os.sep
pdf_folder_2pag = output_dir_path + '_pdfs_2_pages' + os.sep
zip_folder = output_dir_path + 'zips' + os.sep


np_random.seed(seed)

get_from_local_file = (os.getenv('GET_FROM_LOCAL_FILE') == 'TRUE')
items = get_items(sheet_id, credentials_file, from_local_file=get_from_local_file)
subiecte = make_subiecte(dict_zile, nr_comisii, nr_subiecte_comisie, nr_materii, items, output_dir_path)

write_docs(subiecte, doc_folder, verificare=False)
write_pdfs(doc_folder, pdf_folder, pdf_folder_2pag)
write_zips(pdf_folder, zip_folder, dict_zile, nr_comisii)

shutil.rmtree(doc_folder)
shutil.rmtree(pdf_folder)

