from django.db import models
from phases.models import Phase
from players.models import Player
from cards.models import Card

class Turn(models.Model):
	phase = models.ForeignKey(Phase,related_name='turn_phase')
	player = models.ForeignKey(Player,related_name='turn_player')
	start_hand = models.ForeignKey(Card, related_name='turn_card')
	draw = models.ForeignKey(Card,related_name='turn_draw')
	end_hand = models.ForeignKey(Card,related_name='turn_end_hand')
	played = models.ForeignKey(Card,related_name='turn_played')
	target = models.ForeignKey(Player,related_name='turn_target')
	eliminated = models.BooleanField()
