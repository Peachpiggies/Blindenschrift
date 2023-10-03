import torch
from ultralytics import YOLO
import braille
import braille2

def something(img_path):
    model = YOLO("yolov8_braille.pt")
    result = braille2.BrailleToText(str(model.predict(img_path)))
    converted_result = braille.brailleToTextArray(result)
    print(converted_result)

something('./test01.jpg')