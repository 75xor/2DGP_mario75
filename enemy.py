import game_framework
from pico2d import *
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 3.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Enemy:
    def __init__(self):
        self.x, self.y = 0,0
        self.path = '리소스\\bg1.txt'
        self.image = load_image('리소스\\enemy1.png')
        self.dir =0
        self.d=0
        self.enemys=[]

    def update(self):
        pass

    def draw(self):
        for b in self.enemys:
            b.image.draw(self.x, self.y)
            draw_rectangle(*self.get_bb())
    def get_bb(self):
       return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def initxy(self,x,y):
        self.x, self.y = x, y
    def setting(self):
        w, h = 0, 610
        bgdata = open(self.path, 'r')
        i = bgdata.read()
        for a in i:
            if a == '\n':
                w = 0
                h -= 40
                continue
            elif a == 'G':
                b = Enemy()
                b.initxy(w - 20, h - 40)
                self.enemys.append(b)
            w += 40
        bgdata.close()