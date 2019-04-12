import pygame
import sys
import random

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH) / 2
first_elem_y = (SCREEN_HEIGHT - SURF_HEIGHT) - 40

elem_size = 25

# Tablica bloczkow - nieskonczona
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

shapes_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (80, 60, 143), (255, 0, 255), (40, 17, 250),
                 (50, 100, 50)]  # Tu beda potem jakies grafiki


# klasa bloczku
class Brick(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = random.randint(0, len(shape) - 1)

    def draw_brick(self, game):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.shape[self.rotation][i][j]:
                    pygame.draw.rect(game.screen, self.color,
                                     (first_elem_x + (self.x + i) * elem_size, first_elem_y + (self.y + j) * elem_size, elem_size, elem_size))


class Grid(object):
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self, screen):
        frame = pygame.image.load("frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.game_grid[i][j] != 0:
                    pygame.draw.rect(screen, self.game_grid[i][j],
                                     (first_elem_x + i * elem_size, first_elem_y + j * elem_size, elem_size, elem_size))
                else:
                    screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))


class Game(object):
    def __init__(self):
        pygame.init()
        self.tps = 100.0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.grid = Grid()

    def draw_game(self):
        title_img = pygame.image.load("title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 95, 20))
        self.grid.draw_grid(self.screen)

    # def draw_game(self):
    #     empty_block = pygame.image.load("empty.png")
    #     for i in range(ROWS):
    #         for j in range(COLUMNS):
    #             if self.grid.game_grid[i][j] != 0:
    #                 pygame.draw.rect(self.screen, self.grid.game_grid[i][j],
    #                                  (first_elem_x + i * elem_size, first_elem_y + j * elem_size, elem_size, elem_size))
    #             else:
    #                 self.screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))
    #
    #     pygame.display.flip()

    def start_game(self):
        self.draw_game()

        brick = Brick(3, 0, random.choice(shapes))

        while True:
            self.draw_game()
            brick.draw_brick(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        sys.exit(0)
                    if keys[pygame.K_RIGHT]:
                        brick.x += 1
                        brick.draw_brick(self)
                    if keys[pygame.K_LEFT]:
                        brick.x -= 1
                        brick.draw_brick(self)
                    if keys[pygame.K_UP]:
                        brick.rotation = (brick.rotation + 1) % len(brick.shape)
                        brick.draw_brick(self)
                    if keys[pygame.K_DOWN]:
                        brick.y += 2
                        brick.draw_brick(self)
            pygame.display.flip()

Game().start_game()


# A to sie przyda do ustawiania czasu

# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps