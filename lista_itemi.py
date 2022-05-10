import docx  # "pip install python-docx==0.8.10": https://automatetheboringstuff.com/2e/chapter15/
from docx.document import Document  # https://stackoverflow.com/a/52466366/2358837

from prepare_items import get_ord_spreadsheet_values

ord_materii_values = get_ord_spreadsheet_values('1XSOBxM3CwXDD8xa_KY3e2qk6WYpAAI0EdbbONzLMf4k', 'licenta-317513-7b618b818287.json')

OFFSET_ROW = 1  # headerul
OFFSET_COL = 4  # timestamp, email, categoria, materia

NR_MATERII = len(ord_materii_values)
NR_VARIANTE_RASPUNS = 4
NR_PARAGRAPHS_PER_ITEM = NR_VARIANTE_RASPUNS + 1  # intrebarea + variantele de raspuns

NR_ITEMI = []
for row in ord_materii_values:
    row = list(filter(None, row))  # elimina ''
    NR_ITEMI.append((len(row) - OFFSET_COL) // NR_PARAGRAPHS_PER_ITEM)


num = ['a) ', 'b) ', 'c) ', 'd) ']

for i in range(NR_MATERII):
    doc: docx.document.Document = docx.Document('Template.docx')  # https://stackoverflow.com/a/61822452/2358837
    for j in range(NR_ITEMI[i]):
        for k in range(NR_PARAGRAPHS_PER_ITEM):
            pre = str(j + 1) + '. ' if k == 0 else num[k - 1]
            text = pre + ord_materii_values[i][OFFSET_COL + j * NR_PARAGRAPHS_PER_ITEM + k].strip()
            if j == 0 and k == 0:
                doc.paragraphs[0].text = text
            else:
                doc.add_paragraph(text)
            doc.paragraphs[-1].runs[0].italic = (k == 0)  # intrebarea cu italic
            doc.paragraphs[-1].runs[0].bold = (k == 1)  # raspunsul corect cu bold
        doc.add_paragraph('')

        nr_materie, materia = ord_materii_values[i][3].split('.')
        email = ord_materii_values[i][1]
        file_name = ('%02d.' % int(nr_materie)) + materia \
                            + ' [' + email + ']' \
                            + ' (' + str(NR_ITEMI[i]) + ' itemi)'
        doc.save('./Liste_Itemi/' + file_name + '.docx')

print('NR_MATERII: ', NR_MATERII)
