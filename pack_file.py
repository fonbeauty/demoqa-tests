from zipfile import ZipFile
import os
from PyPDF2 import PdfReader


if os.path.exists('resources/arhive.zip'):
    os.remove('resources/arhive.zip')

with ZipFile('resources/arhive.zip', mode='w') as myzip:
    print('start zip file')
    myzip.write('./sample.pdf')
    myzip.write('./file_example_XLS_50.xls')
    myzip.write('./username.csv')
    print('complete zip file')


with ZipFile('resources/arhive.zip', mode='r') as zip_file:
    arhived_file = zip_file.namelist()
    print(f'В архиве находятся {arhived_file}')
    with zip_file.open('sample.pdf') as mypdf:
        reader = PdfReader(mypdf)
        text = reader.pages[0].extractText()
        print(text)



