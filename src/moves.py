import math


def _max_right(n):
    return math.ceil(n / 8) * 8


def _min_left(n):
    return _max_right(n) - 7


def _two_step_on_y_one_on_x(n, y_direction=-1, x_direction=-1):
    max_right = _max_right(n)
    new_max_right = max_right + (16 * y_direction)

    if not (8 <= new_max_right <= 64):
        return

    two_on_y = new_max_right - (max_right - n)
    new_min_left = _min_left(two_on_y)
    one_on_x = two_on_y + x_direction

    if new_min_left <= one_on_x <= new_max_right:
        return one_on_x


def _two_step_on_x_one_on_y(n, y_direction=-1, x_direction=-1):
    max_right = _max_right(n)
    min_left = _min_left(n)
    two_on_x = n + (2 * x_direction)

    if not (min_left <= two_on_x <= max_right):
        return

    new_max_right = max_right + y_direction * 8
    one_on_y = new_max_right - (max_right - two_on_x)
    if 1 <= one_on_y <= 64:
        return one_on_y


def find_available_moves(current_position):
    moves = [
        _two_step_on_y_one_on_x(current_position),
        _two_step_on_y_one_on_x(current_position, x_direction=1),
        _two_step_on_y_one_on_x(current_position, y_direction=1),
        _two_step_on_y_one_on_x(current_position, 1, 1),

        _two_step_on_x_one_on_y(current_position),
        _two_step_on_x_one_on_y(current_position, x_direction=1),
        _two_step_on_x_one_on_y(current_position, y_direction=1),
        _two_step_on_x_one_on_y(current_position, 1, 1)
    ]

    for move in moves:
        if move is not None:
            yield move
