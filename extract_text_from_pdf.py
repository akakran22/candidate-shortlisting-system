from PyPDF2 import PdfReader

#extracting the text from the pdf 
def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text
    
#In this we extracted the text from every page of pdf and store it in var - text
