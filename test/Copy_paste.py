import PIL
from ultralytics import YOLO
from convert import convert_to_braille_unicode, parse_xywh_and_class

def load_model(model_path):
    """load model from path"""
    model = YOLO(model_path)
    return model

def process_image_and_convert_to_braille(model_path, image_data, braille_dict, confidence_threshold=0.01):
    # Load the model
    model = load_model(model_path)

    # Load the image from image data
    image = PIL.Image.open(image_data)

    # Make predictions
    res = model.predict(image, save=True, save_txt=True, exist_ok=True, conf=confidence_threshold)
    boxes = res[0].boxes  # first image
    list_boxes = parse_xywh_and_class(boxes)

    # Convert predictions to Braille
    result = ""
    for box_line in list_boxes:
        str_left_to_right = ""
        box_classes = box_line[:, -1]
        for each_class in box_classes:
            str_left_to_right += convert_to_braille_unicode(model.names[int(each_class)], './braille_map.json')
        result += str_left_to_right + "\n"

    # Convert Braille characters to corresponding text
    output_text = ''.join([braille_dict[char] for char in result if char != '\n'])

    return output_text

# Constants
MODEL_PATH = "./yolov8_braille.pt"
CONFIDENCE_THRESHOLD = 0.01

if __name__ == "__main__":
    # Example usage:
    with open("./save/scaned.png", "rb") as image_file:
        image_data = image_file.read()

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
    '⠼': 'v'
    }

    result_text = process_image_and_convert_to_braille(MODEL_PATH, image_data, braille_dict, CONFIDENCE_THRESHOLD)