import pytest

from functions import add_history, view_history, funds, play, display_result, betting, bet_selection

# def test_basic():
#     assert "hello" == "hello"

def test_funds():
    assert funds(user_input='10') == 10
    assert funds(user_input='100') == 100

# def test_play():
    