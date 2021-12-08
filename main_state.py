import random
import json
import os

from pico2d import *
import game_framework
import game_world
import collision

from boy import Boy
from grass import Grass
from ball import Ball, BigBall

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []







def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)





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
    for game_object in game_world.all_objects():
        game_object.update()

    if collision.collide(boy, grass):
        boy.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






