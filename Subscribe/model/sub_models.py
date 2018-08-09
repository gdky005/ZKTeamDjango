from django.db import models


# Create your models here.
class SubInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    # pid = models.TextField(max_length=50)
    # 创建多对多的关系
    # cid = models.ManyToManyField(to="Class", name="teacher")
    pid = models.ManyToManyField(to="ZKUser.ZKUser", name="pid")

    name = models.TextField(max_length=50, default='', null=True)
    url = models.TextField(max_length=50, default='', null=True)
    des = models.TextField(max_length=50, default='', null=True)
    new_number = models.TextField(max_length=50, default='', null=True)
    add_date = models.DateTimeField(u'添加时间', auto_now_add=True, editable=True, null=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
