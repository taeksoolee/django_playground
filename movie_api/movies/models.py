from imp import NullImporter
from importlib.metadata import requires
from django.db import models

from directors.models import Director

class Movie(models.Model):
  # MovieType = models.TextChoices('Action', 'Thriller')

  class MovieType(models.TextChoices):
        Action = 'Action', '액션'
        Thriller = 'Thriller', '스릴러'

  title = models.CharField(max_length=30)
  description = models.CharField(blank=False, max_length=255)
  movie_type = models.CharField(blank=True, choices=MovieType.choices, max_length=20)
  opening_year = models.DateField()
  director_id = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)

  class Meta:
      # unique_together = ['album', 'order']
      ordering = ['title']

  def __str__(self):
    return self.title
