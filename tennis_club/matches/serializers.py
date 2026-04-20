from rest_framework import serializers
from .models import Match, Team, Player, TennisScore

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']


class TennisScoreSerializer(serializers.ModelSerializer):
    points_display = serializers.SerializerMethodField()

    class Meta:
        model = TennisScore
        fields = ['team1_games', 'team2_games', 'team1_points', 'team2_points', 'sets_history', 'points_display']

    def get_points_display(self, obj):
        return obj.get_points_display()

class MatchSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)
    score = TennisScoreSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['id', 'title', 'created_at', 'is_finished', 'teams', 'score']