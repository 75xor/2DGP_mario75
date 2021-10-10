import obj
from pico2d import *
class map:
    def __init__(self):
        self.path = '리소스\\bg1.txt'
        self.blocks = []

    def draw(self):
        for block in self.blocks:
            block.draw()


    def setting(self):
        w, h = 0, 610
        bgdata = open(self.path, 'r')
        i = bgdata.read()
        for a in i:
            if a == '\n':
                w = 0
                h -= 40
                continue

            b =obj.block()


            b.setting(w - 20, h - 40, a)
            self.blocks.append(b)
            w += 40

        bgdata.close()

def main():
    test = True
    open_canvas(1280, 600)
    bg1 = map()
    bg1.setting()
    while test:
        clear_canvas()
        bg1.draw()
        update_canvas()



if __name__ == '__main__':
    main()
