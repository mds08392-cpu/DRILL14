from pico2d import *


class Bird:
    image = None

    def __init__(self):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = 400, 300

    def update(self):
        pass

    def draw(self):
        # 우선 이미지가 제대로 불러와지는지 확인하기 위해 전체 시트를 그린다
        self.image.draw(self.x, self.y)
