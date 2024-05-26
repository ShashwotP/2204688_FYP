import cv2 #importing OpenCV library
frameWidth = 640 #width of the frame
frameHeight = 480 #height of the frame
cap = cv2.VideoCapture(0) #initialize video capture from webcam
cap.set(3, frameWidth)  #set frame width
cap.set(4, frameHeight)  #set frame height
while True:  #start infinite loop
    success, img = cap.read()  # read frame from webcam
    cv2.imshow("Result", img)  # display the frame
    if cv2.waitKey(1) and 0xFF == ord('q'):  # wait for 'q' key to be pressed to break the loop
        break

        """
        -This module gets an image through the webcam
using the opencv package
        -Display can be turned on or off
-Image size can be defined
"""

import cv2  # importing OpenCV library
cap = cv2.VideoCapture(0)  # initialize video capture from webcam
# function to capture image from webcam
def getImg(display=False, size=[480, 240]):