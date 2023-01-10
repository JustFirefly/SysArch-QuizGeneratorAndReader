"""
Contributors: JustFirefly,

Desc: pdfToQuestions.py is meant to take pdf files and turn them into text files that has one test question
"""

import os
import PyPDF2
import re
import filecmp
from pdfminer.high_level import extract_pages, extract_text 

#TODO > Make a formnat that removes all the 'estion' and 'a. ... b. ...' etc and 'The correct answer is:' sections
# HINT: go line by line in a txt file. 
# https://java2blog.com/remove-unicode-characters-python/

#https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python -- getting an image from a pdf (fitz)
#https://www.youtube.com/watch?v=N6Su4Hk8_-g -- reading pdf files (PyPDF2)

#Step 1. get pdf files.
week = 2
path = f"..//PDFs_HERE//Week {week}"
os.chdir(path)
list_of_files = os.listdir()
list_of_files.sort()

#print(list_of_files)

#Step 2. read through pdf file.
pdf_content = [extract_text(list_of_files[i]) for i in range(len(list_of_files))]
new = [a.replace("\n\uf00c Correct.", "").replace("\n\uf00c Correct answer.", "\b").replace("\nCorrect\n", "\b").replace("\uf00c","\b").replace("This is correct", "\b").replace("This is the correct", "\b").replace("answer.", "\b").replace("\uf00d", "\b").replace("Incorrect.", "\b").replace("Partially correct", "\b").replace("Not correct.","\b").replace("\xa0", '').replace("\x0c", '') for a in pdf_content]
#print(new)# prints the contents of list_of_files[0]

s_pattern = re.compile(r'estion [0-9\s].+?Qu', re.DOTALL) #this one gets questions. all of it.
a_pattern = re.compile(r'estion [0-9\s].+?a\.', re.DOTALL) 
o_pattern = re.compile(r'[a-g][\.\n](.+?)\n', re.DOTALL) # gets each option.
#result_s = s_pattern.findall(new)
#result_q = []
"""
for entry in result_s:
    for x in w_word_pattern.findall(entry):
        entry = entry.replace(x,'').replace('\n\n','')
    result_q.append(o_pattern.findall(entry))
"""
w_word_pattern = re.compile(r'estion .+? of [0-9]\.00\n', re.DOTALL) #removes the 'uestion' stuff at the start of the text.
result_a = [a_pattern.findall(b) for b in new]
for x in range(len(result_a)):
    for y in range(len(result_a[x])):
        for i in w_word_pattern.findall(result_a[x][y]):
            result_a[x][y] = result_a[x][y].replace(i,'').replace('\na.', '').replace('\u2190', ' ').replace('\u2212',' ').replace('\uf002', ' ').replace('\uf075', ' ').replace('\u2192',' ')


n_path = f"..//..//Database//Week{week}"
os.chdir(n_path)
d = 0
for x in range(len(result_a)):
    for q in range(len(result_a[x])):
        with open(f"q{d}.txt", 'w+') as file:
            file.write(result_a[x][q])
        d+=1

directory = os.listdir()
for file in directory:
    for file2 in directory:
        try:
            if filecmp.cmp(file, file2, shallow=False) and file != file2:
                os.remove(file)
        except:
            continue
#Step 3. filter what the questions and answers are.

#Step 4. format txt file into readable format for python.

#Step 5. add contents to the txt file and add to Database folder.

#Step 6. Profit.
