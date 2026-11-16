from maze_solver import parse_maze

MAZE = """
#####
#S..#
#.#.#
#..E#
#####
"""


def test_neighbors_skip_walls():
    maze = parse_maze(MAZE)

    assert list(maze.neighbors((1, 1))) == [(1, 2), (2, 1)]
    assert list(maze.neighbors((2, 3))) == [(1, 3), (3, 3)]


def test_neighbors_stay_inside_the_grid():
    maze = parse_maze(
        """
        S.
        E.
        """
    )

    assert list(maze.neighbors((0, 0))) == [(0, 1), (1, 0)]
    assert list(maze.neighbors((1, 1))) == [(0, 1), (1, 0)]


def test_in_bounds():
    maze = parse_maze(MAZE)

    assert maze.in_bounds((0, 0))
    assert maze.in_bounds((4, 4))
    assert not maze.in_bounds((5, 0))
    assert not maze.in_bounds((0, -1))


def test_symbol_at():
    maze = parse_maze(MAZE)

    assert maze.symbol_at((1, 1)) == "S"
    assert maze.symbol_at((0, 0)) == "#"
    assert maze.is_wall((2, 2))
