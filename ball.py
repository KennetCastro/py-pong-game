import pygame
import random

class Ball:
    def __init__(self, size=15, color=(200, 200, 200)):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()

        self.size = size
        self.x, self.y = self.display_w // 2, self.display_h // 2
        self.color = color

        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
        self.speed = 275
        self.direction = pygame.math.Vector2(-1, 1)

    def check_collision(self, padd1, padd2):
        # collision with the screen borders
        if self.rect.top <= 0:
            self.direction.y = 1
        elif self.rect.bottom >= self.display_h:
            self.direction.y = -1

        if self.rect.left <= -50:
            self.direction.x = 1
        elif self.rect.right >= self.display_w + 50:
            self.direction.x = -1 

        # collision with the left paddle
        if self.rect.colliderect(padd1):
            if abs(self.rect.top - padd1.bottom) < 10 and self.direction.y < 0:
                self.direction.y = 1
            elif abs(self.rect.bottom - padd1.top) < 10 and self.direction.y > 0:
                self.direction.y = -1
            if abs(self.rect.left - padd1.right) < 10 and self.direction.x < 0:
                self.direction.x = 1

        # collision with the right paddle
        if self.rect.colliderect(padd2):
            if abs(self.rect.top - padd2.bottom) < 10 and self.direction.y < 0:
                self.direction.y = 1
            elif abs(self.rect.bottom - padd2.top) < 10 and self.direction.y > 0:
                self.direction.y = -1
            if abs(self.rect.right - padd2.left) < 10 and self.direction.x > 0:
                self.direction.x = -1
    
    def update(self, dt, padd1, padd2):
        self.x = self.direction.x * self.speed * dt
        self.y = self.direction.y * self.speed * dt
        self.rect.centerx += round(self.x)
        self.rect.centery += round(self.y)
        self.check_collision(padd1, padd2)

    def render(self):
        pygame.draw.circle(self.display_surface, self.color, self.rect.center, self.size)