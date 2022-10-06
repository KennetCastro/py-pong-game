import pygame
import time, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 480), flags=pygame.SCALED)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Pong!')
        self.previus_time = time.time()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()
    
    def update(self, dt):
        pygame.display.set_caption(f'Pong!  {self.clock.get_fps():.0f} fps')

    def render(self):
        self.screen.fill((30, 30, 55))

    def run(self):
        while True:
            self.handle_events()
            self.get_deltatime()
            self.update(self.dt)
            self.render()
            
            self.clock.tick(60)
            pygame.display.update()


if __name__ == '__main__':
    pong_game = Game()
    pong_game.run()