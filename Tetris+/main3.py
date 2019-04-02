# To robi jakies dziwne rzeczy i tworzy wielki kwadrat 4x4 nie wiem czemu - trzeba jakos poprawic, bo ogolnie pomysl z tymi 
S, Z itd wydaje mi sie fajny, bo sa od razu wszystkie rotacje i tylko mozna zmieniac pola w tablicy 

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

S = [['....',
      '.11.',
      '11..',
      '....'],
     ['....',
      '.1..',
      '.11.',
      '..1.']]

Z = [['....',
      '.11.',
      '..11',
      '....'],
     ['....',
      '..1.',
      '.11.',
      '.1..']]

I = [['....',
      '1111',
      '....',
      '....'],
     ['.1..',
      '.1..',
      '.1..',
      '.1..']]

O = [['....',
      '.11.',
      '.11.',
      '....']]

T = [['....',
      '.111',
      '..1.',
      '....'],
     ['....',
      '..1.',
      '.11.',
      '..1.'],
     ['....',
      '..1.',
      '.111',
      '....'],
     ['....',
      '..1.',
      '..11',
      '..1.']]

L = [['.1..',
      '.1..',
      '.11.',
      '....'],
     ['....',
      '.111',
      '.1..',
      '....'],
     ['.11.',
      '..1.',
      '..1.',
      '....'],
     ['....',
      '...1',
      '.111',
      '....']]

J = [['..1..',
      '..1..',
      '.11.',
      '....'],
     ['....',
      '.1..',
      '.111',
      '....'],
     ['..11.',
      '..1.',
      '..1.',
      '....'],
     ['....',
      '.111',
      '...1',
      '....']]

shapes = [S, Z, I, O, T, L, J]
shape_colors = [(237, 28, 28), (28, 91, 237), (239, 123, 21), (178, 20, 226), (90, 186, 13),
                (13, 177, 186), (224, 71, 186)]  # Tu beda potem jakies grafiki


# klasa bloczku
class Brick(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = random.randint(0, len(shape) - 1)

    def get_shape(self):
        return Brick(3, 0, random.choice(shapes))

#niepotrzebne, bo wpisuje do grida, a my chcemy inaczej

    def draw_brick(self, game):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.shape[self.rotation][i][j]:
                    game.grid.game_grid[self.x + i][self.y + j] = self.color


class Grid(object):
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self, screen):
        frame = pygame.image.load("frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))

    def create_grid(self, locked_pos={}):
        grid = [[(0,0,0) for _ in range(COLUMNS)] for _ in range(ROWS)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(j, i) in locked_pos:
                    c = locked_pos[(j,i)]
                    grid[i][j] = c
        return grid



class Game(object):
    def __init__(self):
        pygame.init()
        self.tps = 100.0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.grid = Grid()

    def draw_start(self):
        title_img = pygame.image.load("title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 95, 20))
        self.grid.draw_grid(self.screen)


    def draw_game(self):
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.grid.game_grid[i][j] != 0:
                    pygame.draw.rect(self.screen, self.grid.game_grid[i][j],
                                     (first_elem_x + i * elem_size, first_elem_y + j * elem_size, elem_size, elem_size))
                else:
                    self.screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))

        pygame.display.flip()

    def start_game(self):

        self.draw_start()
        self.draw_game()
        current_brick = Brick(3, 0, random.choice(shapes))
      #  current_brick = Brick.get_shape(self)
        pygame.display.flip()

        while True:
            current_brick.draw_brick(self)
            self.draw_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        sys.exit(0)
                    if keys[pygame.K_RIGHT]:
                        current_brick.x += 1
                        current_brick.draw_brick(self)
                        pygame.display.flip()
                    if keys[pygame.K_LEFT]:
                        current_brick.x -= 1
                        pygame.display.flip()
                    if keys[pygame.K_UP]:
                        current_brick.rotation += 1
                    if keys[pygame.K_DOWN]:
                        current_brick.y += 2


Game().start_game()

    # Checking inputs

# A to sie przyda do ustawiania czasu

# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps
