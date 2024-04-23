import pytesseract
from pdf2image import convert_from_path

def ocrmodule(file_path):
    try:
        if file_path.endswith('.pdf'):
            pages = convert_from_path(file_path, 300)
            text = ""
            for page in pages:
                text += pytesseract.image_to_string(page)
            return text
        else:
            return pytesseract.image_to_string(file_path)
    except Exception as e:
        print(f"Error in OCR module: {e}")
        return None
