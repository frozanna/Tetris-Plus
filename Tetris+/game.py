import pygame
import sys
import random
from variables import *
from classes import Grid, Piece
from mechanics import valid_space, shape_at_start, correct_rotation


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.curr_piece = None
        self.next_piece = None

        self.running = True
        self.level = 1

    def draw_game(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load('images/title.png')
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 190, 20))
        self.grid.draw_grid(self.screen)

    def run(self):
        fall_time_game = 0
        fall_speed_game = 0
        fall_time_usr = 0

        while self.running:
            self.draw_game()
            self.curr_piece.draw_piece(self.screen)

            fall_speed_game = 0.75 / (self.level / 1.5)
            fall_time_game += self.clock.get_rawtime()
            fall_time_usr += self.clock.get_rawtime()
            self.clock.tick()

            if fall_time_game / 1000 >= fall_speed_game:
                fall_time_game = 0
                self.curr_piece.y += 1
                if not valid_space(self.curr_piece, self.grid.game_grid):
                    self.curr_piece.y -= 1
                self.curr_piece.draw_piece(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.curr_piece.rotation = (self.curr_piece.rotation + 1) % len(self.curr_piece.shape)
                    correct_rotation(self.curr_piece, self.grid.game_grid)
                    self.curr_piece.draw_piece(self.screen)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.curr_piece.x += 1
                    if not valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.x -= 1
                    self.curr_piece.draw_piece(self.screen)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.curr_piece.x -= 1
                    if not valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.x += 1
                    self.curr_piece.draw_piece(self.screen)

            if fall_time_usr / 1000 >= 0.02:
                fall_time_usr = 0
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    sys.exit(0)
                if keys[pygame.K_DOWN]:
                    self.curr_piece.y += 1
                    if not valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.y -= 1
                    self.curr_piece.draw_piece(self.screen)

            pygame.display.update()

    def start_game(self):
        self.draw_game()
        press_start_img = pygame.image.load('images/press_start.png')
        self.screen.blit(press_start_img, (first_elem_x + COLUMNS * elem_size + 15, first_elem_y + 2 * elem_size))

        self.curr_piece = Piece(3, 0, random.choice(shapes))
        shape_at_start(self.curr_piece)

        self.curr_piece.draw_piece(self.screen)
        pygame.display.update()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run()
