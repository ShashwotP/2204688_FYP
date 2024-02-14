import cv2
import numpy as np

def thresholding(img):#thresholding function
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converts BGR image to HSV
