import cv2 as cv

img=cv.imread('Resources\Photos\group 1.jpg')
cv.imshow('Lady', img)

# resize=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resize)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
harr_cascade=cv.CascadeClassifier('harr_face.xml')

faces_rect=harr_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6)
print(f'number of faces found= {len(faces_rect)}')

# Drawing a rectangle on the image
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv.imshow('Face detection', img)

cv.waitKey(0)