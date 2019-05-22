from variables import ROWS, COLUMNS
#  SCREEN_WIDTH, SCREEN_HEIGHT, SURF_WIDTH, SURF_HEIGHT, first_elem_x
from variables import shapes, shapes_colors, change_shape, next_shape
# first_elem_y, elem_size, powers
from variables import clean_all, minus_line, plus_line
from classes import Piece
# Grid, Power
import random


def shape_at_start(shape):
    clear_shape = shape.shape_without_whitespaces()
    must_put_up = True
    for pos in clear_shape:
        if pos[1] == 0:
            must_put_up = False
            break
    if must_put_up:
        shape.y -= 1


def valid_space(shape, grid):
    grid_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0]
                      for i in range(ROWS)]
    grid_positions = [j for sub in grid_positions for j in sub]
    clear_shape = shape.shape_without_whitespaces()

    for pos in clear_shape:
        if pos not in grid_positions:
            return False

    return True


def correct_rotation(shape, grid):
    ok_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0]
                    for i in range(ROWS)]
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


def clean_rows(game):
    lines_clened = 0
    for i in range(ROWS):
        full_row = True
        for j in range(COLUMNS):
            if game.grid.game_grid[i][j] == 0:
                full_row = False

        if full_row:
            lines_clened += 1
            game.lines += 1
            for r in range(i, -1, -1):
                for c in range(COLUMNS):
                    game.grid.game_grid[r][c] = game.grid.game_grid[r-1][c]

            for c in range(COLUMNS):
                game.grid.game_grid[0][c] = 0

    if lines_clened == 1:
        game.points += 40 * game.level
    elif lines_clened == 2:
        game.points += 100 * game.level
    elif lines_clened == 3:
        game.points += 300 * game.level
    elif lines_clened > 3:
        game.points += 1200 * game.level


def run_power(game):
    game.points += 200
    if game.power.type == clean_all:
        for i in range(ROWS):
            for j in range(COLUMNS):
                game.grid.game_grid[i][j] = 0
    elif game.power.type == next_shape:
        game.curr_piece = game.next_piece
        shape_at_start(game.curr_piece)
        game.next_piece = Piece(3, 0, random.choice(shapes))
        game.curr_piece.draw_piece(game.screen)
    elif game.power.type == change_shape:
        game.curr_piece = \
            Piece(game.curr_piece.x, game.curr_piece.y, random.choice(shapes))
        game.curr_piece.draw_piece(game.screen)
    elif game.power.type == minus_line:
        for r in range(19, -1, -1):
            for c in range(COLUMNS):
                game.grid.game_grid[r][c] = game.grid.game_grid[r - 1][c]

        for c in range(COLUMNS):
            game.grid.game_grid[0][c] = 0
    elif game.power.type == plus_line:
        for c in range(COLUMNS):
            if game.grid.game_grid[0][c] != 0:
                game.running = False
                return

        empty_space = random.randint(0, COLUMNS - 1)
        color = random.choice(shapes_colors)
        for r in range(ROWS - 1):
            for c in range(COLUMNS):
                game.grid.game_grid[r][c] = game.grid.game_grid[r + 1][c]

        for c in range(COLUMNS):
            if c != empty_space:
                game.grid.game_grid[19][c] = color
            else:
                game.grid.game_grid[19][c] = 0


def check_if_power(piece, power):
    clear_shape = piece.shape_without_whitespaces()

    for pos in clear_shape:
        if pos[0] == power.x and pos[1] == power.y:
            return True
    return False


# def is_lost(shape):
#     clear_shape = shape.shape_without_whitespaces()
#     for pos in clear_shape:
#         if pos[1] < 0:
#             return True
#     return False
