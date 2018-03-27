import numpy as py
import cv2

vid_path = r"vid\video0001.mp4"
cap=cv2.VideoCapture(vid_path)

while(cap.isOpened()):
    ret,frame=cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('video', grey)

    print(cap.get(cv2.CAP_PROP_FPS))
    # print(cap.get(cv2.CAP_PROP_FOURCC))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
