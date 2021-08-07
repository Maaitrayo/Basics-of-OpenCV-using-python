# -----------------------------------------------------Reading videos ------------------------------------------------------------
import cv2 as cv

capture = cv.VideoCapture('Resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()