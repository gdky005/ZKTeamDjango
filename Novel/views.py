from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from dss.Serializer import serializer
from pymysql import Error

from Novel import models
from Novel.base_views import getPagingData
from Novel.models import NovelDetailData, NovelData
from api.ResultResponse import ResultResponse


def novel(request):
    projects = models.NovelData.objects.all()
    return render(request, "novel.html")


@cache_page(60 * 5)
def jsonDetailNovel(request):
    return getPagingData(request, NovelDetailData)


@cache_page(60 * 5)
def jsonNovel(request):
    return getPagingData(request, NovelData)


def jsonSearch(request):
    pid = request.GET.get("pid")
    if pid:
        pid = int(pid)

    try:
        project_info = models.NovelDetailData.objects.filter(pid=pid).values()[0]
        return getHttpResponse(0, "ok", project_info)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")
