from block import *
from pico2d import *

class Map:
    def __init__(self):
        self.path = '리소스\\bg1.txt'
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.blocks = []


    def draw(self):
        for b in self.blocks:
            b.draw()


    def setting(self):
        self.w, h = 0, 610
        bgdata = open(self.path, 'r')
        i = bgdata.read()
        for a in i:
            if a == '\n':
                self.w = 0
                h -= 40
                continue
            else:
                b = Block()
                b.setting(self.w - 20, h - 40, a)
                self.blocks.append(b)
            self.w += 40
        bgdata.close()

    def update(self):
        if server.boy.x > 800 and server.boy.state == 1:
            for b in server.map.blocks:
                b.x -= 8
        if server.boy.x < 25and server.boy.state == 1:
            for b in server.map.blocks:
                b.x += 8


    def get_bb(self):
        for b in self.blocks:
            b.get_bb()

def main():

    s = Map()
    s.setting()
    while(1):
        clear_canvas()
        s.draw()
        update_canvas()





if __name__ == '__main__':
    main()
