import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dss.Serializer import serializer
from pymysql import Error

from api import models
from api.ResultResponse import ResultResponse


# Create your views here.
def show(request):
    user_list = models.UserInfo.objects.all()  # 取出该表所有的数据

    return render(request, "show.html", {"user_list": user_list})


def movie(request):
    maxData = int(request.GET.get("pageCount"))
    movie_list = models.MovieInfo.objects.all()[:maxData]  # 取出该表所有的数据

    return render(request, "movie.html", {"movie_list": movie_list})


def jsonMovie(request):
    maxData = 5

    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        movie_list = models.MovieInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        word = list(movie_list)
        # data = json.dumps(word)  # 把list转成json

        resultResponse = ResultResponse(0, "ok", word)

        return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
                            content_type="application/json")
        # return HttpResponse(data, content_type="application/json")
    except Error:
        resultResponse = ResultResponse(10000, "Error", "")

        return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
                            content_type="application/json")


def home(request):
    return render(request, 'index.html')


def page_not_found(request):
    return render_to_response('')
