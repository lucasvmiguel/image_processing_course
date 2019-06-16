from cv2 import cv2
import numpy

capture = cv2.VideoCapture(0)
flag = 1

while True:
    ret, frame = capture.read()

    keypress = cv2.waitKey(1)

    # gray camera
    if keypress == ord("g") and flag != 1:
        flag = 1
        break

    # normal camera
    if keypress == ord("n") and flag != 0:
        flag = 0

    if flag == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Frame", frame)

    if flag == 1:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame", gray_frame)

    # exit camera
    if keypress == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
