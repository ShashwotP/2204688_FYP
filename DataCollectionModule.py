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
def saveData(img, steering):
    global imgList, steeringList  # access global variables
    now = datetime.now()  # get current date and time
    timestamp = str(datetime.timestamp(now)).replace('.', '')  # convert timestamp to string
    # print("timestamp =", timestamp)
    fileName = os.path.join(newPath, f'Image_{timestamp}.jpg')  # create file name for the image
    cv2.imwrite(fileName, img)  # save image
    imgList.append(fileName)  # append image file name to imgList
    steeringList.append(steering)  # append steering data to steeringList


# SAVE LOG FILE WHEN THE SESSION ENDS
def saveLog():
    global imgList, steeringList  # access global variables
    # create a dictionary with image file names and steering data
    rawData = {'Image': imgList,
               'Steering': steeringList}
    df = pd.DataFrame(rawData)  # create a pandas DataFrame
    # Save DataFrame to a CSV file
    df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')  # print a message
    print('Total Images: ', len(imgList))  # print the total number of images saved

