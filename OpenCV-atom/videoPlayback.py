import numpy as py
import cv2
from matplotlib import pyplot as plt
import time


vid_path = r"vid\2047.mp4"
cap = cv2.VideoCapture(vid_path)
font = cv2.FONT_HERSHEY_SIMPLEX
cap.set(cv2.CAP_PROP_FPS, 24)
# cv2.namedWindow('video',cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while (cap.isOpened()):
    timeA = time.time()
    ret, frame = cap.read()

    if ret:
        # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # res = cv2.resize(grey, (0,0),fx=1,fy=1)

        cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (10, 500), font, 3, (255, 255, 255), 2,
                    cv2.LINE_AA)
        cv2.imshow('video', frame)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # print(cap.get(cv2.CAP_PROP_FPS))
    # print(cap.get(cv2.CAP_PROP_POS_FRAMES))
    # cv2.setWindowTitle('video', str(cap.get(cv2.CAP_PROP_POS_FRAMES)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    timeB = time.time()
    cv2.setWindowTitle('video', str(1/(timeB-timeA)))

cap.release()
cv2.destroyAllWindows()
