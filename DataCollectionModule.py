import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

#get current directory path
myDirectory = os.path.join(os.getcwd(), 'DataCollected')
print("Hello********************")
print(myDirectory)