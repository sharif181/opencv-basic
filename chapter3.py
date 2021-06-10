import cv2
import numpy as np

# resize and cropping chapter 3
img = cv2.imread('resources/ronaldo.jpg')

imgResize = cv2.resize(img,(200,200)) #image resize (width,height)

imgCropped = img[0:200,30:300]  #image croping(heigth,width)

print(img.shape)  # shape (Height,Width,Channel)
print(imgResize.shape)

cv2.imshow("Original",img)
cv2.imshow("Resized",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)