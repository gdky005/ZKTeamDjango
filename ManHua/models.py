from django.db import models
from django.contrib import admin


# Create your models here.
class ManHua(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    jid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()

    class Meta:
        ordering = ['id']


class Category(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()

    class Meta:
        # db_table = 'ManHua_category'
        ordering = ['id']
        verbose_name_plural = '漫画分类表'

    class ShowItem(admin.ModelAdmin):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'name', 'url')


class HotData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    picUrl = models.TextField()
    newPage = models.TextField()

    class Meta:
        verbose_name_plural = '热门'
        ordering = ['id']

    class ShowItem(admin.ModelAdmin):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'name', 'picUrl', 'newPage')


class MHDetail(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    author = models.TextField()
    picUrl = models.TextField()
    state = models.TextField()
    time = models.TextField()
    detail = models.TextField()
    category = models.TextField()
    tag = models.TextField()

    class Meta:
        verbose_name_plural = '漫画详情'
        ordering = ['id']

    class ShowItem(admin.ModelAdmin):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'name', 'author', 'picUrl', 'state', 'time', 'detail', 'category', 'tag')


class MHDetailChapter(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    url = models.TextField()
    pCount = models.TextField()
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '漫画章节'
        ordering = ['id']

    class ShowItem(admin.ModelAdmin):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'name', 'url', 'pCount', 'count')


class MHChapterPic(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    mid2 = models.TextField()
    picUrl = models.TextField()
    count = models.IntegerField()
    sourceUrl = models.TextField()

    class Meta:
        verbose_name_plural = '漫画图片'
        ordering = ['id']

    class ShowItem(admin.ModelAdmin):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'mid2', 'picUrl', 'count', 'sourceUrl')
