import pyglet
from pyglet import graphics
from time import time
from movetext import MoveText
from random import choice, uniform, randint
import emoji
import csv

window = pyglet.window.Window(width=1920, height=640, vsync=False)
fps_display = pyglet.window.FPSDisplay(window)
batch_text = graphics.Batch()
batch_quad = graphics.Batch()


def loadLinesFromTxt(filepath):
    scr = []
    with open(str(filepath), 'r', encoding='utf-8') as fp:
        for line in fp.read().split('\n'):
            for char in line:
                if char in emoji.UNICODE_EMOJI:
                    line = line.replace(char, '')
            scr.append(' '.join(line.split()))
            # scr.append(line)
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


def create_quad_vertex_list(x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height


def createLine(mtlist, tlist, w=None, align='right', lang='eng'):
    text = choice(tlist)
    if lang == 'chi':
        font_size = 20 if len(text) < 15 else 15
        font_name = 'Noto Sans CJK TC Bold'
        color = (255, 255, 255, 0)
    elif lang == 'eng':
        font_size = 14
        font_name = 'Noto Sans CJK TC Light'
        color = (0, 0, 0, 0)
    x = uniform(window.width/4, window.width /
                2) if align == 'left' else uniform(window.width/2, window.width*3/4)
    y = uniform(0, window.height)
    # for mt in mtlist:
    #     while abs(y-mt.y) < 20:
    #         y = uniform(0, window.height)
    width = w
    return MoveText(text=text, font_size=font_size, x=x, y=y, font_name=font_name, width=width, batch=batch_text, align=align, anchor_x=align, color=color)
    # return MoveText(text=choice(tlist), font_size=30, x=uniform(0, window.width/3), y=y,font_name='DFPHsiuW3-B5')
    # return MoveText(text=choice(tlist), font_size=20, x=uniform(0, window.width/3), y=y,font_name='Adobe Fan Heiti Std B')
    # return MoveText(text=choice(tlist), font_size=20, x=uniform(0, window.width/3), y=y, font_name='Noto Sans CJK TC Black')


def mt_update(mtlist, tlist):
    for mt in mtlist:
        if not mt.end:
            mt.update()
        else:
            mtlist.remove(mt)
    # print(len(mtlist))


chi_list = loadLinesFromTxt("fbContent.txt")
eng_list = loadLinesFromTxt("LongLines.txt")

chi_mt_list = list()
chi_mt_list.append(createLine(chi_mt_list, chi_list, 5, 'left', 'chi'))
eng_mt_list = list()
eng_mt_list.append(createLine(eng_mt_list, eng_list, 500, 'right', 'eng'))
createTime = time()

wh = 255
# quad = pyglet.graphics.vertex_list(4,
#                                    ('v2i', create_quad_vertex_list(0, 0, 1920, 640)),
#                                    ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))
quad = batch_quad.add(4, pyglet.gl.GL_QUADS, None,
                      ('v2i', create_quad_vertex_list(0, 0, 1920, 640)),
                      ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))

for i in range(12):
    for j in range(4):
        wh = int(randint(0,255))
        batch_quad.add(4, pyglet.gl.GL_QUADS, None,
                       ('v2i', create_quad_vertex_list(i*(window.width//12), j*(window.height//4), window.width//12, window.height//4)),
                       ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))


@window.event
def on_draw():
    window.clear()
    # quad.draw(pyglet.gl.GL_QUADS)
    batch_quad.draw()
    batch_text.draw()
    fps_display.draw()


@window.event
def update(dt):
    global createTime
    mt_update(chi_mt_list, chi_list)
    mt_update(eng_mt_list, eng_list)
    if time() - createTime > randint(3, 8):
        if choice([True, False]):
            chi_mt_list.append(createLine(
                chi_mt_list, chi_list, 5, 'left', 'chi'))
        else:
            eng_mt_list.append(createLine(
                eng_mt_list, eng_list, 500, 'right', 'eng'))
        createTime = time()


# pyglet.clock.schedule(update)
pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()
