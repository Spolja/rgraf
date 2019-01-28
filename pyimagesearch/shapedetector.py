import math

import cv2
import numpy as np


def calculateAngle(vector1, vector2):
    angle = np.math.atan2(np.linalg.det([vector1, vector2]), np.dot(vector1, vector2))
    return np.degrees(angle)


def calculateDistanceBetweenTwoPoints(a, b):
    squared_x = math.pow(b[0][0] - a[0][0], 2)
    squared_y = math.pow(b[0][1] - a[0][1], 2)
    return math.sqrt(squared_x + squared_y)


def calculateVector(a, b):
    return [(b[0][0] - a[0][0]), (b[0][1] - a[0][1])]


def vectorLength(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)


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

            vectorT1T4 = calculateVector(t1, t4)
            vectorT1T2 = calculateVector(t1, t2)

            angle = calculateAngle(vectorT1T4, vectorT1T2)

            # compute the bounding box of the contour and use then bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately equal to one, otherwise, the shape is a rectangle
            if 80 < angle < 100:
                shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

            print(approx)
            print(shape)

        # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "irregular pentagon"
            t1 = approx[0]
            t2 = approx[1]
            t3 = approx[2]
            t4 = approx[3]
            t5 = approx[4]

            vectorT1T2 = calculateVector(t1, t2)
            vectorT1T2_length = vectorLength(vectorT1T2)

            vectorT2T3 = calculateVector(t2, t3)
            vectorT2T3_length = vectorLength(vectorT2T3)

            vectorT3T4 = calculateVector(t3, t4)
            vectorT3T4_length = vectorLength(vectorT3T4)

            vectorT4T5 = calculateVector(t4, t5)
            vectorT4T5_length = vectorLength(vectorT4T5)

            vectorT5T1 = calculateVector(t5, t1)
            vectorT5T1_length = vectorLength(vectorT5T1)

            meanLength = (
                                 vectorT1T2_length + vectorT2T3_length + vectorT3T4_length + vectorT4T5_length + vectorT5T1_length) / 5

            acceptedDeviation = meanLength * 0.10
            minLength = meanLength - acceptedDeviation
            maxLength = meanLength + acceptedDeviation

            ##Best algoritham EU
            if minLength <= vectorT2T3_length <= maxLength:
                if minLength <= vectorT3T4_length <= maxLength:
                    if minLength <= vectorT4T5_length <= maxLength:
                        if minLength <= vectorT5T1_length <= maxLength:
                            shape = "regular pentagon"

        # if the shape is a hexagon, it will have 6 vertices
        elif len(approx) == 6:
            shape = "irregular hexagon"
            t1 = approx[0]
            t2 = approx[1]
            t3 = approx[2]
            t4 = approx[3]
            t5 = approx[4]
            t6 = approx[5]

            vectorT1T2 = calculateVector(t1, t2)
            vectorT1T2_length = vectorLength(vectorT1T2)

            vectorT2T3 = calculateVector(t2, t3)
            vectorT2T3_length = vectorLength(vectorT2T3)

            vectorT3T4 = calculateVector(t3, t4)
            vectorT3T4_length = vectorLength(vectorT3T4)

            vectorT4T5 = calculateVector(t4, t5)
            vectorT4T5_length = vectorLength(vectorT4T5)

            vectorT5T6 = calculateVector(t5, t6)
            vectorT5T6_length = vectorLength(vectorT5T6)

            vectorT6T1 = calculateVector(t6, t1)
            vectorT6T1_length = vectorLength(vectorT6T1)

            meanLength = (
                                 vectorT1T2_length + vectorT2T3_length + vectorT3T4_length + vectorT4T5_length + vectorT5T6_length + vectorT6T1_length) / 6

            acceptedDeviation = meanLength * 0.10
            minLength = meanLength - acceptedDeviation
            maxLength = meanLength + acceptedDeviation

            ##Best algoritham EU
            if minLength <= vectorT2T3_length <= maxLength:
                if minLength <= vectorT3T4_length <= maxLength:
                    if minLength <= vectorT4T5_length <= maxLength:
                        if minLength <= vectorT5T6_length <= maxLength:
                            if minLength <= vectorT6T1_length <= maxLength:
                                shape = "regular hexagon"

        # if the shape is a hexagon, it will have 7 vertices
        elif len(approx) == 7:
            shape = "irregular heptagon"
            t1 = approx[0]
            t2 = approx[1]
            t3 = approx[2]
            t4 = approx[3]
            t5 = approx[4]
            t6 = approx[5]
            t7 = approx[6]

            vectorT1T2 = calculateVector(t1, t2)
            vectorT1T2_length = vectorLength(vectorT1T2)

            vectorT2T3 = calculateVector(t2, t3)
            vectorT2T3_length = vectorLength(vectorT2T3)

            vectorT3T4 = calculateVector(t3, t4)
            vectorT3T4_length = vectorLength(vectorT3T4)

            vectorT4T5 = calculateVector(t4, t5)
            vectorT4T5_length = vectorLength(vectorT4T5)

            vectorT5T6 = calculateVector(t5, t6)
            vectorT5T6_length = vectorLength(vectorT5T6)

            vectorT6T7 = calculateVector(t6, t7)
            vectorT6T7_length = vectorLength(vectorT6T7)

            vectorT7T1 = calculateVector(t7, t1)
            vectorT7T1_length = vectorLength(vectorT7T1)

            meanLength = (
                                 vectorT1T2_length + vectorT2T3_length + vectorT3T4_length + vectorT4T5_length + vectorT5T6_length + vectorT6T7_length + vectorT7T1_length) / 7

            acceptedDeviation = meanLength * 0.10
            minLength = meanLength - acceptedDeviation
            maxLength = meanLength + acceptedDeviation

            ##Best algoritham EU
            if minLength <= vectorT2T3_length <= maxLength:
                if minLength <= vectorT3T4_length <= maxLength:
                    if minLength <= vectorT4T5_length <= maxLength:
                        if minLength <= vectorT5T6_length <= maxLength:
                            if minLength <= vectorT6T7_length <= maxLength:
                                if minLength <= vectorT7T1_length <= maxLength:
                                    shape = "regular heptagon"

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"
            print(shape)
            print(approx)

        # return the name of the shape
        return shape
