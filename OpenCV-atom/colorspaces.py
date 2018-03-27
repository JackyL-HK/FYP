import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # get frame
    _, frame = cap.read()
    # BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue in HSV
    low_blue = np.array([110,50,50])
    high_blue = np.array([130,255,255])
    # threshold image to get mask
    mask = cv2.inRange(hsv, low_blue, high_blue)
    # bitwise mask and image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
