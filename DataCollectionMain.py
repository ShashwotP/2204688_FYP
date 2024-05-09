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
            dcM.saveLog()  # save log file containing collected data
            record = 0  # reset record counter
        if joyVal['o'] == 1:  # if 'o' button is pressed (throttle active)
            motor.move(throttle, 0)  # move motor with throttle value
        else:
            motor.move(throttle, -steering)  # move motor with throttle and steering values
            cv2.waitKey(1)  # wait for a key press


# import pandas as pd
            # import os
            # import cv2
            # from datetime import datetime
            #
# global imgList, steeringList
            # countFolder = 0
            # count = 0
            # imgList = []
            # steeringList = []
#
            # #get current directory path
            # myDirectory = os.path.join(os.getcwd(), 'DataCollected')
            # print("Hello********************")
            # print(myDirectory)
#
            # #creates a new folder that is based on previous folder count
            # while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
            #     countFolder += 1
# newPath = myDirectory + "/IMG"+str(countFolder)
            # os.makedirs(newPath)
            #

