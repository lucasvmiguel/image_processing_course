from cv2 import cv2

image = cv2.imread("test.jpg")

# SQUARE
image[300:320, 320:340] = (0, 0, 255)

# LINE
cv2.line(image, (200, 100), (100, 100), (0, 0, 255), 10)

# CIRCLE
cv2.circle(image, (500, 500), 20, (0, 0, 255), 2)

cv2.imshow("Show", image)
cv2.waitKey(5000)
