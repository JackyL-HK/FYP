import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# resize
print(cap.get(3),cap.get(4))
cap.set(3,640),cap.set(4,360)
print(cap.get(3),cap.get(4))
# define Codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # MJPG #DIVX etc, need test individually
out = cv2.VideoWriter(r'vid\output.mp4', fourcc, 25.0, (640,360))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # write frame
        out.write(frame)

        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release everything when all is done
cap.release()
out.release()
cv2.destroyAllWindows()

print("End.")
