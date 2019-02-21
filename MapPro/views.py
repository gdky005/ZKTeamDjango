from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse
from django.shortcuts import render

from dss.Serializer import serializer
from pymysql import Error

from MapPro import models
from api.ResultResponse import ResultResponse


def show(request):
    return render(request, "map_shop.html")


def MapDataView(request):
    projects = models.MapData.objects.all()
    return render(request, 'MapData', {"projects": projects})


def MapDataView(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        # projects = models.xxx.objects.all()

        project_info = models.MapData.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")
