import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread('Blue.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

b, g, r = cv2.split(img)

#TODO: Crop Image

croppedImage = img[1462:1914, 336:1020]

#Maybe use color specific hist

hist = cv2.calcHist(croppedImage, [0, 1], None, [180, 256], [0, 180, 0, 256])

histFile = open('RedCroppedHistogram.txt', 'w')

for item in hist:
    histFile.write(str(item)+'\n')


histFile.close()


gray = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
grayFiltered = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(grayFiltered, 30, 200)

cv2.imshow("Cropped Image", croppedImage)
cv2.imshow("Edged Image", edged)



plt.plot(hist)

plt.show()