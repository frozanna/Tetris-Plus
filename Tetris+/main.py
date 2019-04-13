import pygame
import sys
import random

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH) / 2 - 100
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


shapes_colors = [pygame.image.load("red.png"), pygame.image.load("blue.png"), pygame.image.load("aqua.png"),
                 pygame.image.load("yellow.png"), pygame.image.load("magenta.png"), pygame.image.load("green.png"),
                 pygame.image.load("orange.png")]


class Brick:
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = random.randint(0, len(shape) - 1)


    def draw_brick(self, screen):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.shape[self.rotation][i][j]:
                    screen.blit(self.color, (first_elem_x + (self.x + j) * elem_size, first_elem_y + (self.y + i) * elem_size, elem_size, elem_size))

    def shape_without_whitespaces(self):
        curr_shape = self .shape[self.rotation]
        clear_shape = []
        for i, line in enumerate(curr_shape):
            row = list(line)
            for j, element in enumerate(row):
                if element == 1:
                    clear_shape.append((self.x + j, self.y + i))

        return clear_shape

    def shape_at_start(self):
        clear_shape = self.shape_without_whitespaces()
        must_put_up = True
        for pos in clear_shape:
            if pos[1] == 0:
                must_put_up = False
                break
        if must_put_up:
            self.y -= 1

class Grid:
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self, screen):
        frame = pygame.image.load("frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.game_grid[i][j] != 0:
                    screen.blit(self.game_grid[i][j], (first_elem_x + i * elem_size, first_elem_y + j * elem_size))

class Mechanics:
    def valid_space(shape, grid):
        ok_possitions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0] for i in range(ROWS)]
        ok_possitions = [j for sub in ok_possitions for j in sub]
        clear_shape = shape.shape_without_whitespaces()

        for pos in clear_shape:
            if pos not in ok_possitions:
                return False

        return True

    def check_rotation(shape,grid):
        ok_possitions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0] for i in range(ROWS)]
        ok_possitions = [j for sub in ok_possitions for j in sub]
        clear_shape = shape.shape_without_whitespaces()

        for pos in clear_shape:
            if pos not in ok_possitions:
                if pos[0] < 0:
                    shape.x += 1
                if pos[0] > 9:
                    shape.x -= 1
                if pos[1] < 0:
                    shape.y += 1
                if pos[1] > 19:
                    shape.y -= 1

class Game:
    def __init__(self):
        pygame.init()
        self.tps = 100.0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.grid = Grid()
        self.bricks = Brick(3, 0, random.choice(shapes))

    def draw_game(self):
        title_img = pygame.image.load("title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 190, 20))
        self.grid.draw_grid(self.screen)

    def start_game(self):
        self.draw_game()

        brick = Brick(3, 0, random.choice(shapes))
        brick.shape_at_start()


        while True:
            self.draw_game()
            brick.draw_brick(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    brick.rotation = (brick.rotation + 1) % len(brick.shape)
                    Mechanics.check_rotation(brick, self.grid.game_grid)
                    brick.draw_brick(self.screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
            if keys[pygame.K_RIGHT]:
                brick.x += 1
                if not Mechanics.valid_space(brick,self.grid.game_grid):
                    brick.x -= 1
                brick.draw_brick(self.screen)
            if keys[pygame.K_LEFT]:
                brick.x -= 1
                if not Mechanics.valid_space(brick,self.grid.game_grid):
                    brick.x += 1
                brick.draw_brick(self.screen)
            if keys[pygame.K_DOWN]:
                brick.y += 1
                if not Mechanics.valid_space(brick,self.grid.game_grid):
                    brick.y -= 1
                brick.draw_brick(self.screen)

            pygame.display.update()

Game().start_game()


# A to sie przyda do ustawiania czasu

# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps