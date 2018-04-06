import pyglet
from pyglet import graphics, text
from time import time
from movetext import MoveText, map_range
from random import choice, uniform, randint
import emoji
import csv

# display = pyglet.window.get_platform().get_default_display()
# screens = display.get_screens()
# window = pyglet.window.Window(width=1920, height=640, vsync=True,fullscreen=True,screen=screens[0])
window = pyglet.window.Window(
    width=1920, height=548, vsync=True)  # 3.5:1 ratio // 4.2*1.2m
window.set_caption('Certificate of Death v0.1')
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


def loadStudentsList(filepath):
    scr = []
    with open(str(filepath), 'r', encoding='utf-8') as fp:
        for row in csv.DictReader(fp):
            scr.append(row)
    return scr


def create_quad_vertex_list(x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height


def createLine(mtlist, tlist, w=None, align='right', lang='eng'):
    text = choice(tlist)
    if lang == 'chi':
        font_size = 20 if len(text) < 15 else 15
        if any(t == '攰' for t in text):
            font_name = choice(['Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin'])
        else:
            font_name = choice(['Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin', 'MLingWaiFHK-Light', 'DFPHsiuW3-B5', 'DFPErW3-B5'])
        color = (255, 255, 255, 0)
    elif lang == 'eng':
        font_size = 14
        font_name = 'Noto Sans CJK TC Light'
        color = (0, 0, 0, 0)
    x = uniform(0, window.width /
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
quad = pyglet.graphics.vertex_list(4,
                                   ('v2i', create_quad_vertex_list(
                                       0, 0, window.width, window.height)),
                                   ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))
# quad = batch_quad.add(4, pyglet.gl.GL_QUADS, None,
#                       ('v2i', create_quad_vertex_list(0, 0, 1920, 640)),
#                       ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))

students = loadStudentsList('students_list.csv')
for i in range(20):
    for j in range(4):
        # wh = int(randint(0, 255))
        wh = int(map_range(int(students[i+j*20]['age']), int(min(row['age']
                                                                 for row in students)), int(max(row['age'] for row in students)), 0, 255))
        batch_quad.add(4, pyglet.gl.GL_QUADS, None, ('v2i', create_quad_vertex_list(i*(window.width//20), j*(window.height//4),
                                                                                    window.width//20, window.height//4)), ('c3B', (wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh)))
        text.Label(text=str(students[i+j*20]['age']), font_name='Noto Sans CJK TC Light',
                   font_size=12, anchor_x='center', anchor_y='center', x=i*(window.width//20)+window.width//40, y=j*(window.height//4)+window.height//16*3, batch=batch_quad)
        text.Label(text=str(students[i+j*20]['sex'].capitalize()), font_name='Noto Sans CJK TC Light',
                   font_size=12, anchor_x='center', anchor_y='center', x=i*(window.width//20)+window.width//40, y=j*(window.height//4)+window.height//16*2, batch=batch_quad)
        text.Label(text=str(students[i+j*20]['date']), font_name='Noto Sans CJK TC Light',
                   font_size=12, anchor_x='center', anchor_y='center', x=i*(window.width//20)+window.width//40, y=j*(window.height//4)+window.height//16, batch=batch_quad, dpi=100)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        pyglet.image.get_buffer_manager().get_color_buffer().save(
            'screenshot{}.png'.format(time()))


@window.event
def on_draw():
    window.clear()
    quad.draw(pyglet.gl.GL_QUADS)
    # batch_quad.draw()
    batch_text.draw()
    fps_display.draw()


@window.event
def update(dt):
    global createTime
    mt_update(chi_mt_list, chi_list)
    mt_update(eng_mt_list, eng_list)
    # if time() - createTime > randint(3, 8):
    if time() - createTime > 3:
        if choice([True, False]):
            chi_mt_list.append(createLine(
                chi_mt_list, chi_list, 5, 'left', 'chi'))
        else:
            eng_mt_list.append(createLine(
                eng_mt_list, eng_list, 500, 'right', 'eng'))
        createTime = time()


# pyglet.clock.schedule(update)
pyglet.clock.schedule_interval(update, 1/24.0)
pyglet.app.run()
