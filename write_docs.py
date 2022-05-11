import os

import docx  # "pip install python-docx==0.8.10": https://automatetheboringstuff.com/2e/chapter15/
             # functioneaza si 0.8.11
from docx.document import Document  # https://stackoverflow.com/a/52466366/2358837


def write_subiect_item(index_item, item, doc, verificare=False):
    if len(doc.paragraphs) == 1 and len(doc.paragraphs[0].runs) == 0:
        para = doc.paragraphs[0]
    else:
        doc.add_paragraph()
        doc.add_paragraph()
        para = doc.paragraphs[-1]

    categ_mat = '[C' + str(item['categorie']) + '/M' + str(item['materie']) \
                + '/I' + str(item['index_original']+1) + '] ' \
                if verificare else ''

    para.text = categ_mat + str(index_item + 1) + '. ' + item['intrebare']  # intrebarea
    para.runs[0].italic = True

    num = ['a) ', 'b) ', 'c) ', 'd) ']
    for i in range(4):
        corect = '[' + str(item['raspunsuri'][i]['corect']) + ']' if verificare else ''
        doc.add_paragraph(corect + num[i] + item['raspunsuri'][i]['text'])
    return doc


def write_raspuns_item(index_item, item, doc):
    if len(doc.paragraphs) == 1 and len(doc.paragraphs[0].runs) == 0:
        para = doc.paragraphs[0]
    else:
        para = doc.paragraphs[-1]
    para.add_run(str(index_item + 1) + '.')  # intrebarea
    num = ['a) ', 'b) ', 'c) ', 'd) ']
    for i in range(4):
        if item['raspunsuri'][i]['corect']:
            para.add_run(num[i])
            para.runs[-1].bold = True
    return doc


def write_subiect(path: str, filename: str, subiect: dict, verificare=False):
    doc: docx.document.Document = docx.Document('templates/Template.docx')  # https://stackoverflow.com/a/61822452/2358837
    for index_item, item in enumerate(subiect['itemi']):
        write_subiect_item(index_item, item, doc, verificare)
    doc.save(path + filename)
    print('Doc created ' + filename)


def write_raspuns(path: str, filename: str, subiect: dict):
    doc: docx.document.Document = docx.Document('templates/Template.docx')  # https://stackoverflow.com/a/61822452/2358837
    for index_item, item in enumerate(subiect['itemi']):
        write_raspuns_item(index_item, item, doc)
    doc.save(path + filename)
    print('Doc created ' + filename)


def write_docs(subiecte: list, doc_folder, verificare=False):
    os.mkdir(doc_folder)
    os.mkdir(doc_folder + 'subiecte')
    os.mkdir(doc_folder + 'raspunsuri')
    for subiect in subiecte:
        write_subiect(doc_folder + 'subiecte/',
                      'Subiect_%s%s_%02d.docx' % (subiect['zi'], subiect['comisie'], subiect['index'] + 1),
                      subiect, verificare=verificare)
        write_raspuns(doc_folder + 'raspunsuri/',
                      'Raspuns_%s%s_%02d.docx' % (subiect['zi'], subiect['comisie'], subiect['index'] + 1),
                      subiect)