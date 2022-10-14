import pygame.locals as pg_l

# general
SCREEN_W, SCREEN_H = 720, 480
CAPTION = "Pong!"
FPS = 60

# themes
DEFAULT_T = {"bg": (30, 30, 55), "obj": (200, 200, 200), "ball": (200, 200, 200)}
DARK_T = {"bg": (30, 30, 30), "obj": (200, 200, 200), "ball": (200, 200, 200)}
LIGHT_T = {"bg": (200, 200, 200), "obj": (30, 30, 30), "ball": (30, 30, 30)}
WATERMELON_T = {"bg": (205, 51, 46), "obj": (117,184,85), "ball": (30, 30, 30)}


# controlls
THEME_CONTROLL = {"default": pg_l.K_1, "dark": pg_l.K_2, "light": pg_l.K_3, "watermelon": pg_l.K_4}
FIRST_CONTROLL = {"up": pg_l.K_w, "down": pg_l.K_s}
SECOND_CONTROLL = {"up": pg_l.K_UP, "down": pg_l.K_DOWN}

# paddles
PADD_SIZE = (10, 110)
POS_1 = 0
POS_2 = SCREEN_W//2
