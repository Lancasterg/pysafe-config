import logging

import pytest

from pysafe_config import getenv_bool, getenv_float, getenv_int, getenv_str

logger = logging.getLogger(__name__)

"""
Slightly hacky approach to an integration test, but this script allows for a test to be run in the Github CI
that reads in environment variables from the Github CI environment.

Environment
    INT_TEST_VAR: 1
    STR_TEST_VAR: "secret message"
    BOOL_TEST_VAR: "TRUE"
    FLOAT_TEST_VAR: 73.9
"""

INT_TEST_VAR: int = getenv_int("INT_TEST_VAR")
STR_TEST_VAR: str = getenv_str("STR_TEST_VAR")
BOOL_TEST_VAR: bool = getenv_bool("BOOL_TEST_VAR")
FLOAT_TEST_VAR: float = getenv_float("FLOAT_TEST_VAR")


def integration_test() -> None:
    if (
        INT_TEST_VAR == 1
        and STR_TEST_VAR == "secret message"
        and BOOL_TEST_VAR is True
        and FLOAT_TEST_VAR == 73.9
    ):
        logger.info("Integration test passed")
    else:
        pytest.fail("Integration test failed")


if __name__ == "__main__":
    integration_test()
