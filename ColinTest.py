from PIL import Image
import pytesseract
import os

filename = "download.jpeg"
text = pytesseract.image_to_string(Image.open(filename))
print(text)


