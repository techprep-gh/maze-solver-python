from maze_solver import parse_maze, shortest_path


def test_follows_a_corridor():
    maze = parse_maze(
        """
        ######
        #S...#
        ####.#
        #E...#
        ######
        """
    )

    assert shortest_path(maze) == [
        (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1),
    ]


def test_takes_the_shorter_of_two_routes():
    maze = parse_maze(
        """
        #######
        #S....#
        #.###.#
        #.....#
        #E#####
        #######
        """
    )

    assert shortest_path(maze) == [(1, 1), (2, 1), (3, 1), (4, 1)]


def test_start_next_to_the_exit():
    maze = parse_maze(
        """
        ####
        #SE#
        ####
        """
    )

    assert shortest_path(maze) == [(1, 1), (1, 2)]
