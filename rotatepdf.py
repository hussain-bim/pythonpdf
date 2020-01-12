import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import glob

def pdf_rotate(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        new_page = pdf.getPage(page)
        new_page.rotateClockwise(270)
        pdf_writer.addPage(new_page)

    with open('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\' + fname + '.pdf', 'wb') as out:
        pdf_writer.write(out)

    print('Rotated: {}'.format(fname))

if __name__ == '__main__':
    paths = glob.glob('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\*.pdf')
    paths.sort()

    for path in paths:
        pdf_rotate(path)