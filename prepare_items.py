from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

import json

OFFSET_ROW = 1  # headerul
OFFSET_COL = 4  # timestamp, email, categoria, materia
NR_VARIANTE_RASPUNS = 4
NR_PARAGRAPHS_PER_ITEM = NR_VARIANTE_RASPUNS + 1  # intrebarea + variantele de raspuns


def get_ord_spreadsheet_values(sheet_id: str, json_keyfile_name: str) -> list:
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    # https://google-auth.readthedocs.io/en/master/oauth2client-deprecation.html
    # https://developers.google.com/sheets/api/quickstart/python
    # https://google-auth.readthedocs.io/en/master/user-guide.html
    credentials = service_account.Credentials.from_service_account_file(json_keyfile_name)
    scoped_credentials = credentials.with_scopes(scopes)
    sample_range_name = 'Form Responses 1!A1:CZ24'

    try:
        service = build('sheets', 'v4', credentials=scoped_credentials)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=sample_range_name).execute()
        sheet_values = result.get('values', [])
        # Ordonam dupa coloana Materie
        ord_materii_values = sorted(sheet_values[OFFSET_ROW:], key=lambda r: int((r[3].split('.'))[0]))

        return ord_materii_values

    except HttpError as err:
        print(err)


def make_items(ord_materii_values: list) -> list:
    items = []
    for row in ord_materii_values:
        row = list(filter(None, row))  # elimina ''
        nr_items = (len(row) - OFFSET_COL) // NR_PARAGRAPHS_PER_ITEM
        for i in range(nr_items):
            raspunsuri = []
            for j in range(NR_VARIANTE_RASPUNS):
                raspunsuri.append({
                    'text': row[OFFSET_COL + i * NR_PARAGRAPHS_PER_ITEM + j + 1].strip(),
                    'corect': (j == 0),
                    'index_original': j,
                })
            item = {
                'categorie': int(row[2].split('.')[0]),
                'materie': int(row[3].split('.')[0]),
                'intrebare': row[OFFSET_COL + i*NR_PARAGRAPHS_PER_ITEM].strip(),
                'raspunsuri': raspunsuri,
                'index_original': i,
                'zile_comisii': [],
                'comisii': []
            }
            items.append(item)
    return items


def get_items(sheet_id: str, json_keyfile_name: str, from_local_file=True) -> list:
    if from_local_file:
        f = open('./items.json', 'r')
        items = json.load(f)
    else:
        spreadsheet_values = get_ord_spreadsheet_values(sheet_id, json_keyfile_name)
        items = make_items(spreadsheet_values)
        with open('./items.json', 'w+') as f:
            json.dump(items, f)
            f.close()
    return items
