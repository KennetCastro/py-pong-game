import pygame
import time, sys
from paddle import Paddle, AiPaddle
from ball import Ball

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.player_1 = Paddle()
        self.player_2 = AiPaddle()
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