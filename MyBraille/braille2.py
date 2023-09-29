import cv2
import numpy as np
import os
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from pytesseract import image_to_string
from model import charToArray, asciicodes, brailles

ascii_braille = {}

arrayLength = len(asciicodes)
counter = 0

def addImages(list_im):
    imgs = [ PIL.Image.open(i) for i in list_im ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save('output.jpg')  
def writeImage(b_string):
    images = []
    for letter in b_string:
        images.append(letterToImgPath[letter])
    addImages(images)    
    img = Image.open('output.jpg')
    img.show()

while counter < arrayLength:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

letterToImgPath = {
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
    ' ': ' '
}

def BrailleToText(text):
    final_chars = []
    for char in text:
        char = char.lower()
        if char in letterToImgPath:
            final_chars.append(letterToImgPath[char])
        else:
            final_chars.append(char)  # Keep non-Braille characters as-is
    final_string = ''.join(final_chars)
    print(final_string)
    return final_string

import cv2

def BrailleImgToText(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess the image (you may need to adjust these steps)
    # Example preprocessing: resizing and thresholding
    img = cv2.resize(img, (0, 0), fx=2, fy=2)  # Resize for better recognition
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Automatic character segmentation (example)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_characters = len(contours)


    # Character segmentation (you may need to implement this)
    # Example segmentation: assuming characters are evenly spaced
    char_width = img.shape[1] // num_characters
    char_images = [img[:, i * char_width:(i + 1) * char_width] for i in range(num_characters)]

    def recognize_char(char_img):
        # Calculate the area of the character
        char_area = cv2.countNonZero(char_img)

        # You may need to adjust this threshold based on your images
        threshold_area = char_img.shape[0] * char_img.shape[1] * 0.2  # 20% of the total area

        # Compare the character area with the threshold to determine if it's a dot or empty space
        if char_area > threshold_area:
            return '⠿'  # Represents a dot in Braille
        else:
            return ' '  # Represents an empty space in Braille

    # Character recognition and translation
    result = ''
    for char_img in char_images:
        # Recognize the character (you may need to implement character recognition)
        recognized_char = recognize_char(char_img)

        # Map the recognized character to English using your lookup table
        if recognized_char in letterToImgPath:
            result += letterToImgPath[recognized_char]
        else:
            result += recognized_char  # Keep unrecognized characters as-is

    print(result)
    return result

# Example usage
image_path = 'img_asset/test2.png'
result_text = BrailleImgToText(image_path)
