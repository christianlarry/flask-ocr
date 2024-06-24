from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from image_processing import preprocess_image
from image_ocr import image_ocr
import os

from save_to_docx import save_as_docx
from save_to_pdf import save_as_pdf
from save_to_text import save_as_text

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
  # Pastikan 'file' adalah bagian dari permintaan
  if 'file' not in request.files:
      return jsonify({'error': 'No file part in the request'}), 400

  file = request.files['file']

  # Pastikan file tidak kosong
  if file.filename == '':
      return jsonify({'error': 'No selected file'}), 400

  # Pastikan ekstensi file diizinkan (misalnya: png, jpg, jpeg)
  allowed_extensions = {'png', 'jpg', 'jpeg'}
  if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
      return jsonify({'error': 'Invalid file extension'}), 400

  # Simpan file ke direktori uploads
  upload_path = app.config['UPLOAD_FOLDER'] + file.filename
  file.save(upload_path)

  try:
      # Preprocessing gambar
      img = preprocess_image(upload_path)

      # OCR
      text = image_ocr(img)

      # Simpan ke format dokumen yang diminta
      output_format = request.form.get('format', 'docx')
      output_filename = f'output.{output_format}'

      if output_format == 'docx':
          save_as_docx(text, output_filename)
      elif output_format == 'pdf':
          save_as_pdf(text, output_filename)
      elif output_format == 'txt':
          save_as_text(text, output_filename)
      else:
          return jsonify({'error': 'Unsupported output format'}), 400

      # Mengembalikan file output sebagai respons
      return send_file(output_filename, as_attachment=True)

  finally:
      # Hapus file upload setelah selesai
      if os.path.exists(upload_path):
          os.remove(upload_path)


if __name__ == '__main__':
    app.run(debug=True)