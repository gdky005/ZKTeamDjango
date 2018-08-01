import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymysql import Error

from Subscribe import models
from ZKTeam import settings
from api.ResultResponse import ResultResponse
from dss.Serializer import serializer

from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


# Create your views here.


@login_required
def show(request):
    subs = models.SubInfo.objects.all()
    return render(request, 'index_sub.html', {"subs": subs})


# @login_required
def jsonShow(request):
    return sendJsonResponse(request, models.SubInfo)


def addData(request):
    id = request.GET.get("id")
    pid = request.GET.get("pid")
    name = request.GET.get("name")
    url = request.GET.get("url")
    number = request.GET.get("number")
    des = request.GET.get("des")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        maxData = 100  # 默认取100条数据

        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
        # data = list(projects)
        # return getHttpResponse(0, "ok", data)

        obj = models.SubInfo(id=id, name=name, url=url, des=des, pid=pid, new_number=number)
        obj.save()

        return getHttpResponse(0, "ok", "")
    except Error:
        return getHttpResponse(10000, "Error", "")


def query(request):
    pid = request.GET.get("pid")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据

        project = models.SubInfo.objects.filter(pid=pid).values()

        if project.__len__() > 0:
            project = project[0]
        else:
            project = ''

        data = project
        return getHttpResponse(0, "ok", data)
    except Error:
        return getHttpResponse(10000, "Error", "")


# 删除指定的 pid
def delete(request):
    pid = request.GET.get("pid")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        models.SubInfo.objects.filter(pid=pid).delete()

        return getHttpResponse(0, "ok", "")
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
        projects = models.SubInfo.objects.all()

        if jid is not None:
            if obj == models.SubInfo:
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


# 用户注册
@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('邮箱不能为空')
        else:
            email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
            user = User.objects.create_user(account, email, password)
            user.save()

            userlogin = auth.authenticate(username=account, password=password)
            auth.login(request, userlogin)

            userInfo = get_user_info(userlogin)
            return getHttpResponse(0, "ok", userInfo)

    return render(request, 'blog/register.html', {'errors': errors})


# 用户登录
@csrf_exempt
def my_login(request):
    errors = []
    account = None
    password = None
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = auth.authenticate(username=account, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    userInfo = get_user_info(user)
                    return getHttpResponse(0, "ok", userInfo)
                else:
                    return getHttpResponse(10000, "Error", "用户名错误")
            else:
                return getHttpResponse(10000, "Error", "用户名或密码错误")
    return render(request, 'blog/login.html', {'errors': errors})


# 用户退出
def my_logout(request):
    auth.logout(request)
    return getHttpResponse(0, "ok", "退出成功！")


def get_user_info(user):
    userInfo = {}
    userInfo.__setitem__("username", user.username)
    userInfo.__setitem__("email", user.email)
    userInfo.__setitem__("is_active", user.is_active)
    return userInfo
