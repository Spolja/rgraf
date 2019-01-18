import argparse

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

img = cv2.imread('star.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

perimeter = cv2.arcLength(cnt, True)

print(perimeter)
