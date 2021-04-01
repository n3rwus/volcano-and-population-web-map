import cv2 as cv

img = cv.imread("geeks14.png", cv.IMREAD_COLOR)

cv.imshow("Test", img)

cv.waitKey(0)
cv.destroyAllWindows()