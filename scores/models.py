from django.db import models
from games.models import Game
from users.models import User

class Score(models.Model):
	game = models.ForeignKey(Game,related_name='score_game')
	player = models.ForeignKey(User, related_name='score_player')
	score = models.IntegerField(default = 0)
