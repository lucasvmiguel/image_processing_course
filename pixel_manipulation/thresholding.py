from cv2 import cv2

image = cv2.imread("test.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_image, 130, 255, cv2.THRESH_BINARY)

# cv2.imshow("gray", gray_image)
# cv2.waitKey(5000)

cv2.imshow("thresh", thresh)
cv2.waitKey(5000)
