import pytest

from pysafe_config import _getenv


def test_getenv_disallowed_return_type(monkeypatch):
    monkeypatch.setenv("ENV_VAR", "fail")

    def _helper_function(_: str) -> bytes:
        return bytes([1, 2, 3])

    with pytest.raises(TypeError):
        _getenv(
            "ENV_VAR", bytes, _helper_function, default=bytes([1, 2, 3]), required=False
        )
