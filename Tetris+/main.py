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
        ]

shapes_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)] #Tu beda potem jakies grafiki

#klasa bloczku
class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = 0


# Inicjalizacja siatki
class Grid(object):
    def __init__(self):
        #To sie przy pozniej w grze, zeby sprawdzic, ktore pola sa wypelnione
        grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    # Rysowanie siatki
    def draw_grid(self,screen):
        #Ramka
        frame = pygame.image.load("frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))

        #Bloczki
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                screen.blit(empty_block, (first_elem_x + j * elem_size, first_elem_y + i * elem_size))



#Glowna klasa gry
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

    def start_game(self):
        self.draw_game()

        piece = Piece(5,0,random.choice(shapes))
        # Tu sie cos bedzie robic, na razie tylko sprawia, ze da sie zamknac okienko
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            pygame.display.flip()



Game().start_game()


# A to sie przyda do ustawiania czasu


# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps
