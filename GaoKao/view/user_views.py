from pymysql import Error

from ZKUser.models import ZKUser
from django.contrib import auth
from django.shortcuts import render
from Subscribe.view.base_views import getHttpResponse
from django.views.decorators.csrf import csrf_exempt


# 用户注册
@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST' or request.method == "OPTIONS":
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
            # 去除邮箱
        # if not request.POST.get('email'):
        #     errors.append('邮箱不能为空')
        # else:
        #     email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        # 暂时去除邮箱
        # if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
        if account is not None and password is not None and password2 is not None and CompareFlag:
            try:
                user = ZKUser.objects.create_user(account, email, password)
                user.save()

                userlogin = auth.authenticate(username=account, password=password)
                auth.login(request, userlogin)

                userInfo = get_user_info(userlogin)
                return getHttpResponse(0, "ok", userInfo)
            except Exception as e:
                baseException = e.args
                errorCode = baseException[0]
                errorMsg = baseException[1]

                if errorCode == 1062:
                    errorMsg = "该用户名已经注册：" + errorMsg

                return getHttpResponse(errorCode, "error", errorMsg)

    return render(request, 'blog/register.html', {'errors': errors})


# 用户登录
@csrf_exempt
def my_login(request):
    errors = []
    account = None
    password = None
    if request.method == "POST" or request.method == "OPTIONS":
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
    userInfo.__setitem__("user_id", user.id)
    userInfo.__setitem__("wx_openid", user.wx_openid)
    userInfo.__setitem__("username", user.username)
    userInfo.__setitem__("email", user.email)
    userInfo.__setitem__("is_active", user.is_active)
    return userInfo


# 获取用户关键数据信息 // 等待写入
def jsonUserInfo(request):
    try:
        allUser = []

        users = ZKUser.objects.all()

        for user in users:
            zkUser = get_user_info(user)
            allUser.append(zkUser)

        projects = list(allUser)

        return getHttpResponse(0, "ok", projects)
    except Error as e:
        return getHttpResponse(10000, "Error", "")
