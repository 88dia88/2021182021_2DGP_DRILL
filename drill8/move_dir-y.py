from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            if event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

    pass


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
dir_y = 0
heading = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir < 0:
        heading = 0
    elif dir > 0:
        heading = 1
    elif dir_y != 0:
        if heading % 2 == 0:
            heading = 0
        else:
            heading = 1
    elif dir == 0:
        if heading % 2 == 0:
            heading = 2
        else:
            heading = 3
    character.clip_draw(frame * 100, 100 * (heading), 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x > TUK_WIDTH - 25:
        x -= 1
    elif x < 25:
        x += 1
    else:
        x += dir * 5

    if y > TUK_HEIGHT - 25:
        y -= 1
    elif y < 25:
        y += 1
    else:
        y += dir_y * 5

    delay(0.01)

close_canvas()