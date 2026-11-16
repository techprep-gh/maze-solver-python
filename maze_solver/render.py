from typing import Iterable, Optional

from maze_solver.maze import OPEN, Cell, Maze

PATH = "*"


def render(maze: Maze, path: Optional[Iterable[Cell]] = None) -> str:
    """Draw the maze as text, marking the open cells a path goes through with '*'."""
    on_path = set(path or ())
    lines = []
    for row in range(maze.height):
        chars = []
        for col in range(maze.width):
            cell = (row, col)
            symbol = maze.symbol_at(cell)
            if cell in on_path and symbol == OPEN:
                symbol = PATH
            chars.append(symbol)
        lines.append("".join(chars))
    return "\n".join(lines)
