import pygame
import sys

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620

SURF_WIDTH = 250
SURF_HEIGHT = 500

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH)/2
first_elem_y = (SCREEN_HEIGHT - SURF_HEIGHT) - 40

elem_size = 25

class Grid(object):
    def __init__(self):
        grid = [[0 for x in range(COLUMNS)] for x in range(ROWS)]


    def draw_grid(self,screen):
        empty_block = pygame.image.load("empty.png")
        frame = pygame.image.load("frame.png")
        screen.blit(frame,(first_elem_x - 12, first_elem_y - 12))
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

    def draw_game(self):
        title_img = pygame.image.load("title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 75, 20))
        self.grid.draw_grid(self.screen)

    def start_game(self):
        self.draw_game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            pygame.display.flip()



Game().start_game()


# self.delta += self.clock.tick() / 1000.0
# while self.delta > 1 / self.tps:
#     self.tick()
#     self.delta -= 1 / self.tps
