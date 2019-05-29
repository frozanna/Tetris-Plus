import pygame

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH) / 2 - 100
first_elem_y = 80


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

shapes_colors = [pygame.image.load('images/aqua.jpg'),
                 pygame.image.load('images/red.jpg'),
                 pygame.image.load('images/blue.jpg'),
                 pygame.image.load('images/green.jpg'),
                 pygame.image.load('images/yellow.jpg'),
                 pygame.image.load('images/magenta.jpg'),
                 pygame.image.load('images/orange.jpg')]

change_shape = pygame.image.load('images/p_change_shape.jpg')
next_shape = pygame.image.load('images/p_next_shape.jpg')
clean_all = pygame.image.load('images/p_clean_all.jpg')
minus_line = pygame.image.load('images/p_minus_line.jpg')
plus_line = pygame.image.load('images/p_plus_line.jpg')

powers = [change_shape, next_shape, clean_all, minus_line, plus_line]
