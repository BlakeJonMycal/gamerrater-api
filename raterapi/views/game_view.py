from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from raterapi.models import Game, Category
from django.contrib.auth.models import User

class GameView(ViewSet):



    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        # Get the data from the client's JSON payload
        title = request.data.get('title')
        description = request.data.get('description')
        designer = request.data.get('designer')
        year_released = request.data.get('year_released')
        number_of_players = request.data.get('number_of_players')
        estimated_play_time = request.data.get('estimated_play_time')
        age_recommendation = request.data.get('age_recommendation')




        # Create a book database row first, so you have a
        # primary key to work with
        game = Game.objects.create(
            user=request.user,
            title=title,
            description=description,
            designer=designer,
            year_released=year_released,
            number_of_players=number_of_players,
            estimated_play_time=estimated_play_time,
            age_recommendation=age_recommendation)

        # Establish the many-to-many relationships
        category_ids = request.data.get('categories', [])
        game.categories.set(category_ids)

        serializer = GameSerializer(game, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)


    class Meta:
        model = Game
        fields = ( 'id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'estimated_play_time', 'age_recommendation', 'categories'  )
