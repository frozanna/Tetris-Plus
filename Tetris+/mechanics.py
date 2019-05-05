from variables import *


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
    grid_positions = [[(j, i) for j in range(COLUMNS) if grid[i][j] == 0] for i in range(ROWS)]
    grid_positions = [j for sub in grid_positions for j in sub]
    clear_shape = shape.shape_without_whitespaces()

    for pos in clear_shape:
        if pos not in grid_positions:
            return False

    return True


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

# def is_lost(shape):
#     clear_shape = shape.shape_without_whitespaces()
#     for pos in clear_shape:
#         if pos[1] < 0:
#             return True
#     return False
