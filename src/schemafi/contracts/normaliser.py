from typing import Protocol

from src.schemafi.models.provider_schema import ProviderSchema


class SchemaNormaliser(Protocol):
    """Normalise a schema received from upstream services."""

    def normalise(self, raw: ProviderSchema) -> dict[str, str]:
        """Normalises a given schema to a standard format.

        Args:
            raw (ProviderSchema): The input schema to be normalised

        Returns:
            ProviderSchema: The normalised schema
        """
        ...
