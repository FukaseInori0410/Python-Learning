# import cv
import cv2 as cv


def face_detect_demo(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier\
        ('C:/Users/HP/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/'
         'haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray_img)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w,  y+h), color=(0, 0, 255), thickness=2)
        cv.imshow('result', img)


# read the camera
# cap = cv.VideoCapture(0)

# read a video
cap = cv.VideoCapture('246455366-1-208.mp4')

# wait for a 'q'
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)

    if ord('q') == cv.waitKey(1):  # 0 will remain the first frame, change to 1
        break

# release the memory
cv.destroyAllWindows()

# release the camera
cap.release()
