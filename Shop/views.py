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


def addData(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    price = request.GET.get("price")
    des = request.GET.get("des")

    if not id:
        return getHttpResponse(10000, "Error", "id not null!")

    try:
        maxData = 100 #默认取100条数据

        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        # data = list(projects)
        # return getHttpResponse(0, "ok", data)

        obj = models.ShopInfo(id=id, name=name, price=price, des=des)
        obj.save()

        return getHttpResponse(0, "ok", "")
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
                        content_type="application/json")
    # return HttpResponse(data, content_type="application/json")