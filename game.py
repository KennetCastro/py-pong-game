import pygame
import time, sys
from paddle import Paddle, AiPaddle
from ball import Ball
from settings import *

class Game:
    def __init__(self, multiplayer=False):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()

        self.player_1 = Paddle(size=PADD_SIZE, pos=(0, self.display_h//2))
        if multiplayer:
            self.player_2 = Paddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2),
                controll=SECOND_CONTROLL
            )
        else:
            self.player_2 = AiPaddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2)
            )
        self.ball = Ball()

        self.previus_time = time.time()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()
    
    def update(self, dt):
        self.player_1.update(dt)
        self.player_2.update(dt)
        self.ball.update(dt, self.player_1.rect, self.player_2.rect)

    def render(self):
        self.display_surface.fill((30, 30, 55))
        self.player_1.render()
        self.player_2.render()
        self.ball.render()

    def run(self):
        self.handle_events()
        self.get_deltatime()
        self.update(self.dt)
        self.render()