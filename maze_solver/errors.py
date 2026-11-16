class MazeFormatError(ValueError):
    """The maze text cannot be read as a maze."""


class SearchLimitExceeded(RuntimeError):
    """The search ran for more steps than it is allowed."""

    def __init__(self, max_steps: int):
        super().__init__(f"gave up after {max_steps} steps")
        self.max_steps = max_steps
