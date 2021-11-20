import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
PIXEL_PER_METER = (4.0 / 0.2)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer = 1000

    def exit(boy, event):
        if event == SPACE:
            boy.jump()

    def do(boy):
        pass


    def draw(boy):
        if boy.dir == 1:
            boy.img.clip_draw(0, 90, 40, 80, boy.x, boy.y, boy.w, boy.h)
        else:
            boy.img.clip_draw(0, 0, 40, 80, boy.x, boy.y, boy.w, boy.h)


class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        if event == SPACE:
            boy.isjump = 1

    def do(boy):
        #boy.frame = (boy.frame + 1) % 8
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        if boy.dir == 1:
            boy.img.clip_draw(int(boy.frame) * 50, 90, 40, 80, boy.x, boy.y, boy.w, boy.h)
        else:
            boy.img.clip_draw(int(boy.frame) * 50, 0, 40, 80, boy.x, boy.y, boy.w, boy.h)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}

}


class Boy:

    def __init__(self):
        self.x, self.y = 50, 110
        # Boy is only once created, so instance image loading is fine
        self.img = load_image('리소스\\mario.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.w = 40  # 캐릭터 크기
        self.h = 80
        self.frame = 0
        self.power = 10
        self.pd = 0  # power dir
        self.isjump=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
       return self.x-20,self.y-40,self.x+20,self.y+40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        if self.isjump:
            if self.power < 20:
                self.power += 1
            if self.y >= 210:
                self.isjump = 0
            if self.y <= 110:
                self.y = 110
                self.pd = 0
            else:
                self.pd = -1

        self.y += self.pd * self.power

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

