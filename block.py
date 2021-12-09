from pico2d import *
from main_state import *
import game_world
import game_framework
import random
import server
import collide
class Block:
    def __init__(self):
        self.block0 = load_image('리소스\\block0.png')
        self.block1 = load_image('리소스\\block1.png')
        self.block2 = load_image('리소스\\block2.png')
        self.block3 = load_image('리소스\\block3.png')
        self.block4 = load_image('리소스\\block4.png')
        self.blockA = load_image('리소스\\blockA.png')
        self.blockB = load_image('리소스\\blockB.png')
        self.blockC = load_image('리소스\\blockC.png')
        self.blockD = load_image('리소스\\blockD.png')
        self.Qblock = load_image('리소스\\Qblock.png')
        self.Gumba = load_image('리소스\\enemy1.png')
        self.box = load_image('리소스\\box.png')
        self.c=0
        self.x, self.y = 0, 0
        self.data = '0'

    def draw(self):
        if self.data == '0':
            self.block0.draw(self.x, self.y, 40, 40)
        elif self.data == '1':
            self.block1.draw(self.x, self.y, 40, 40)
        elif self.data == '2':
            self.block2.draw(self.x, self.y, 40, 40)
        elif self.data == '3':
            self.block3.draw(self.x, self.y, 40, 40)
        elif self.data == '4':
            self.block4.draw(self.x, self.y, 40, 40)
        elif self.data == 'A':
            self.blockA.draw(self.x, self.y, 40, 40)
        elif self.data == 'B':
            self.blockB.draw(self.x, self.y, 40, 40)
        elif self.data == 'C':
            self.blockC.draw(self.x, self.y, 40, 40)
        elif self.data == 'D':
            self.blockD.draw(self.x, self.y, 40, 40)
        elif self.data == 'Q':
            self.Qblock.draw(self.x, self.y, 40, 40)
        elif self.data == 'G':
            if self.c ==1:
                self.block0.draw(self.x, self.y, 40, 40)
            else:
                self.Gumba.draw(self.x, self.y, 40, 40)
        elif self.data == 'X':
            self.box.draw(self.x, self.y, 40, 40)


    def setting(self, x, y,data):
        self.x, self.y = x, y
        self.data = data
    def get_bb(self):
        if self.data == '0':
            return 0, 0, 0, 0
        else:
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        pass




