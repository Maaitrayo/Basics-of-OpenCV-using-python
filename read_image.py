#-------------------------------------------Reading images--------------------------------------------------
import cv2 as cv

img = cv.imread('Resources/photos/cat.jpg')

cv.imshow('cat',img)
print(img)

cv.waitKey(0)
