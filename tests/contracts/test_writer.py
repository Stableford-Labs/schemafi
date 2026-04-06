from pathlib import Path

from src.schemafi.contracts.writer import OutputWriter


def test_document_writer_protocol(test_data_dir: str) -> None:
    """Tests the DocumentWriter protocol.

    Creates a mock implementation and verifies if a file is written correctly.
    """
    mock_path = Path(test_data_dir, "mock_schema_documentation.md")

    class MockWriter(OutputWriter):
        def write(self, path: Path, content: str) -> None:
            """Write the rendered content to a specified output."""
            with open(path, "w") as f:
                f.write(content)

    writer = MockWriter()
    writer.write(mock_path, "This is a test schema documentation.")
    assert mock_path.exists()
