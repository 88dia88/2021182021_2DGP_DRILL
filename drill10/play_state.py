from pico2d import *
import game_framework
import title_state
import item_state
import character_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1  # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.item = 'BigBall'
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1  # 왼쪽
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):

        if self.dir > 0:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        elif self.dir < 0:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10 * self.dir, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10 * self.dir, self.y + 50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(character_state)


boy = None
boys = None
grass = None
running = None


def enter():
    global boy, boys, grass, running
    boy = Boy()
    boys = [boy]
    grass = Grass()
    running = True


def exit():
    global boy, boys, grass
    del boy
    del boys
    del grass


def update():
    for BoyGang in boys:
        BoyGang.update()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for BoyGang in boys:
        BoyGang.draw()


def pause():
    pass


def resume():
    pass
