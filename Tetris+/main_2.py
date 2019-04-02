import pygame
import sys
import random

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH)/2
first_elem_y = (SCREEN_HEIGHT - SURF_HEIGHT) - 40

elem_size = 25

# Tablica bloczkow - nieskonczona
shapes = [
            [
                [(0,0,0,0),
                 (0,1,1,0),
                 (0,1,1,0),
                 (0,0,0,0),],
            ],
            [
                [(0,0,0,0),
                 (1,1,1,1),
                 (0,0,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (0,1,0,0),
                 (0,1,0,0),
                 (0,1,0,0),],
            ],
            [
                [(0,0,0,0),
                 (0,1,1,0),
                 (1,1,0,0),
                 (0,0,0,0),],
                [(1,0,0,0),
                 (1,1,0,0),
                 (0,1,0,0),
                 (0,0,0,0),],
            ],
            [
                [(0,0,0,0),
                 (1,1,0,0),
                 (0,1,1,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (1,1,0,0),
                 (1,0,0,0),
                 (0,0,0,0),],
            ],
            [
                [(0,0,0,0),
                 (1,1,1,0),
                 (1,0,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (0,1,0,0),
                 (0,1,1,0),
                 (0,0,0,0),],
                [(0,0,1,0),
                 (1,1,1,0),
                 (0,0,0,0),
                 (0,0,0,0),],
                [(1,1,0,0),
                 (0,1,0,0),
                 (0,1,0,0),
                 (0,0,0,0),],
            ],
            [
                [(0,0,0,0),
                 (1,1,1,0),
                 (0,0,1,0),
                 (0,0,0,0),],
                [(0,1,1,0),
                 (0,1,0,0),
                 (0,1,0,0),
                 (0,0,0,0),],
                [(1,0,0,0),
                 (1,1,1,0),
                 (0,0,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (0,1,0,0),
                 (1,1,0,0),
                 (0,0,0,0),],
            ],
            [
                [(0,0,0,0),
                 (1,1,1,0),
                 (0,1,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (0,1,1,0),
                 (0,1,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (1,1,1,0),
                 (0,0,0,0),
                 (0,0,0,0),],
                [(0,1,0,0),
                 (1,1,0,0),
                 (0,1,0,0),
                 (0,0,0,0),],
            ],
    ]

shapes_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (80, 60, 143),(255, 0, 255), (40, 17, 250), (50, 100, 50)] #Tu beda potem jakies grafiki

#klasa bloczku
class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = random.randint(0,len(shape)-1)

    def draw_piece(self,game):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.shape[self.rotation][i][j]:
                    game.grid.game_grid[self.x + i][self.y + j] = self.color

class Grid(object):
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self,screen):
        frame = pygame.image.load("frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))

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

        piece = Piece(3, 0, random.choice(shapes))
        while True:
            piece.draw_piece(self)
            self.draw_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)




Game().start_game()


# A to sie przyda do ustawiania czasu

# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps
