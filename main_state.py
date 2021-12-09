import random
import json
import os

from pico2d import *
import game_framework
import game_world
import ending
from boy import Boy
from map import Map
from enemy import Enemy
from ball import Ball
from block import Block



name = "MainState"

import server
block = []




def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def enter():

    server.boy = Boy()
    game_world.add_object(server.boy, 1)


    server.map = Map()
    server.map.setting()
    game_world.add_object(server.map, 0)







def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(ending)
        else:
            server.boy.handle_event(event)


def update():
    bgm = load_music('Sound\\clear.mp3')
    bgm.set_volume(32)
    dgm = load_music('Sound\\enemy_die.mp3')
    dgm.set_volume(32)
    for game_object in game_world.all_objects():
        game_object.update()


    for b in server.map.blocks:
        if collide(b, server.boy):
            if b.data == '3':
                b1, b2, b3, b4 = server.boy.get_bb()  # 왼 아래 우 상
                b5, b6, b7, b8 = b.get_bb()  # 왼 아래 우 상
                if b1 < b5:
                    server.boy.setpos(b5 - b1, 0)
                elif b3 > b7:
                    server.boy.setpos(b7 - b3, 0)
                server.boy.setpos(0, b8 - b2)


            if b.data == 'X':
                bgm.play(1)
                game_framework.change_state(ending)
            if b.data == 'G':
                dgm.play()
                b.c = 1







def draw():

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






