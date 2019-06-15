from cv2 import cv2
from matplotlib import pyplot

image = cv2.imread("dark_image.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 255])

cv2.imshow("Original", image)

cv2.waitKey(5000)

pyplot.figure()
pyplot.xlim([0, 255])
pyplot.xlabel(" pixel intensities ")
pyplot.xlabel(" number of pixels ")

pyplot.plot(histogram, color="red")
pyplot.show()
