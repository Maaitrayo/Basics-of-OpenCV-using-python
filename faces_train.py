import cv2 as cv
import os
import numpy as np

people=['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling', 'Anubhab Das']
DIR= 'Resources/Faces/train'

harr_cascade = cv.CascadeClassifier('harr_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                face_roi=gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print('---------------------------Training Done--------------------------')
# print(f'Length of festures list = {len(features)}')
# print(f'Length of labels list = {len(labels)}')
features = np.array(features, dtype='object')
labels = np.array(labels)
# print(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the rrecognizer on thr features and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)