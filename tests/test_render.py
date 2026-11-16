from maze_solver import parse_maze, render

MAZE = "\n".join(
    [
        "#####",
        "#S..#",
        "#.#.#",
        "#..E#",
        "#####",
    ]
)


def test_render_without_a_path_draws_the_maze():
    assert render(parse_maze(MAZE)) == MAZE


def test_render_with_an_empty_path_draws_the_maze():
    assert render(parse_maze(MAZE), []) == MAZE
