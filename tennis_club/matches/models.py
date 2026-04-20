from django.db import models

class Match(models.Model):
    """Теннисный матч (парная игры, 4 игрока)"""
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Match {self.id} - {self.created_at.strftime('%d.%m %H:%M')}"


class Team(models.Model):
    """Команда (2 игрока)"""
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name or f'Team {self.id}'

class Player(models.Model):
    """Игрок (один человек)"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TennisScore(models.Model):
    """Текущий счёт матча (связа)"""
    match = models.OneToOneField(Match, on_delete=models.CASCADE, related_name='score')

    sets_history = models.JSONField(default=list) # [[6,4], [7,6]]

    current_set_num = models.IntegerField(default=1)

    team1_games = models.IntegerField(default=0)
    team2_games = models.IntegerField(default=0)

    team1_points = models.IntegerField(default=0)
    team2_points = models.IntegerField(default=0)

    def __str__(self):
        return f'Match {self.match.id}: {self.team1_games}-{self.team2_games} ({self.get_points_display()})'
    
    def get_points_display(self):
        """Возвращает красивый счёт очков: 0->0, 1->15, 2->30, 3->40, 4->AD"""
        points_map = {0: '0', 1: '15', 2: '30', 3: '40', 4: 'AD'}
        p1 = points_map.get(self.team1_points, '?')
        p2 = points_map.get(self.team2_points, '?')
        return f'{p1}-{p2}'