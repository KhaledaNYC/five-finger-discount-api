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
	winner = models.ForeignKey(User,related_name='game_winner')
	rounds_to_win = models.IntegerField(default = 0)

class Phase(models.Model):
	game = models.ForeignKey(Game,related_name='phase_game')
	winner = models.ForeignKey(User, related_name='phase_winner')

class Score(models.Model):
	game = models.ForeignKey(Game,related_name='score_game')
	player = models.ForeignKey(User, related_name='score_player')
	score = models.IntegerField(default = 0)

class Turn(models.Model):
	phase = models.ForeignKey(Phase,related_name='turn_phase')
	player = models.ForeignKey(User,related_name='turn_player')
	start_hand = models.ForeignKey(Card, related_name='turn_card')
	draw = models.ForeignKey(Card,related_name='turn_draw')
	end_hand = models.ForeignKey(Card,related_name='turn_end_hand')
	played = models.ForeignKey(Card,related_name='turn_played')
	target = models.ForeignKey(User,related_name='turn_target')
	eliminated = models.BooleanField()
