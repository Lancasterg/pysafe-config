import pytest

from pysafe_config import _getenv


@pytest.fixture
def bad_helper_function() -> bytes:
    return bytes([1, 2, 3])


def test_getenv_disallowed_return_type(bad_helper_function, monkeypatch):
    monkeypatch.setenv("ENV_VAR", "fail")

    with pytest.raises(TypeError):

        _getenv(
            "ENV_VAR",
            bytes,
            bad_helper_function,
            default=bytes([1, 2, 3]),
            required=False,
        )
