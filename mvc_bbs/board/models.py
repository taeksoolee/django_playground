from django.db import models

class BbsReple(models.Model):
  text = models.CharField(max_length=200)

  def __str__(self) -> str:
      return self.text

# Create your models here.
class BbsBoard(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=255)

  reples = models.ManyToOneRel(BbsReple, null=True, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title


