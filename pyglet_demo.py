import pyglet
from pyglet import graphics, text, image, sprite
from time import time
from movetext import MoveText, map_range
from random import choice, uniform, randrange, random
import emoji
import csv
import os.path
# import pathlib

chi_list_path = 'fbContent.txt'
eng_list_path = 'LongLines.txt'
students_list_path = 'students_list.csv'

currentFrame = 0
pgmStartTime = time()
preset = 0
screen_height = 551
text_height = 50
linespace = 2
empty = [True]*(screen_height//text_height)*linespace
student_empty = [True]*10
x_num, y_num = 5, 2  # for A1 landscape
# empty = [True, False, True, False, True, False, False, True, False, False, True] # 1,3,5,6,8,9
# print(type(list(enumerate(empty))))

# print(choice(list(i for i,c in enumerate(empty) if c== False)))
# pathlib.Path(r'screenshots\{}'.format(pgmStartTime)
# ).mkdir(parents=True, exist_ok=True)

display = pyglet.window.get_platform().get_default_display()
screens = display.get_screens()
window = pyglet.window.Window(width=1920, height=1080, vsync=True, fullscreen=True, screen=screens[0])
# window = pyglet.window.Window(
#    width=1920, height=screen_height, vsync=True)  # 3.5:1 ratio // 4.2*1.2m
# window.set_location(0, (1080-window.height)//2)
window.set_caption('Certificate of Death v0.2')
fps_display = pyglet.window.FPSDisplay(window)
# batch_text = graphics.Batch()
chi_batch_text = graphics.Batch()
eng_batch_text = graphics.Batch()
batch_quad = graphics.Batch()
batch_cert = graphics.Batch()
test_name = graphics.Batch()


cert_img = image.load(os.path.join('final_cert.jpg'))


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
            # if (float(row['polarity']) < -0.2):
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


def createLine(mtlist, tlist, w=None, lang='eng'):
    text = choice(tlist)
    if lang == 'chi':
        font_name = 'Noto Sans CJK TC Bold'
        font_size = 25  # 15
        color = (255, 255, 255, 0)
        batch_text = chi_batch_text
        align = 'left'
        x = uniform(window.width/3, window.width*3/4)
        # y = randrange(0, screen_height, 10)
        index = choice(list(i for i, c in enumerate(empty) if c == True))
        empty[index] = False
        y = index*25+1
    elif lang == 'eng':
        font_size = 24  # 14
        font_name = 'Noto Sans CJK TC Black'
        if preset == 0:
            color = (150, 150, 150, 0)
        elif preset == 1:
            color = (0, 0, 0, 0)
        batch_text = eng_batch_text
        align = 'right'
        x = uniform(0, window.width/3)
        # y = randrange(0, screen_height, 10)
        index = choice(list(i for i, c in enumerate(empty) if c == True))
        empty[index] = False
        y = index*25+1
    return MoveText(text=text, font_size=font_size, x=x, y=y, font_name=font_name, width=None, batch=batch_text, align=align, anchor_x='left', anchor_y='top', color=color, index=index)


def createStudent(students, i, j):
    hold_time = randrange(15, 30)
    item = choice(students)
    student_empty[i+j*x_num] = False
    return [MoveText(text=item['\ufeffname'], font_size=16, x=i*(window.width//x_num)+320, y=j*(screen_height//y_num)+60, font_name='Noto Sans CJK TC Bold',
                     batch=test_name, anchor_x='center', anchor_y='center', color=(150, 150, 150, 0), hold_time=hold_time, index=i+j*x_num),
            MoveText(text=item['date'], font_size=12, x=i*(window.width//x_num)+335, y=j*(screen_height//y_num)+205, font_name='Noto Sans CJK TC Bold',
                     batch=test_name, anchor_x='center', anchor_y='center', color=(150, 150, 150, 0), hold_time=hold_time, index=i+j*x_num),
            MoveText(text=item['grade'], font_size=16, x=i*(window.width//x_num)+325, y=j*(screen_height//y_num)+165, font_name='Noto Sans CJK TC Bold',
                     batch=test_name, anchor_x='center', anchor_y='center', color=(150, 150, 150, 0), hold_time=hold_time, index=i+j*x_num)]


chi_mt_list = list()
eng_mt_list = list()
student_mt_list = list()
createTime = time()


def mt_update(mtlist, dt):
    for mt in mtlist:
        if mt.end or mt.x+mt.content_width < 0:
            empty[mt.index] = True
            mtlist.remove(mt)
        else:
            mt.update(dt)
    # print(len(mtlist))


def st_update(stlist, dt):
    for st in stlist:
        if st[0].end:
            student_empty[st[0].index] = True
            stlist.remove(st)
        else:
            for item in st:
                item.update(dt)


chi_list = loadLinesFromTxt(chi_list_path)
eng_list = loadLinesFromTxt(eng_list_path)
# eng_list = loadLinesFromCsv(eng_list_path)


wh = 255
quad = pyglet.graphics.vertex_list(4,
                                   ('v2i', create_quad_vertex_list(
                                       0, 0, window.width, screen_height)),
                                   ('c3B', (100, 100, 100, wh, wh, wh, wh, wh, wh, 100, 100, 100)))
sign = pyglet.graphics.vertex_list(4,
                                   ('v2i', create_quad_vertex_list(0, 0, 300, 100)),
                                   ('c3B', (wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh)))
wip = text.Label(text='Work in Progress', font_name='Noto Sans CJK TC Bold', color=(200, 0, 0, 200),
                 font_size=25, anchor_x='left', anchor_y='center', x=10, y=50)

students = loadStudentsList(students_list_path)

cert_sprites = []
# x_num, y_num = 20, 4 # for A4 portrait
# x_num, y_num = 10, 4 # for A3 landscape
# x_num, y_num = 10, 2  # for A2 portrait

# x_num, y_num = 5, 1 # for A0 portrait
# for i in range(x_num):
#     for j in range(y_num):
#         # wh = int(randint(0, 255))
#         # wh = int(map_range(int(students[i+j*x_num]['age']), int(min(row['age']
#         #                                                             for row in students)), int(max(row['age'] for row in students)), 0, 255))
#         # batch_quad.add(4, pyglet.gl.GL_QUADS, None, ('v2i', create_quad_vertex_list(i*(window.width//x_num), j*(screen_height//y_num),
#         #                                                                             window.width//x_num, screen_height//y_num)), ('c3B', (wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh, wh)))
#         cert_sprites.append(sprite.Sprite(
#             cert_img, i*(window.width//x_num), j*(screen_height//y_num), batch=batch_cert))
#         text.Label(text=str(students[i+j*x_num]['\ufeffname']), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 150),
#                    font_size=16, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+320, y=j*(screen_height//y_num)+60, batch=test_name)
#         text.Label(text=str(students[i+j*x_num]['date']), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 150),
#                    font_size=12, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+335, y=j*(screen_height//y_num)+205, batch=test_name)
#         text.Label(text=str(students[i+j*x_num]['grade']), font_name='Noto Sans CJK TC Bold', color=(255, 255, 255, 150),
#                    font_size=16, anchor_x='center', anchor_y='center', x=i*(window.width//x_num)+325, y=j*(screen_height//y_num)+165, batch=test_name)

# for j in range(y_num):
#     for i in range(x_num):
#         hold_time = randrange(10, 20)
#         item = choice(students)
#         student_mt_list.append([
#             MoveText(text=item['\ufeffname'], font_size=16, x=i*(window.width//x_num)+320, y=j*(screen_height//y_num)+60, font_name='Noto Sans CJK TC Bold',
#                      batch=test_name, anchor_x='center', anchor_y='center', color=(255, 255, 255, 0), hold_time=hold_time, index=i+j*x_num),
#             MoveText(text=item['date'], font_size=12, x=i*(window.width//x_num)+335, y=j*(screen_height//y_num)+205, font_name='Noto Sans CJK TC Bold',
#                      batch=test_name, anchor_x='center', anchor_y='center', color=(255, 255, 255, 0), hold_time=hold_time, index=i+j*x_num),
#             MoveText(text=item['grade'], font_size=16, x=i*(window.width//x_num)+325, y=j*(screen_height//y_num)+165, font_name='Noto Sans CJK TC Bold',
#                      batch=test_name, anchor_x='center', anchor_y='center', color=(255, 255, 255, 0), hold_time=hold_time, index=i+j*x_num)])


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        pyglet.image.get_buffer_manager().get_color_buffer().save(
            'screenshot{}.png'.format(time()))


@window.event
def on_draw():
    window.clear()
    if preset == 1:
        quad.draw(pyglet.gl.GL_QUADS)
    # batch_cert.draw()
    test_name.draw()
    # batch_quad.draw()
    eng_batch_text.draw()
    chi_batch_text.draw()
    # sign.draw(pyglet.gl.GL_QUADS)
    # wip.draw()
    # fps_display.draw()


@window.event
def update(dt):
    # global currentFrame
    # pyglet.image.get_buffer_manager().get_color_buffer().save(
    #     r'screenshots\{}\screenshot{}.png'.format(pgmStartTime, str(currentFrame).zfill(5)))
    # currentFrame += 1

    global createTime
    mt_update(chi_mt_list, dt)
    mt_update(eng_mt_list, dt)
    st_update(student_mt_list, dt)
    # if time() - createTime > randint(3, 8):
    # if time() - createTime > 2 and (len(chi_mt_list)+len(eng_mt_list)) < 10:
    if time() - createTime > 5 and any(empty):
        # if choice([True, False]):
        if random() > 0.33:
            chi_mt_list.append(createLine(
                chi_mt_list, chi_list, 5, 'chi'))
        else:
            eng_mt_list.append(createLine(
                eng_mt_list, eng_list, 500, 'eng'))
        createTime = time()

    if all(student_empty):
        for j in range(y_num):
            for i in range(x_num):
                student_mt_list.append(createStudent(students, i, j))

    # print(len(chi_mt_list), len(eng_mt_list), len(chi_mt_list) + len(eng_mt_list))


# pyglet.clock.schedule(update)
pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()

# for all in chi_mt_list:
#     print(all.text)
#     print('x', all.x, 'y', all.y, 'width',
#           all.content_width, 'height', all.content_height)
# for all in eng_mt_list:
#     print(all.text)
#     print(all.x, all.y, all.content_width, all.content_height)
# print(len(chi_mt_list), len(eng_mt_list))
