import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import time
import csv
from random import randrange
# from matplotlib import pyplot as plt

fp = open("NegPolarity-TextBlob-Default.csv", 'r', encoding='utf-8')
scr = []
for row in csv.DictReader(fp):
    if (float(row['polarity']) < -0.3):
        print("{0:.02f}".format(float(row['polarity'])), '|', row['string'])
        scr.append(row['string'])
fp.close()
# scr[randint(0,len(scr))]
pTime = time.time()
# print(sum(scr)/len(scr))
img = np.zeros((720, 1280, 3), np.uint8)
black = np.zeros((720, 1280, 3), np.uint8)
# cv2.putText(img, scr[0], (10, 720//2), font,
#             1, (255, 255, 255), 1, cv2.LINE_AA)
while(True):
    cv2.namedWindow('window')
    cv2.addWeighted(img, 0.99, black, 0.01, 0, img)
    # cv2.rectangle(img, (0,0), (500,500), (0,0,0,100))
    # img_pil = Image.fromarray(img)
    # draw = ImageDraw.Draw(img_pil)
    # draw.rectangle([0, 0, 1280, 720], fill=(0, 0, 255, 125))
    # img = np.array(img_pil)
    font = cv2.FONT_HERSHEY_PLAIN
    # cv2.putText(img, scr[0], (10, 720//2), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    if time.time() - pTime > 1:
        cv2.putText(img, scr[randrange(0, len(scr))], (10, randrange(0, 720)), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        pTime = time.time()
    cv2.imshow('window', img)
    if cv2.waitKey(41) & 0xFF == 27:
        break

cv2.destroyAllWindows()

while(True):
    ## Make canvas and set the color
    img = np.zeros((200, 400, 3), np.uint8)
    b, g, r, a = 255, 255, 255, 0
    ## Use cv2.FONT_HERSHEY_XXX to write English.
    text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
    print(text)
    cv2.putText(img,  text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (b, g, r), 1, cv2.LINE_AA)

    ## Use simsum.ttc to write Chinese.
    fontpath = "font\combuspl.ttf"
    font = ImageFont.truetype(fontpath, 10)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((50, 100),  str(randrange(0, 100)), font=font, fill=(b, g, r, a))
    img = np.array(img_pil)

    ## Display
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
