from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie # model 설정
  
    fields = ('id', 'title', 'description', 'movie_type', 'opening_year', 'director_id')