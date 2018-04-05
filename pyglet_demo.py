import pyglet
from pyglet import text, font, graphics
from pyglet.window import mouse
from time import time
from movetext import MoveText
from random import randrange
import emoji
import csv


def loadLinesFromTxt(filepath):
    scr = []
    with open(str(filepath), 'r', encoding='utf-8') as fp:
        for line in fp.read().split('\n'):
            for char in line:
                if char in emoji.UNICODE_EMOJI:
                    line = line.replace(char, '')
            scr.append(line)
    return scr


def loadLinesFromCsv(filepath):
    scr = []
    with open(str(filepath), 'r', encoding='utf-8') as fp:
        for row in csv.DictReader(fp):
            if (float(row['polarity']) < -0.2):
                # print("{0:.02f}".format(
                #     float(row['polarity'])), '|', row['string'])
                scr.append(row['string'])
    return scr


font.add_file(r'font\DFHsiuW3.ttc')
font.add_file(r'font\AdobeFanHeitiStdB.otf')
font.add_file(r'font\NotoSansCJKtc-Bold.otf')
font.add_file(r'font\NotoSansCJKtc-Black.otf')

window = pyglet.window.Window(width=1920, height=640)
fps_display = pyglet.window.FPSDisplay(window)
batch_text = graphics.Batch()
# textlines = loadLinesFromCsv("NegPolarity-TextBlob-Default.csv")
textlines = loadLinesFromTxt("fbContent.txt")


def createLine(textlist):
    y = randrange(0, window.height)
    for t in textlist:
        # while any(abs(y-t.y) < 20 for t in textlist):
        while abs(y-t.y) < 20:
            y = randrange(0, window.height)

    # return MoveText(text=textlines[randrange(0, len(textlines))], font_size=30, x=randrange(0, window.width/3), y=y, color=(255, 255, 255, 255),font_name='DFPHsiuW3-B5')
    # return MoveText(text=textlines[randrange(0, len(textlines))], font_size=20, x=randrange(0, window.width/3), y=y, color=(255, 255, 255, 255),font_name='Adobe Fan Heiti Std B')
    return MoveText(text=textlines[randrange(0, len(textlines))], font_size=20, x=randrange(0, window.width/3), y=y, color=(255, 255, 255, 255), font_name='Noto Sans CJK TC Bold', batch=batch_text)
    # return MoveText(text=textlines[randrange(0, len(textlines))], font_size=20, x=randrange(0, window.width/3), y=y, color=(255, 255, 255, 255),font_name='Noto Sans CJK TC Black')


textlist = list()
textlist.append(createLine(textlist))
createTime = time()


def create_quad_vertex_list(x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height


quad = pyglet.graphics.vertex_list(4,
                                   ('v2i', create_quad_vertex_list(0, 0, 1920, 640)),
                                   ('c3B', (0, 0, 0, 205, 205, 205, 205, 205, 205, 0, 0, 0)))


@window.event
def on_draw():
    window.clear()
    # for t in textlist:
    #     t.draw()
    quad.draw(pyglet.gl.GL_QUADS)
    batch_text.draw()
    fps_display.draw()


@window.event
def update(dt):
    global createTime
    if time() - createTime > randrange(3, 6):
        textlist.append(createLine(textlist))
        createTime = time()
    for i, t in enumerate(textlist):
        if not t.end:
            t.update()
        else:
            textlist.pop(i)
    # print(len(textlist))


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
