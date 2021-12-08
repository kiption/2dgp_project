import random
import json
import os

from pico2d import *
import game_framework
import game_world

from collide import collide_check
from obj_maker import ObjType, make_obj
from scrolling import get_scroll

from boy import Boy
from background import Background

name = "Main3State"

boy = None
bg = None

import ending_state

def enter():
    global boy, bg

    bg = Background()
    bg.val = 1
    bg.scroll = 0

    boy = Boy()
    boy.y = 128
    game_world.add_object(boy, 1)

    # 맵 만들기
    # 1. 발판
    for j in range(0, 1+1):
        for i in range(0, 33):  # 맵길이 800
            make_obj(32*i, 32*j, ObjType.o_ground, 'brown')

    # 2. 박스
    make_obj(32 * 1, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 1, 32 * 3, ObjType.o_pipe, 'LT')
    make_obj(32 * 2, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 2, 32 * 3, ObjType.o_pipe, 'RT')

    make_obj(32 * 20, 32 * 6.5, ObjType.o_flag, None)


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
            game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    global bg

    bg.update()

    for game_object in game_world.all_objects():
        game_object.update()

    # 스크롤링
    bg.scroll = get_scroll(800, boy)

    for obj in game_world.all_objects():
        obj.scroll = get_scroll(800, boy)

    if boy.gameclear:
        game_framework.change_state(ending_state)


def draw():
    global bg

    clear_canvas()
    bg.draw()

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






