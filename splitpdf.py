# pdf_splitter.py

import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            fname, page + 1)

        with open('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\' + output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    paths = glob.glob('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\*.pdf')
    paths.sort()

    for path in paths:
        pdf_splitter(path)