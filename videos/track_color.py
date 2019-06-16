from cv2 import cv2
import numpy

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = numpy.array([110, 50, 50])
    upper_range = numpy.array([130, 255, 255])

    mask = cv2.inRange(hsv_frame, lower_range, upper_range)

    cv2.imshow("Frame", frame)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Track", result)

    # exit camera
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
