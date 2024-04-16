import os #importing the os module
import pandas as pd #importing the pandas library
import numpy as np #importing the numpy library
import matplotlib.pyplot as plt #importing the matplotlib library
from sklearn.utils import shuffle #importing shuffle function from sklearn
import cv2 #importing the OpenCV library

from tensorflow.keras.models import Sequential #importing Sequential model from Keras
from tensorflow.keras.layers import Convolution2D,Flatten,Dense #importing layers from Keras

import matplotlib.image as mpimg #importing matplotlib.image module
from imgaug import augmenters as iaa #importing augmenters from imgaug

import random #importing the random module

#### STEP 1 - INITIALIZE DATA
def getName(filePath):
    myImagePathL = filePath.split('/')[-2:]  #get the last two elements of the file path
    folder_name = myImagePathL[-2] #get the folder name
    print(folder_name) #print the folder name
    myImagePath = os.path.join(myImagePathL[0], myImagePathL[1]) #join the elements to get the file path
    # print(myImagePath)
    return myImagePath #return the file path

def importDataInfo(path):
    columns = ['Center', 'Steering'] #define column names
    noOfFolders = len(os.listdir(path)) // 2 #calculate the number of folders
    data = pd.DataFrame() #create an empty DataFrame
    for x in range(12, 17): #iterate through folders
        dataNew = pd.read_csv(os.path.join(path, f'log_{x}.csv'), names=columns) #read CSV files
        print(f'{x}:{dataNew.shape[0]} ', end='') #print folder number and data shape
        #### REMOVE FILE PATH AND GET ONLY FILE NAME
        # print(getName(data['center'][0]))
        dataNew['Center'] = dataNew['Center'].apply(getName) #print total number of imported imagesdataNew['Center'].apply(getName) # Apply getName function to 'Center' column
        data = data._append(dataNew, True) #append new data to DataFrame
    print(' ')
    print('Total Images Imported', data.shape[0]) #print total number of imported images
    return data #return the DataFrame




#### STEP 2 - VISUALIZE AND BALANCE DATA
def balanceData(data,display=True):
    nBin = 31 #define number of bins
    samplesPerBin = 300 #define number of samples per bin
    hist, bins = np.histogram(data['Steering'], nBin) #compute histogram
    if display:
        center = (bins[:-1] + bins[1:]) * 0.5 #compute bin centers
        plt.bar(center, hist, width=0.03) #plot histogram
        plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin)) #plot line for balanced data
        plt.title('Data Visualisation') #set plot title
        plt.xlabel('Steering Angle') #set x-axis label
        plt.ylabel('No of Samples') #set y-axis label
        plt.show() #display plot
    removeindexList = [] #initialize list to store indices to be removed
    for j in range(nBin): #iterate through bins
        binDataList = [] #initialize list to store indices in current bin
        for i in range(len(data['Steering'])): #iterate through steering data
            if data['Steering'][i] >= bins[j] and data['Steering'][i] <= bins[j + 1]: #check if steering angle is within current bin
                binDataList.append(i) #append index to binDataList
        binDataList = shuffle(binDataList) #shuffle binDataList
        binDataList = binDataList[samplesPerBin:] #get indices to be removed
        removeindexList.extend(binDataList) #extend removeindexList with indices to be removed
    print('Removed Images:', len(removeindexList)) #print number of removed images
    data.drop(data.index[removeindexList], inplace=True) #remove rows with specified indices
    print('Remaining Images:', len(data)) #print number of remaining images
    if display:
        hist, _ = np.histogram(data['Steering'], (nBin)) #compute histogram for balanced data
        plt.bar(center, hist, width=0.03) #plot histogram for balanced data
        plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin)) #plot line for balanced data
        plt.title('Balanced Data') #set plot title
        plt.xlabel('Steering Angle') #set x-axis label
        plt.ylabel('No of Samples') #set y-axis label
        plt.show() #display plot
    return data #return balanced data

#### STEP 3 - PREPARE FOR PROCESSING
def loadData(path, data):
    imagesPath = [] #initialize list to store image paths
    steering = [] #initialize list to store steering angles
    for i in range(len(data)): #iterate through the data
        indexed_data = data.iloc[i] #get the data at current index
        imagesPath.append(os.path.join(path, indexed_data[0])) #append the image path to imagesPath
        steering.append(float(indexed_data[1])) #append the steering angle to steering
    imagesPath = np.asarray(imagesPath) #convert imagesPath to a NumPy array
    steering = np.asarray(steering) #convert steering to a NumPy array
    return imagesPath, steering #return image paths and steering angles


#### STEP 5 - AUGMENT DATA
def augmentImage(imgPath,steering):
    img = mpimg.imread(imgPath) #read the image
    if np.random.rand() < 0.5: #randomly select whether to perform augmentation
        pan = iaa.Affine(translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)}) #define pan augmentation
        img = pan.augment_image(img) #apply pan augmentation to the image
    if np.random.rand() < 0.5: #randomly select whether to perform augmentation
        zoom = iaa.Affine(scale=(1, 1.2)) #define zoom augmentation
        img = zoom.augment_image(img) #apply zoom augmentation to the image
    if np.random.rand() < 0.5: #randomly select whether to perform augmentation
        brightness = iaa.Multiply((0.5, 1.2)) #define brightness augmentation
        img = brightness.augment_image(img) #apply brightness augmentation to the image
    if np.random.rand() < 0.5: #randomly select whether to perform augmentation
        img = cv2.flip(img, 1) #flip the image horizontally
        steering = -steering #invert the steering angle
    return img, steering #return the augmented image and steering angle

# imgRe,st = augmentImage('DataCollected/IMG12/Image_17081497507544.jpg',0)
# mpimg.imsave('Result.jpg',imgRe)
# plt.imshow(imgRe)
# plt.show()

#### STEP 6 - PREPROCESS
def preProcess(img):
    img = img[54:120, :, :] #crop the image to focus on the road
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV) #convert the color space to YUV
    img = cv2.GaussianBlur(img, (3, 3), 0) #apply Gaussian blur to the image
    img = cv2.resize(img, (200, 66)) #resize the image to the desired dimensions
    img = img / 255 # normalize the pixel values
    return img #return the preprocessed image

imgRe = preProcess(mpimg.imread('DataCollected/IMG12/Image_17081497376683.jpg'))
# mpimg.imsave('Result.jpg',imgRe)
plt.imshow(imgRe)
plt.show()


#### STEP 7 - CREATE MODEL
def createModel():
    model = Sequential() #initialize a Sequential model
    model.add(Convolution2D(24, (5, 5), (2, 2), input_shape=(66, 200, 3), activation='elu')) #add a convolutional layer
    model.add(Convolution2D(36, (5, 5), (2, 2), activation='elu')) #add a convolutional layer
    model.add(Convolution2D(48, (5, 5), (2, 2), activation='elu')) #add a convolutional layer
    model.add(Convolution2D(64, (3, 3), activation='elu')) #add a convolutional layer
    model.add(Convolution2D(64, (3, 3), activation='elu')) #add a convolutional layer

    model.add(Flatten()) #flatten the output
    model.add(Dense(100, activation='elu')) #add a fully connected layer
    model.add(Dense(50, activation='elu')) #add a fully connected layer
    model.add(Dense(10, activation='elu')) #add a fully connected layer
    model.add(Dense(1)) #add a fully connected layer with linear activation

    model.compile(Adam(lr=0.0001), loss='mse') #compile the model with mean squared error loss
    return model #return the compiled model


#### STEP 8 - TRAINNING
def dataGen(imagesPath, steeringList, batchSize, trainFlag):
    while True:
        imgBatch = [] #initialize list to store image batches
        steeringBatch = [] #initialize list to store steering batches

        for i in range(batchSize): #iterate through the batch size
            index = random.randint(0, len(imagesPath) - 1) #randomly select an index
            if trainFlag: #check if training flag is True
                img, steering = augmentImage(imagesPath[index], steeringList[index]) # augment the image
            else:
                img = mpimg.imread(imagesPath[index]) #read the image
                steering = steeringList[index] # get the steering angle
            img = preProcess(img) #preprocess the image
            imgBatch.append(img) # append the preprocessed image to imgBatch
            steeringBatch.append(steering) #append the steering angle to steeringBatch
        yield (np.asarray(imgBatch), np.asarray(steeringBatch)) #yield the image and steering batches





























