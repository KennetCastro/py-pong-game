import pygame
import time, sys
from game import Game
from scoreboard import Board
from settings import *

class Menu:
    def __init__(self, theme=DEFAULT_T, fun=None):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
        self.clock = pygame.time.Clock()
        self.theme = theme

        self.title = Board(name="ARCADECLASSIC.ttf", size=100)

        self.previus_time = time.time()
        self.fps = Board(name="ARCADECLASSIC.ttf", size=16)

        self.next = True
        self.running = True

        self.fun = fun



    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()


    def control(self):
        key = pygame.key.get_pressed()
        if key[THEME_CONTROLL["default"]]:
            self.theme = DEFAULT_T
        if key[THEME_CONTROLL["dark"]]:
            self.theme = DARK_T
        if key[THEME_CONTROLL["light"]]:
            self.theme = LIGHT_T
        if key[THEME_CONTROLL["watermelon"]]:
            self.theme = WATERMELON_T
        

        if key[pygame.K_m]:
            self.running = False
            self.fun(True, self.theme)
        if key[pygame.K_n]:
            self.running = False
            self.fun(False, self.theme)
        if key[pygame.K_b]:
            self.theme = DARK_T


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        pass


    def render(self):
        self.display_surface.fill(self.theme["bg"])
        self.title.render('PONG!', (self.display_w//2, self.display_h//8), self.theme["obj"])


    def run(self):
        while self.running:
            self.handle_events()
            self.control()
            self.update()
            self.render()
            self.fps.render(f'{self.clock.get_fps():.0f}', pos=(20, 10), color=self.theme["obj"])
            self.clock.tick(FPS)
            pygame.display.update()
