from django.db import models
from phase import Phase
from users import User
from cards import Card

class Turn(models.Model):
	phase = models.ForeignKey(Phase)
	player = models.ForeignKey(User)
	start_hand = models.ForeignKey(Card)
	draw = models.ForeignKey(Card)
	end_hand = models.ForeignKey(Card)
	played = models.ForeignKey(Card)
	target = models.ForeignKey(User)
	eliminated = models.Boolean()
