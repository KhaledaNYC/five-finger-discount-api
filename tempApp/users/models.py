from django.db import models

class User(models.Model):
	username = models.CharField()
	avatar = models.ImageField()
