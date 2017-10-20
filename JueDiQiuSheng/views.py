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


def JDQSCategory(request):
    projects = models.JDQSCategory.objects.all()
    return render(request, "JDQS_category_index.html", {"projects": projects})


def JDQSPicCategory(request):
    projects = models.JDQSPicCategory.objects.all()
    return render(request, "JDQS_pic_category_index.html", {"projects": projects})


def JDQSDetail(request):
    jid = request.GET.get("jid")
    if jid is not None:
        detail = models.JDQSContent.objects.get(jid_id=jid)
        return render(request, "JDQS_artifact_index.html", {"detail": detail})
    else:
        return JDQS(request)


def JDQSItem(request):
    projects = models.JDQSItem.objects.all()
    return render(request, "JDQS_item_index.html", {"projects": projects})


def JDQSPicUrl(request):
    projects = models.JDQSPicUrl.objects.all()
    return render(request, "JDQS_pic_url_item_index.html", {"projects": projects})


def JDQSContent(request):
    projects = models.JDQSContent.objects.all()
    return render(request, "JDQS_content_index.html", {"projects": projects})




def JDQSItemJson(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        project_info = models.JDQSItem.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def JDQSPicCategoryJson(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        project_info = models.JDQSPicCategory.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


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