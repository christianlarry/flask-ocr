import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# -- OCR FUNCTION, READ TEXT IN IMAGE
def image_ocr(img):

  # -- KONFIGURASI

  #  opsi --oem 3 untuk menggunakan mode OCR engine LSTM (Long Short-Term Memory) yang lebih akurat, dan --psm 6 untuk mengasumsikan bahwa gambar input adalah blok teks terpisah.
  config = r'--oem 3 --psm 6'

  # -- PENGENALAN TEKS
  text = pytesseract.image_to_string(img, config=config)

  print(text)

  return text