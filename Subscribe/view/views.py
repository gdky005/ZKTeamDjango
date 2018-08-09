from pymysql import Error
from Subscribe import models
from utils.Email import send
from django.shortcuts import render
from Subscribe.models import SubInfo, SubMovieLastestInfo, SubMovieDownload
from Subscribe.view.wx_views import wxNotify
from Subscribe.view.base_views import getHttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def show(request):
    subs = models.SubInfo.objects.all()
    return render(request, 'index_sub.html', {"subs": subs})


# 获取用户订阅信息
def jsonShow(request):
    return sendJsonResponse(request, models.SubInfo)


def notifyMsg2User(emailList):
    # send("我是测试主题，", "我是测试内容！")
    emailNotify(emailList)
    wxNotify(emailList)


# 测试邮件系统。
def emailNotify(emailList):
    # 邮件通知
    print("正在处理 邮件通知")
    for data in emailList:
        name = data.name
        pid = data.pid
        url = data.url
        new_number = data.new_number

        movieDownload = SubMovieDownload.objects.filter(pid=pid).values()[0]
        fjUrl = movieDownload.get("fj_download_url")

        emailTitle = name + " 更新到 第" + new_number + "集！"
        emailDetail = '''
            hi, 小同学, 您订阅的 {name}（{pid}） 已经更新到 {new_number} 啦！当前订阅内容是的最新资源是：
        
                {fjUrl}
        
            请拷贝连接，使用迅雷下载，后期将默认添加调用迅雷 or 小米路由器。
            需要了解详情可以去官网查看：{url}''' \
            .format(name=name, pid=pid, url=url, new_number=new_number, fjUrl=fjUrl)
        send(emailTitle, emailDetail)


def jsonFJUpdate(request):
    emailList = []

    lastInfos = SubMovieLastestInfo.objects.all()
    subInfos = SubInfo.objects.all()

    for lastInfo in lastInfos:
        fj_number = lastInfo.fj_number
        pid_id = lastInfo.id

        for subInfo in subInfos:
            subPid = int(subInfo.pid)
            subNumber = subInfo.new_number

            if pid_id == subPid:
                if int(fj_number) > int(subNumber):
                    subInfo.new_number = fj_number
                    emailList.append(subInfo)

    projects = list(emailList)

    notifyMsg2User(emailList)

    return getHttpResponse(0, "ok", projects)


# 获取更新表的信息
def jsonLastInfo(request):
    return sendJsonResponse(request, models.SubMovieLastestInfo)


def addData(request):
    jid = request.GET.get("id")
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

        obj = models.SubInfo(id=jid, name=name, url=url, des=des, pid=pid, new_number=number)
        obj.save()

        return getHttpResponse(0, "ok", "")
    except Error:
        return getHttpResponse(10000, "Error", "")


def jsonQueryInfo(request):
    des = request.GET.get("des")

    if not des:
        return getHttpResponse(10000, "Error", "des not null!")

    try:
        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据

        project = models.SubInfo.objects.filter(des=des).values()
        return getHttpResponse(0, "ok", project)
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
