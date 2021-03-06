#!usr/bin/python
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dss.Serializer import serializer
from pymysql import Error

from api import models
from api.ResultResponse import ResultResponse


# Create your views here.
def masterInfo(request):
    users = models.MasterInfo.objects.all()  # 取出该表所有的数据

    return render(request, "master_info.html", {"users": users})


def jsonMasterInfo(request):
    maxData = 5

    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        users = models.MasterInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        user_list = list(users)
        # data = json.dumps(word)  # 把list转成json

        return getHttpResponse(0, "ok", user_list)
    except Error:
        return getHttpResponse(10000, "Error", "")


def masterArticle(request):
    uid = request.GET.get("uid")
    user_article = models.MasterArticle.objects.filter(uid=uid)

    return render(request, "master_article.html", {"user_article": user_article})


def jsonMasterArticle(request):
    maxData = 5
    uid = request.GET.get("uid")
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        master_article = models.MasterArticle.objects.filter(uid=uid).values()[:maxData]  # 取出该表所有的数据
        article = list(master_article)
        # data = json.dumps(word)  # 把list转成json

        return getHttpResponse(0, "ok", article)
    except Error:
        return getHttpResponse(10000, "Error", "")


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

        return getHttpResponse(0, "ok", word)
    except Error:
        return getHttpResponse(10000, "Error", "")


def getHttpResponse(code, message, word):
    resultResponse = ResultResponse(code, message, word)
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
                        content_type="application/json")
    # return HttpResponse(data, content_type="application/json")


def home(request):
    return render(request, 'index.html')


def page_not_found(request):
    return render_to_response('')
