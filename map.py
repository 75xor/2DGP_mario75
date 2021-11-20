from block import *
from pico2d import *
class Map:
    def __init__(self):
        self.path = '리소스\\bg1.txt'
        self.blocks = []

    def draw(self):
        for b in self.blocks:
            b.draw()

    def setting(self):
        w, h = 0, 610
        bgdata = open(self.path, 'r')
        i = bgdata.read()
        for a in i:
            if a == '\n':
                w = 0
                h -= 40
                continue
            else:
                b = Block()
                b.setting(w - 20, h - 40, a)
                self.blocks.append(b)
            w += 40
        bgdata.close()

    def update(self):
        pass
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
