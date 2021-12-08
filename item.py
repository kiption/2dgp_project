from pico2d import *
import game_framework
import game_world


class Coin:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 32, 32
        self.value = None
        self.timer = 300

    def update(self):
        if self.value == 'effect':
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.timer = 300
                game_world.remove_object(self)
        pass


    def draw(self):
        if self.image == None:
            self.image = load_image('coin.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2


class Transform:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 32, 32
        self.value = None

    def update(self):
        pass


    def draw(self):
        if self.image == None:
            if self.value == 'mush':
                self.image = load_image('item_mush.png')
            elif self.value == 'flower':
                self.image = load_image('item_flower.png')
            else:   # default
                self.image = load_image('item_mush.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2