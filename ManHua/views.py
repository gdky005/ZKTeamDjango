import json
from django.http import HttpResponse
from django.shortcuts import render

from dss.Serializer import serializer
from pymysql import Error

from ManHua import models
from api.ResultResponse import ResultResponse


def ManHuaIndex(request):
    projects = models.ManHua.objects.all()
    return render(request, 'manhua_index.html', {"projects": projects})


def xxx(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        # projects = models.xxx.objects.all()

        project_info = models.xxx.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")
