import cv2
import numpy as np
from PIL import Image

def preprocess_image(image, save_path="normalized_image.png"):
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    # Normalize the image
    normalized_img = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

    # Save the normalized image
    # cv2.imwrite(save_path, normalized_img)

    return normalized_img
