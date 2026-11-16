import pytest

from maze_solver import MazeFormatError, parse_maze


def test_parses_a_plain_grid():
    maze = parse_maze(
        """
        #####
        #S.E#
        #####
        """
    )

    assert (maze.height, maze.width) == (3, 5)
    assert maze.start == (1, 1)
    assert maze.end == (1, 3)


def test_parses_a_one_line_maze():
    maze = parse_maze("5:#####S..E######")

    assert maze.rows == ["#####", "S..E#", "#####"]
    assert maze.start == (1, 0)
    assert maze.end == (1, 3)


def test_rejects_rows_of_different_lengths():
    with pytest.raises(MazeFormatError, match="row 2 has 4 cells, expected 5"):
        parse_maze(
            """
            #####
            #S.E
            #####
            """
        )


def test_rejects_unknown_symbols():
    with pytest.raises(MazeFormatError, match="unknown symbols 'x'"):
        parse_maze(
            """
            #####
            #SxE#
            #####
            """
        )


def test_rejects_empty_text():
    with pytest.raises(MazeFormatError, match="empty"):
        parse_maze("   \n  ")


def test_rejects_a_maze_without_a_start():
    with pytest.raises(MazeFormatError, match="no start"):
        parse_maze(
            """
            #####
            #..E#
            #####
            """
        )
