import pygame
import time, sys
from game import Game

class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720), flags=pygame.SCALED)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pong!')

        self.game = Game()
    
    def run(self):
        while True:
            self.game.run()
            self.clock.tick(60)
            pygame.display.update()


if __name__ == '__main__':
    pong_game = Pong()
    pong_game.run()