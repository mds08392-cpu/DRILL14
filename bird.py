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
        # 시트는 5열 x 3행(918x506), 첫 번째 프레임만 잘라서 그린다 (애니메이션은 이후 작업)
        self.image.clip_draw(0, 506 - 168, 183, 168, self.x, self.y)
