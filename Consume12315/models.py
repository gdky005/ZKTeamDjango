from django.db import models


# Create your models here.
class ConsumeDetail(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    number = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()

