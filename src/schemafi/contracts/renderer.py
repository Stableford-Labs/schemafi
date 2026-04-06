from typing import Protocol


class DocumentRenderer(Protocol):
    """Object that defines the interface for rendering documentation in a specific format."""

    def render(self, doc: str) -> str:
        """Render a given schema documentation into a specific format.

        Args:
            doc (str): The input documentation to be rendered

        Returns:
            str: The rendered content
        """
        ...

    def file_extension(self) -> str:
        """Return the file extension associated with the rendered format.

        Returns:
            str: The file extension (e.g., 'md' for Markdown)
        """
        ...
