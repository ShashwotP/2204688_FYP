import pandas as pd #importing pandas library
import os #importing os module
import cv2 #importing OpenCV library
from datetime import datetime #importing datetime module


global imgList, steeringList #declaring global variables
countFolder = 0 #initializing folder count variable
count = 0 #initializing count variable
imgList = [] #initializing empty list to store images
steeringList = []  #initializing empty list to store steering data



#get current directory path
myDirectory = os.path.join(os.getcwd(), 'DataCollected') #get the current directory path
print("Hello********************") #print a message
print(myDirectory) #print the current directory path

#creates a new folder that is based on previous folder count
while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')): #check if folder exists
    countFolder += 1  # increment the folder count
newPath = myDirectory + "/IMG" + str(countFolder)  # create a new folder path
os.makedirs(newPath)  # create a new folder

# SAVE IMAGES IN THE FOLDER
