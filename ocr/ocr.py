import pytesseract
import argparse
from PIL import Image

data = argparse.ArgumentParser()

data.add_argument("-i", "--image", required=True, help="path to image")
args = vars(data.parse_args())

image = Image.open(args["image"])

text = pytesseract.image_to_string(image, lang="eng+ben")


print(text)