from django.shortcuts import render
from .serializers import DirectorSerializer
from .models import Director
from rest_framework import viewsets

# Create your views here.
class DirectorViewSet(viewsets.ModelViewSet):
  queryset = Director.objects.all()
  serializer_class = DirectorSerializer