import io, sys

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import PyPDF2, re, os



def parseText(text):
    output = re.findall('\(внутр.код: (\d+)/(\d+)\)', text, flags=re.IGNORECASE)
    try:
        output = output[0]
    except:
        print("The except statement has executed!")
        output = False
    return output


def merge_files(path):
    merger = PyPDF2.PdfFileMerger()
    files = os.listdir(path)
    for pdf in files:
        merger.append(open(path+'/'+pdf, 'rb'))
    merger.write(path+"/result.pdf")

def safeFile(pdf_file, numPage, filename='./test_file.pdf'):
    output = PyPDF2.PdfFileWriter()
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(numPage)
    output.addPage(page)
    outputStream = open(filename, 'wb')
    output.write(outputStream)
    outputStream.close()


def extract_text_by_page(fh):
    for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
        yield text

        converter.close()
        fake_file_handle.close()


def extract_text(pdf_path, target_path):
    i = 1
    errors = []
    fh = open(pdf_path, 'rb')
    for page in extract_text_by_page(fh):
        if i > 10:
            break
        parse_result = parseText(page)
        if not parse_result:
            errors.append('In page {0} bad User code'.format(i))
            continue
        filepath = target_path + '/' + parse_result[0]
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        info = "[{2}] User Code is {0}, Legal ID is {1}".format(parse_result[0], parse_result[1], i)
        print(info)
        safeFile(fh, i-1, filepath + '/' + parse_result[1] + '.pdf')
        i += 1
    return errors

