import pygame
import time, sys
from paddle import Paddle, AiPaddle
from ball import Ball
from scoreboard import Board
from settings import *

class Game:
    def __init__(self, multiplayer=False, theme=DEFAULT_T):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
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

        self.previus_time = time.time()


    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()
    

    def update(self, dt):
        self.player_1.update(dt)
        self.player_2.update(dt)
        self.ball.update(dt, self.player_1.rect, self.player_2.rect, self.score)


    def render(self):
        # clean screen
        self.display_surface.fill(self.theme["bg"])

        # show score
        self.p1_score.render(f'{self.score[0]}', pos=(self.display_w//2 - 25, self.display_h//2))
        self.p2_score.render(f'{self.score[1]}', pos=(self.display_w//2 + 25, self.display_h//2))
        
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
        self.get_deltatime()
        self.update(self.dt)
        self.render()
