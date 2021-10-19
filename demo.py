from pico2d import *

class block:
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
        self.gumba = load_image('리소스\\enemy1.png')


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
            self.gumba.draw(self.x, self.y, 40, 40)


    def setting(self, x, y, data):
        self.x, self.y = x, y
        self.data = data

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

            b =block()

            b.setting(w - 20, h - 40, a)
            self.blocks.append(b)
            w += 40

        bgdata.close()

class mario:
    def __init__(self):
        self.x, self.y = 120,110
        self.state = 'idle'
        self.img = load_image('리소스\\mario.png')
        self.dir = 0
        self.frame = 0
        self.d = 1
        self.w = 40
        self.h = 80
        self.running = True
        self.v = 7
        self.m =2
        self.j=0


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.type == SDL_QUIT:
                    self.running = False
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    self.running = False
                if event.key == SDLK_RIGHT:
                    self.d = 1
                    self.dir += 1
                    self.state = 'run'
                elif event.key == SDLK_LEFT:
                    self.state = 'run'
                    self.d = 0
                    self.dir -= 1
                elif event.key == SDLK_SPACE:
                    self.state = 'jump'
                    self.y += 50


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                elif event.key == SDLK_SPACE:
                    self.y-=50
                self.state = 'idle'


    def update(self):
        self.x += self.dir*5
        if self.state == 'run':
            self.frame = (self.frame+1) % 4
            delay(0.01)



    def draw(self):
        if(self.state == 'idle'):
            self.img.clip_draw(0, 90 * self.d, 40, 80, self.x, self.y)
        elif(self.state == 'run'):
            self.img.clip_draw(self.frame * 50, 90 * self.d, 40, 80, self.x, self.y, self.w, self.h)
        elif(self.state == 'jump'):
            self.img.clip_draw(200, 90 * self.d, 40, 80, self.x, self.y, self.w, self.h)


open_canvas(1280, 600)
Mario = mario()
Map = map()
Map.setting()


while Mario.running:

    clear_canvas()
    Mario.handle_events()
    Mario.update()
    Map.draw()
    Mario.draw()
    update_canvas()


close_canvas()