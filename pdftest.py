from PyPDF2 import PdfReader

reader = PdfReader("C:/Users/ImBaby/Documents/Acceptance Letter.pdf")
number_of_pages = len(reader.pages)
pages = reader.pages[0]
text = pages.extract_text()