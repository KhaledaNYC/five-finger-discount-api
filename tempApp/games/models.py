from django.db import models
from django.apps import apps
from users import User

class Game(models.Model):
	winner = models.ForeignKey(apps.get_model('users', User))
	rounds_to_win = models.IntegerField(default = 0)
