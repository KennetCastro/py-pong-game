import pygame
import time, sys
from game import Game
from settings import *

class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), flags=pygame.SCALED)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(CAPTION)

        self.game = Game(multiplayer=True, clock=self.clock)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.handle_events()
            self.game.run()
            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    pong_game = Pong()
    pong_game.run()