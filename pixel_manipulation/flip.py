from cv2 import cv2

image = cv2.imread("test.jpg")

# Horizontal
flipped_horizontal = cv2.flip(image, 1)

# Vertical
flipped_vertical = cv2.flip(image, 0)

# Both
flipped_both = cv2.flip(image, -1)

# cv2.INTER_LINEAR or cv2.CUBIC
resized = cv2.resize(image, None, fx=0.6, fy=0.9, interpolation=cv2.INTER_LINEAR)


cv2.imshow("test", resized)
cv2.waitKey(5000)
