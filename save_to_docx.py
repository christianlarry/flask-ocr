from docx import Document

def save_as_docx(text, file_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_path)