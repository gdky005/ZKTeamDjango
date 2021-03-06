from django.db import models


# Create your models here.
from django.utils import timezone


class ShopInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    pid = models.TextField(max_length=50)
    name = models.TextField(max_length=50, default='', null=True)
    price = models.IntegerField(default=0, null=True)
    des = models.TextField(max_length=50, default='', null=True)
    add_date = models.DateTimeField(u'添加时间', auto_now_add=True, editable=True, null=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
