# Maze solver

Reads a maze from text, finds a shortest route from the start to the exit and
prints the maze with the route drawn on it.

```
#####      #####
#S..#      #S**#
#.#.#  ->  #.#*#
#..E#      #..E#
#####      #####
```

`#` is a wall, `.` is open floor, `S` is the start and `E` is the exit. Moves are
up, down, left and right.

## Modules

- `maze_solver/parser.py`: `parse_maze(text)`, which checks the text and builds a
  `Maze`. Besides one row per line, it reads the maze generator's one-line
  format, `<cols>:<cells>`, where the cells run row after row
  (`5:#####S..E######` is a 3 by 5 maze).
- `maze_solver/maze.py`: `Maze`, the grid, with its start and exit, walls,
  bounds and the neighbours of a cell.
- `maze_solver/solver.py`: `shortest_path(maze)`, a breadth-first search that
  returns the cells of a shortest route, or `None` when the exit cannot be
  reached. It gives up with `SearchLimitExceeded` after `max_steps` cells.
- `maze_solver/render.py`: `render(maze, path)`, which draws the maze with the
  route marked by `*`.

```python
from maze_solver import parse_maze, render, shortest_path

maze = parse_maze(open("maze.txt").read())
print(render(maze, shortest_path(maze)))
```

## Tests

```bash
pip install -r requirements.txt
pytest
```
