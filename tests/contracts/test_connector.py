from src.schemafi.contracts.connector import SchemaConnector


def test_schema_connector_protocol() -> None:
    """Tests the SchemaConnector protocol.

    Creates a mock implementation and verifies its methods.
    """

    class MockConnector(SchemaConnector):
        def list_tables(self, database: str) -> list[str]:
            return ["table1", "table2"]

        def fetch_schema(self, database: str, table: str) -> dict[str, str]:
            return {"column1": "string", "column2": "integer"}

    connector = MockConnector()
    assert callable(connector.list_tables)
    assert callable(connector.fetch_schema)
    assert connector.list_tables("test_db") == ["table1", "table2"]
    assert connector.fetch_schema("test_db", "table1") == {
        "column1": "string",
        "column2": "integer",
    }
