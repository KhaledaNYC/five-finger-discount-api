from django.db import models
from games.models import Game
from users.models import User

class Phase(models.Model):
	game = models.ForeignKey(Game,related_name='phase_game')
	winner = models.ForeignKey(User, related_name='phase_winner')
