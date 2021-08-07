# ------------------------------------- DRAWING ON IMAGES --------------------------------------------------------

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black', blank)

#Paint the image green
blank[:] = 0,255,0
cv.imshow('Green',blank)

#setting limits in color 
blank[200:300, 300:400] = 0,0,255
cv.imshow('Pattern', blank)

#Drawing a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,250), thickness=2)
cv.imshow('Rectangle', blank)

#Drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255))
cv.imshow('Circle', blank)

#Drawing a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('line', blank)

#Writing a text on an image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Test', blank)

cv.waitKey(0)