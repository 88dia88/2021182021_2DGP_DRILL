import random
import server

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

        pass

    def update(self):
        self.window_left = clamp(0,
                                 int(server.boy.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.boy.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)
        pass

    def handle_event(self, event):
        pass






class TileBackground:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800 * 3
        self.h = 600 * 3
        self.tiles = [[load_image('cube%d%d.png' % (x, y)) for x in range(3)] for y in range(3)]
        pass

    def update(self):
        pass

    def draw(self):
        self.window_left = clamp(0,
                                 int(server.boy.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.boy.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)
        tile_left = self.window_left // 800
        tile_right = (self.window_left + self.canvas_width) // 800
        left_offset = self.window_left % 800
        tile_bottom = self.window_bottom // 600
        tile_top = (self.window_bottom + self.canvas_height) // 600
        bottom_offset = self.window_bottom % 600
        for ty in range(tile_bottom, tile_top + 1):
            for tx in range(tile_left, tile_right + 1):
                self.tiles[ty][tx].draw_to_origin(-left_offset + (tx - tile_left) * 800,
                                                  -bottom_offset + (ty - tile_bottom) * 600)
        pass




