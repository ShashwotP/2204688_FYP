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











