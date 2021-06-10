import cv2
import numpy as np

#Joining Images chapter 6

img = cv2.imread('resources/ronaldo.jpg')

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))


cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)