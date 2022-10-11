import pygame
from menu import Menu
from game import Game
from scoreboard import Board
from settings import *

class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), flags=pygame.SCALED)
        pygame.display.set_caption(CAPTION)

        self.menu = Menu()
        self.game = Game(multiplayer=True)
    

    def run(self):
        self.menu.run()
        #self.game.run()


if __name__ == '__main__':
    pong_game = Pong()
    pong_game.run()