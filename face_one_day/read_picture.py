# import cv
import cv2 as cv

# read the picture
img = cv.imread('face1.jpg')

# show the picture
cv.imshow('read_img', img)

# wait
cv.waitKey(0)

# release the memory
cv.destroyAllWindows()
