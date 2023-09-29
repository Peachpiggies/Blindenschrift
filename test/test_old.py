import cv2
import numpy as np

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

def main():
    image_path = "img_asset/test.jpg"  # Replace with the path to your image
    braille_characters = detect_braille(image_path)

    # Print the detected Braille characters
    for idx, char_image in enumerate(braille_characters):
        print(f"Braille Character {idx + 1}:")
        print(char_image)
        print("\n")

if __name__ == "__main__":
    main()
