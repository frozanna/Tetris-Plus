import pygame
from variables import *

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH) / 2 - 100
first_elem_y = (SCREEN_HEIGHT - SURF_HEIGHT) - 40

elem_size = 25


shapes = [
    [
        [(0, 0, 0, 0),
         (0, 1, 1, 0),
         (0, 1, 1, 0),
         (0, 0, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (1, 1, 1, 1),
         (0, 0, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 1, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (0, 1, 1, 0),
         (1, 1, 0, 0),
         (0, 0, 0, 0), ],
        [(1, 0, 0, 0),
         (1, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (1, 1, 0, 0),
         (0, 1, 1, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (1, 1, 0, 0),
         (1, 0, 0, 0),
         (0, 0, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (1, 1, 1, 0),
         (1, 0, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 1, 1, 0),
         (0, 0, 0, 0), ],
        [(0, 0, 1, 0),
         (1, 1, 1, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0), ],
        [(1, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (1, 1, 1, 0),
         (0, 0, 1, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 1, 0),
         (0, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
        [(1, 0, 0, 0),
         (1, 1, 1, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (0, 1, 0, 0),
         (1, 1, 0, 0),
         (0, 0, 0, 0), ],
    ],
    [
        [(0, 0, 0, 0),
         (1, 1, 1, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (0, 1, 1, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (1, 1, 1, 0),
         (0, 0, 0, 0),
         (0, 0, 0, 0), ],
        [(0, 1, 0, 0),
         (1, 1, 0, 0),
         (0, 1, 0, 0),
         (0, 0, 0, 0), ],
    ],
]

shapes_colors = [pygame.image.load('images/aqua.png'), pygame.image.load('images/red.png'),
                 pygame.image.load('images/blue.png'), pygame.image.load('images/green.png'),
                 pygame.image.load('images/yellow.png'), pygame.image.load('images/magenta.png'),
                 pygame.image.load('images/orange.png')]

change_shape = pygame.image.load('images/p_change_shape.png')
next_shape = pygame.image.load('images/p_next_shape.png')
clean_all = pygame.image.load('images/p_clean_all.png')
minus_line = pygame.image.load('images/p_minus_line.png')
plus_line = pygame.image.load('images/p_plus_line.png')

powers = [change_shape, next_shape, clean_all, minus_line, plus_line]
