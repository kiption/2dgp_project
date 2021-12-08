from pico2d import *


class Background:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 800, 600

        self.image = load_image('background.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.imageWidth, self.imageHeight,
                             self.imageWidth/2 - int(self.scroll) % self.imageWidth, self.imageHeight/2)
        self.image.clip_draw(0, 0, int(self.scroll) % self.imageWidth, self.imageHeight,
                             self.imageWidth - int(self.scroll) % self.imageWidth / 2, self.imageHeight/2)


class Background2:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 800, 600

        self.image = load_image('blackbackground.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.imageWidth, self.imageHeight,
                             self.imageWidth/2 - int(self.scroll) % self.imageWidth, self.imageHeight/2)
        self.image.clip_draw(0, 0, int(self.scroll) % self.imageWidth, self.imageHeight,
                             self.imageWidth - int(self.scroll) % self.imageWidth / 2, self.imageHeight/2)