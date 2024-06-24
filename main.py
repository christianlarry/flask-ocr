from image_processing import preprocess_image
from image_ocr import image_ocr
from save_to_docx import save_as_docx 
from save_to_pdf import save_as_pdf 
from save_to_text import save_as_text 

# -- VARIABEL
imagePath = "images/document1.png"

# -- PROCESSING IMAGE
img = preprocess_image(imagePath)

# -- GET TEXT WITH OCR TESSERACT
text = image_ocr(img)

# -- SAVE OUTPUT
# save_as_docx(text, "output/docx/output.docx")
# save_as_text(text, "output/txt/output.txt")
# save_as_pdf(text, "output/pdf/output.pdf")

print(text)