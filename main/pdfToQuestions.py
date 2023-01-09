"""
Contributors: JustFirefly,

Desc: pdfToQuestions.py is meant to take pdf files and turn them into text files that has one test question
"""

import os
import PyPDF2
import re
from pdfminer.high_level import extract_pages, extract_text 

#function reads through a pdf file and returns its contents - takes pdfFile as a parameter.
#TODO find out how the hell to format the text into something readable. >> text is inconsistent in seperating the answers
#                                                                       >> text has nonsense scattered between the questions and answers
#                                                                       + need to scan through the pdf -> filter out answers, seem to always be seperated by periods ('.')
#                                                                       + can filter Questions knowing there is exactly one question between to "Question" words in the PDF.
def readPDF(pdfFile):        
    pdf = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    complete = ""
    for p in range(pdfReader.numPages):
        page = pdfReader.getPage(p)
        #print(f'{("Page "+str(p)):-^100}')
        #print(page.extractText())
        complete+=page.extractText()
    return complete

#https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python -- getting an image from a pdf (fitz)
#https://www.youtube.com/watch?v=N6Su4Hk8_-g -- reading pdf files (PyPDF2)

#Step 1. get pdf files.

path = ".//PDFs_HERE//firefly_0826"
os.chdir(path)
list_of_files = os.listdir()
list_of_files.sort()

#print(list_of_files)

#Step 2. read through pdf file.
pdf_content = extract_text(list_of_files[2])
new = pdf_content.replace("\n\uf00c Correct.", "").replace("\n\uf00c Correct answer.", "").replace("\nCorrect\n", "").replace("\uf00c", "").replace("\uf00d", "").replace("Incorrect.", "").replace("Partially correct", "").replace("Not correct.","")
#print(new)# prints the contents of list_of_files[0]

s_pattern = re.compile(r'estion [0-9\s].+?.+?Qu', re.DOTALL) #this one gets questions. all of it.
q_word_pattern = re.compile(r'estion .+? of 1.00', re.DOTALL) #removes the 'uestion' stuff at the start of the text.
q_pattern = re.compile(r'[abcdefg]\..+?The correct answer', re.DOTALL) #get the options.
o_pattern = re.compile(r'[abcdefg]\..+?\n', re.DOTALL) # gets each option.
result_s = re.findall(s_pattern, new)
result_q = []
print(new)
for entry in result_s:
    print(f'{"":-^100}')
    replacement = re.findall(q_word_pattern, entry)
    entry = entry.replace(replacement[0],'')
    print(entry)

#
print(f'{"OPTIONS":-^100}')
for entry in result_s:
    addToResult = re.findall(q_pattern, entry)[0]
    result_q.append(addToResult)
    print(addToResult)

print(f'{"OPTIONS-E":-^100}')
#print entries
for entry in result_q:
    print(f'{"":-^100}')
    print(entry)
#Step 3. filter what the questions and answers are.

#Step 4. format txt file into readable format for python.

#Step 5. add contents to the txt file and add to Database folder.

#Step 6. Profit.