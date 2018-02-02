import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([89, 163, 121]) #254, 73, 251
    upper_blue = np.array([124, 255, 255])

    lower_red = np.array([163,62,62])
    upper_red = np.array([255,0,0]) 
    # Threshold the HSV image to get only blue colors
    maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskRed = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    resBlue = cv2.bitwise_and(frame,frame, mask= maskBlue)
    resRed = cv2.bitwise_and(frame,frame, mask= maskRed)

    #res = cv2.bitwise_and(resBlue,resBlue, mask= resRed)

    cv2.imshow('frame',frame)

    cv2.imshow('maskBlue',maskBlue)
    cv2.imshow('maskRed',maskRed)

    cv2.imshow('resBlue',resBlue)
    cv2.imshow('resRed',resRed)

    #cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()