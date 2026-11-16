from typing import Iterator, List, Tuple

from maze_solver.errors import MazeFormatError

Cell = Tuple[int, int]

WALL = "#"
OPEN = "."
START = "S"
END = "E"
SYMBOLS = {WALL, OPEN, START, END}

# Up, right, down, left. The solver explores neighbours in this order.
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Maze:
    """A rectangular grid of walls and open cells, with one start and one exit.

    Cells are (row, col) tuples with (0, 0) at the top left.
    """

    def __init__(self, rows: List[str]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.start = self._find(START, "start")
        self.end = self._find(END, "exit")

    def _find(self, symbol: str, name: str) -> Cell:
        for row in range(self.height):
            for col in range(self.width):
                if self.rows[row][col] == symbol:
                    return (row, col)
        raise MazeFormatError(f"maze has no {name} ({symbol!r})")

    def symbol_at(self, cell: Cell) -> str:
        row, col = cell
        return self.rows[row][col]

    def in_bounds(self, cell: Cell) -> bool:
        row, col = cell
        return 0 <= row < self.height and 0 <= col < self.width

    def is_wall(self, cell: Cell) -> bool:
        return self.symbol_at(cell) == WALL

    def neighbors(self, cell: Cell) -> Iterator[Cell]:
        row, col = cell
        for d_row, d_col in DIRECTIONS:
            nxt = (row + d_row, col + d_col)
            if self.in_bounds(nxt) and not self.is_wall(nxt):
                yield nxt
