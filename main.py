import pygame
import time, sys
from paddle import Paddle, AiPaddle
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720), flags=pygame.SCALED)
        self.clock = pygame.time.Clock()

        self.player_1 = Paddle()
        self.ai_player = AiPaddle()

        self.ball = Ball()

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
        self.player_1.update(dt)
        self.ai_player.update(dt)
        self.ball.update(dt, self.player_1.rect, self.ai_player.rect)

    def render(self):
        self.screen.fill((30, 30, 55))
        self.player_1.render()
        self.ai_player.render()
        self.ball.render()

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