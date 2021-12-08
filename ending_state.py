import game_framework
from pico2d import *

import title_state

name = "EndingState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('ending.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if (logo_time > 2.0):
        logo_time = 0
        game_framework.quit()
    logo_time += game_framework.frame_time


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




