import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

from env_class import Env
from faker import Faker


env = Env()


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
        ord_courses_values = sorted(sheet_values[env.offset_row:], key=lambda r: int((r[3].split('.'))[0]))

        return ord_courses_values

    except HttpError as err:
        print(err)


def make_items(ord_courses_values: list, fake_data: bool = False) -> list:
    fake = Faker()
    items = []
    for row in ord_courses_values:
        row = list(filter(None, row))  # elimina ''
        nr_items = (len(row) - env.offset_col) // env.nr_paragraphs_per_item
        for i in range(nr_items):
            answers = []
            for j in range(env.answers_per_item):
                answers.append({
                    'text': fake.text(50) if fake_data else row[env.offset_col + i * env.nr_paragraphs_per_item + j + 1].strip(),
                    'correct': (j == 0),
                    'original_index': j,
                })
            item = {
                'category': int(row[2].split('.')[0]),
                'course': int(row[3].split('.')[0]),
                'question': fake.text(250) if fake_data else row[env.offset_col + i * env.nr_paragraphs_per_item].strip(),
                'answers': answers,
                'original_index': i,
                'days_exam_boards': [],
                'exam_boards': []
            }
            items.append(item)
    return items


def get_items(sheet_id: str, json_keyfile_name: str, fake_data: bool = False) -> list:
    spreadsheet_values = get_ord_spreadsheet_values(sheet_id, json_keyfile_name)
    items = make_items(spreadsheet_values, fake_data)
    with open('secret/items.json', 'w+') as f:
        json.dump(items, f)
        f.close()
    return items
