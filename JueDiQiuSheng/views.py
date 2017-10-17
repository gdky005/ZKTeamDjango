import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dss.Serializer import serializer
from pymysql import Error

from JueDiQiuSheng import models
from api.ResultResponse import ResultResponse


def JDQS(request):
    projects = models.JDQSCategory.objects.all()
    return render(request, "JDQS_index.html", {"projects": projects})


def JDQSJson(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        # projects = models.ProjectInfo.objects.all()

        project_info = models.JDQSCategory.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def JDQSDetail(request):
    projects = models.JDQSDetail.objects.all()
    return render(request, "JDQS_Detail.html", {"projects": projects})


# 发送通用的 Response
def sendResponse(request, obj, template_name):
    projects = obj.objects.all()
    return render(request, template_name, {"projects": projects})


# 发送通用的 Json Response
def sendJsonResponse(request, obj):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)
    try:
        # projects = models.ProjectInfo.objects.all()

        project_info = obj.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")