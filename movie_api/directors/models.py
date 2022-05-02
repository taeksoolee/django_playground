from importlib.metadata import requires
from django.db import models

class Director(models.Model):
  name = models.CharField(max_length=30)
  birth = models.DateField()

  def __str__(self):
    return self.name
