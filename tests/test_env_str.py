import pytest
from pysafe_config import env_str


def test_env_str_pass(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = env_str("MY_API_KEY")

    assert result == expected
