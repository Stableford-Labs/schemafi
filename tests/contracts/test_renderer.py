from src.schemafi.contracts.renderer import DocumentRenderer


def test_document_renderer_protocol() -> None:
    """Tests the DocumentRenderer protocol.

    Creates a mock implementation and verifies its methods.
    """

    class MockRenderer(DocumentRenderer):
        def render(self, doc: str) -> str:
            return "rendered content"

        def file_extension(self) -> str:
            return "md"

    renderer = MockRenderer()
    assert callable(renderer.render)
    assert callable(renderer.file_extension)

    expected_output = "rendered content"
    assert renderer.render("rendered content") == expected_output
