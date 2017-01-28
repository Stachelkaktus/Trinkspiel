from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    sips_game = models.IntegerField = 0
    shots_game = models.IntegerField = 0
    sips_total = models.IntegerField = 0
    shots_total = models.IntegerField = 0
    gender = (
        ('male', 'männlich'),
        ('female', 'weiblich'),
    )

class Game(models.Model):
    difficulty = models.IntegerField = 1
    players = models.ManyToManyField(Player)

class Task(models.Model):
    target = Player
    task = models.CharField(max_length=500)