import torch
from ultralytics import YOLO
import braille2

def something(img_path):
    model = YOLO("yolov8_braille.pt")
    result = braille2.BrailleToText(str(model.predict(img_path)))
    print(result)

something('./test01.jpg')