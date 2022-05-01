from dataclasses import fields
from rest_framework import serializers

from .models import Director

class DirectorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Director # model 설정
    fields = ('id', 'name', 'birth')
    