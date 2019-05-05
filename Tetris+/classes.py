from variables import *
import random


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
        clean_shape = []
        for i, line in enumerate(curr_shape):
            row = list(line)
            for j, element in enumerate(row):
                if element == 1:
                    clean_shape.append((self.x + j, self.y + i))

        return clean_shape


class Grid:
    def __init__(self):
        self.game_grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self, screen):
        frame = pygame.image.load('images/frame.png')
        screen.blit(frame, (first_elem_x - 10, first_elem_y - 10))
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.game_grid[i][j] != 0:
                    screen.blit(self.game_grid[i][j], (first_elem_x + j * elem_size, first_elem_y + i * elem_size))
