from django.db import models
from games import Games
from users import User

class Phase(models.Model):
	game = models.ForeignKey(Game)
	winner = models.ForeignKey(User)
