from django.db import models
from users.models import User
from games.models import Game

class Player(models.Model):
	user = models.ForeignKey(User, related_name="player_user")
	game = models.ForeignKey(Game, related_name="player_game")
