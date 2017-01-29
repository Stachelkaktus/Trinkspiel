from django.db import models

# Create your models here.

class Game(models.Model):
    difficulty = models.IntegerField = 1

class Player(models.Model):
    name = models.CharField(max_length=100)
    sips_game = models.IntegerField = 0
    shots_game = models.IntegerField = 0
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gender = (
        ('male', 'männlich'),
        ('female', 'weiblich'),
    )

class Task(models.Model):
    target = models.ForeignKey(Player)
    task = models.CharField(max_length=500)