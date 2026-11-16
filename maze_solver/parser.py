from typing import List

from maze_solver.errors import MazeFormatError
from maze_solver.maze import SYMBOLS, Maze


def parse_maze(text: str) -> Maze:
    """Read a maze from text, one row per line.

    The maze generator writes a maze on a single line instead, as
    "<cols>:<cells>", with the cells running row after row.
    """
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    if not lines:
        raise MazeFormatError("maze text is empty")

    if len(lines) == 1 and ":" in lines[0]:
        rows = _split_run(lines[0])
    else:
        rows = lines
        width = len(rows[0])
        for number, row in enumerate(rows, start=1):
            if len(row) != width:
                raise MazeFormatError(
                    f"row {number} has {len(row)} cells, expected {width}"
                )

    for number, row in enumerate(rows, start=1):
        unknown = set(row) - SYMBOLS
        if unknown:
            raise MazeFormatError(
                f"row {number} has unknown symbols {''.join(sorted(unknown))!r}"
            )
    return Maze(rows)


def _split_run(line: str) -> List[str]:
    width_text, cells = line.split(":", 1)
    if not width_text.isdigit() or int(width_text) == 0:
        raise MazeFormatError(f"row width must be a positive number, got {width_text!r}")
    width = int(width_text)
    height = len(cells) // width
    if height * width != len(cells):
        raise MazeFormatError(f"{len(cells)} cells do not fill rows of {width}")
    return [cells[start:start + width] for start in range(0, len(cells), width)]
