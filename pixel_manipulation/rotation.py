from cv2 import cv2
import random
import numpy

image = cv2.imread("test.jpg")
(rows, cols, planes) = numpy.shape(image)

center = (cols // 2, rows // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1)

rotation = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("test", rotation)
cv2.waitKey(5000)
