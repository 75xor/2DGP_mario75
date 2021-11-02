from pico2d import *
import obj

class mario:
    def __init__(self):
        self.x, self.y = 120,110
        self.state = 'idle'
        self.img = load_image('리소스\\mario.png')
        self.dir = 0
        self.frame = 0
        self.speed=1
        self.d = 1
        self.w = 40  #캐릭터 크기
        self.h = 80
        self.running = True #게임 러닝
        self.isjump = 0
        self.power = 10
        self.pd = 0 #power dir





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
                elif event.key == SDLK_LEFT:
                    self.d = 0
                    self.dir -= 1
                elif event.key == SDLK_SPACE:
                    self.isjump = 1
                    self.pd = 1

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                    self.speed = 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                    self.speed = 1

    def update(self):
        if self.speed < 10:
            self.speed += 0.2
        if self.isjump:
            if self.power < 20:
                self.power += 1
            if self.y >= 210:
                self.isjump = 0
        else:
            if self.y <= 110:
                self.y = 110
                self.pd = 0
            else:
                self.pd = -1

        self.x += self.dir * self.speed
        self.y += self.pd * self.power


        # if self.state == 'run':
        #     self.frame = (self.frame+1) % 4
        #     delay(0.01)
    def draw(self):
        if(self.state == 'idle'):
            self.img.clip_draw(0, 90 * self.d, 40, 80, self.x, self.y)






