import pygame

class Paddle:
    def __init__(self, size=(50, 150), color=(200, 200, 200)):
        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()

        self.width, self.height = size
        self.x, self.y = 0, self.display_h // 2
        self.color = color

        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.speed = 175
        self.direction = 0

    def control(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            self.direction = -1
        elif key[pygame.K_s]:
            self.direction = 1
        else:
            self.direction = 0

    def check_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.display_h:
            self.rect.bottom = self.display_h

    def update(self, dt):
        self.control()
        self.check_collision()
        self.rect.y += round(self.direction * self.speed * dt)

    def render(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)


class AiPaddle(Paddle):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.rect.x = self.display_w - self.width

    def control(self):
        self.direction = 0