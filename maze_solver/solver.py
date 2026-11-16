from collections import deque
from typing import List, Optional

from maze_solver.errors import SearchLimitExceeded
from maze_solver.maze import Cell, Maze

DEFAULT_MAX_STEPS = 10_000


def shortest_path(maze: Maze, max_steps: int = DEFAULT_MAX_STEPS) -> Optional[List[Cell]]:
    """Breadth-first search from the start to the exit.

    Returns the cells of a shortest path, start and exit included, or None when
    the exit cannot be reached. Raises SearchLimitExceeded after max_steps cells.
    """
    queue = deque([(maze.start, [maze.start])])
    visited = {maze.start}
    steps = 0
    while queue:
        steps += 1
        if steps > max_steps:
            raise SearchLimitExceeded(max_steps)
        cell, path = queue.popleft()
        if cell == maze.end:
            return path
        for nxt in maze.neighbors(cell):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None
