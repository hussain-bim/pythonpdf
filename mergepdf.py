# pdf_merger2.py

import glob
from PyPDF2 import PdfFileMerger

def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []

    for path in input_paths:
        pdf_merger.append(path)

    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == '__main__':
    paths = glob.glob('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\*.pdf')
    paths.sort()
    merger('C:\\Users\\Admin\\Downloads\\pdfmergeorsplit\\Merged_file.pdf', paths)