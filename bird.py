from pico2d import *

import game_framework

# 맵 스케일: 1 pixel = 3 cm (boy.py 의 10 pixel = 30 cm 와 동일)
PIXEL_PER_METER = (10.0 / 0.3)

# 일반적인 새의 순항 속도 (작은 새 기준 약 30 km/h)
FLY_SPEED_KMPH = 30.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)


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
