import pygame.locals as pg_l
# general
SCREEN_W, SCREEN_H = 720, 480
CAPTION = "Pong!"
FPS = 60

# themes
DEFAULT_T = {"bg": (30, 30, 55), "obj": (200, 200, 200)}

# controlls
FIRST_CONTROLL = {"up": pg_l.K_w, "down": pg_l.K_s}
SECOND_CONTROLL = {"up": pg_l.K_UP, "down": pg_l.K_DOWN}

# paddles
PADD_SIZE = (20, 100)
POS_1 = 0
POS_2 = SCREEN_W//2
