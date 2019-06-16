from cv2 import cv2
import numpy


def build_threshhold(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_image, (9, 9), 0)
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshold


def filter_contours(image, contours):
    filtered_contours = []
    image_area = image.shape[0] * image.shape[1]
    for i in contours:
        area = cv2.contourArea(i)
        if (area >= 0.001 * image_area) and (area < 0.01 * image_area):
            filtered_contours.append(i)

    return filtered_contours


def draw_contours(image, contours):
    for i in range(0, len(contours)):
        (x, y, w, h) = cv2.boundingRect(contours[i])
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


image = cv2.imread("people.jpg")
threshold = build_threshhold(image)
contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
filtered_contours = filter_contours(image, contours)
draw_contours(image, filtered_contours)

cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
cv2.imshow("Display", image)


masked_image = cv2.bitwise_and(image, image, mask=threshold)
cv2.imshow("Threshold", masked_image)


cv2.waitKey(5000)
