from django.db import models


class GKSKX(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    year = models.TextField()
    kind = models.TextField()
    pici = models.TextField()
    scoreLine = models.TextField()
