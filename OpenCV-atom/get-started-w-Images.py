import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt
# imread() imshow() imwrite()
img_path = "img\photo001_r.jpg"
img = cv2.imread(img_path, 1)
#
# cv2.namedWindow('window', cv2.WINDOW_NORMAL)
# cv2.imshow('window', img)
#
# k = cv2.waitKey(0) & 0xFF
# if k == ord('s'):
#     cv2.imwrite(r"img\bnw.png", img)
#     cv2.destroyAllWindows()
# else:
#     cv2.destroyAllWindows()

# Matplotlib-pyplot
plt.imshow(img[..., ::-1], cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis
plt.show()

print("End.")
