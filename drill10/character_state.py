import game_framework
import play_state
from pico2d import *

running = True
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass


def exit():
    global image
    del image
    pass


def update():
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            # match event.key:
            #     case pico2d.SDLK_ESCAPE:
            #         game_framework.pop_state()
            #     case pico2d.SDLK_EQUALS:
            #         play_state.boy.count += 1
            #         game_framework.pop_state()
            #     case pico2d.SDLK_MINUS:
            #         if play_state.boy.count > 1:
            #             play_state.boy.count -= 1
            #             game_framework.pop_state()

            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_EQUALS:
                    play_state.boys.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if len(play_state.boys) > 1:
                        play_state.boys.remove(play_state.boys[-1])
                        game_framework.pop_state()
