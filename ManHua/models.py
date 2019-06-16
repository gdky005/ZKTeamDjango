import xadmin
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

    def __str__(self):
        return self.name

    # class ShowItem(admin.ModelAdmin):
    #     # 需要显示的字段信息
    #     list_display = ('id', 'mid', 'name', 'url')


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

    def __str__(self):
        return self.name

    # class ShowItem(admin.ModelAdmin):
    #     # 需要显示的字段信息
    #     list_display = ('id', 'mid', 'name', 'author', 'picUrl', 'state', 'time', 'detail', 'category', 'tag')


class CategoryForCategoryId(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    cid = models.ForeignKey(Category)
    mid = models.ForeignKey(MHDetail)

    class Meta:
        # db_table = 'ManHua_category'
        ordering = ['id']
        verbose_name_plural = '某分类下的具体漫画'

    def __str__(self):
        return self.cid


class HotData(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    picUrl = models.TextField()
    newPage = models.TextField()

    class Meta:
        verbose_name_plural = '热门'
        ordering = ['id']

    def __str__(self):
        return self.name
    #
    # class ShowItem(admin.ModelAdmin):
    #     # 需要显示的字段信息
    #     list_display = ('id', 'mid', 'name', 'picUrl', 'newPage')


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

    def __str__(self):
        return self.name

    # class ShowItem(admin.ModelAdmin):
    #     # 需要显示的字段信息
    #     list_display = ('id', 'mid', 'name', 'url', 'pCount', 'count')


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

    class ShowXItem(object):
        # 需要显示的字段信息
        list_display = ('id', 'mid', 'mid2', 'picUrl', 'count', 'sourceUrl')

        # class BannerAdmin(object):
        #     list_display = ['title', 'image', 'url', 'index', 'add_time']
        #     search_fields = ['title', 'image', 'url', 'index']
        #     list_filter = ['title', 'image', 'url', 'index', 'add_time']


class MHBanner(models.Model):
    id = models.IntegerField(primary_key=True).auto_created
    mid = models.IntegerField()
    name = models.TextField()
    picUrl = models.TextField()

    class Meta:
        verbose_name_plural = '漫画推荐位'
        ordering = ['id']

    def __str__(self):
        return self.name
