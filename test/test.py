import cv2
import numpy as np

# Define Braille patterns and their corresponding English characters
braille_patterns = {
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
    '⠵': 'z',
    ' ' : ' '
}

def detect_braille(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Image not found")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform image processing to detect Braille dots (you may need to fine-tune this)
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

    # Check if the grayscale image is empty
    if gray is None:
        return ""

    # Define the Braille cell positions for each dot
    dot_positions = [
        (1, 1), (1, 2),
        (2, 1), (2, 2),
        (3, 1), (3, 2)
    ]

    # Initialize an empty Braille pattern
    braille_pattern = ""

    # Convert the Braille character image to grayscale
    gray = cv2.cvtColor(braille_char_image, cv2.COLOR_BGR2GRAY)

    # Iterate through the dot positions
    for position in dot_positions:
        x, y = position
        # Check if the dot is present (black pixel)
        if gray[y, x] == 0:
            # Append the dot position to the Braille pattern
            braille_pattern += '1'
        else:
            # Append a space for no dot
            braille_pattern += '0'

    # Map the Braille pattern to an English character (or '?' for unknown patterns)
    english_char = braille_patterns.get(braille_pattern, '?')

    return english_char

def translate_braille_to_english(braille_characters):
    english_text = ""
    for braille_char_image in braille_characters:
        # Translate each Braille character and append to the result
        braille_char_text = translate_braille_image_to_text(braille_char_image)
        english_text += braille_char_text

    return english_text

def main():
    image_path = "img_asset/test2.png"  # Replace with the path to your image
    braille_characters = detect_braille(image_path)

    # Translate and print the detected Braille characters
    english_text = translate_braille_to_english(braille_characters)
    print("Detected Braille Text:")
    print(english_text)

if __name__ == "__main__":
    main()