import braille
import numpy as np
import os
from PIL import Image
from pytesseract import image_to_string
import PIL
from model import charToArray, asciicodes, brailles

braille_text = braille.brailleToSpeechImg("img_asset/test.jpg")