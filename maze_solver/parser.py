from maze_solver.errors import MazeFormatError
from maze_solver.maze import SYMBOLS, Maze


def parse_maze(text: str) -> Maze:
    """Read a maze from text, one row per line.

    The grid may be preceded by a size header, "<rows> <cols>", as the puzzle
    files from the maze generator are. When it is there, the grid must match it.
    """
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    if not lines:
        raise MazeFormatError("maze text is empty")

    header = lines[0].split()
    if len(header) == 2 and all(part.isdigit() for part in header):
        height, width = (int(part) for part in header)
        rows = lines[1:]
        if len(rows) != height:
            raise MazeFormatError(f"expected {height} rows, found {len(rows)}")
    else:
        rows = lines
        width = len(rows[0])

    for number, row in enumerate(rows, start=1):
        if len(row) != width:
            raise MazeFormatError(
                f"row {number} has {len(row)} cells, expected {width}"
            )
        unknown = set(row) - SYMBOLS
        if unknown:
            raise MazeFormatError(
                f"row {number} has unknown symbols {''.join(sorted(unknown))!r}"
            )
    return Maze(rows)
