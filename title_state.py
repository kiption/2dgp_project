import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None
button_image = None

def enter():
    global image, button_image
    image = load_image('title.png')
    button_image = load_image('start_button.png')


def exit():
    global image, button_image
    del(image)
    del(button_image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if 400 - 160 < event.x < 400 + 160 and 400 - 48 < event.y < 400 + 48:
                    game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    button_image.draw(400, 200)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






