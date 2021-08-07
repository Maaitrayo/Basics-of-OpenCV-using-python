import cv2 as cv

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Original', img)

#Average blur algorithm
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussian blur
gaussian = cv.GaussianBlur(img,(7,7), 0)
cv.imshow('Gaussing ', gaussian)

#Median blur
median = cv.medianBlur(img,7)
cv.imshow('Median', median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img,5,10,15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)