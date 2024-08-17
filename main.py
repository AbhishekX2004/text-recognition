from pdf_processing import pdf_to_images
from image_processing import preprocess_image
from text_extraction import extract_text_from_image
from PIL import Image
import os

def extract_text_from_file(file_path, is_pdf=False):
    """
    Extract text from a file. If the file is a PDF, it processes each page.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    if is_pdf:
        images = pdf_to_images(file_path)
        text = ""
        for image in images:
            preprocessed_image = preprocess_image(image)
            text += extract_text_from_image(preprocessed_image)
        return text
    else:
        try:
            image = Image.open(file_path)
            preprocessed_image = preprocess_image(image)
            return extract_text_from_image(preprocessed_image)
        except Exception as e:
            raise RuntimeError(f"Failed to process the image: {e}")

if __name__ == "__main__":
    file_path = "C:/Users/asus/Desktop/TextRecognition/test8.jpeg"
    is_pdf = False  # Change to False if it's an image
    try:
        text = extract_text_from_file(file_path, is_pdf=is_pdf)
        print(text)
    except Exception as e:
        print(f"Error: {e}")
