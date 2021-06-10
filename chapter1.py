import cv2
import numpy as np

# read and show image chapter 1
img = cv2.imread("resources/robot.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)

# read and show video
cap = cv2.VideoCapture("resources/index.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# read and show from web cam
cap = cv2.VideoCapture(0)
cap.set(3,640) #for width
cap.set(4,480)  #for height
cap.set(10,100)   # for brightness

while True:
    success,img = cap.read()
    cv2.imshow("From web cam",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

