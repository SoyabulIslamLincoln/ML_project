import cv2
import pytesseract
import argparse


data = argparse.ArgumentParser()

data.add_argument("-i", "--image", required=True, help="path to image")
args = vars(data.parse_args())


image = cv2.imread(args["image"])
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
output = pytesseract.image_to_data(image_rgb, output_type=pytesseract.Output.DICT, lang="bengali+eng")
for i in range(0, len(output["text"])):
    x = output["left"][i]
    y = output["top"][i]
    w = output["width"][i]
    h = output["height"][i]
    text = output["text"][i]
    text_output = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(image, text_output, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            1.2, (0,0,0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)