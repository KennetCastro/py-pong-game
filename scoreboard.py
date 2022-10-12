import pygame
import pygame.freetype
from settings import *

class Board:
    def __init__(self, name='freesansbold.ttf', size=32):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(name, size)
        

    def render(self, text, pos, color=DEFAULT_T['obj'], bgcolor=None):
        self.text_surface = self.font.render(text, False, color, bgcolor)
        self.rect = self.text_surface.get_rect(midtop=pos)
        self.display_surface.blit(self.text_surface, self.rect)
        