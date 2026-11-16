# Maze solver overview

A small Python library that reads a maze from text, finds a shortest route from
the start to the exit, and prints the maze with that route drawn on it.

## The maze format

| Symbol | Meaning |
|---|---|
| `#` | wall |
| `.` | open floor |
| `S` | the start |
| `E` | the exit |

Each line of text is one row, and every row has the same width. Moves are up,
down, left and right, never diagonal. Cells are `(row, col)` with `(0, 0)` at the
top left. The maze generator can also write a maze on one line as
`<cols>:<cells>`, with the cells running row after row: `5:#####S..E######` is
three rows of five.

A maze and the same maze printed with its route:

```
#####      #####
#S..#      #S**#
#.#.#      #.#*#
#..E#      #..E#
#####      #####
```

## Modules

All in `maze_solver/`:

- `parser.py`: `parse_maze(text)`, turns text in either format into a `Maze`
- `maze.py`: `Maze`, the grid with its start, exit, walls and neighbours
- `solver.py`: `shortest_path(maze)`, a breadth-first search with a step limit
- `render.py`: `render(maze, path)`, prints the maze with a route marked `*`
- `errors.py`: `MazeFormatError` and `SearchLimitExceeded`

## Running the tests

```bash
pytest tests/
```
