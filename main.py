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

        self.menu = Menu(fun=self.play)
        self.state = self.menu

    def play(self, multi):
        self.state = Game(multiplayer=multi, fun=self.stop_play)

    def stop_play(self):
        self.state = Menu(fun=self.play)
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def run(self):
        while True:
            self.handle_events()
            self.state.run()
            
            
if __name__ == '__main__':
    pong_game = Pong()
    pong_game.run()