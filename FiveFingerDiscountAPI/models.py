from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 30)
	avatar = models.ImageField()

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


class Game(models.Model):
	winner = models.ForeignKey(User)
	rounds_to_win = models.IntegerField(default = 0)

class Phase(models.Model):
	game = models.ForeignKey(Game)
	winner = models.ForeignKey(User)

class Score(models.Model):
	game = models.ForeignKey(Game)
	player = models.ForeignKey(User)
	score = models.IntegerField(default = 0)

class Turn(models.Model):
	phase = models.ForeignKey(Phase)
	player = models.ForeignKey(User)
	start_hand = models.ForeignKey(Card)
	draw = models.ForeignKey(Card)
	end_hand = models.ForeignKey(Card)
	played = models.ForeignKey(Card)
	target = models.ForeignKey(User)
	eliminated = models.BooleanField()
