from pico2d import *
import map

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_UP, SPACE_DOWN = range(6)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
(SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
(SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
(SDL_KEYUP, SDLK_LEFT): LEFT_UP,
(SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
(SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        # boy.timer = 100
    def exit(boy, event):
         pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    def draw(boy):
        if boy.velocity == 1:
            boy.img.clip_draw(0, 90, 40, 80, boy.x, boy.y, boy.w, boy.h)
        else:
            boy.img.clip_draw(0, 0, 40, 80, boy.x, boy.y, boy.w, boy.h)




class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
    def draw(boy):
        if boy.velocity == 1:
            boy.img.clip_draw(boy.frame * 50, 90, 40, 80, boy.x, boy.y, boy.w, boy.h)
        else:
            boy.img.clip_draw(boy.frame * 50, 0, 40, 80, boy.x, boy.y, boy.w, boy.h)
next_state_table = {

IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
},

RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
}

}
class mario:
    def __init__(self):
        self.x, self.y = 120, 110
        self.state = 'idle'
        self.img = load_image('리소스\\mario.png')
        self.dir = 1
        self.frame = 0
        self.velocity = 0
        self.acceleration = 0
        self.speed=1
        self.d = 1
        self.w = 40  #캐릭터 크기
        self.h = 80
        self.running = True #게임 러닝
        self.isjump = 0
        self.power = 10
        self.event_que = []
        self.timer = 0
        self.pd = 0 #power dir
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self, state):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_events(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        events = get_events()
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.type == SDL_QUIT:
                    self.running = False
                elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
                    self.running = False







