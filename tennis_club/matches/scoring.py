def add_point(p1, p2, winner): # вернуть p1, p2, game_won (true\false)

    if winner == 1:
        p1 += 1
    else: 
        p2 += 1

    game_end = False

    