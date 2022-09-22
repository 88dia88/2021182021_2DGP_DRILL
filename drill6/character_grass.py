from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character_Male.png')

time = 0
x = 0
y = 0

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)

    time = time + 1

    if time <= 300:
        x = time
    elif time <= 700:
        y = time - 300
    elif time <= 1300:
        x = 1000 - time
    elif time <= 1700:
        y = 1700 - time
    elif time <= 2000:
        x = time - 2000
    elif time <= 4000:
        x = math.sin(time / 2000 * 2 * math.pi) * 220
        y = math.cos(time / 2000 * 2 * math.pi) * 220
    else:
        time = 0
    
    if time <= 2000:
        character.draw_now(x + 400, y + 80)
    else:
        character.draw_now(-x + 400, -y + 300)

        

    
close_canvas()
