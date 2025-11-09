from pysafe_config import _getenv, _getenv_strict

import pytest


def test_getenv_disallowed_return_type(monkeypatch):
    monkeypatch.setenv("ENV_VAR", "fail")

    def _helper_function(_: str) -> bytes:
        return bytes([1, 2, 3])

    with pytest.raises(TypeError):
        _getenv(
            "ENV_VAR",
            bytes,
            _helper_function,
            default=bytes([1,2,3]),
            required=False
        )


def test_getenv_strict_disallowed_return_type(monkeypatch):
    monkeypatch.setenv("ENV_VAR", "fail")

    def _helper_function(_: str) -> bytes:
        return bytes([1, 2, 3])

    with pytest.raises(TypeError):
        _getenv_strict(
            "ENV_VAR",
            bytes,
            _helper_function
        )


def test_getenv_strict_disallowed_return_type_post_read(monkeypatch):
    monkeypatch.setenv("ENV_VAR", "fail")

    def _helper_function(_: str) -> bytes:
        return bytes([1, 2, 3])

    with pytest.raises(TypeError):
        _getenv_strict(
            "ENV_VAR",
            str,
            _helper_function
        )
