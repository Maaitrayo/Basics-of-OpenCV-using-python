import cv2 as cv
import numpy as np

img=cv.imread('Resources\Photos\park.jpg')
cv.imshow('Cats', img)
 
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacing
lap=cv.Laplacian(img,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacing', lap)

# Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combine=cv.bitwise_or(sobelx,sobely)
cv.imshow('SobelX',sobelx)
cv.imshow('SobelY',sobely)
cv.imshow('Combine',combine)

# Canny
canny=cv.Canny(gray, 150,170)
cv.imshow('Canny',canny)

cv.waitKey(0)