from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_as_pdf(text, file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Memecah teks menjadi beberapa baris berdasarkan newline (\n)
    lines = text.split('\n')
    y = height - 40  # Menentukan posisi awal vertikal

    for line in lines:
        c.drawString(40, y, line)
        y -= 14  # Menentukan jarak antar baris

    c.save()