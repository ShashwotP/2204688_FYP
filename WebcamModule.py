import cv2 #importing OpenCV library
frameWidth = 640 #width of the frame
frameHeight = 480 #height of the frame
cap = cv2.VideoCapture(0) #initialize video capture from webcam
cap.set(3, frameWidth)  #set frame width
cap.set(4, frameHeight)  #set frame height
while True:  #start infinite loop
    success, img = cap.read()  # read frame from webcam
    cv2.imshow("Result", img)  # display the frame
