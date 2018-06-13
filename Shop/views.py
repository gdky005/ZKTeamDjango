import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dss.Serializer import serializer
from pymysql import Error

from Shop import models
from Shop.ResultResponse import ResultResponse


def shop(request):
    projects = models.ShopInfo.objects.all()
    return render(request, 'index_shop.html', {"shops": projects})


def jsonShow(request):
    return sendJsonResponse(request, models.ShopInfo)


def addData(request):
    id = request.GET.get("id")
    pid = request.GET.get("pid")
    name = request.GET.get("name")
    price = request.GET.get("price")
    des = request.GET.get("des")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        maxData = 100 #默认取100条数据

        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        # data = list(projects)
        # return getHttpResponse(0, "ok", data)

        obj = models.ShopInfo(id=id, name=name, price=price, des=des, pid=pid)
        obj.save()

        return getHttpResponse(0, "ok", "")
    except Error:
        return getHttpResponse(10000, "Error", "")


def query(request):
    pid = request.GET.get("pid")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        maxData = 5 #默认取100条数据

        projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        data = list(projects)
        return getHttpResponse(0, "ok", data)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
                        content_type="application/json")
    # return HttpResponse(data, content_type="application/json")


# 发送通用的 Json Response
def sendJsonResponse(request, obj):
    maxData = 5
    page = 0
    jid = request.GET.get("id")
    count = request.GET.get("pageCount")
    currentPage = request.GET.get("page")

    if count:
        maxData = int(count)

    if currentPage:
        page = int(currentPage)

    try:
        # projects = models.ProjectInfo.objects.all()

        if jid is not None:
            if obj == models.ShopInfo:
                obj = obj.objects.filter(id=jid)
            else:
                try:
                    obj = obj.objects.filter(id=jid)
                except:
                    obj = obj.objects.filter(id=jid)
                pass
        else:
            obj = obj.objects

        project_info = obj.values()[page * maxData:(page + 1) * maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")
