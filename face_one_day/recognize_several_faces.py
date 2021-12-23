# import cv
import cv2 as cv


def face_detect_demo():
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier\
        ('C:/Users/HP/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/'
         'haarcascade_frontalface_alt.xml')  # change the data set
    face = face_detect.detectMultiScale(gray_img, 1.01, 5)  # change the parameter
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w,  y+h), color=(0, 0, 255), thickness=2)
        cv.imshow('result', img)


img = cv.imread('face1.jpg')

# invoke the function
face_detect_demo()

# wait for a 'q'
while True:
    if ord('q') == cv.waitKey(0):
        break

# release the memory
cv.destroyAllWindows()
