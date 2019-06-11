from django.shortcuts import render

from GaoKao.model import GKNewsInfo
from ManHua import models
from ManHua.base_views import getPagingData
from ManHua.models import Category, HotData, MHDetail, MHDetailChapter, MHChapterPic


def ManHuaIndex(request):
    projects = models.ManHua.objects.all()
    return render(request, 'manhua_index.html', {"projects": projects})


def JsonMHCategoryView(request):
    return getPagingData(request, Category)


def JsonMHHotDataView(request):
    return getPagingData(request, HotData)


def JsonMHDetailView(request):
    return getPagingData(request, MHDetail)


def JsonMHDetailChapterView(request):
    return getPagingData(request, MHDetailChapter)


def JsonMHChapterPicView(request):
    return getPagingData(request, MHChapterPic)
