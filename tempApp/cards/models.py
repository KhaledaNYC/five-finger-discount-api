from django.db import models

class Card(models.Model):
	name = models.CharField()
	description = models.CharField()
	rank = models.IntegerField()
	image = models.ImageField()

	CARD_ACTIONS = (
		(ELIMINATE, 'Eliminate'),
		(TRADE, 'Trade'),
		(REVEAL, 'Reveal'),
		(DISCARD, 'Discard'),
		(IMMUNITY, 'Immunity'),
		(DUEL, 'Duel'),
	)
	action = models.CharField(choices = CARD_ACTIONS)
