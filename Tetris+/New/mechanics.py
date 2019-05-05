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


def is_lost(shape):
    clear_shape = shape.shape_without_whitespaces()
    for pos in clear_shape:
        if pos[1] < 0:
            return True
    return False
