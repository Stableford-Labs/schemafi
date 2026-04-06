from typing import Protocol

from src.schemafi.models.provider_schema import ProviderSchema


class SchemaConnector(Protocol):
    """Protocol for connector classes that define the interface.

    Use for listing tables and fetching schemas from a database.
    """

    def list_tables(self, database: str) -> list[str]:
        """List all available tables in a given database.

        Args:
            database (str): Database name

        Returns:
            list[str]: A list of table names
        """
        ...

    def fetch_schema(self, database: str, table: str) -> ProviderSchema:
        """Fetch schema of a given table in a defined database.

        Args:
            database (str): Database name
            table (str): Table name

        Returns:
            ProviderSchema: Table schema
        """
        ...
