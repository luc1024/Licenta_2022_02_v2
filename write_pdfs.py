import sys
import os
import comtypes.client
import PyPDF2

wdFormatPDF = 17


def doc2pdf(filepath_doc: str, filepath_pdf: str, filepath_pdf_2pag: str, word_app):
    doc = word_app.Documents.Open(filepath_doc)
    doc.SaveAs(filepath_pdf, FileFormat=wdFormatPDF)

    pdfFileObj = open(filepath_pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.numPages > 1:
        doc.SaveAs(filepath_pdf_2pag, FileFormat=wdFormatPDF)
        print('\n!!! >= 2 pages\n')
    pdfFileObj.close()

    doc.Close()


def docs2pdfs(doc_folder: str, pdf_folder: str, pdf_folder_2pag: str, word_app):
    ds = doc_folder + 'assignments' + os.sep
    dr = doc_folder + 'solutions' + os.sep
    for file_name in os.listdir(ds):
        doc2pdf(ds + file_name,
                pdf_folder + 'assignments' + os.sep + file_name.replace('docx', 'pdf'),
                pdf_folder_2pag + file_name.replace('docx', 'pdf'),
                word_app)
        print('PDF created for ' + file_name)
    for file_name in os.listdir(dr):
        doc2pdf(dr + file_name,
                pdf_folder + 'solutions' + os.sep + file_name.replace('docx', 'pdf'),
                pdf_folder_2pag + file_name.replace('docx', 'pdf'),
                word_app)
        print('PDF created for ' + file_name)


def write_pdfs(doc_folder: str, pdf_folder: str, pdf_folder_2pag: str) -> bool:
    os.mkdir(pdf_folder)
    os.mkdir(pdf_folder + 'assignments')
    os.mkdir(pdf_folder + 'solutions')
    os.mkdir(pdf_folder_2pag)
    try:
        word_app = comtypes.client.CreateObject('Word.Application')
    except:
        print("Sorry, couldn't create PDFs. Error: ", sys.exc_info()[0])
        # raise
        return False
    else:
        docs2pdfs(doc_folder, pdf_folder, pdf_folder_2pag, word_app)
        word_app.Quit()
        return True
    # finally:
    #     word_app.Quit()
