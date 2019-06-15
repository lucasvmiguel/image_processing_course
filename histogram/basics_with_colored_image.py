from cv2 import cv2
from matplotlib import pyplot

image = cv2.imread("test.jpg")

b_histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
g_histogram = cv2.calcHist([image], [1], None, [256], [0, 256])
r_histogram = cv2.calcHist([image], [2], None, [256], [0, 256])

pyplot.figure()
pyplot.xlabel(" pixel intensities ")
pyplot.xlabel(" number of pixels ")

pyplot.plot(b_histogram, color="blue")
pyplot.plot(g_histogram, color="green")
pyplot.plot(r_histogram, color="red")
pyplot.show()
