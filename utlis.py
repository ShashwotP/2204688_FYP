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






