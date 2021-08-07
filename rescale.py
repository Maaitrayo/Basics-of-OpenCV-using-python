# -----------------------------------------------HOW TO RESCALE AN IMAGE -------------------------------------------------------

import cv2 as cv

# Rescale frame function reads images, videos and live videos
# frame.shape[1] ---> Width, frame.shape[0] ---> height
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#end


#Reading images
img = cv.imread('Resources/photos/cat.jpg')

resized_img = rescaleFrame(img)
cv.imshow('cat',img)
cv.imshow('resized_cat', resized_img)
#end

def changeRes(width,height):
    #only works on live video
    capture.set(3,width)
    capture.set(4,height)
#end


#Reading videos
capture = cv.VideoCapture('Resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
#end

