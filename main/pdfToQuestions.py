"""
Contributors: JustFirefly,

Desc: main.py is meant to take pdf files and turn them into text files that has one test question
"""

import os
import fitz
import PyPDF2

#https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python -- getting an image from a pdf (fitz)
#https://www.youtube.com/watch?v=N6Su4Hk8_-g -- reading pdf files (PyPDF2)

#Step 1. get pdf files.

path = "..//PDFs_HERE//firefly_0826"
os.chdir(path)
list_of_files = os.listdir()
print(list_of_files)


#Step 2. read through pdf file.
def readPDF(pdfFile):        
    pdf = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    for p in range(pdfReader.numPages):
        page = pdfReader.getPage(p)
        print(page.extractText())


#Step 3. filter what the questions and answers are.

#Step 4. format txt file into readable format for python.

#Step 5. add contents to the txt file and add to Database folder.

#Step 6. Profit.