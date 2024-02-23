import cv2
import numpy as np

def thresholding(img):#thresholding function
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converts BGR image to HSV
    lowerWhite = np.array([85, 0, 0])  # lower bound of white color
    upperWhite = np.array([179, 160, 255])  # upper bound of white color
    maskedWhite = cv2.inRange(hsv, lowerWhite, upperWhite)  # creates binary mask using upper and lower bounds
    return maskedWhite

def warpImg (img,points,w,h,inv=False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp

def nothing(a):
    pass

def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0], wT // 2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2], wT // 2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)


def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop),
                         (widthBottom, heightBottom), (wT - widthBottom, heightBottom)])
    return points

def drawPoints(img,points):
    for x in range( 0,4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 15, (0, 0, 255), cv2.FILLED)
    return img

def getHistogram(img, display=False, minPer=0.1, region=4):
    if region == 1:
        histValues = np.sum(img, axis=0)
    else:
        histValues = np.sum(img[img.shape[0] // region:, :], axis=0)
        # histValues = np.sum(img, axis=0)
        # print(histValues)
    maxValue = np.max(histValues)  # FIND THE MAX VALUE
        # print(maxValue)
    minValue = minPer * maxValue
    indexArray = np.where(histValues >= minValue)  # ALL INDICES WITH MIN VALUE OR ABOVE
    basePoint = int(np.average(indexArray))  # AVERAGE ALL MAX INDICES VALUES
    # print(basePoint)

    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            # print(intensity)
            if intensity > minValue:
                color = (255, 0, 255)
            else:
                color = (0, 0, 255)
                ##intensity // 255
            print('Value', (type(x), type(int(img.shape[0] - (intensity // 255 // region)))))
            cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - (intensity // 255 // region)), color, 1)
        cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
        return basePoint, imgHist

    return basePoint

def stackImages(scale,imgArray):
