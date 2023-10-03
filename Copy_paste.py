import PIL
from ultralytics import YOLO
from convert import convert_to_braille_unicode, parse_xywh_and_class

def load_model(model_path):
    """load model from path"""
    model = YOLO(model_path)
    return model

def load_image(image_path):
    """load image from path"""
    image = PIL.Image.open(image_path)
    return image

braille_dict = {
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
    '⠨': 'k',
    '⠇': 'l',
    '⠍': 'm',
    '⠩': 'm',
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
    '⠿': 'y',
    '⠵': 'z',
    '⠪': 'o',
    '⠻': 'er',
    ' ': ' ',
    '⠼': 'v',
    '⠼⠁': '1',
    '⠼⠃': '2',
    '⠼⠉': '3',
    '⠼⠙': '4',
    '⠼⠑': '5',
    '⠼⠋': '6',
    '⠼⠛': '7',
    '⠼⠓': '8',
    '⠼⠊': '9',
    '⠼⠚': '0'
}

# constants
CONF = 0.01 # or other desirable confidence threshold level
MODEL_PATH = "./yolov8_braille.pt"
IMAGE_PATH = "./test/ikea.png"

# receiving results from the model
image = load_image(IMAGE_PATH)
model = YOLO(MODEL_PATH)
res = model.predict(image, save=True, save_txt=True, exist_ok=True, conf=CONF)
boxes = res[0].boxes  # first image
list_boxes = parse_xywh_and_class(boxes)

result = ""
for box_line in list_boxes:
    str_left_to_right = ""
    box_classes = box_line[:, -1]
    for each_class in box_classes:
        str_left_to_right += convert_to_braille_unicode(model.names[int(each_class)], './braille_map.json')
    result += str_left_to_right + "\n"

print(''.join([braille_dict[char] for char in result if char != '\n']))