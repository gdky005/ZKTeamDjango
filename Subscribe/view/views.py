from pymysql import Error

from ZKUser.models import ZKUser
from utils.Email import send
from django.shortcuts import render
from Subscribe.model.sub_models import SubInfo
from Subscribe.model.sub_movie_models import SubMovieLastestInfo, SubMovieDownload
from Subscribe.view.wx_views import wxNotify, wxSendMsg
from Subscribe.view.base_views import getHttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def show(request):
    subs = SubInfo.objects.all()
    return render(request, 'index_sub.html', {"subs": subs})


# 获取用户订阅信息
def jsonShow(request):
    return sendJsonResponse(request, SubInfo)


# 测试邮件系统。
def notifyMsg2User(notifyData):
    # 邮件通知
    print("正在处理 邮件通知")

    notifyResponse = {}

    for data in notifyData:
        name = data.name
        pid = data.pid
        url = data.url
        new_number = data.new_number

        movieDownload = SubMovieDownload.objects.filter(pid=pid).values()[0]
        fjUrl = movieDownload.get("fj_download_url")

        notifyDataResponse = {}

        subInfoList = SubInfo.objects.filter(pid=pid)
        for subInf in subInfoList:
            zkUsers = subInf.zk_user.all()

            zkUserResponse = {}

            for zkUser in zkUsers:
                userName = zkUser.username
                userEmail = zkUser.email
                userWXOpenid = zkUser.wx_openid

                emailUserName = userName

                emailTitle = name + " 更新到 第" + new_number + "集！"
                emailDetail = '''
                            hi, {emailUserName}, 您订阅的 {name}（{pid}） 已经更新到 {new_number} 啦！当前订阅内容是的最新资源是：

                                {fjUrl}

                            请拷贝连接，使用迅雷下载，后期将默认添加调用迅雷 or 小米路由器。
                            需要了解详情可以去官网查看：{url}''' \
                    .format(emailUserName=emailUserName, name=name, pid=pid, url=url, new_number=new_number,
                            fjUrl=fjUrl)

                print("查询用户信息：userName=" + userName + ", userEmail=" + userEmail + ", userWXOpenid=" + userWXOpenid)

                zkUserResponse = {"sendUser": userEmail, "sendUserName": userName, "sendWXOpenid": userWXOpenid}

                # 发送邮件内容
                emailResponse = send(emailTitle, emailDetail, userEmail, userName)
                zkUserResponse["emailType"] = emailResponse

                # 发送微信消息通知
                wxResponse = wxSendMsg(userWXOpenid,
                          "http://www.zkteam.cc",
                          "您订阅的 《" + name + "》有更新啦！",
                          "最新一集是：第" + new_number + "集",
                          "已经通过邮件和微信给您通知啦",
                          "您可以点击详情将最新一集下载到您的 路由器 或者 电脑上。", "json")
                zkUserResponse["wxType"] = wxResponse
                notifyDataResponse[userName] = zkUserResponse

        notifyResponse[pid] = notifyDataResponse

    return notifyResponse


def jsonFJUpdate(request):
    notifyData = []

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
                    notifyData.append(subInfo)

    projects = list(notifyData)
    notifyResponseData = notifyMsg2User(notifyData)
    response = {"notifyData": projects, "notifyResponseData": notifyResponseData}

    return getHttpResponse(0, "ok", response)


# 获取更新表的信息
def jsonLastInfo(request):
    return sendJsonResponse(request, SubMovieLastestInfo)


def addData(request):
    uid = request.GET.get("user_id")
    # jid = request.GET.get("id")
    pid = request.GET.get("pid")
    name = request.GET.get("name")
    url = request.GET.get("url")
    number = request.GET.get("number")
    des = request.GET.get("des")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    if not uid:
        return getHttpResponse(10000, "Error", "uid not null!")

    try:
        maxData = 100  # 默认取100条数据

        subInfoObj = SubInfo.objects.get_or_create(pid=pid, name=name, url=url, des=des, new_number=number)[0]
        userObj = ZKUser.objects.get(id=uid)
        SubInfo.objects.filter(pid=subInfoObj.pid).first().zk_user.add(userObj)

        return getHttpResponse(0, "ok", subInfoObj)
    except Exception as e:
        return getHttpResponse(10000, "Error", "" + str(e))


def jsonQueryInfo(request):
    des = request.GET.get("des")

    if not des:
        return getHttpResponse(10000, "Error", "des not null!")

    try:
        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据

        project = SubInfo.objects.filter(des=des).values()
        return getHttpResponse(0, "ok", project)
    except Error:
        return getHttpResponse(10000, "Error", "")


def query(request):
    pid = request.GET.get("pid")

    if not pid:
        return getHttpResponse(10000, "Error", "pid not null!")

    try:
        # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据

        project = SubInfo.objects.filter(pid=pid).values()

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
        SubInfo.objects.filter(pid=pid).delete()

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
            if obj == SubInfo:
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
