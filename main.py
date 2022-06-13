import json
import shutil
from numpy import random as np_random

from prepare_items import get_items
from prepare_assignments import make_assignments
from write_docs import write_docs
from write_pdfs import write_pdfs
from write_zips import write_zips
from items_list import write_items_list

from env_class import Env


def run():
    env = Env()
    if env.generate_liste_itemi:
        write_items_list(env.sheet_id, env.credentials_file, env.output_dir_name)
    np_random.seed(env.seed)
    if env.get_from_local_file:
        with open('secret/items.json', 'r') as f:
            items = json.load(f)
            f.close()
    else:
        items = get_items(env.sheet_id, env.credentials_file, env.fake_data)
    assignments = make_assignments(env.dict_exam_days, env.exam_boards_count, env.assignments_per_board,
                                   env.courses_count, items, env.output_dir_path)
    write_docs(assignments, env.doc_folder, verify=False)
    success = write_pdfs(env.doc_folder, env.pdf_folder, env.pdf_folder_2pag)
    if not success:
        print('PDFs not created, we\'ll use DOCs instead')
        source_folder = env.doc_folder
    else:
        source_folder = env.pdf_folder
    write_zips(source_folder, env.zip_folder, env.dict_exam_days, env.exam_boards_count)
    shutil.rmtree(env.doc_folder)
    shutil.rmtree(env.pdf_folder)


if __name__ == '__main__':
    run()
