import cv2
import numpy as np

from tensorflow.keras.models import load_model

import WebCamModule as wM
import MotorModule as mM


#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27) # Pin Numbers
model = load_model('C:/Users/Dell/PycharmProjects/Trial/model.h5')
#model1 = load_model()
######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)

