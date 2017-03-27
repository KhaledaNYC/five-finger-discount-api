from django.db import models
from phases.models import Phase
from users.models import User
from cards.models import Card

class Turn(models.Model):
	phase = models.ForeignKey(Phase,related_name='turn_phase')
	player = models.ForeignKey(User,related_name='turn_player')
	start_hand = models.ForeignKey(Card, related_name='turn_card')
	draw = models.ForeignKey(Card,related_name='turn_draw')
	end_hand = models.ForeignKey(Card,related_name='turn_end_hand')
	played = models.ForeignKey(Card,related_name='turn_played')
	target = models.ForeignKey(User,related_name='turn_target')
	eliminated = models.BooleanField()
