from cv2 import cv2

image = cv2.imread("test.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image_gray)
cv2.imwrite("grey_test.jpg", image_gray)

print(image_gray.shape)


cv2.waitKey(5000)
