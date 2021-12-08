from pico2d import *


class BoxQuestion:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 32, 32
        self.value = None
        self.used = False
        self.item_value = 0

    def update(self):
        pass


    def draw(self):
        if self.image == None:
            if self.value == 'brown':
                self.image = load_image('box_q_brown.png')
            elif self.value == 'blue':
                self.image = load_image('box_q_blue.png')
            elif self.value == 'used':
                self.image = load_image('box_used.png')
            else:   # default
                self.image = load_image('box_q_brown.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2


class Brick:
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
                self.image = load_image('brick_brown.png')
            elif self.value == 'blue':
                self.image = load_image('brick_blue.png')
            else:   # default
                self.image = load_image('brick_brown.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2


class Pipe:
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
            if self.value == 'LT':
                self.image = load_image('pipe_left_top.png')
            elif self.value == 'LB':
                self.image = load_image('pipe_left_bottom.png')
            elif self.value == 'RT':
                self.image = load_image('pipe_right_top.png')
            elif self.value == 'RB':
                self.image = load_image('pipe_right_bottom.png')
            else:   # default
                self.image = load_image('pipe_left_top.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2


class BluePipe:
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
            if self.value == 'LT':
                self.image = load_image('pipe_blue_left_top.png')
            elif self.value == 'LB':
                self.image = load_image('pipe_blue_left_bottom.png')
            elif self.value == 'RT':
                self.image = load_image('pipe_blue_right_top.png')
            elif self.value == 'RB':
                self.image = load_image('pipe_blue_right_bottom.png')
            else:   # default
                self.image = load_image('pipe_blue_left_top.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2


class Flag:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.scroll = 0
        self.imageWidth, self.imageHeight = 32, 320
        self.value = None

    def update(self):
        pass

    def draw(self):
        if self.image == None:
            self.image = load_image('flag.png')

        self.image.draw(self.x - self.scroll, self.y)

        # 바운딩박스
        draw_rectangle(self.x - self.imageWidth / 2 - self.scroll, self.y - self.imageHeight / 2,
                       self.x + self.imageWidth / 2 - self.scroll, self.y + self.imageHeight / 2)

    def get_bb(self):
        return self.x - self.imageWidth/2 - self.scroll, self.y - self.imageHeight/2,\
               self.x + self.imageWidth/2 - self.scroll, self.y + self.imageHeight/2