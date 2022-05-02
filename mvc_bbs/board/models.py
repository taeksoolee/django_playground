from django.db import models

# Create your models here.
class BbsBoard(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=255)

  def __str__(self) -> str:
      return self.title