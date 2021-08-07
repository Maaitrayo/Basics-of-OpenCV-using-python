# ------------------------------------ BASIC FUNCTIONS IN OPENCV--------------------------------------------------------------

import cv2 as cv

img = cv.imread('Resources/photos/park.jpg')
cv.imshow('Park', img)


#changing to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Park_Grey', gray)


#Bluring an image--->reduces noise
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #has to be an odd number
cv.imshow('Park_Blur', blur)


# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Park_Edges', canny)


# Diliting the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Park_Edges_Dialated', dilated)


# Eroded
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)


# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)