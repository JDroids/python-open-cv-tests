import cv2
import numpy as np
import matplotlib.pyplot as plt
import os



for filename in os.listdir(".\Pictures"):
    
    img = cv2.imread('.\Pictures\\' + str(filename))
    #hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #TODO: Crop Image

    croppedImage = img[1462:1914, 336:1020]


    b, g, r = cv2.split(croppedImage)

    #Maybe use color specific hist

    blueHist = cv2.calcHist([b],[0],None,[256],[0,256])
    redHist = cv2.calcHist([r],[0],None,[256],[0,256])

    print(filename)

    lastBlue = blueHist[-1][0]
    lastRed = redHist[-1][0]

    #print("Blue Hist " + str(lastBlue)
    #print("Red Hist " + str(redHist)
    
    if(lastBlue > lastRed): print("Blue Jewel")
    elif(lastRed > lastBlue): print("Red Jewel")
    else: print("What?!?!?!??!?!??!?")
    
    print("\n")

    '''maxNumber = 0
    for item in hist:
        for number in item:
            if number > maxNumber:
                maxNumber = number
                correctArray = item

    print(maxNumber)
    print(np.argwhere(hist == correctArray)[0])'''

    
    '''
    gray = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(grayFiltered, 30, 200)

    plt.plot(redHist, 'r')
    plt.plot(blueHist, 'b')

    cv2.imwrite('.\Results\\' + 'Cropped' + filename, croppedImage)

    plt.savefig('.\Results\\' + filename)''' 
