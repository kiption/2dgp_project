from pico2d import *


class Ground:
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
            if self.value == 'brown':
                self.image = load_image('ground_brown.png')
            elif self.value == 'blue':
                self.image = load_image('ground_blue.png')
            else:   # default
                self.image = load_image('ground_brown.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2