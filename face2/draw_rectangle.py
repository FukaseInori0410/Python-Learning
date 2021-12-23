# import cv
import cv2 as cv

# read the picture
img = cv.imread('face1.jpg')

# draw the coordinate
x, y, w, h = 100, 100, 100, 100

# draw a rectangle
cv.rectangle(img, (x, y, x+w, y+h), color=(0, 0, 255), thickness=1)

# draw a circle
cv.circle(img, center=(x+w, y+h), radius=100, color=(255, 0, 0), thickness=2)

# show
cv.imshow('draw_img', img)

# wait for a 'q'
while True:
    if ord('q') == cv.waitKey(0):
        break

# release the memory
cv.destroyAllWindows()
