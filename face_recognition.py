import numpy as np
import cv2 as cv

harr_cascade = cv.CascadeClassifier('harr_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling', 'Anubhab Das']


# features = np.load('features.npy', allow_pickel=True)
# features = np.load('lables.npy')
 
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Resources\Faces/val/ben_afflek/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
face_rect = harr_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)