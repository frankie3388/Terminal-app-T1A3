import pytest
from functions import add_history, view_history, funds, play, display_result, betting, bet_selection, win_lose


def test_funds():
    assert funds(user_input='10') == 10
    assert funds(user_input='100') == 100

def test_win_lose():
    assert win_lose(["red"], 3, 50, 450, "red", "odd") == 550
    assert win_lose(["red"], 3, 50, 550, "red", "odd") == 650

def test_betting(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 10)
    assert betting("red", 500) == 10

   