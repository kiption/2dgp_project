import game_framework
import pico2d

import intro_state

pico2d.open_canvas(800, 600)
game_framework.run(intro_state)
pico2d.close_canvas()