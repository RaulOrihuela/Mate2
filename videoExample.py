import cv2
import numpy as np
from matplotlib import pyplot as plt

cannyMin = 125
cannyMax = 150
borderCount = 220
cap = cv2.VideoCapture(0)


while(True):
    #MODIFY PARAMS BASED ON FEEDBACK
    if borderCount > 320:
        cannyMin += 25
        cannyMax += 25
    if borderCount < 180:
        if cannyMin >= 25 and cannyMax >= 50:
            cannyMin -= 25
            cannyMax -= 25

    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFrame = cv2.medianBlur(grayFrame,5)
    grayFrame = cv2.adaptiveThreshold(grayFrame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    grayFrame = cv2.medianBlur(grayFrame,5)

    #EDGE DETECTION
    grayFrame = cv2.Canny(grayFrame,cannyMin,cannyMax,apertureSize = 3)
    #EDGE REDUCTION
    grayFrame = cv2.dilate(grayFrame,None)

    #grayFrame = cv2.GaussianBlur(grayFrame,(5,5),0)
    cv2.imshow('video gray', grayFrame)
    cv2.imshow('video original', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
