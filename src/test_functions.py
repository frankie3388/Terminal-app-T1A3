import pytest

from functions import add_history, view_history, funds, play, display_result, betting, bet_selection, win_lose

# def test_basic():
#     assert "hello" == "hello"

def test_funds():
    assert funds(user_input='10') == 10
    assert funds(user_input='100') == 100

# def test_play():

def test_win_lose():
    assert win_lose(["red"], 3, 50, 450, "red", "odd") == 550
    assert win_lose(["red"], 3, 50, 550, "red", "odd") == 650