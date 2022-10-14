import pygame
import time, sys
from scripts.paddle import Paddle, AiPaddle
from scripts.ball import Ball
from scripts.scoreboard import Board
from scripts.settings import *

class Game():
    def __init__(self, multiplayer=False, theme=DEFAULT_T, fun=None):
        pygame.mixer.pre_init(44100, -16, 2, 512)

        self.display_surface = pygame.display.get_surface()
        self.display_w, self.display_h = self.display_surface.get_size()
        self.clock = pygame.time.Clock()
        self.theme = theme 

        self.ball = Ball(color=self.theme["ball"])
        self.player_1 = Paddle(size=PADD_SIZE, pos=(0, self.display_h//2-PADD_SIZE[1]//2), color=self.theme["obj"])
        if multiplayer:
            self.player_2 = Paddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2-PADD_SIZE[1]//2),
                color=self.theme["obj"],
                controll=SECOND_CONTROLL
            )
        else:
            self.player_2 = AiPaddle(
                size=PADD_SIZE,
                pos=(self.display_w - PADD_SIZE[0], self.display_h//2-PADD_SIZE[1]//2),
                color=self.theme["obj"],
                target=self.ball
            )
        
        self.score = [0, 0]
        self.p1_score = Board(name="assets/ARCADECLASSIC.ttf")
        self.p2_score = Board(name="assets/ARCADECLASSIC.ttf")

        self.playing_time = 63
        self.previus_time = time.time()
        self.time_board = Board(name="assets/ARCADECLASSIC.ttf", size=40)
        self.fps = Board(name="assets/ARCADECLASSIC.ttf", size=16)

        self.running = True
        self.fun = fun


    def count_play_time(self):
        # playing couter
        self.actual_time = self.start_playing - time.perf_counter()
        self.time = self.playing_time + self.actual_time
        self.display_time = self.time if self.time < self.playing_time - 3 else 60
        if self.time <= 0:
            self.running = False
            self.fun(self.theme)


    def get_deltatime(self):
        self.dt = time.time() - self.previus_time
        self.previus_time = time.time()
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self, dt):
        self.player_1.update(dt)
        self.player_2.update(dt)
        self.ball.update(dt, self.player_1.rect, self.player_2.rect, self.score)


    def render(self):
        # clean screen
        self.display_surface.fill(self.theme["bg"])

        # middle line
        pygame.draw.line(
            self.display_surface,
            self.theme["obj"],
            (self.display_w//2, 0),
            (self.display_w//2, self.display_h),
            2
        )

        # show score
        self.p1_score.render(f'{self.score[0]}', pos=(self.display_w//2 - 30, self.display_h//2), color=self.theme["obj"])
        self.p2_score.render(f'{self.score[1]}', pos=(self.display_w//2 + 30, self.display_h//2), color=self.theme["obj"])
        self.time_board.render(f'{self.display_time: .0f}', pos=(self.display_w//2, 10), color=self.theme["ball"], bgcolor=self.theme["bg"])

        # show player and ball
        self.player_1.render()
        self.player_2.render()
        self.ball.render()


    def run(self):
        self.start_playing = time.perf_counter()
        while self.running:
            self.handle_events()
            self.get_deltatime()
            self.count_play_time()
            self.update(self.dt)
            self.render()
            self.fps.render(f'{self.clock.get_fps():.0f}', pos=(20, 10), color=self.theme["obj"])
            self.clock.tick(FPS)
            pygame.display.update()
        