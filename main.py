import pygame
import sys
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

        self.state = 'menu'
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def run(self):
        while True:
            self.handle_events()
            if self.state == 'menu':
                if self.menu.run():
                    self.state = 'multi'
            elif self.state == 'multi':
                if self.game.run():
                    self.state = 'menu'
            
            

            


if __name__ == '__main__':
    pong_game = Pong()
    pong_game.run()