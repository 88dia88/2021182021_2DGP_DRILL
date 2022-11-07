from pico2d import *
import game_world
import game_framework

# Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class FLY:
    def enter(self):
        print('ENTER FLY')

    def exit(self):
        print('EXIT RUN')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)
        if (self.x >= 1600 and self.dir > 0) or (self.x <= 0 and self.dir < 0):
            self.dir *= -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 184, 336 - (int(self.frame) // 5) * 168, 183, 168, 0, 'h', self.x, self.y, 25, 25)
        elif self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 184, 336 - (int(self.frame) // 5) * 168, 183, 168, 0, '', self.x, self.y, 25, 25)


class Bird:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
