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


shapes_colors = [pygame.image.load("images/red.png"), pygame.image.load("images/blue.png"),
                 pygame.image.load("images/aqua.png"), pygame.image.load("images/yellow.png"),
                 pygame.image.load("images/magenta.png"), pygame.image.load("images/green.png"),
                 pygame.image.load("images/orange.png")]


class Piece:
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes_colors[shapes.index(shape)]
        self.rotation = random.randint(0, len(shape) - 1)

    def draw_piece(self, screen):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.shape[self.rotation][i][j]:
                    screen.blit(self.color, (first_elem_x + (self.x + j) * elem_size,
                                             first_elem_y + (self.y + i) * elem_size, elem_size, elem_size))

    def shape_without_whitespaces(self):
        curr_shape = self .shape[self.rotation]
        clear_shape = []
        for i, line in enumerate(curr_shape):
            row = list(line)
            for j, element in enumerate(row):
                if element == 1:
                    clear_shape.append((self.x + j, self.y + i))

        return clear_shape


class Grid:
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self, screen):
        frame = pygame.image.load("images/frame.png")
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.game_grid[i][j] != 0:
                    screen.blit(self.game_grid[i][j], (first_elem_x + i * elem_size, first_elem_y + j * elem_size))


class Mechanics:
    @staticmethod
    def shape_at_start(shape):
        clear_shape = shape.shape_without_whitespaces()
        must_put_up = True
        for pos in clear_shape:
            if pos[1] == 0:
                must_put_up = False
                break
        if must_put_up:
            shape.y -= 1

    @staticmethod
    def valid_space(shape, grid):
        grid_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0] for i in range(ROWS)]
        grid_positions = [j for sub in grid_positions for j in sub]
        clear_shape = shape.shape_without_whitespaces()

        for pos in clear_shape:
            if pos not in grid_positions:
                return False

        return True

    @staticmethod
    def correct_rotation(shape, grid):
        ok_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0] for i in range(ROWS)]
        ok_positions = [j for sub in ok_positions for j in sub]
        clear_shape = shape.shape_without_whitespaces()

        for pos in clear_shape:
            if pos not in ok_positions:
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
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.curr_piece = Piece(3, 0, random.choice(shapes))

        self.running = True
        self.level = 1

    def draw_game(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load("images/title.png")
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 190, 20))
        self.grid.draw_grid(self.screen)

    def run(self):
        fall_time_game = 0
        fall_speed_game = 0
        fall_time_usr = 0
        fall_speed_usr = 0.02

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
                if not Mechanics.valid_space(self.curr_piece, self.grid.game_grid):
                    self.curr_piece.y -= 1
                self.curr_piece.draw_piece(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.curr_piece.rotation = (self.curr_piece.rotation + 1) % len(self.curr_piece.shape)
                    Mechanics.correct_rotation(self.curr_piece, self.grid.game_grid)
                    self.curr_piece.draw_piece(self.screen)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.curr_piece.x += 1
                    if not Mechanics.valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.x -= 1
                    self.curr_piece.draw_piece(self.screen)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.curr_piece.x -= 1
                    if not Mechanics.valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.x += 1
                    self.curr_piece.draw_piece(self.screen)

            if fall_time_usr / 1000 >= fall_speed_usr:
                fall_time_usr = 0
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    sys.exit(0)
                if keys[pygame.K_DOWN]:
                    self.curr_piece.y += 1
                    if not Mechanics.valid_space(self.curr_piece, self.grid.game_grid):
                        self.curr_piece.y -= 1
                    self.curr_piece.draw_piece(self.screen)

            pygame.display.update()

    def start_game(self):
        self.draw_game()
        press_start_img = pygame.image.load("images/press_start.png")
        self.screen.blit(press_start_img, (first_elem_x + COLUMNS * elem_size + 15, first_elem_y + 2 * elem_size))

        self.curr_piece = Piece(3, 0, random.choice(shapes))
        Mechanics.shape_at_start(self.curr_piece)

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


if __name__ == "__main__":
    Game().start_game()
