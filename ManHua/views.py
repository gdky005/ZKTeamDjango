from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ManHua import models
from ManHua.base_views import getPagingData
from ManHua.models import Category, HotData, MHDetail, MHDetailChapter, MHChapterPic, MHBanner


@cache_page(60 * 15)  # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def ManHuaIndex(request):
    projects = models.ManHua.objects.all()
    return render(request, 'manhua_index.html', {"projects": projects})


@cache_page(60 * 5)
def JsonMHCategoryView(request):
    print("开始读取 分类 数据")
    return getPagingData(request, Category)


@cache_page(60 * 5)
def JsonMHHotDataView(request):
    return getPagingData(request, HotData)


@cache_page(60 * 5)
def JsonMHDetailView(request):
    return getPagingData(request, MHDetail)


@cache_page(60 * 5)
def JsonMHDetailChapterView(request):
    return getPagingData(request, MHDetailChapter)


@cache_page(60 * 5)
def JsonMHChapterPicView(request):
    return getPagingData(request, MHChapterPic)


@cache_page(60 * 5)
def JsonMHBannerView(request):
    return getPagingData(request, MHBanner)
