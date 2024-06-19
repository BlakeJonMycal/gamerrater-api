from django.db import models
from django.contrib.auth.models import User

class GameImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image_created")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_image")
    img = models.URLField(max_length=200)
