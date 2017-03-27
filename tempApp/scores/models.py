from django.db import models
from games import Game
from users import User

class Score(models.Model):
	game = models.ForeignKey(Game)
	player = models.ForeignKey(User)
	score = models.IntegerField(default = 0)
