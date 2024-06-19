from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_play_time = models.CharField(max_length=255)
    age_recommendation = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_created")

    categories = models.ManyToManyField(
        "Category",
        through="GameCategory",
        related_name="game_set"
    )