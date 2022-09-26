from pico2d import *
open_canvas()
door = load_image('door_animation.png')

frame = 0
time = 0
while(time < 25):
    clear_canvas()
    #door.draw(400, 300)
    door.clip_draw(frame % 5 * 300, 800 - frame // 5 * 200, 300, 200, 400, 300)
    update_canvas()
    frame = (frame + 1) % 25
    time = time + 1
    delay(0.1)
    get_events()

close_canvas()
