from pico2d import *

import game_framework

# 맵 스케일: 1 pixel = 3 cm (boy.py 의 10 pixel = 30 cm 와 동일)
PIXEL_PER_METER = (10.0 / 0.3)

# 일반적인 새의 순항 속도 (작은 새 기준 약 30 km/h)
FLY_SPEED_KMPH = 30.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# 날개짓 한 번에 나아가는 거리 (보폭). 작은 새는 초당 약 5회 날개짓 -> 8.33m/s / 5 = 약 1.67m
STRIDE_LENGTH_M = 1.67
# 시트의 한 줄(5프레임)이 날개짓 한 번
FRAMES_PER_STRIDE = 5
# 날개짓 한 번에 걸리는 시간 = 보폭 / 속도 (약 0.2초)
TIME_PER_STRIDE = STRIDE_LENGTH_M / FLY_SPEED_MPS
# 프레임당 재생시간 (약 0.04초)
TIME_PER_FRAME = TIME_PER_STRIDE / FRAMES_PER_STRIDE
# 초당 프레임 수 (약 25 FPS)
FRAMES_PER_SECOND = 1.0 / TIME_PER_FRAME


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
