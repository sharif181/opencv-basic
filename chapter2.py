# some basic function of opencv chapter 2
import cv2
import numpy as np


img = cv2.imread('resources/ronaldo.jpg')
kernal = np.ones((5,5),np.uint8)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image from BGR to Gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)  #convert image into blur(Can use orginal image also gray image)
imgCanny = cv2.Canny(img,100,100)   #to detect the edge of image...
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)  
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)




cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialiation image",imgDialation)
cv2.imshow("Erode image",imgEroded)
cv2.waitKey(0)
