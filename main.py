from pico2d import *
from mario import *
from map import *
import time

open_canvas(1280, 600)
Mario = mario()
current_time = time.time()
Map = map()
Map.setting()
while Mario.running:

    clear_canvas()
    Mario.handle_events()
    Mario.update()
    Map.draw()
    Mario.draw()
    update_canvas()


close_canvas()