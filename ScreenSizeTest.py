import pyglet
from pyglet import graphics, text, image, sprite
from pyglet.window import key as key
from time import time

display = pyglet.window.get_platform().get_default_display()
screens = display.get_screens()
# print(screens)
window = pyglet.window.Window(
    width=1920, height=1080, vsync=True, fullscreen=True, screen=screens[0])
window.set_caption('Projection Size Test')
fps_display = pyglet.window.FPSDisplay(window)
x, y, w, h = 0, 0, window.width, window.height//2


def create_quad_vertex_list(x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height


bk = 255
wh = 255
quad = pyglet.graphics.vertex_list(4,
                                   ('v2i', create_quad_vertex_list(x, y, w, h)),
                                   ('c3B', (bk, bk, bk, wh, wh, wh, wh, wh, wh, bk, bk, bk)))
# quad = batch_quad.add(4, pyglet.gl.GL_QUADS, None,
#                       ('v2i', create_quad_vertex_list(0, 0, 1920, 640)),
#                       ('c3B', (0, 0, 0, wh, wh, wh, wh, wh, wh, 0, 0, 0)))


@window.event
def on_key_press(symbol, modifiers):
    global x,y,w,h,quad
    if symbol == pyglet.window.key.ENTER:
        print('x:', x, 'y:', y, 'w:', w, 'h:', h)
    if symbol == key.UP:
        h+=1
    if symbol == key.DOWN:
        h-=1
    quad = pyglet.graphics.vertex_list(4,
                                       ('v2i', create_quad_vertex_list(x, y, w, h)),
                                       ('c3B', (bk, bk, bk, wh, wh, wh, wh, wh, wh, bk, bk, bk)))

@window.event
def on_draw():
    window.clear()
    # if preset == 1:
        # quad.draw(pyglet.gl.GL_QUADS)
    quad.draw(pyglet.gl.GL_QUADS)
    # batch_cert.draw()
    # test_name.draw()
    # # batch_quad.draw()
    # eng_batch_text.draw()
    # chi_batch_text.draw()
    fps_display.draw()
    # # item_count.draw()


# @window.event
def update(dt):
    return
    # global currentFrame
    # pyglet.image.get_buffer_manager().get_color_buffer().save(
    #     r'screenshots\{}\screenshot{}.png'.format(pgmStartTime, str(currentFrame).zfill(5)))
    # currentFrame += 1

    # global createTime
    # mt_update(chi_mt_list, dt)
    # mt_update(eng_mt_list, dt)
    # # if time() - createTime > randint(3, 8):
    # if time() - createTime > 1 and len(chi_mt_list)+len(eng_mt_list) < 15:
    #     if choice([True, False]):
    #         chi_mt_list.append(createLine(
    #             chi_mt_list, chi_list, 5, 'left', 'chi'))
    #     else:
    #         eng_mt_list.append(createLine(
    #             eng_mt_list, eng_list, 500, 'right', 'eng'))
    #     createTime = time()

    # global item
    # item = str(len(chi_mt_list), len(eng_mt_list), len(chi_mt_list) + len(eng_mt_list))


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
