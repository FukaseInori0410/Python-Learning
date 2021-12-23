import cv2 as cv

cap = cv.VideoCapture(0)

flag = 1
num = 1

while cap.isOpened():
    ret_flag, Vshow = cap.read()
    cv.imshow('Capture_test', Vshow)
    k = cv.waitKey(1)
    if k == ord('s'):
        cv.imwrite('D:/codes/Python/face2/printscreen/'+str(num)+'_name.jpg', Vshow)
        print('success to save'+str(num)+'_name.jpg')
        print('====================================')
        num += 1
    elif k == ord(' '):
        break

cap.release()
cv.destroyAllWindows()
