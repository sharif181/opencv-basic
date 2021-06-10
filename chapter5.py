import cv2
import numpy as np

# Warp prespective chapter 5

img = cv2.imread('resources/card.png')

width,height = 250,250

pts1 = np.float32([[111,213],[234,166],[134,421],[321,412]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
impOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Output",img)
cv2.imshow("Wrap perspective",impOutput)
cv2.waitKey(0)