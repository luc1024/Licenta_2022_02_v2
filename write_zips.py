import os
import zipfile
import itertools


def write_zips(source_folder: str, zip_folder: str, dict_exam_days: dict, exam_boards_count: int):
    list_exam_days = list(dict_exam_days.keys())
    os.mkdir(zip_folder)
    for day in list_exam_days:
        os.mkdir(zip_folder + day)

    range_exam_boards = range(ord('A'), ord('A') + exam_boards_count)
    subfolder = ['Assignments', 'Solutions']

    for cod in itertools.product(list(dict_exam_days.keys()), [chr(i) for i in range_exam_boards]):
        f = '_' + ''.join(cod) + '_'
        fisiere_exam_board_a = [ff for ff in os.listdir(source_folder + 'assignments' + os.sep) if
                             ff.find(f) > -1]
        fisiere_exam_board_s = [ff for ff in os.listdir(source_folder + 'solutions' + os.sep) if
                             ff.find(f) > -1]
        if len(fisiere_exam_board_a) > 0:
            zip_name = 'Assignments & Solutions, Board ' + \
                       str(ord(cod[1]) - ord('A') + 1).zfill(2) + \
                       ', ' + dict_exam_days[cod[0]]
            zip_file = zipfile.ZipFile(zip_folder + cod[0] + os.sep + zip_name + '.zip', 'w')
            for file_name in fisiere_exam_board_a:
                subf = subfolder[(file_name.find('Assignment') == -1)]
                zip_file.write(source_folder + 'assignments' + os.sep + file_name, subf + os.sep + file_name,
                               compress_type=zipfile.ZIP_DEFLATED)
            for file_name in fisiere_exam_board_s:
                subf = subfolder[(file_name.find('Assignment') == -1)]
                zip_file.write(source_folder + 'solutions' + os.sep + file_name, subf + os.sep + file_name,
                               compress_type=zipfile.ZIP_DEFLATED)

            zip_file.close()
            print('Zip created ' + zip_name)

