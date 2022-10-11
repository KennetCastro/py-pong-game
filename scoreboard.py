import pygame
import pygame.freetype
from settings import *

class Board:
    def __init__(self, name='freesansbold.ttf', size=32, color=DEFAULT_T['obj']):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(name, size)
        self.color = color
        

    def render(self, text, pos):
        self.text_surface = self.font.render(text, False, self.color)
        self.rect = self.text_surface.get_rect(midtop=pos)
        self.display_surface.blit(self.text_surface, self.rect)
        