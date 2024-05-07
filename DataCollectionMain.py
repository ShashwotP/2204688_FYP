import WebcamModule as wM #importing WebcamModule as wM
import DataCollectionModule as dcM #importing DataCollectionModule as dcM
import JoyStickModule as jsM #importing JoyStickModule as jsM
import MotorModule as mM #importing MotorModule as mM
import cv2 #importing OpenCV library
from time import sleep #importing the sleep function from time module


maxThrottle = 0.25 #maximum throttle value
motor = mM.Motor(2, 3, 4, 17, 22, 27) #initialize motor object with specified GPIO pins
record = 0 #initialize record variable


while True: #start infinite loop
    joyVal = jsM.getJS()  # get joystick values
    # print(joyVal)
    steering = joyVal['axis1']  # get steering value from joystick
    throttle = joyVal['o'] * maxThrottle  # get throttle value from joystick and scale it
    if joyVal['share'] == 1:  # if the 'share' button is pressed
        # if recording has just started
        if record == 0: print('Recording Started ...')  # print message indicating recording has started
        record += 1  # increment record counter
        sleep(0.300)  # wait for a short duration
        if record == 1:  # on the first press of the 'share' button
            img = wM.getImg(True, size=[240, 120])  # capture image from webcam
            dcM.saveData(img, steering)  # save image and steering data
        elif record == 2:  # on the second press of the 'share' button
