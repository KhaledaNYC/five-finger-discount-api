from rest_framework import serializers
from games.models import Game
# from players.serializers import PlayerSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Game
        fields = ('winner','rounds_to_win','player_game','phase_game')
