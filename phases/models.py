from django.db import models
from games.models import Game
from players.models import Player

class Phase(models.Model):
	game = models.ForeignKey(Game,related_name='phase_game')
	winner = models.ForeignKey(Player, related_name='phase_winner')
