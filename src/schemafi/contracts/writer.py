from pathlib import Path
from typing import Protocol


class OutputWriter(Protocol):
    """Object that defines the interface for writing rendered documentation to a specific output."""

    def write(self, path: Path, content: str) -> None:
        """Write the rendered content to a specified output.

        Args:
            content (str): The content to be written
            filename (str): The name of the output file
        """
        ...
