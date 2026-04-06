from src.schemafi.contracts.normaliser import SchemaNormaliser


def test_schema_normaliser_protocol() -> None:
    """Tests the SchemaNormaliser protocol.

    Creates amock implementation and verifies its methods.
    """

    class MockNormaliser(SchemaNormaliser):
        def normalise(self, raw: dict[str, str]) -> dict[str, str]:
            return {k: v.upper() for k, v in raw.items()}

    normaliser = MockNormaliser()
    assert callable(normaliser.normalise)
    input_schema = {"column1": "string", "column2": "integer"}
    expected_output = {"column1": "STRING", "column2": "INTEGER"}
    assert normaliser.normalise(input_schema) == expected_output
