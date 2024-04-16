print('Setting UP')#print message indicating setup process is starting
import os#importing os module
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'#set environment variable to suppress TensorFlow logs
from sklearn.model_selection import train_test_split #importing train_test_split function from sklearn
from utlis import * #importing custom utility functions

#### STEP 1 - INITIALIZE DATA
path = 'DataCollected' #define path to data directory
data = importDataInfo(path) #import data information from the specified path
print(data.head()) #print first few rows of the imported data
print(data['Center'][0]) #print the value of 'Center' column in the first row of data

#### STEP 2 - VISUALIZE AND BALANCE DATA
data = balanceData(data,display=True) #visualize and balance the data

#### STEP 3 - PREPARE FOR PROCESSING
imagesPath, steerings = loadData(path,data) #load image paths and corresponding steering angles
# print('No of Path Created for Images ',len(imagesPath),len(steerings))
# cv2.imshow('Test Image',cv2.imread(imagesPath[5]))
# cv2.waitKey(0)

#### STEP 4 - SPLIT FOR TRAINING AND VALIDATION
xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings,
                                              test_size=0.2,random_state=10) #split data into training and validation sets
print('Total Training Images: ',len(xTrain)) #print total number of training images
print('Total Validation Images: ',len(xVal)) #print total number of validation images

#### STEP 5 - AUGMENT DATA

#### STEP 6 - PREPROCESS

#### STEP 7 - CREATE MODEL
model = createModel() #create a neural network model

#### STEP 8 - TRAINNING
history = model.fit(dataGen(xTrain, yTrain, 100, 1),
                                  steps_per_epoch=100,
                                  epochs=10,
                                  validation_data=dataGen(xVal, yVal, 50, 0),
                                  validation_steps=50) #train the model

#### STEP 9 - SAVE THE MODEL
model.save('model.h5') #save the trained model
print('Model Saved') #print message indicating model has been saved

#### STEP 10 - PLOT THE RESULTS
plt.plot(history.history['loss']) #plot training loss
plt.plot(history.history['val_loss']) #plot validation loss
plt.legend(['Training', 'Validation']) #add legend
plt.title('Loss') #add title
plt.xlabel('Epoch') #add x-axis label
plt.show() #display the plot