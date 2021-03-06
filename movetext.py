from pyglet import text, font
from time import time
from noise import snoise2
from random import randrange
import os.path

font.add_file(os.path.join('font', 'DFHsiuW3.ttc'))
font.add_file(os.path.join('font', 'DFErW3.ttc'))
font.add_file(os.path.join('font', 'MLingWaiFHK-Light.otf'))
font.add_file(os.path.join('font', 'AdobeFanHeitiStdB.otf'))
font.add_file(os.path.join('font', 'AdobeFangsongStdR.otf'))
font.add_file(os.path.join('font', 'NotoSansCJKtc-Bold.otf'))
font.add_file(os.path.join('font', 'NotoSansCJKtc-Black.otf'))
font.add_file(os.path.join('font', 'NotoSansCJKtc-Light.otf'))
font.add_file(os.path.join('font', 'NotoSansCJKtc-Thin.otf'))
font.add_file(os.path.join('font', 'AdobeKaitiStd-Regular.otf'))


def map_range(OldValue, OldMin, OldMax, NewMin, NewMax):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin


class MoveText(text.Label):

    def __init__(self, text='', font_name=None, font_size=None, bold=False, italic=False, color=None, x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='center', align='left', multiline=False, dpi=None, batch=None, group=None, index=None, hold_time=None):
        super().__init__(text, font_name, font_size, bold, italic, color, x, y,
                         width, height, anchor_x, anchor_y, align, multiline, dpi, batch, group)

        self.color = (255, 255, 255, 0) if not color else color
        self.multiline = True if width else False
        font_size *= 1

        self.alpha = 1
        self.scale = 0
        self.time = time()
        self.n = 0
        self.index = index
        self.fade_mode = 1  # 1: fade-in | 0: hold | -1: fade-out
        self.hold_time = randrange(10, 20) if not hold_time else hold_time # hold time
        self.end = False
        self.align = align

    def update(self, dt):
        self.fade()
        # self.color = (self.color[0], self.color[1],
        #               self.color[2], int(map_range(snoise2(self.index, self.n), -1, 1, 0.5, 1) * self.scale))
        # self.n += 0.001
        self.color = (self.color[0], self.color[1],
                      self.color[2], self.scale)
        if self.align == 'left':
            self.x += 0
        elif self.align == 'right':
            self.x -= 1

    def fade(self):
        if self.fade_mode == 1:
            self.scale += 5
            self.font_size += 0.0
            if self.scale >= 255:
                self.time = time()
                self.fade_mode = 0
        if self.fade_mode == 0:
            self.font_size += 0.0
        if self.fade_mode == 0 and time()-self.time > self.hold_time:
            self.fade_mode = -1
        if self.fade_mode == -1:
            self.scale -= 5
            self.font_size += 0.0
            if self.scale <= 0:
                self.end = True
