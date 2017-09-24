from django.shortcuts import render

from Consume12315 import models
import json
from pymysql import Error
from django.http import HttpResponse
from dss.Serializer import serializer
from api.ResultResponse import ResultResponse
# Create your views here.


def Consume12315(request):
    projects = models.ConsumeDetail.objects.all()
    return render(request, 'consume12315_index.html', {"projects": projects})


def Consume12315Json(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        # projects = models.ProjectInfo.objects.all()

        project_info = models.ConsumeDetail.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")