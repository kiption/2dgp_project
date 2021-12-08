import random
import json
import os

from pico2d import *
import game_framework
import game_world

from collide import collide_check
from obj_maker import ObjType, make_obj
from scrolling import get_scroll

import box
from boy import Boy
from background import Background2

name = "Main2State"

boy = None
bg = None

map_trigger = False

import main3_state


def enter():
    global boy, bg

    bg = Background2()
    bg.val = 1
    bg.scroll = 0

    boy = Boy()
    game_world.add_object(boy, 1)

    # 맵 만들기
    # 1. 발판
    for j in range(0, 1+1):
        for i in range(0, 71):
            make_obj(32*i, 32*j, ObjType.o_ground, 'blue')

        for i in range(74, 74+16):  # 맵길이 2880
            make_obj(32*i, 32*j, ObjType.o_ground, 'blue')

    # 2. 박스
    # 1)
    for i in range(10, 15+1):
        make_obj(32 * i, 32 * 5, ObjType.o_brick, 'blue')

    for i in range(2, 9+1):
        make_obj(32 * 15, 32 * i, ObjType.o_brick, 'blue')

    make_obj(32 * 16, 32 * 7, ObjType.o_brick, 'blue')
    make_obj(32 * 17, 32 * 7, ObjType.o_brick, 'blue')
    make_obj(32 * 18, 32 * 7, ObjType.o_brick, 'blue')
    for i in range(2, 11+1):
        make_obj(32 * 19, 32 * i, ObjType.o_brick, 'blue')

    make_obj(32 * 25, 32 * 5, ObjType.o_box_q, 'blue')
    make_obj(32 * 26, 32 * 5, ObjType.o_brick, 'blue')
    make_obj(32 * 27, 32 * 5, ObjType.o_box_q, 'blue')

    make_obj(32 * 26, 32 * 9, ObjType.o_box_q, 'blue')

    make_obj(32 * 33, 32 * 2, ObjType.o_pipe_b, 'LB')
    make_obj(32 * 33, 32 * 3, ObjType.o_pipe_b, 'LT')
    make_obj(32 * 34, 32 * 2, ObjType.o_pipe_b, 'RB')
    make_obj(32 * 34, 32 * 3, ObjType.o_pipe_b, 'RT')

    make_obj(32 * 40, 32 * 2, ObjType.o_pipe_b, 'LB')
    make_obj(32 * 40, 32 * 3, ObjType.o_pipe_b, 'LB')
    make_obj(32 * 40, 32 * 4, ObjType.o_pipe_b, 'LT')
    make_obj(32 * 41, 32 * 2, ObjType.o_pipe_b, 'RB')
    make_obj(32 * 41, 32 * 3, ObjType.o_pipe_b, 'RB')
    make_obj(32 * 41, 32 * 4, ObjType.o_pipe_b, 'RT')

    for i in range(2, 4+1):
        make_obj(32 * 49, 32 * i, ObjType.o_pipe_b, 'LB')
        make_obj(32 * 50, 32 * i, ObjType.o_pipe_b, 'RB')
    make_obj(32 * 49, 32 * 5, ObjType.o_pipe_b, 'LT')
    make_obj(32 * 50, 32 * 5, ObjType.o_pipe_b, 'RT')

    make_obj(32 * 56, 32 * 5, ObjType.o_box_q, 'blue')

    for i in range(62, 66+1):
        make_obj(32 * i, 32 * 5, ObjType.o_brick, 'blue')
    make_obj(32 * 64, 32 * 9, ObjType.o_box_q, 'blue')

    # 2)
    make_obj(32 * 78, 32 * 5, ObjType.o_box_q, 'blue')

    make_obj(32 * 83, 32 * 2, ObjType.o_pipe, 'LB')
    make_obj(32 * 83, 32 * 3, ObjType.o_pipe, 'LT')
    make_obj(32 * 84, 32 * 2, ObjType.o_pipe, 'RB')
    make_obj(32 * 84, 32 * 3, ObjType.o_pipe, 'RT')


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
                game_framework.change_state(main3_state)
        else:
            boy.handle_event(event)


def update():
    global bg, map_trigger

    bg.update()

    for game_object in game_world.all_objects():
        game_object.update()

    # 스크롤링
    bg.scroll = get_scroll(2880, boy)

    for obj in game_world.all_objects():
        obj.scroll = get_scroll(2880, boy)

    for o in game_world.all_objects():
        if o.__class__ == box.Pipe:
            if o.value == 'LT' or o.value == 'RT':
                if collide_check(boy, o) == 'bottom':
                    print('a')
                    map_trigger = True
                    break


def draw():
    global bg

    clear_canvas()
    bg.draw()

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






