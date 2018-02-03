import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    croppedImage = cap
    hist = cv2.calcHist(croppedImage, [0, 1], None, [180, 256], [0, 180, 0, 256])

    maxNumber = 0
    for item in hist:
        for number in item:
            if number > maxNumber:
                maxNumber = number
                correctArray = item

    print(maxNumber)
    print(np.argwhere(hist == correctArray)[0])



    gray = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
    grayFiltered = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(grayFiltered, 30, 200)

    cv2.imshow("Cropped Image", croppedImage)
    cv2.imshow("Edged Image", edged)



    plt.plot(hist)

    plt.show()