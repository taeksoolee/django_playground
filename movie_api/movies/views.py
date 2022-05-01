from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import viewsets

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer