import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import cv2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D,Flatten,Dense

import matplotlib.image as mpimg
from imgaug import augmenters as iaa

import random

#### STEP 1 - INITIALIZE DATA
def getName(filePath):
    myImagePathL = filePath.split('/')[-2:]
    folder_name = myImagePathL[-2]
    print(folder_name)
    myImagePath = os.path.join(myImagePathL[0], myImagePathL[1])
    # print(myImagePath)
    return myImagePath

def importDataInfo(path):
    columns = ['Center', 'Steering']
    noOfFolders = len(os.listdir(path)) // 2
    data = pd.DataFrame()
    for x in range(12, 17):
        dataNew = pd.read_csv(os.path.join(path, f'log_{x}.csv'), names=columns)
        print(f'{x}:{dataNew.shape[0]} ', end='')
        #### REMOVE FILE PATH AND GET ONLY FILE NAME
        # print(getName(data['center'][0]))
        dataNew['Center'] = dataNew['Center'].apply(getName)
        data = data._append(dataNew, True)
    print(' ')
    print('Total Images Imported', data.shape[0])
    return data




#### STEP 2 - VISUALIZE AND BALANCE DATA
def balanceData(data,display=True):
    nBin = 31
    samplesPerBin = 300
    hist, bins = np.histogram(data['Steering'], nBin)
    if display:
        center = (bins[:-1] + bins[1:]) * 0.5
        plt.bar(center, hist, width=0.03)








