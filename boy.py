import game_framework
from pico2d import *
from ball import Ball

import game_world
import server
import collide
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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE,JUMP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_a): JUMP
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
        elif event == JUMP:
            boy.jump += 1
        boy.timer = 1000
        boy.state =0

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()


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
        elif event == JUMP:
            boy.jump += 1
        boy.dir = clamp(-1, boy.velocity, 1)
        boy.state = 1

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()


    def do(boy):
        #boy.frame = (boy.frame + 1) % 8
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(20, boy.x, 810)

    def draw(boy):
        if boy.dir == 1:
            boy.img.clip_draw(int(boy.frame) * 50, 90, 40, 80, boy.x, boy.y, boy.w, boy.h)
        else:
            boy.img.clip_draw(int(boy.frame) * 50, 0, 40, 80, boy.x, boy.y, boy.w, boy.h)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,SPACE:IdleState,JUMP:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,SPACE:RunState,JUMP:RunState}

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
        self.jump = 0  # jump 를 했나, 안했나 판단.
        self.i = 100  # jump 의 i 상수
        self.jumpPoint = self.y  # jump 를 하는 위치
        self.highPoint = 200  # jump 높이
        self.state = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.hit_bgm = load_music('Sound\\fire_ball.mp3')
        self.hit_bgm.set_volume(32)
        self.bgm = load_music('Sound\\main_bgm.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()




    def get_bb(self):
       return self.x-20,self.y-40,self.x+20,self.y+40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        t = self.i / 100
        self.y = (2 * t ** 2 - 3 * t + 1) * self.jumpPoint + (-4 * t ** 2 + 4 * t) * (
                    self.jumpPoint + self.highPoint) + (2 * t ** 2 - t) * self.jumpPoint
        if self.jump == 0:
            self.i = 0
        else:
            self.i += 0.7

        if self.y < 110:
            self.y = 110
            self.jump=0

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def setpos(self, x, y):
        self.x += x
        self.y += y


    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        server.ball = Ball(self.x,self.y,self.dir*20)
        self.bgm.pause()
        self.hit_bgm.play()
        game_world.add_object(server.ball,1)
        self.bgm.resume()



