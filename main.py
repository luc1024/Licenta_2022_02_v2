import os
import shutil
from numpy import random as np_random

from prepare_items import get_items
from prepare_subiecte import make_subiecte
from write_docs import write_docs
from write_pdfs import write_pdfs
from write_zips import write_zips
from lista_itemi import write_liste_itemi

from env_class import Env


env = Env()

if env.generate_liste_itemi:
    write_liste_itemi(env.sheet_id, env.credentials_file, env.output_dir_name + os.sep)

np_random.seed(env.seed)

items = get_items(env.sheet_id, env.credentials_file, from_local_file=env.get_from_local_file)
subiecte = make_subiecte(env.dict_zile, env.nr_comisii, env.nr_subiecte_comisie, env.nr_materii, items,
                         env.output_dir_path)

write_docs(subiecte, env.doc_folder, verificare=False)
write_pdfs(env.doc_folder, env.pdf_folder, env.pdf_folder_2pag)
write_zips(env.pdf_folder, env.zip_folder, env.dict_zile, env.nr_comisii)

shutil.rmtree(env.doc_folder)
shutil.rmtree(env.pdf_folder)
