from django.db import models


class SubMovieInfo(models.Model):
    # id = models.AutoField(auto_created=True, primary_key=True)
    pid = models.IntegerField(primary_key=True, default=1).auto_created
    name = models.TextField(max_length=50, default='', null=True)
    pic = models.TextField(max_length=50, default='', null=True)
    url = models.TextField(max_length=50, default='', null=True)
    update_time = models.TextField(max_length=50, default='', null=True)
    intro = models.TextField(max_length=50, default='', null=True)
    capture_pic = models.TextField(max_length=50, default='', null=True)


class SubMovieDownload(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    pid = models.ForeignKey(SubMovieInfo)
    fj_name = models.TextField(max_length=50, default='', null=True)
    fj_download_url = models.TextField(max_length=50, default='', null=True)


class SubMovieLastestInfo(models.Model):
    id = models.IntegerField(primary_key=True, default=1).auto_created
    pid = models.ForeignKey(SubMovieInfo)
    fj_number = models.TextField(max_length=50, default='', null=True)
    # fj_name = models.ForeignKey(SubMovieDownload)
    # fj_download_url = models.ForeignKey(SubMovieDownload)
