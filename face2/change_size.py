# import cv
import cv2 as cv

# read the picture
img = cv.imread('face1.jpg')

# change size
resize_img = cv.resize(img, dsize=(400, 300))

# show the raw picture
cv.imshow('raw_img', img)

# show the changed picture to make a comparison
cv.imshow('resize_img', resize_img)

# print their sizes
print('未修改：', img.shape)
print('修改后：', resize_img.shape)

# wait for a 'q'
while True:
    if ord('q') == cv.waitKey(0):
        break

# release the memory
cv.destroyAllWindows()
