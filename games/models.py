from django.db import models
from django.apps import apps
from users.models import User

class Game(models.Model):
	winner = models.ForeignKey(User,related_name='game_winner', null=True)
	rounds_to_win = models.IntegerField(default = 0)
