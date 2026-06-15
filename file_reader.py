from PyPDF2 import PdfReader
from docx import Document


def read_pdf(file):
    text = ""

    pdf_reader = PdfReader(file)

    for page in pdf_reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text


def read_docx(file):
    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def read_txt(file):
    return file.read().decode("utf-8")