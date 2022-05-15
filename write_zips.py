import os
import zipfile
import itertools


def write_zips(source_folder: str, zip_folder: str, dict_zile: dict, nr_comisii: int):
    list_zile = list(dict_zile.keys())
    os.mkdir(zip_folder)
    for zi in list_zile:
        os.mkdir(zip_folder + zi)

    range_comisii = range(ord('A'), ord('A') + nr_comisii)
    subfolder = ['Subiecte', 'Raspunsuri']

    for cod in itertools.product(list(dict_zile.keys()), [chr(i) for i in range_comisii]):
        f = '_' + ''.join(cod) + '_'
        fisiere_comisie_s = [ff for ff in os.listdir(source_folder + 'subiecte' + os.sep) if
                             ff.find(f) > -1]
        fisiere_comisie_r = [ff for ff in os.listdir(source_folder + 'raspunsuri' + os.sep) if
                             ff.find(f) > -1]
        if len(fisiere_comisie_s) > 0:
            zip_name = 'Subiecte si raspunsuri Comisia ' + \
                       str(ord(cod[1]) - ord('A') + 1).zfill(2) + \
                       ', ' + dict_zile[cod[0]]
            zip_file = zipfile.ZipFile(zip_folder + cod[0] + os.sep + zip_name + '.zip', 'w')
            for file_name in fisiere_comisie_s:
                subf = subfolder[(file_name.find('Subiect') == -1)]
                zip_file.write(source_folder + 'subiecte' + os.sep + file_name, subf + os.sep + file_name,
                               compress_type=zipfile.ZIP_DEFLATED)
            for file_name in fisiere_comisie_r:
                subf = subfolder[(file_name.find('Subiect') == -1)]
                zip_file.write(source_folder + 'raspunsuri' + os.sep + file_name, subf + os.sep + file_name,
                               compress_type=zipfile.ZIP_DEFLATED)

            zip_file.close()
            print('Zip created ' + zip_name)

