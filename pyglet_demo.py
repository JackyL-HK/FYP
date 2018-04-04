import pyglet
from pyglet import text, font
from pyglet.window import mouse
from time import time
from movetext import MoveText
from random import randrange
import emoji

font.add_file('font\DFHsiuW3.ttc')

def loadLines(filepath):
    # import csv
    # with open('fbContent.txt', 'r', encoding='utf-8') as fp:
    #     scr = []
    #     for line in fp.read().split('\n'):
    #         scr.append(line)
    #     return scr
    with open('fbContent.txt', 'r', encoding='utf-8') as fp:
        scr = []
        for line in fp.read().split('\n'):
            # if any(char in emoji.UNICODE_EMOJI for char in line):
            for char in line:
                if char in emoji.UNICODE_EMOJI:
                    line = line.replace(char,'')
            scr.append(line)
        return scr

# def loadLines(filepath):
#     import csv
#     fp = open(str(filepath), 'r', encoding='utf-8')
#     scr = []
#     for row in csv.DictReader(fp):
#         if (float(row['polarity']) < -0.2):
#             # print("{0:.02f}".format(
#             #     float(row['polarity'])), '|', row['string'])
#             scr.append(row['string'])
#     fp.close()
#     return scr

textlist=[]

def createLine():
    y = randrange(0, window.height)
    for t in textlist:
        while abs(y-t.y) < 20:
            y = randrange(0, window.height)

    return MoveText(text=textlines[randrange(0, len(textlines))], font_size=30, x=randrange(
        0, window.width/3), y=y, color=(255, 255, 255, 255),font_name='DFPHsiuW3-B5')


createTime = time()

window = pyglet.window.Window(width=1920, height=640)
fps_display = pyglet.window.FPSDisplay(window)

textlines = loadLines("NegPolarity-TextBlob-Default.csv")

# label = MoveText(text='Hello World', font_name='Times New Roman', font_size=100,
#                  x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center', color=(50, 0, 125, 255))

textlist = [createLine()]


@window.event
def on_draw():
    window.clear()
    # label.draw()
    for t in textlist:
        t.draw()
    fps_display.draw()


@window.event
def update(dt):
    global createTime
    if time() - createTime > randrange(3, 6):
        textlist.append(createLine())
        createTime = time()
    for i, t in enumerate(textlist):
        if not t.end:
            t.update()
        else:
            textlist.pop(i)


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
