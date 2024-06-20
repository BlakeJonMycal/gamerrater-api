from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from raterapi.models import Game
from django.contrib.auth.models import User

class GameView(ViewSet):
    """Rock view set"""



    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
        


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Game
        fields = ( 'id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'estimated_play_time', 'age_recommendation'  )
