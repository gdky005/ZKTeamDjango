from django.db import models


class GKRecommendInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    title = models.TextField()
    imgUrl = models.TextField()
    url = models.TextField()


class GKCategoryInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    title = models.TextField()
    imgUrl = models.TextField()
    url = models.TextField()


class GKNewsInfo(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    title = models.TextField()
    imgUrl = models.TextField()
    url = models.TextField()

    class Meta:
        ordering = ['-id']

