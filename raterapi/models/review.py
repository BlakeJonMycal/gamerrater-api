from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_review")
    comment = models.TextField()
