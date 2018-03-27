import numpy as np
import cv2
from matplotlib import pyplot as plt

# black image (3D-Array of 512x512x3, all in Greyscale: 0)
img = np.zeros((512, 512, 3), np.uint8)
# diagonal blue line with thickness of 5px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# green rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0))
# red filled circle
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# ellipse
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))
# add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'HelloWorld', (10, 500), font, 3, (255, 255, 255), 2,
            cv2.LINE_AA)

plt.imshow(img[..., ::-1], cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis
plt.show()

print("End.")
