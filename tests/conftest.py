import shutil
from typing import Generator

import pytest


@pytest.fixture(scope="session")
def test_data_dir(
    tmp_path_factory: pytest.TempdirFactory,
) -> Generator[str, None, None]:
    """Temporary Directory Fixture.

    A fixture that provides a temporary directory for test data.
    This directory is created at the beginning of the test session and can be
    used to store any necessary files for testing.

    Returns:
        str: The path to the temporary test data directory.
    """
    tmp_path = tmp_path_factory.mktemp("test_data")
    yield str(tmp_path)
    shutil.rmtree(str(tmp_path_factory.getbasetemp()), ignore_errors=True)
