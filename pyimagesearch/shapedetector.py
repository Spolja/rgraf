import math

import cv2


def calculateAngleBetweenThreePoints(t1, t2, t3):
    a = math.pow(t2[0][0] - t1[0][0], 2) + math.pow(t2[0][1] - t1[0][1], 2)
    b = math.pow(t2[0][0] - t3[0][0], 2) + math.pow(t2[0][1] - t3[0][1], 2)
    c = math.pow(t3[0][0] - t1[0][0], 2) + math.pow(t3[0][1] - t1[0][1], 2)

    x = a + b + c
    y = math.sqrt(4 * a * b)
    z = x / y
    #TODO: calculated something wrong, fix this next
    return math.acos(z)


def calculateDistanceBetweenTwoPoints(t1, t2):
    squared_x = math.pow(t2[0][0] - t1[0][0], 2)
    squared_y = math.pow(t2[0][1] - t1[0][1], 2)
    return math.sqrt(squared_x + squared_y)


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):

        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # if the shape is a triangle, it will have 3 vertices
        if len(approx) == 3:
            shape = "triangle"
            print(approx)
            print(shape)

        # if the shape has 4 vertices, it is either a square or rect
        elif len(approx) == 4:
            t1 = approx[0]
            t2 = approx[1]
            t3 = approx[2]
            t4 = approx[3]

            # calculate distance between T1-T2
            distance_t1_t2 = calculateDistanceBetweenTwoPoints(t1, t2)

            # calculate distance between T2-T3
            distance_t2_t3 = calculateDistanceBetweenTwoPoints(t2, t3)

            # calculate distance between T3-T4
            distance_t3_t4 = calculateDistanceBetweenTwoPoints(t3, t4)

            # calculate distance between T1-T
            distance_t1_t4 = calculateDistanceBetweenTwoPoints(t4, t1)

            angle = calculateAngleBetweenThreePoints(t1, t2, t3)

            # compute the bounding box of the contour and use then bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately equal to one, otherwise, the shape is a rectangle
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
            print(approx)
            print(shape)

        # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "pentagon"
            print(shape)
            print(approx)

        # if the shape is a hexagon, it will have 6 vertices
        elif len(approx) == 6:
            shape = "hexagon"
            print(shape)
            print(approx)

        # if the shape is a hexagon, it will have 7 vertices
        elif len(approx) == 7:
            shape = "heptagon"
            print(shape)
            print(approx)

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"
            print(shape)
            print(approx)

        # return the name of the shape
        return shape
