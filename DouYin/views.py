from django.shortcuts import render

# Create your views here.
from DouYin import models


def DouYin(request):
    return render(request, "DouYin.html")


def VideoInfo(request):
    projects = models.VideoList.objects.all()
    return render(request, 'dou_yin_video.html', {"projects": projects})
