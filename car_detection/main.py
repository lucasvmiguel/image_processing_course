from cv2 import cv2
from matplotlib import pyplot

filename = "traffic1.avi"
capture = cv2.VideoCapture(filename)
reference_frame = None
image_area = None


def build_image_blur(image):
    return cv2.medianBlur(image, 31)


def build_image_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def build_image_threshold(image):
    _, threshold = cv2.threshold(image, 20, 255, cv2.THRESH_BINARY)

    return threshold


def build_contours(image):
    filtered_contours = []
    contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        filtered_contours.append(i)

    return contours


# def draw_contours(image, contours):
#     for i in range(0, len(contours)):
#         (x, y, w, h) = cv2.boundingRect(contours[i])
#         image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


while True:
    ret, frame = capture.read()
    if ret == False:
        break

    if reference_frame is None:
        reference_frame = build_image_gray(frame)
        image_area = frame.shape[0] * frame.shape[1]

    difference_image = cv2.absdiff(reference_frame, build_image_gray(frame))
    blurred_image = build_image_blur(difference_image)
    threshold_image = build_image_threshold(blurred_image)

    contours = build_contours(threshold_image)
    for i in contours:
        contour_area = cv2.contourArea(i)
        if (contour_area > 0.001 * image_area) and (contour_area < 0.03 * image_area):
            (x, y, w, h) = cv2.boundingRect(i)
            cv2.rectangle(frame, (x, y), (x + w, h + y), (0, 0, 255), 2)
    # cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)

    cv2.imshow("frames", frame)

    if cv2.waitKey(1) == ord("q"):
        break

