import pygame
import sys
from states.menu import Menu
from states.game import Game
from scripts.scoreboard import Board
from scripts.settings import *
class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.icon = pygame.image.load('assets/pong.ico').convert()
        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(self.icon)

        self.menu = Menu(fun=self.play)
        self.state = self.menu

    def play(self, multi, theme):
        self.state = Game(theme=theme, multiplayer=multi, fun=self.stop_play)

    def stop_play(self, theme):
        self.state = Menu(theme=theme, fun=self.play)
    

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