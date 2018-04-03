import pyglet
from pyglet import text, font
import time

alpha, step = 0, 1

window = pyglet.window.Window(width=1280, height=720)
arial = font.load('Times New Roman', 100)
label = text.Label('Hello World', font_name='Times New Roman', font_size=100,
                   x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
label.color = (255, 255, 255, alpha)
label2 = font.Text(arial, text='Hello World', x=window.width //
                   2, y=window.height//2+200, halign='center', valign='center')


@window.event
def on_draw():
    window.clear()
    label.draw()
    label2.draw()

@window.event
def update(dt):
    global alpha,step
    label.color = (255, 255, 255, alpha)
    alpha += step
    if alpha <= 0 or alpha >= 255:
        step *= -1

pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()


from pyglet.window import mouse
from pyglet import *
import pyglet

window = pyglet.window.Window(800, 600)
n = 0
label = pyglet.text.Label(str(n), x = window.width/2, y = window.width/2 )

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        global n
        n += 1
        label.text=str(n)

@window.event
def on_draw():
    window.clear()
    label.draw()

def update():
    pass

pyglet.app.run()
pyglet.clock.schedule_interval(update, 1/30.0)
