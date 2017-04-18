from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=4)


class MovieInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.TextField(max_length=None)
    movieInfo = models.TextField(max_length=None)
    star = models.IntegerField(default=0)
    quote = models.TextField(max_length=None)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class MasterInfo(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.IntegerField(default=0)
    name = models.TextField(max_length=None)
    nick_name = models.TextField(max_length=None)
    img = models.TextField(max_length=None)
    info = models.TextField(max_length=None)
    isVip = models.BooleanField(default=False)
    index = models.IntegerField(default=0)
    blog = models.IntegerField(max_length=None)


class MasterArticle(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.IntegerField(default=0)
    name = models.TextField(max_length=None)
    nick_name = models.TextField(max_length=None)
    des = models.TextField(max_length=None)
    article_title = models.IntegerField(max_length=None)
    article_address = models.IntegerField(max_length=None)
