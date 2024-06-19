from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_rating")
    score = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ]

)
