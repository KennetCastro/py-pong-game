import pygame
from settings import *

class Board:
    def __init__(self, text, name='freesansbold.ttf', size=32, color=DEFAULT_T['obj']):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()

        self.font = pygame.font.Font(name, size)
        self.color = color
        self.text_surface = self.font.render(
            text,
            False,
            self.color
        )
        self.rect = self.text_surface.get_rect()
        self.rect.x, self.rect.y = (self.display_surface.get_width()//2 - self.rect.width//2, 10)
        

    def render(self, text):
        self.text_surface = self.font.render(
            text,
            False,
            self.color
        )
        self.rect.x, self.rect.y = (self.display_surface.get_width()//2 - self.rect.width//2, 10)
        self.display_surface.blit(self.text_surface, self.rect)
        