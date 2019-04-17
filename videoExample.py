import numpy as np
import cv2

debug = False
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

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #EDGE DETECTION
    edges = cv2.Canny(gray,cannyMin,cannyMax,apertureSize = 3)
    #EDGE REDUCTION
    edges = cv2.dilate(edges,None)

    #CONTOUR DETECTION
    vals = edges.copy() #Make a clone because FindContours can modify the image
    contours0, hierarchy=cv2.findContours(vals, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]

    #GIVE FEEDBACK
    borderCount = len(contours0)
    if debug:
        print (borderCount, cannyMin , cannyMax)

    #DRAWING CONTOURS
    _black = (0, 0, 0)
    levels=2 #1 contours drawn, 2 internal contours as well, 3 ...
    cv2.drawContours (frame, contours, (-1, 2)[levels <= 0], _black, 3, cv2.LINE_AA, hierarchy, abs(levels))

    # Display the resulting frame
    cv2.imshow('frame',frame)

    #KEYBOARD CALLBACK
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()