import pathlib
from tkinter import filedialog as fd
#from PyPDF2 import PdfFileReader
#from docx import Document
def open_file_selection():
    files = fd.askopenfiles()
    for file in files:
        print(files)


open_file_selection()

#we only want users to upload .pdf, .jpg, .jpeg, .png, .raw