import cv2
import numpy as np
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = 'C:/Users/Peachpiggies/AppData/Local/Programs/Tesseract-OCR'

# Define a dictionary to map Braille characters to English characters
braille_to_english = {

        '⠁': 'a',
        '⠃': 'b',
        '⠉': 'c', 
        '⠙': 'd',
        '⠑': 'e', 
        '⠋': 'f',
        '⠛': 'g', 
        '⠓': 'h',
        '⠊': 'i', 
        '⠚': 'j',
        '⠅': 'k',
        '⠇': 'l',
        '⠍': 'm',
        '⠝': 'n',
        '⠕': 'o',
        '⠏': 'p',
        '⠟': 'q',
        '⠗': 'r',
        '⠎': 's',
        '⠞': 't',
        '⠥': 'u',
        '⠧': 'v',
        '⠺': 'w',
        '⠭': 'x',
        '⠽': 'y',
        '⠵': 'z'

    }

def detect_braille(image_path):
    
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Image not found")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform image processing to detect Braille dots (you may need to fine-tune this)
    # This is a basic example using thresholding
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_braille = []

    # Loop through the detected contours
    for contour in contours:
        # Check the area of each contour to filter out small noise
        if cv2.contourArea(contour) > 50:
            # Get the coordinates of the contour
            x, y, w, h = cv2.boundingRect(contour)
            detected_braille.append((x, y, x + w, y + h))

    # Sort the detected Braille dots by their x-coordinate
    detected_braille.sort(key=lambda x: x[0])

    # Extract Braille characters based on dot positions
    braille_characters = []
    for i in range(0, len(detected_braille), 2):
        if i + 1 < len(detected_braille):
            braille_characters.append(
                image[detected_braille[i][1]:detected_braille[i + 1][3], detected_braille[i][0]:detected_braille[i + 1][2]]
            )

    return braille_characters

def translate_braille_image_to_text(braille_char_image):
    # Check if the input image is None or empty
    if braille_char_image is None or len(braille_char_image) == 0:
        return ""

    # Convert the Braille character image to grayscale
    gray = cv2.cvtColor(braille_char_image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to recognize text from the image
    custom_config = r'--psm 6 -l braille'  # Set language to Braille
    braille_text = pytesseract.image_to_string(gray, config=custom_config)

    return braille_text

def translate_braille_to_english(braille_characters):
    english_text = ""
    for braille_char_image in braille_characters:
        # You need to implement a function to translate the braille image to text
        braille_char_text = translate_braille_image_to_text(braille_char_image)
        english_char = braille_to_english.get(braille_char_text, "?")  # Default to "?" for unknown characters
        english_text += english_char

    return english_text

def main():
    image_path = "img_asset/test.jpg"  # Replace with the path to your image
    braille_characters = detect_braille(image_path)

    # Translate and print the detected Braille characters
    english_text = translate_braille_to_english(braille_characters)
    print("Detected Braille Text:")
    print(english_text)

if __name__ == "__main__":
    main()
