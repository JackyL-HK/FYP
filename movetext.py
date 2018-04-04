from pyglet import text, font
from time import time
from noise import snoise2
from random import randrange


def map_range(OldValue, OldMin, OldMax, NewMin, NewMax):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin


class MoveText(text.Label):

    def __init__(self, text='', font_name=None, font_size=None, bold=False, italic=False, color=None, x=0, y=0, width=5, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=True, dpi=None, batch=None, group=None):
        super().__init__(text, font_name, font_size, bold, italic, color, x, y,
                         width, height, anchor_x, anchor_y, align, multiline, dpi, batch, group)
        self.alpha = 1
        self.scale = 0
        self.time = time()
        self.n = 0
        self.index = randrange(100000)
        self.fade_mode = 1  # 1: fade-in | 0: hold | -1: fade-out
        self.hold_time = 10  # hold time
        self.end = False

        self.color = (255, 0, 0, 255) if not color else color
        self.color = (self.color[0], self.color[1], self.color[2], 0)

    def update(self):
        self.fade()
        self.color = (self.color[0], self.color[1],
                      self.color[2], int(map_range(snoise2(self.index, self.n), -1, 1, 0.5, 1) * self.scale))
        self.n += 0.001

    def fade(self):
        if self.fade_mode == 1:
            self.scale += 5
            if self.scale >= 255:
                self.time = time()
                self.fade_mode = 0
        if self.fade_mode == 0 and time()-self.time > self.hold_time:
            self.fade_mode = -1
        if self.fade_mode == -1:
            self.scale -= 5
            if self.scale <= 0:
                self.end = True
