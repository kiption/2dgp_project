import game_framework
from pico2d import *
from ball import Ball
import collision
import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

gravity = 9.8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, JUMP_TIMER = range(7)

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

        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(0 * 32, 32*10, 32, 32, boy.x, boy.y)
        else:
            boy.image.clip_draw(0 * 32, 32*9, 32, 32, boy.x, boy.y)


class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
            boy.dir = 1
        elif event == LEFT_DOWN:
            boy.dir = -1
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.dir = 1
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.dir = -1
            boy.velocity += RUN_SPEED_PPS
        #boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        pass

    def do(boy):
        #boy.frame = (boy.frame + 1) % 8
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 32, 32*10, 32, 32, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 32, 32*9, 32, 32, boy.x, boy.y)


class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 32, 32*8, 32, 32, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 32, 32)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 32, 32*7, 32, 32, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 32, 32)

class JumpState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
            boy.dir = 1
        elif event == LEFT_DOWN:
            boy.dir = -1
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.dir = 1
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.dir = -1
            boy.velocity -= RUN_SPEED_PPS
        #boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        pass

    def do(boy):
        #print(boy.JumpAccel)
        boy.JumpAccel += game_framework.frame_time
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        boy.x += boy.velocity * game_framework.frame_time
        boy.y += (boy.JumpPPS + (-10.0) * boy.JumpAccel) * boy.JumpAccel
        boy.JumpDuring += 1
        boy.x = clamp(25, boy.x, 1600 - 25)
        if boy.JumpDuring >= 20.0:
            boy.JumpAccel = 0.0
            print('----', boy.JumpAccel)
            boy.add_event(JUMP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 32, 32*4, 32, 32, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 32, 32*3, 32, 32, boy.x, boy.y)

class FallingState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.dir = 1
        elif event == LEFT_DOWN:
            boy.dir = -1
        boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        pass

    def do(boy):
        boy.JumpAccel += game_framework.frame_time
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        boy.y += ((-10.0) * boy.JumpAccel) * boy.JumpAccel - 1
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.JumpDuring -= 1

        if boy.JumpDuring <= 0.0:
            boy.JumpDuring = 0.0
            boy.JumpAccel = 0.0
            #boy.add_event(JUMP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 32, 32*4, 32, 32, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 32, 32*3, 32, 32, boy.x, boy.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState, SPACE: JumpState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState, SPACE: JumpState},
    JumpState: {SPACE: JumpState, RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP_TIMER: FallingState},
    FallingState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState,
                   LEFT_DOWN: IdleState, SPACE: FallingState, JUMP_TIMER: IdleState}
}

class Boy:
    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('mario_growth.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.JumpPPS = RUN_SPEED_PPS
        self.JumpDuring = 0.0
        self.JumpAccel = 0.0
    def get_bb(self):
        return 0, 0, 0, 0

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        game_world.add_object(ball, 1)

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
        self.font.draw(self.x - 60, self.y + 50, str(self.cur_state), (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def stop(self):
        #self.add_event(JUMP_TIMER)
        pass
