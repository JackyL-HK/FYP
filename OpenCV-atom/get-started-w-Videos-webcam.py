import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print(cap.get(3),cap.get(4))
cap.set(3,640),cap.set(4,360)
print(cap.get(3),cap.get(4))
while(True):
    # capture frame-by-frame
    ret, frame = cap.read()
    # covert to greyscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # display the result frame
    cv2.imshow('video', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release the capture when all is done
cap.release()
cv2.destroyAllWindows()

print("End.")
