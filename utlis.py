import cv2
import numpy as np

def thresholding(img):#thresholding function
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converts BGR image to HSV
    lowerWhite = np.array([85, 0, 0])  # lower bound of white color
    upperWhite = np.array([179, 160, 255])  # upper bound of white color
