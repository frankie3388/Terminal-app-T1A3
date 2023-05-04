import pytest
import csv
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

def test_view_history(capfd):
    test_file = "mock_history.csv"
    expected_output = "['3', 'red', 'odd']\n"
    with open(test_file, "w") as history_file:
        writer = csv.writer(history_file)
        writer.writerow(['3', "red", "odd"])
    view_history(test_file)
    captured = capfd.readouterr()
    assert captured.out == expected_output