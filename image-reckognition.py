#!/usr/bin/python

import argparse

import cv2
import imutils


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom = geom


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, contour):
        shape = "undefined"
        peri = int(cv2.arcLength(contour, True))

        # Dougles pecker algorithm
        contourApproximation = cv2.approxPolyDP(contour, 0.04, peri, True)

        print("__________________________________________")
        print("peri: " + str(peri))
        print("__________________________________________")

        # if the shape is a triangle, it will have 3 vertices
        if len(contourApproximation) == 3:
            shape = "triangle"

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        elif len(contourApproximation) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(contourApproximation)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

        # if the shape is a pentagon, it will have 5 vertices
        elif len(contourApproximation) == 5:
            shape = "pentagon"

        elif len(contourApproximation) == 6:
            shape = "hexagon"

        elif len(contourApproximation) == 7:
            shape = "heptagon"

        elif len(contourApproximation) == 8:
            shape = "octagon"

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"

        # return the name of the shape
        return shape


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

sd = ShapeDetector()

# loop over the contours
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)

    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# window = tkinter.Tk()
# app = FullScreenApp(window)

# straight_line_image = cv2.imread("images/straight_line.jpg")
# straight_line_image_height, straight_line_image_width, straight_line_image_no_channels = straight_line_image.shape

# circle_image = cv2.imread("images/circle.jpg")
# circle_image_height, circle_image_width, circle_image_no_channels = circle_image.shape

# canvas = tkinter.Canvas(window, width=straight_line_image_width, height=straight_line_image_height)
# canvas.pack()


# photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(straight_line_image))
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# window.mainloop()
