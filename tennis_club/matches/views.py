from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from .models import Match, Team, Player, TennisScore
from .serializers import MatchSerializer
import json

def scoreboard(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'matches/scoreboard.html', {'match_id': match.id})

@api_view(['POST'])
def create_match(request):
    # Ожидаем JSON: {"team1": ["Игрок А", "Игрок Б"], "team2": ["Игрок В", "Игрок Г"]}
    data = request.data
    match = Match.objects.create()
    for idx, team_data in enumerate([data.get('team1'), data.get('team2')], start=1):
        team = Team.objects.create(match=match, name=f"Команда {idx}")
        for player_name in team_data:
            Player.objects.create(team=team, name=player_name)
    TennisScore.objects.create(match=match)
    serializer = MatchSerializer(match)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    serializer = MatchSerializer(match)
    return Response(serializer.data)

@api_view(['POST'])
def add_point(request, match_id):
    winner = request.data.get('winner')  # 'team1' или 'team2'
    if winner not in ('team1', 'team2'):
        return Response({'error': 'winner must be team1 or team2'}, status=400)
    
    match = get_object_or_404(Match, id=match_id)
    score = match.score
    # Обновляем очки (упрощённая логика, без геймов/сетов, для демо)
    if winner == 'team1':
        score.team1_points += 1
    else:
        score.team2_points += 1
    
    # Проверка выигрыша гейма (условие: >=4 очков и разница >=2)
    if score.team1_points >= 4 and score.team1_points - score.team2_points >= 2:
        score.team1_games += 1
        score.team1_points = 0
        score.team2_points = 0
    elif score.team2_points >= 4 and score.team2_points - score.team1_points >= 2:
        score.team2_games += 1
        score.team1_points = 0
        score.team2_points = 0
    
    score.save()
    serializer = MatchSerializer(match)
    return Response(serializer.data)