import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread('BlueCropped.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

b, g, r = cv2.split(img)

#TODO: Crop Image

#Maybe use color specific hist

hist = cv2.calcHist(img, [0, 1], None, [180, 256], [0, 180, 0, 256])

histFile = open('RedCroppedHistogram.txt', 'w')

for item in hist:
    histFile.write(str(item)+'\n')


histFile.close()


plt.plot(hist)

plt.show()