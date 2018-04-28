import pyglet
from pyglet import graphics, text, image, sprite
from time import time
from movetext import MoveText, map_range
from random import choice, uniform, randrange
import emoji
import csv
# import pathlib

currentFrame = 0
pgmStartTime = time()
# pathlib.Path(r'screenshots\{}'.format(pgmStartTime)
#              ).mkdir(parents=True, exist_ok=True)

# display = pyglet.window.get_platform().get_default_display()
# screens = display.get_screens()
# window = pyglet.window.Window(width=1920, height=640, vsync=True,fullscreen=True,screen=screens[0])
window = pyglet.window.Window(
    width=1920, height=548, vsync=True)  # 3.5:1 ratio // 4.2*1.2m
# window.set_location(0, (1080-window.height)//2)
window.set_caption('Certificate of Death v0.2')
fps_display = pyglet.window.FPSDisplay(window)
# batch_text = graphics.Batch()
chi_batch_text = graphics.Batch()
eng_batch_text = graphics.Batch()
batch_quad = graphics.Batch()
batch_cert = graphics.Batch()

cert_img = image.load('dse_cert_temp_resize.jpg')


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
        font_name = 'Noto Sans CJK TC Bold'
        # font_name = choice(['Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin'])
        font_size = 15
        # if any(t == '攰' for t in text):
        #     font_name = choice(
        #         ['Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin'])
        # else:
        #     font_name = choice(['Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin',
        #                         'MLingWaiFHK-Light', 'DFPHsiuW3-B5', 'DFPErW3-B5'])
        # font_size = 20 if len(text) < 15 or font_name not in [
        #                       'Noto Sans CJK TC Bold', 'Noto Sans CJK TC Thin'] else 15
        color = (255, 255, 255, 0)
        batch_text = chi_batch_text
        x = uniform(0, window.width / 2)
        y = randrange(0, 600, 30)
    elif lang == 'eng':
        font_size = 14  # 14
        font_name = 'Noto Sans CJK TC Light'
        color = (0, 0, 0, 0)
        batch_text = eng_batch_text
        x = uniform(window.width/2, window.width*3/4)
        y = randrange(0, 600, 28)
    width = w
    return MoveText(text=text, font_size=font_size, x=x, y=y, font_name=font_name, width=None, batch=batch_text, align=align, anchor_x='center', color=color)
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

cert_sprites = []
x_num, y_num = 4, 2
for i in range(20):
    for j in range(4):
        # wh = int(randint(0, 255))
        wh = int(map_range(int(students[i+j*x_num]['age']), int(min(row['age']
                                                                    for row in students)), int(max(row['age'] for row in students)), 0, 255))
        # batch_quad.add(4, pyglet.gl.GL_QUADS, None, ('v2i', create_quad_vertex_list(i*(window.width//x_num), j*(window.height//y_num),
        #                                                                             window.width//x_num, window.height//y_num)), ('c3B', (wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh)))
        cert_sprites.append(sprite.Sprite(
            cert_img, i*(window.width//x_num), j*(window.height//y_num), batch=batch_cert))
        text.Label(text=str(students[i+j*x_num]['\ufeffname']), font_name='Noto Sans CJK TC Bold', color=(0,0,0, 130),
                   font_size=15, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+window.width//(x_num*16)*13, y=j*(window.height//y_num)+window.height//(y_num*64)*36, batch=batch_quad)
        # text.Label(text=str(students[i+j*x_num]['age']), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 30),
        #            font_size=30, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+window.width//(x_num*2), y=j*(window.height//y_num)+window.height//(y_num*4)*3, batch=batch_quad)
        # text.Label(text=str(students[i+j*x_num]['sex'].capitalize()), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 30),
        #            font_size=30, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+window.width//(x_num*2), y=j*(window.height//y_num)+window.height//(y_num*4)*2, batch=batch_quad)
        # text.Label(text=str(students[i+j*x_num]['date']), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 30),
        #            font_size=30, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+window.width//(x_num*2), y=j*(window.height//y_num)+window.height//(y_num*4)*1, batch=batch_quad, dpi=100)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        pyglet.image.get_buffer_manager().get_color_buffer().save(
            'screenshot{}.png'.format(time()))


@window.event
def on_draw():
    window.clear()
    # quad.draw(pyglet.gl.GL_QUADS)
    batch_cert.draw()
    batch_quad.draw()
    eng_batch_text.draw()
    chi_batch_text.draw()
    # fps_display.draw()


@window.event
def update(dt):
    # global currentFrame
    # pyglet.image.get_buffer_manager().get_color_buffer().save(
    #     r'screenshots\{}\screenshot{}.png'.format(pgmStartTime, str(currentFrame).zfill(5)))
    # currentFrame += 1

    global createTime
    mt_update(chi_mt_list, chi_list)
    mt_update(eng_mt_list, eng_list)
    # if time() - createTime > randint(3, 8):
    if time() - createTime > 1 and len(chi_mt_list)+len(eng_mt_list) < 15:
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

for all in chi_mt_list:
    print(all.text)
    print('x', all.x, 'y', all.y, 'width',
          all.content_width, 'height', all.content_height)
for all in eng_mt_list:
    print(all.text)
    print(all.x, all.y, all.content_width, all.content_height)
print(len(chi_mt_list), len(eng_mt_list))
