def tenis_game(a, b):
    points_map = {
        0: 'Love',
        1: 'Fifteen',
        2: 'Thirty',
        3: 'Fourty',
    }
    remis_map = {
        (0, 0): 'Love-All',
        (1, 1): 'Fifteen-All',
        (2, 2): 'Thirty-All',
        (3, 3): 'Fourty-All',
    }
    is_remis = None
    if a == b:
        is_remis = remis_map.get((a, b), 'Deuce')
    if is_remis:
        return is_remis
    if a >= 4 and b <= a - 2:
        return 'Win for Player 1'
    if b >= 4 and a <= b - 2:
        return 'Win for Player 2'
    if b == a - 1 and a > 3:
        return 'Advantage Player 1'
    if a == b - 1 and b > 3:
        return 'Advantage Player 2'
    return f"{points_map[a]}-{points_map[b]}"
