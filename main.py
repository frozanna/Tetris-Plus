import pygame
import sys

ROWS = 20
COLUMNS = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 660

SURF_WIDTH = 300
SURF_HEIGHT = 600

first_elem_x = (SCREEN_WIDTH - SURF_WIDTH)/2
first_elem_y = (SCREEN_HEIGHT - SURF_HEIGHT)

elem_size = 30


class Game(object):
    def __init__(self):
        pygame.init()
        self.tps = 100.0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta = 0.0

    def draw_grid(self):
        empty_block = pygame.image.load("empty.png")
        for i in range(ROWS):
            for j in range(COLUMNS):
                self.screen.blit(empty_block, (first_elem_x + j*elem_size,first_elem_y + i*elem_size))
                pass

    def draw_game(self):
        title_img = pygame.image.load("title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 75, 10))

        self.draw_grid()
        grid = [[0 for x in range(COLUMNS)] for x in range(ROWS)]


    def start_game(self):
        self.draw_game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # self.delta += self.clock.tick() / 1000.0
            # while self.delta > 1 / self.tps:
            #     self.tick()
            #     self.delta -= 1 / self.tps

            pygame.display.flip()


def start():
    Game().start_game()

start()