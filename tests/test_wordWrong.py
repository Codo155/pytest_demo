import pytest


@pytest.fixture
def message():
    return "hello"


def test_change_message(message):
    message = "world"
    assert message == "world"

def test_message(message):
    assert message== "hello"