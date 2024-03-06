import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


"""
-This module gets an image through the webcam
using the opencv package
-Display can be turned on or off
-Image size can be defined
"""

import cv2

cap = cv2.VideoCapture(0)


def getImg(display=False, size=[480, 240]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))

