import cv2
import numpy as np
import csv
from random import randint
# from matplotlib import pyplot as plt

fp = open("NegPolarity-TextBlob-Default.csv", 'r', encoding='utf-8')
scr=[]
for row in csv.DictReader(fp):
    if (float(row['polarity'])<-0.3):
        print("{0:.02f}".format(float(row['polarity'])),'|',row['string'])
        scr.append(row['string'])
fp.close()
# scr[randint(0,len(scr))]

# print(sum(scr)/len(scr))
while(True):
    img = np.zeros((500,500, 3), np.uint8)
    cv2.namedWindow('window')
    # cv2.imshow('window', img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, scr[randint(0,len(scr))], (50,50), font,
                1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('window', img)
    if cv2.waitKey(12):
        break
cv2.destroyAllWindows()
