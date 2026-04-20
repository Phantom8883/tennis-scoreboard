def add_point(team1_points, team2_points, winner_team):
    """
    Обновляет счёт в гейме после выигрыша очка командой winner_team.
    
    Аргументы:
        team1_points (int): текущие очки команды 1 (0,1,2,3,4...)
        team2_points (int): текущие очки команды 2
        winner_team (int): 1 или 2 (какая команда выиграла очко)
    
    Возвращает:
        tuple: (новые_очки_команды1, новые_очки_команды2, флаг_завершения_гейма)
    """
    
    # 1. Начисляем очко команде-победителю
    if winner_team == 1:
        team1_points += 1
    else:
        team2_points += 1
    
    # 2. Проверяем, закончился ли гейм
    #    Гейм заканчивается, если у одной из команд >=4 очков И разница >=2
    
    # Проверяем, не выиграла ли команда 1
    if team1_points >= 4 and (team1_points - team2_points) >= 2:
        game_won = True
        team1_points = 0
        team2_points = 0
    # Проверяем, не выиграла ли команда 2
    elif team2_points >= 4 and (team2_points - team1_points) >= 2:
        game_won = True
        team1_points = 0
        team2_points = 0
    else:
        game_won = False
    
    # 3. Возвращаем результат
    return team1_points, team2_points, game_won



if __name__ == "__main__":
    # Тест 1: счёт 3-3, команда 1 выигрывает очко → преимущество (4-3)
    p1, p2, won = add_point(3, 3, 1)
    print(f"3-3, +1 для команды1 → {p1}-{p2}, гейм закончен: {won}")  # 4-3, False
    
    # Тест 2: счёт 4-3, команда 1 выигрывает очко → выигрыш гейма (0-0)
    p1, p2, won = add_point(4, 3, 1)
    print(f"4-3, +1 для команды1 → {p1}-{p2}, гейм закончен: {won}")  # 0-0, True
    
    # Тест 3: счёт 3-4, команда 2 выигрывает очко → выигрыш гейма (0-0)
    p1, p2, won = add_point(3, 4, 2)
    print(f"3-4, +1 для команды2 → {p1}-{p2}, гейм закончен: {won}")  # 0-0, True
    
    # Тест 4: счёт 0-0, команда 1 выигрывает → 1-0
    p1, p2, won = add_point(0, 0, 1)
    print(f"0-0, +1 для команды1 → {p1}-{p2}, гейм закончен: {won}")  # 1-0, False



