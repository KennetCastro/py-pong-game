import pygame
import time, sys
from paddle import Paddle, AiPaddle
from ball import Ball
from scoreboard import Board
from settings import *

class Game():
    def __init__(self, multiplayer=False, theme=DEFAULT_T, fun=None):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
        self.clock = pygame.time.Clock()
        self.theme = theme 

        self.player_1 = Paddle(size=PADD_SIZE, pos=(0, self.display_h//2), color=self.theme["obj"])
        if multiplayer:
            self.player_2 = Paddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2),
                color=self.theme["obj"],
                controll=SECOND_CONTROLL
            )
        else:
            self.player_2 = AiPaddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2),
                color=self.theme["obj"]
            )
        self.ball = Ball(color=self.theme["obj"])
        
        self.score = [0, 0]
        self.p1_score = Board(name="ARCADECLASSIC.ttf")
        self.p2_score = Board(name="ARCADECLASSIC.ttf")

        self.playing_time = 30
        self.previus_time = time.time()
        self.time_board = Board(name="ARCADECLASSIC.ttf", size=40)

        self.fps = Board(name="ARCADECLASSIC.ttf", size=16)
        self.running = True

        self.fun = fun


    def count_play_time(self):
        self.actual_time = self.start_playing - time.perf_counter()
        self.time = self.playing_time + self.actual_time
        if self.time <= 0:
            self.running = False
            self.fun()


    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self, dt):
        self.player_1.update(dt)
        self.player_2.update(dt)
        self.ball.update(dt, self.player_1.rect, self.player_2.rect, self.score)


    def render(self):
        # clean screen
        self.display_surface.fill(self.theme["bg"])

        # show score
        self.p1_score.render(f'{self.score[0]}', pos=(self.display_w//2 - 30, self.display_h//2))
        self.p2_score.render(f'{self.score[1]}', pos=(self.display_w//2 + 30, self.display_h//2))
        self.time_board.render(f'{self.time: .0f}', pos=(self.display_w//2, 5))
        
        # middle line
        pygame.draw.line(
            self.display_surface,
            self.theme["obj"],
            (self.display_w//2, 0),
            (self.display_w//2, self.display_h),
            2
        )

        # show player and ball
        self.player_1.render()
        self.player_2.render()
        self.ball.render()


    def run(self):
        self.start_playing = time.perf_counter()
        while self.running:
            self.handle_events()
            self.get_deltatime()
            self.count_play_time()
            self.update(self.dt)
            self.render()
            self.fps.render(f'{self.clock.get_fps():.0f}', pos=(20, 10))
            self.clock.tick(FPS)
            pygame.display.update()
        