import pygame
from pygame.locals import FULLSCREEN
import sys
import random
from variables import COLUMNS, SCREEN_WIDTH, SCREEN_HEIGHT,  first_elem_x,\
    first_elem_y, elem_size, shapes
# ROWS, SURF_WIDTH, SURF_HEIGHT, shapes_colors, change_shape, next_shape,\
# clean_all, minus_line, plus_line, powers
from classes import Grid, Piece, Power
from mechanics import valid_space, shape_at_start, correct_rotation,\
    clean_rows, run_power, check_if_power_hit, gamer_lost, draw_pause


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.curr_piece = None
        self.next_piece = None
        self.power = None
        self.changed_controls = False

        self.running = True
        self.paused = False
        self.level = 1
        self.lines = 0
        self.points = 0

    def draw_game(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load('images/title.png')
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 190,
                                     first_elem_y - 60))
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
                                     (first_elem_x + 245 +
                                      (self.next_piece.x + j) * elem_size,
                                      first_elem_y + 381 +
                                      (self.next_piece.y + i) * elem_size,
                                      elem_size, elem_size))

    def evaluate_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.paused = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.curr_piece.rotation = (self.curr_piece.rotation + 1) \
                                           % len(self.curr_piece.shape)
                correct_rotation(self.curr_piece, self.grid.game_grid)
                self.curr_piece.draw_piece(self.screen)
            elif (event.type == pygame.KEYDOWN and
                  event.key == pygame.K_RIGHT and not self.changed_controls) or \
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_LEFT and self.changed_controls):
                self.curr_piece.x += 1
                if not valid_space(self.curr_piece, self.grid.game_grid):
                    self.curr_piece.x -= 1
                self.curr_piece.draw_piece(self.screen)
            elif (event.type == pygame.KEYDOWN and
                  event.key == pygame.K_LEFT and not self.changed_controls) or \
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_RIGHT and self.changed_controls):
                self.curr_piece.x -= 1
                if not valid_space(self.curr_piece, self.grid.game_grid):
                    self.curr_piece.x += 1
                self.curr_piece.draw_piece(self.screen)

    def run(self):
        to_power_time = 0
        power_last_time = 0
        fall_time_game = 0
        fall_speed_game = 0
        fall_time_usr = 0
        changed_controls_time = 0

        pygame.mixer.music.load('sounds/Tetris.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        while self.running:
            if self.paused:
                draw_pause(self.screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.paused = False
                continue

            self.draw_game()
            self.curr_piece.draw_piece(self.screen)

            fall_speed_game = 0.75 / (self.level / 2.5)
            fall_time_game += self.clock.get_rawtime()
            fall_time_usr += self.clock.get_rawtime()

            if self.changed_controls:
                if changed_controls_time >= 25000:
                    changed_controls_time = 0
                    self.changed_controls = False
                else:
                    changed_controls_time += self.clock.get_rawtime()

            if self.power is None:
                to_power_time += self.clock.get_rawtime()
                if to_power_time >= 17500:
                    to_power_time = 0
                    self.power = Power(self.grid.game_grid, self.curr_piece)
            else:
                power_last_time += self.clock.get_rawtime()
                if power_last_time >= 10000:
                    self.power = None
                    power_last_time = 0
                else:
                    self.power.draw_power(self.screen)
                    if check_if_power_hit(self.curr_piece, self.power):
                        run_power(self)
                        self.power = None
                        continue
            self.clock.tick()

            if fall_time_game / 1000 >= fall_speed_game:
                fall_time_game = 0
                self.curr_piece.y += 1

            if gamer_lost(self):
                continue

            self.evaluate_keys()

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

        pygame.mixer.music.stop()
        power_sound = pygame.mixer.Sound('sounds/game_over.wav')
        power_sound.play()
        game_over_img = pygame.image.load('images/game_over.png')
        self.screen.blit(game_over_img,
                         (first_elem_x + 25, first_elem_y + 150))
        pygame.time.delay(200)
        pygame.display.update()

    def start_game(self):
        self.curr_piece = Piece(3, 0, random.choice(shapes))
        self.next_piece = Piece(3, 0, random.choice(shapes))

        self.draw_game()
        press_start_img = pygame.image.load('images/press_start.png')
        self.screen.blit(press_start_img,
                         (first_elem_x + COLUMNS * elem_size + 15,
                          first_elem_y + 2 * elem_size))

        shape_at_start(self.curr_piece)

        self.curr_piece.draw_piece(self.screen)
        pygame.display.update()

        started = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_SPACE and not started:
                    self.run()
                    started = True
