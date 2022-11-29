import pytest
from tenis import tenis_game


@pytest.mark.parametrize("a, b",
                         [(0, "Love-All"), (1, "Fifteen-All"), (2, "Thirty-All"), (3, "Fourty-All"), (4, "Deuce")])
def test_remis(a, b):
    assert tenis_game(a, a) == b


@pytest.mark.parametrize("p1, p2, result",
                         [(1, 0, 'Fifteen-Love'),
                          (2, 0, 'Thirty-Love'),
                          (3, 0, 'Fourty-Love'),
                          (2, 1, 'Thirty-Fifteen'),
                          (3, 1, 'Fourty-Fifteen'),
                          (3, 2, 'Fourty-Thirty'),
                          (4, 0, 'Win for Player 1'),
                          (4, 1, 'Win for Player 1'),
                          (4, 2, 'Win for Player 1'),
                          (4, 3, 'Advantage Player 1'),
                          (5, 3, 'Win for Player 1')]
                         )
def test_better_player1(p1, p2, result):
    assert tenis_game(p1, p2) == result


@pytest.mark.parametrize("p1, p2, result", [
    (0, 1, 'Love-Fifteen'),
    (0, 2, 'Love-Thirty'),
    (0, 3, 'Love-Fourty'),
    (3, 5, 'Win for Player 2'),
    (3, 4, 'Advantage Player 2'),]
                         )
def test_better_player2(p1, p2, result):
    assert tenis_game(p1, p2) == result
