from PIL import Image, ImageEnhance, ImageFilter

def preprocess_image(image_path):
    # Buka gambar menggunakan Pillow
    image = Image.open(image_path)

    # Konversi ke grayscale
    image = image.convert('L')

    # Tingkatkan kontras
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  # Sesuaikan faktor peningkatan kontras di sini

    # Binarisasi menggunakan ambang batas adaptif
    image = image.point(lambda p: p > 150 and 255)

    # Haluskan gambar dengan Gaussian Blur
    image = image.filter(ImageFilter.GaussianBlur(radius=1))

    return image