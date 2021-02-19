from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterprojectapi.models import Game


class Games(ViewSet):

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all()

        gamer = self.request.query_params.get('type', None)
        if gamer is not None:
            games = games.filter(gamer__id=gamer)

        serializer = GameSerializer(
                games, many=True, context={'request': request})
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'estimated_time_of_play' ,
        'age_recommendation', 'gamer')
        depth = 1
    

