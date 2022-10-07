import pygame
from settings import *
class Paddle:
    def __init__(self, size=(50, 80), pos=(0, 0), color=(200, 200, 200), controll=FIRST_CONTROLL):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
        self.controlls = controll

        self.width, self.height = size
        self.x, self.y = pos
        self.color = color

        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.speed = 275
        self.direction = 0

    def control(self):
        key = pygame.key.get_pressed()
        if key[self.controlls["up"]]:
            self.direction = -1
        elif key[self.controlls["down"]]:
            self.direction = 1
        else:
            self.direction = 0

    def check_collision(self):
        if self.rect.top <= 0 and self.direction < 0:
            self.rect.top = 0
            self.direction = 0
        if self.rect.bottom >= self.display_h and self.direction > 0:
            self.rect.bottom = self.display_h
            self.direction = 0

    def update(self, dt):
        self.control()
        self.y = self.direction * self.speed * dt
        self.rect.centery += round(self.y)
        self.check_collision()

    def render(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect, border_radius=8)


class AiPaddle(Paddle):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.rect.x = self.display_w - self.width

    def control(self):
        pass

    