import random
import json
import os

from pico2d import *

import box
import game_framework
import game_world

from collide import collide_check
from obj_maker import ObjType, make_obj
from scrolling import get_scroll

from boy import Boy
from background import Background

import main2_state

name = "MainState"

boy = None
bg = None

map_trigger = False

def enter():
    global boy, bg

    bg = Background()
    bg.val = 0
    bg.scroll = 0

    boy = Boy()
    game_world.add_object(boy, 1)

    # 맵 만들기
    # 1. 발판
    for j in range(0, 1+1):
        for i in range(0, 71):
            make_obj(32*i, 32*j, ObjType.o_ground, 'brown')

        for i in range(74, 74+16):
            make_obj(32*i, 32*j, ObjType.o_ground, 'brown')

        for i in range(94, 94+56): # 156 x 32 = 4800 = 맵의 길이
            make_obj(32 * i, 32 * j, ObjType.o_ground, 'brown')

    # 2. 박스
    # 1)
    make_obj(32 * 10, 32 * 5, ObjType.o_box_q, 'brown')

    make_obj(32 * 15, 32 * 5, ObjType.o_box_q, 'brown')
    make_obj(32 * 16, 32 * 5, ObjType.o_brick, 'brown')
    make_obj(32 * 17, 32 * 5, ObjType.o_box_q, 'brown')

    make_obj(32 * 16, 32 * 9, ObjType.o_box_q, 'brown')

    make_obj(32 * 24, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 24, 32 * 3, ObjType.o_pipe, 'LT')
    make_obj(32 * 25, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 25, 32 * 3, ObjType.o_pipe, 'RT')

    make_obj(32 * 33, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 33, 32 * 3, ObjType.o_pipe, 'LT')
    make_obj(32 * 34, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 34, 32 * 3, ObjType.o_pipe, 'RT')

    make_obj(32 * 40, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 40, 32 * 3, ObjType.o_pipe, 'LB')
    make_obj(32 * 40, 32 * 4, ObjType.o_pipe, 'LT')
    make_obj(32 * 41, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 41, 32 * 3, ObjType.o_pipe, 'RB')
    make_obj(32 * 41, 32 * 4, ObjType.o_pipe, 'RT')

    for i in range(2, 4+1):
        make_obj(32 * 49, 32 * i, ObjType.o_pipe, 'LB')
        make_obj(32 * 50, 32 * i, ObjType.o_pipe, 'RB')
    make_obj(32 * 49, 32 * 5, ObjType.o_pipe, 'LT')
    make_obj(32 * 50, 32 * 5, ObjType.o_pipe, 'RT')

    make_obj(32 * 56, 32 * 5, ObjType.o_box_q, 'brown')

    for i in range(62, 66+1):
        make_obj(32 * i, 32 * 5, ObjType.o_brick, 'brown')
    make_obj(32 * 64, 32 * 9, ObjType.o_box_q, 'brown')

    # 2)
    make_obj(32 * 78, 32 * 5, ObjType.o_box_q, 'brown')

    make_obj(32 * 83, 32 * 5, ObjType.o_box_q, 'brown')
    make_obj(32 * 84, 32 * 5, ObjType.o_brick, 'brown')
    make_obj(32 * 85, 32 * 5, ObjType.o_box_q, 'brown')

    make_obj(32 * 84, 32 * 9, ObjType.o_brick, 'brown')

    # 3)
    make_obj(32 * 99, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 99, 32 * 3, ObjType.o_pipe, 'LT')
    make_obj(32 * 100, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 100, 32 * 3, ObjType.o_pipe, 'RT')

    make_obj(32 * 106, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 106, 32 * 3, ObjType.o_pipe, 'LB')
    make_obj(32 * 106, 32 * 4, ObjType.o_pipe, 'LT')
    make_obj(32 * 107, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 107, 32 * 3, ObjType.o_pipe, 'RB')
    make_obj(32 * 107, 32 * 4, ObjType.o_pipe, 'RT')

    for i in range(2, 4+1):
        make_obj(32 * 114, 32 * i, ObjType.o_pipe, 'LB')
        make_obj(32 * 115, 32 * i, ObjType.o_pipe, 'RB')
    make_obj(32 * 114, 32 * 5, ObjType.o_pipe, 'LT')
    make_obj(32 * 115, 32 * 5, ObjType.o_pipe, 'RT')

    for i in range(2, 5+1):
        make_obj(32 * 123, 32 * i, ObjType.o_pipe_b, 'LB')
        make_obj(32 * 124, 32 * i, ObjType.o_pipe_b, 'RB')
    make_obj(32 * 123, 32 * 6, ObjType.o_pipe_b, 'LT')
    make_obj(32 * 124, 32 * 6, ObjType.o_pipe_b, 'RT')


    # for i in range(0, 3):
    #     make_obj(128 + 32*i, 130, ObjType.o_ground, 'blue')


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if map_trigger:
                game_framework.change_state(main2_state)
        else:
            boy.handle_event(event)


def update():
    global bg, map_trigger

    bg.update()

    for game_object in game_world.all_objects():
        game_object.update()

    # 스크롤링
    bg.scroll = get_scroll(4800, boy)

    for obj in game_world.all_objects():
        obj.scroll = get_scroll(4800, boy)

    for o in game_world.all_objects():
        if o.__class__ == box.BluePipe:
            if o.value == 'LT' or o.value == 'RT':
                if collide_check(boy, o) == 'bottom':
                    map_trigger = True
                    break


def draw():
    global bg

    clear_canvas()
    bg.draw()

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






