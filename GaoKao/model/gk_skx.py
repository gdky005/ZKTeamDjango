from django.db import models


class GKSKX(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    name = models.TextField()
    year = models.TextField()
    kind = models.TextField()
    ben1 = models.IntegerField(default=0)
    ben2 = models.IntegerField(default=0)
    gz = models.IntegerField(default=0)
