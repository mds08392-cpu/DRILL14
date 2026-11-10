import random

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


# 스프라이트 시트: 918x506, 5열 x 3행 (마지막 줄은 4프레임), 총 14프레임
SHEET_W, SHEET_H = 918, 506
SHEET_COLS, SHEET_ROWS = 5, 3
FRAME_W = SHEET_W // SHEET_COLS          # 183
FRAME_H = SHEET_H // SHEET_ROWS          # 168
TOTAL_FRAMES = 14


class Bird:
    image = None

    def __init__(self):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        # 랜덤 위치에서 시작 (하늘 영역: 풀밭 위쪽)
        half_w, half_h = FRAME_W / 2, FRAME_H / 2
        self.x = random.randint(int(half_w), int(get_canvas_width() - half_w))
        self.y = random.randint(int(150 + half_h), int(get_canvas_height() - half_h))
        self.frame = random.random() * TOTAL_FRAMES  # 새마다 날개짓 시작 시점을 다르게
        self.dir = random.choice((-1, 1))  # 1: 오른쪽, -1: 왼쪽

    def update(self):
        dt = game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_SECOND * dt) % TOTAL_FRAMES
        self.x += self.dir * FLY_SPEED_PPS * dt

        # 맵 끝에 닿으면 반대 방향으로 돌아선다
        half_w = FRAME_W / 2
        if self.x >= get_canvas_width() - half_w:
            self.x = get_canvas_width() - half_w
            self.dir = -1
        elif self.x <= half_w:
            self.x = half_w
            self.dir = 1

    def draw(self):
        index = int(self.frame)
        col = index % SHEET_COLS
        row = index // SHEET_COLS  # 위에서부터 몇 번째 줄인지
        left = col * FRAME_W
        bottom = SHEET_H - (row + 1) * FRAME_H
        # 시트 속 새는 오른쪽을 보고 있으므로 왼쪽으로 갈 때는 좌우 반전
        flip = '' if self.dir == 1 else 'h'
        self.image.clip_composite_draw(left, bottom, FRAME_W, FRAME_H,
                                       0, flip, self.x, self.y, FRAME_W, FRAME_H)
