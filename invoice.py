from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe")

text=pytesseract.image_to_string(Image.open('C:/Users/shaba/OneDrive/Desktop/projects/invoice ocr/invoice.png'),
                                   config="--psm 6")
print(text)