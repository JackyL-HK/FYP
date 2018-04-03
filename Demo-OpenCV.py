import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageFilter
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
# pTime = time.time()
# # print(sum(scr)/len(scr))
# img = np.zeros((720, 1280, 3), np.uint8)
# img[:]=(255,0,0)
# black = np.zeros((720, 1280, 3), np.uint8)
# # cv2.putText(img, scr[0], (10, 720//2), font,
# #             1, (255, 255, 255), 1, cv2.LINE_AA)
# while(True):
#     cv2.namedWindow('window')
#     # cv2.addWeighted(img, 0.99, black, 0.01, 0, img)
#     # cv2.rectangle(img, (0,0), (500,500), (0,0,0,100))
#     # img_pil = Image.fromarray(img)
#     # draw = ImageDraw.Draw(img_pil)
#     # draw.rectangle([0, 0, 1280, 720], fill=(0, 0, 255, 125))
#     # img = np.array(img_pil)
#     # font = cv2.FONT_HERSHEY_PLAIN
#     font = cv2.FONT_HERSHEY_TRIPLEX
#     # cv2.putText(img, scr[0], (10, 720//2), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
#     if time.time() - pTime > 1:
#         cv2.putText(img, scr[randrange(0, len(scr))], (10, randrange(0, 720)), font, 10, (255, 255, 255,128), 1, cv2.LINE_AA)
#         pTime = time.time()
#     cv2.imshow('window', img)
#     if cv2.waitKey(41) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()

# height,width
# img = np.zeros((720, 1280, 3), np.uint8)
# text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
# cv2.putText(img,  text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
#             0.7, (b, g, r), 1, cv2.LINE_AA)
# img_pil = Image.fromarray(img)
# draw = ImageDraw.Draw(img_pil)
# img = np.array(img_pil)

step = 5
# b,g,r,a
alpha = 0
textColor = (255, 255, 255, alpha)
b, g, r, a = textColor
# img_pil = Image.new('RGBA', (1280, 720), (0, 0, 0, 255))
# txt = Image.new('RGBA', img_pil.size, (255, 255, 255, 0))
# draw = ImageDraw.Draw(txt)
fontpath = "font\combuspl.ttf"
font = ImageFont.truetype(fontpath, 100)
while(True):
    img_pil = Image.new('RGBA', (1280, 720), (0, 0, 0, 255))
    # txt = Image.new('RGBA', img_pil.size, (255, 255, 255, 0))
    txt.filter(ImageFilter.GaussianBlur(radius=3))
    draw = ImageDraw.Draw(txt)
    # print(alpha)
    draw.text((0,0),  'HELLO WORLD',
              font=font, fill=(0, 0, 255, alpha))
    alpha += step
    textColor = (255, 255, 255, alpha)
    if alpha <= 0 or alpha >= 255:
        step *= -1
    out = Image.alpha_composite(img_pil, txt)
    ## Display
    img = np.array(out)
    cv2.imshow("res", img)
    if cv2.waitKey(40) & 0xFF == 27:
        break
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# from matplotlib import pyplot as plt
# # get an image
# base = Image.open('cloud.jpg').convert('RGBA')
#
# # make a blank image for the text, initialized to transparent text color
# txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
#
# # get a font
# fnt = ImageFont.truetype('font\combuspl.ttf', 40)
# # get a drawing context
# d = ImageDraw.Draw(txt)
#
# # draw text, half opacity
# d.text((10, 10), "Hello", font=fnt, fill=(255, 0, 0, 128))
# # draw text, full opacity
# d.text((10, 60), "World", font=fnt, fill=(255, 0, 0, 255))
#
# out = Image.alpha_composite(base, txt)
# # type(out)
# # cv2.imshow('window', np.array(out))
# # if cv2.waitKey(0) & 0xFF == 27:
# #     cv2.destroyAllWindows()
# # %matplotlib
# plt.imshow(out)
# plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis
# plt.show()
