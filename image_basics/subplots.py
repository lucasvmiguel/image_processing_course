from cv2 import cv2
from matplotlib import pyplot

pic = cv2.imread("test.jpg")

pic_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
pic_proper = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)

figure = pyplot.figure()

pyplot.subplot(1, 2, 1), pyplot.title("Original"), pyplot.imshow(pic_proper)
pyplot.subplot(1, 2, 2), pyplot.title("Gray"), pyplot.imshow(pic_gray, cmap="gray")

pyplot.show()
