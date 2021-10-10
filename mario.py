from pico2d import *
import obj

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
                    if self.j == 0:
                        self.j = 1
                    elif self.j  == 1:
                        self.j =2
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                self.state = 'idle'


    def update(self):
        self.x += self.dir*5
        if self.state == 'run':
            self.frame = (self.frame+1) % 4
            delay(0.01)

        if self.state == 'jump':
            if self.j > 0:
                if self.j == 2:
                    self.v = 7

                # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
                if self.v > 0:

                    F = (0.5 * self.m * (self.v * self.v))
                else:

                    F = -(0.5 * self.m * (self.v * self.v))


                self.y -= round(F)


                self.v -= 1


                if self.y > 110:
                    self.y = 110
                    self.j = 0
                    self.state ='idle'
                    self.v = 7





    def draw(self):
        if(self.state == 'idle'):
            self.img.clip_draw(0, 90 * self.d, 40, 80, self.x, self.y)
        elif(self.state == 'run'):
            self.img.clip_draw(self.frame * 50, 90 * self.d, 40, 80, self.x, self.y, self.w, self.h)
        elif(self.state == 'jump'):
            self.img.clip_draw(200, 90 * self.d, 40, 80, self.x, self.y, self.w, self.h)





