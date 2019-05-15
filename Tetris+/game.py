import pygame
import sys
import random
from variables import ROWS, COLUMNS, SCREEN_WIDTH, SCREEN_HEIGHT, SURF_WIDTH, SURF_HEIGHT, first_elem_x,\
    first_elem_y, elem_size, shapes, shapes_colors, change_shape, next_shape,\
    clean_all, minus_line, plus_line, powers
from classes import Grid, Piece, Power
from mechanics import valid_space, shape_at_start, correct_rotation, clean_rows, run_power,\
    check_if_power



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.curr_piece = None
        self.next_piece = None
        self.power = None

        self.running = True
        self.level = 1
        self.lines = 0
        self.points = 0

    def draw_game(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load('images/title.png')
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 190, 20))
        self.grid.draw_grid(self.screen)
        font = pygame.font.Font('Pixeled.ttf', 14)
        levels = font.render(str(self.level), 1, (255, 255, 255))
        self.screen.blit(levels, (first_elem_x + 265, first_elem_y + 135))
        lines = font.render(str(self.lines), 1, (255, 255, 255))
        self.screen.blit(lines, (first_elem_x + 265, first_elem_y + 215))
        points = font.render(str(self.points), 1, (255, 255, 255))
        self.screen.blit(points, (first_elem_x + 265, first_elem_y + 296))

        for i in range(0, 4):
            for j in range(0, 4):
                if self.next_piece.shape[self.next_piece.rotation][i][j]:
                    self.screen.blit(self.next_piece.color,
                                     (first_elem_x + 245 + (self.next_piece.x + j) * elem_size,
                                      first_elem_y + 380 + (self.next_piece.y + i) * elem_size, elem_size, elem_size))

    def run(self):
        to_power_time = 0
        power_last_time = 0
        fall_time_game = 0
        fall_speed_game = 0
        fall_time_usr = 0

        while self.running:
            self.draw_game()
            if self.running:
                self.curr_piece.draw_piece(self.screen)

            fall_speed_game = 0.75 / (self.level / 2.5)
            fall_time_game += self.clock.get_rawtime()
            fall_time_usr += self.clock.get_rawtime()
            if self.power is None:
                to_power_time += self.clock.get_rawtime()
            else:
                power_last_time += self.clock.get_rawtime()
            self.clock.tick()

            if self.power is None:
                if to_power_time >= 17500:
                    to_power_time = 0
                    self.power = Power(self.grid.game_grid, self.curr_piece)
            else:
                if power_last_time >= 10000:
                    self.power = None
                    power_last_time = 0
                else:
                    self.power.draw_power(self.screen)
                    if check_if_power(self.curr_piece, self.power):
                        run_power(self) == 1
                        self.power = None
                        continue

            if fall_time_game / 1000 >= fall_speed_game:
                fall_time_game = 0
                self.curr_piece.y += 1

            if not valid_space(self.curr_piece, self.grid.game_grid):
                self.curr_piece.y -= 1
                if self.curr_piece.y < 0:
                    self.running = False
                    continue

                piece_pos = [[(j + self.curr_piece.x, i + self.curr_piece.y) for j in range(0, 4)
                              if self.curr_piece.shape[self.curr_piece.rotation][i][j] != 0] for i in range(0, 4)]
                piece_pos = [j for el in piece_pos for j in el]
                for p in piece_pos:
                    self.grid.game_grid[p[1]][p[0]] = self.curr_piece.color

                if self.running:
                    self.curr_piece = self.next_piece
                    shape_at_start(self.curr_piece)
                    self.next_piece = Piece(3, 0, random.choice(shapes))
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

            clean_rows(self)
            self.level = self.lines // 10 + 1
            pygame.display.update()

        game_over_img = pygame.image.load('images/game_over.png')
        self.screen.blit(game_over_img, (first_elem_x + 25, first_elem_y + 150))
        pygame.time.delay(200)
        pygame.display.update()
        pygame.time.delay(5000)

    def start_game(self):
        self.curr_piece = Piece(3, 0, random.choice(shapes))
        self.next_piece = Piece(3, 0, random.choice(shapes))

        self.draw_game()
        press_start_img = pygame.image.load('images/press_start.png')
        self.screen.blit(press_start_img, (first_elem_x + COLUMNS * elem_size + 15, first_elem_y + 2 * elem_size))

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
