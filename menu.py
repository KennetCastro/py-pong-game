import pygame
import time, sys
from scoreboard import Board
from settings import *

class Menu():
    def __init__(self, theme=DEFAULT_T):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
        self.clock = pygame.time.Clock()
        self.theme = theme

        self.title = Board(name="ARCADECLASSIC.ttf", size=100)

        self.previus_time = time.time()
        self.fps = Board(name="ARCADECLASSIC.ttf", size=16)

        self.next = True
        self.running = True


    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()


    def control(self):
        key = pygame.key.get_pressed()
        if key[FIRST_CONTROLL["up"]]:
            self.theme["bg"] = (55, 30, 30)
        elif key[FIRST_CONTROLL["down"]]:
            self.theme["bg"] = (30, 55, 30)
        else:
            self.theme["bg"] = (30, 30, 55)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        self.control()


    def render(self):
        self.display_surface.fill(self.theme["bg"])
        self.title.render('PONG!', (self.display_w//2, self.display_h//8))


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.fps.render(f'{self.clock.get_fps():.0f}', pos=(20, 10))
            self.clock.tick(FPS)
            pygame.display.update()