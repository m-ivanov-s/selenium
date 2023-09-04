import pytest


@pytest.fixture()
def right_word():
    return "молоко"


@pytest.fixture()
def wrong_word():
    return "малако"