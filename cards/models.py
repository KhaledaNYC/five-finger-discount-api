from django.db import models

class Card(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 30)
	rank = models.IntegerField()
	image = models.ImageField()

	# CARD_ACTIONS = (
	# 	(ELIMINATE, 'Eliminate'),
	# 	(TRADE, 'Trade'),
	# 	(REVEAL, 'Reveal'),
	# 	(DISCARD, 'Discard'),
	# 	(IMMUNITY, 'Immunity'),
	# 	(DUEL, 'Duel'),
	# )
	action = models.CharField(max_length = 30)
