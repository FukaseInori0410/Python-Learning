# import cv
import cv2 as cv

# read the picture
img = cv.imread('face1.jpg')

# change to gray image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# show the gray image
cv.imshow('gray_img', gray_img)

# save the gray image
cv.imwrite('gray_face1.jpg', gray_img)

# show the picture
cv.imshow('read_img', img)

# wait
cv.waitKey(0)

# release the memory
cv.destroyAllWindows()
