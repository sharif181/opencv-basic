import cv2
import numpy as np

# shapes and text chapter 4

img = np.zeros((512,512,3),np.uint8)  #creating a black image
print(img)
img[:] = 123,123,123        #color the image(Whole)
img[200:300,100:300] = 0,0,233 #color in any custom area
cv2.line(img,(0,0),(300,300),(0,255,0),3)   #creating line
cv2.line(img,(300,0),(0,300),(0,255,0),3) 

cv2.rectangle(img,(0,0),(250,250),(0,0,123),cv2.FILLED) #reactangular
cv2.circle(img,(340,341),65,(244,233,123),cv2.FILLED)   #circle

cv2.putText(img,"This is test text",(110,110),cv2.FONT_HERSHEY_COMPLEX,1,(0,213,2),3)   #add text on image

cv2.imshow("Image",img)
cv2.waitKey(0)