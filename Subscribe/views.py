import json
from xml.etree import ElementTree

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str
from pymysql import Error

from Subscribe import models
from Subscribe.models import SubInfo, SubMovieLastestInfo, SubMovieDownload
from ZKTeam import settings
from ZKUser.models import ZKUser
from api.ResultResponse import ResultResponse
from dss.Serializer import serializer

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from utils.Constant import WXConstant
from utils.Email import send

# import hashlib
# import json
# from lxml import etree
# from django.utils.encoding import smart_str
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# from auto_reply.views import auto_reply_main  # 修改这里
#
#
# # Create your views here.
#
# WEIXIN_TOKEN = 'write-a-value'
#
# @csrf_exempt
# def weixin_main(request):
#     """
#     所有的消息都会先进入这个函数进行处理，函数包含两个功能，
#     微信接入验证是GET方法，
#     微信正常的收发消息是用POST方法。
#     """
#     if request.method == "GET":
#         signature = request.GET.get("signature", None)
#         timestamp = request.GET.get("timestamp", None)
#         nonce = request.GET.get("nonce", None)
#         echostr = request.GET.get("echostr", None)
#         token = WEIXIN_TOKEN
#         tmp_list = [token, timestamp, nonce]
#         tmp_list.sort()
#         tmp_str = "%s%s%s" % tuple(tmp_list)
#         tmp_str = hashlib.sha1(tmp_str).hexdigest()
#         if tmp_str == signature:
#             return HttpResponse(echostr)
#         else:
#             return HttpResponse("weixin  index")
#     else:
#         xml_str = smart_str(request.body)
#         request_xml = etree.fromstring(xml_str)
#         response_xml = auto_reply_main(request_xml)# 修改这里
#         return HttpResponse(response_xml)

import hashlib


# 测试数据：/Subscribe/weiXin/?signature=5e1c55f68fa10321419b62b171d3518a398096f3&echostr=7370345721803176943&timestamp=1533393832&nonce=2102056081, zkteam 服务器返回类似：6801932741839289079
# 微信服务器的信息是：signature=5e1c55f68fa10321419b62b171d3518a398096f3, timestamp=1533393832, nonce=2102056081, echostr=7370345721803176943
def wxTemplateMsg(request):
    openid = 'oQrNzwaFHdvdufYEGZhz4cNwhznk' # 孤独狂饮的openid
    # template_id = '5U1Ykxvb00WBt9WpMpaBKFpC3UFszbhQHGaZ9alczy0' #订阅模板消息
    template_id = '4KOE8MczMCka1CW_q_BcegEzBVrAacFv81oEeVNTPRw' #预约服务提醒
    url = "http://www.zkteam.cc"
    data = {
        "content": {"value": "content！", "color": "#173177"},
        "first": {"value": "恭喜你购买成功！", "color": "#173177"},
        "keyword1": {"value": "这是预约内容！", "color": "#173177"},
        "keyword2": {"value": "服务说明！", "color": "#173177"},
        "remark": {"value": "感谢你的使用！", "color": "#173177"},
    }

    templeUrl = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
    token = WXConstant.wx_access_token

    paramsData = {"access_token": token,
                  "touser": openid,
                  "template_id": template_id,
                  "url": url,
                  "data": data}

    result = requests.post(templeUrl + "?access_token=" + token, json=paramsData).json()
    return getHttpResponse(0, "ok", result)


def wxAllTemplate(request):
    getTemplateId = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template'
    token = WXConstant.wx_access_token

    paramsData = {"access_token": token}

    result = requests.post(getTemplateId + "?access_token=" + token, json=paramsData).json()

    return getHttpResponse(0, "ok", result)


@csrf_exempt
def weiXin(request):
    response = None
    if request.method == "GET":
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')

        print("微信服务器的信息是：signature=" + str(signature) + ", timestamp=" + str(timestamp) + ", nonce=" + str(nonce) + ", echostr=" + str(echostr))

        token = "zkteam"
        tmpArr = [token,timestamp,nonce]
        tmpArr.sort()
        string = ''.join(tmpArr).encode('utf-8')
        string = hashlib.sha1(string).hexdigest()
        if string == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("false")
    elif request.method == "POST":
        responseData = responseMsg(request.body)
        print("wx：weiXin responseData" + str(responseData))

        response = HttpResponse(responseData, content_type="application/xml")
        print("wx：weiXin response" + str(response))
        return response

    return HttpResponse("false")


def responseMsg(postContent):
    print("收到的微信内容是：" + str(postContent))
    resultStr = ''

    postStr = smart_str(postContent)

    print("收到的微信内容smart_str后是：" + str(postStr))
    if postStr:
        msg = xmlContent2Dic(postStr)
        msgType = msg['MsgType']
        if msgType:
            print("收到的微信内容 MsgType 是：" + msgType)
            if msgType == 'event':
                resultStr = handleEvent(msg)  #处理事件推送
            elif msgType == 'text':
                resultStr = handleText(msg)  #处理消息文本推送
        else:
            resultStr = 'Input something...'

    return resultStr


# 处理微信的事件推送
def handleEvent(msg):
    resultStr = ''

    event = msg['Event']
    print("wx handleEvent：" + event)

    if event == 'subscribe':
        print("wx handleEvent subscribe：" + event)

        event_key = msg["EventKey"]
        print("wx handleEvent subscribe：" + event_key)

        subStr = "qrscene_"

        if subStr in event_key:
            event_key = str(event_key)
            user_id = event_key[event_key.rindex("_") + 1: event_key.__len__()]

            bindUser(user_id, msg["FromUserName"])
            resultStr = sendMsgForSubUser(event, msg, u'感谢您关注哦！你说啥，我说啥，哈哈哈 😆')
        else:
            # resultStr = sendMsgForSubUser(event, msg, u'你又扫我了一下哈！')
            pass

    elif event == 'unsubscribe':
        pass
    elif event == 'CLICK':
        pass
    elif event == 'SCAN':
        # user_id = msg["EventKey"] # 扫描过来的，直接检测是否需要更新用户的 token
        # bindUser(user_id, msg["FromUserName"])

        resultStr = sendMsgForSubUser(event, msg, u'你又扫我了一下, 我要 check 你哦！')

    return resultStr


# 绑定微信的 openid  到 user 表中
def bindUser(user_id, openid):
    print("当前绑定的用户 user_id：" + user_id + ", openid:" + openid)
    ZKUser.objects.filter(id=user_id).update(wx_openid=openid)
    print("将用户 user_id：" + user_id + " 的openid 存入数据库中, openid:" + openid)


# 给初次订阅的用户反馈消息
def sendMsgForSubUser(event, msg, toUserMsg):
    # 给关注的用户反馈 关注消息
    resultStr = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
    resultStr = resultStr % (
        msg['FromUserName'],
        msg['ToUserName'],
        str(int(time.time())),
        'text', toUserMsg)
    print("wx handleEvent qrscene_ resultStr：" + event)
    return resultStr


# 处理微信的事件推送
def handleText(msg):
    resultStr = ''
    print("wx handleText：" + str(msg))

    userContent = msg["Content"]

    resultStr = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
    resultStr = resultStr % (
    msg['FromUserName'], msg['ToUserName'], str(int(time.time())), 'text', u'你好呀，你刚刚说了一个：' + userContent)

    print("wx handleText resultStr：" + resultStr)
    return resultStr

from urllib import parse
#函数把微信XML格式信息转换成字典格式
def xmlContent2Dic(xmlContent):
    print("wx xmlContent2Dic：" + xmlContent)
    dics = {}
    elementTree = ElementTree.fromstring(xmlContent)
    if elementTree.tag == 'xml':
        for child in elementTree:
            text = child.text
            if text is None:
                text = ''
            else:
                text = parse.unquote(text)

            dics[child.tag] = text

    print("wx xmlContent2Dic dics：" + dics.__str__())
    return dics


import requests
import time

# 获取微信 Token
def wxToken(request):
    APPID = 'wx740fa691ebcc886c'
    APPSECRET = 'e24c9a81a9991460600bda24a73f3a3b'
    result = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + APPID + "&secret=" + APPSECRET).json()
    # print(result)

    wx_access_token = result["access_token"]
    expires_in = result["expires_in"]

    currentTime = int(time.time())

    WXConstant.wx_access_token = wx_access_token
    WXConstant.expires_in = expires_in
    WXConstant.refresh_time = currentTime + expires_in

    currentTimeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(currentTime))
    missTokenTimeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(WXConstant.refresh_time))

    print("微信当前的 Token 是：\n" + WXConstant.wx_access_token)
    print("微信 Token 有效期时间是：" + str(WXConstant.expires_in))
    print("获取 WXToken 的时间是：" + str(currentTime) + ", 服务器当前具体时间是：" + currentTimeStr)
    print("WXToken 过期的时间是：" + str(WXConstant.refresh_time) + ", 变成具体时间是：" + missTokenTimeStr)

    wxData = []
    wxData.append(wx_access_token)
    wxData.append(expires_in)
    wxData.append(currentTimeStr)
    wxData.append(missTokenTimeStr)

    projects = list(wxData)

    return getHttpResponse(0, "ok", projects)


def wxUsers(requst):
    token = WXConstant.wx_access_token

    # 默认从头拉取，也可以根据这个 id 获取后面的： &next_openid=NEXT_OPENID
    result = requests.get("https://api.weixin.qq.com/cgi-bin/user/get?access_token=" + token).json()

    projects = list(result["data"]["openid"])

    return getHttpResponse(0, "ok", projects)


def wxUserInfo(requst):
    token = WXConstant.wx_access_token
    OPENID = requst.GET.get("OPENID")

    # 默认从头拉取，也可以根据这个 id 获取后面的： &next_openid=NEXT_OPENID
    result = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token=" + token + "&openid=" + str(OPENID) +"&lang=zh_CN").json()

    # projects = list(result)
    return getHttpResponse(0, "ok", result)


wx_QRcode_Cache = {}
from urllib import parse
def wxQRcode(requst):
    checkWXToken()

    user_id = requst.GET.get("user_id")

    userBean = wx_QRcode_Cache.get(user_id)
    result = {}

    nowTime = int(time.time())
    exprise_time = 604800

    if userBean is None or nowTime > int(userBean["time"] + exprise_time):
        # 参考：https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1443433542

        # scene_str 字段: 场景值ID（字符串形式的ID），字符串类型，长度限制为1到64
        # scene_id  字段: 场景值ID，临时二维码时为32位非0整型，永久二维码时最大值为100000（目前参数只支持1--100000）

        # {"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "test"}}}
        params = '{"expire_seconds": '\
                 + str(exprise_time) + ', "action_name": "QR_LIMIT_STR_SCENE", "action_info":  {"scene": {"scene_str": '\
                 + str(user_id) + '}}}'

        token = WXConstant.wx_access_token
        result = requests.post("https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=" + token, data=params).json()
        ticket = result["ticket"]
        url = result["url"]

        ticketUrl = "https://mp.weixin.qq.com/cgi-bin/showqrcode?" + parse.urlencode({'ticket': ticket})

        bean = {}
        bean.__setitem__("time", nowTime)
        bean.__setitem__("ticket", ticket)
        bean.__setitem__("ticketUrl", ticketUrl)
        wx_QRcode_Cache.__setitem__(user_id, bean)
        result["url"] = ticketUrl
    else:
        result["url"] = userBean["ticketUrl"]
        result["ticket"] = userBean["ticket"]

    return getHttpResponse(0, "ok", result)


@login_required
def show(request):
    subs = models.SubInfo.objects.all()
    return render(request, 'index_sub.html', {"subs": subs})


# 获取用户订阅信息
# @login_required
def jsonShow(request):
    return sendJsonResponse(request, models.SubInfo)


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
            需要了解详情可以去官网查看：{url}'''\
            .format(name=name, pid=pid, url=url, new_number=new_number, fjUrl=fjUrl)
        send(emailTitle, emailDetail)


def wxNotify(emailList):
    # 微信通知
    print("待处理 微信通知")
    checkWXToken()

    # 用户的openid
    openId = "oQrNzwaFHdvdufYEGZhz4cNwhznk" #默认是孤独狂饮的哈
    zk_h5_url = 'http://www.zkteam.cc' #微信打开的 H5 页面哈，可以让用户下载视频，或者拷贝数据。



    for data in emailList:
        name = data.name
        pid = data.pid
        url = data.url
        new_number = data.new_number

        movieDownload = SubMovieDownload.objects.filter(pid=pid).values()[0]
        fjUrl = movieDownload.get("fj_download_url")

        # emailTitle = name + " 更新到 第" + new_number + "集！"
        # emailDetail = '''
        #     hi, 小同学, 您订阅的 {name}（{pid}） 已经更新到 {new_number} 啦！当前订阅内容是的最新资源是：
        #
        #         {fjUrl}
        #
        #     请拷贝连接，使用迅雷下载，后期将默认添加调用迅雷 or 小米路由器。
        #     需要了解详情可以去官网查看：{url}''' \
        #     .format(name=name, pid=pid, url=url, new_number=new_number, fjUrl=fjUrl)

        # 发起微信通知。
        wxSendMsg(openId,
                  zk_h5_url,
                  "您订阅的 《" + name + "》有更新啦！",
                  "最新一集是：第" + new_number + "集",
                  "已经通过邮件和微信给您通知啦",
                  "您可以点击详情将最新一集下载到您的 路由器 或者 电脑上。")


def checkWXToken():
    t = time.time()
    currentTime = int(t)
    if currentTime > WXConstant.refresh_time:
        wxToken(None)


# 这里会发起微信通知消息
def wxSendMsg(openid, url, wx_msg_title, wx_msg_content, wx_msg_ps, wx_msg_des):
    # url = "http://www.zkteam.cc"
    # openid = 'oQrNzwaFHdvdufYEGZhz4cNwhznk' # 孤独狂饮的openid

    template_id = '4KOE8MczMCka1CW_q_BcegEzBVrAacFv81oEeVNTPRw' #预约服务提醒
    data = {
        "content": {"value": "content！", "color": "#173177"},
        "first": {"value": wx_msg_title, "color": "#173177"},
        "keyword1": {"value": wx_msg_content, "color": "#173177"},
        "keyword2": {"value": wx_msg_ps, "color": "#173177"},
        "remark": {"value": wx_msg_des, "color": "#173177"},
    }

    templeUrl = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
    token = WXConstant.wx_access_token

    paramsData = {"access_token": token,
                  "touser": openid,
                  "template_id": template_id,
                  "url": url,
                  "data": data}

    result = requests.post(templeUrl + "?access_token=" + token, json=paramsData).json()
    return getHttpResponse(0, "ok", result)


def notifyMsg2User(emailList):
    # send("我是测试主题，", "我是测试内容！")
    emailNotify(emailList)
    wxNotify(emailList)


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
    except Error:
        return getHttpResponse(10000, "Error", "")


# 获取更新表的信息
def jsonLastInfo(request):
    return sendJsonResponse(request, models.SubMovieLastestInfo)


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


def notifyUser(request):

    requests.get("")

    pass


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
            user = ZKUser.objects.create_user(account, email, password)
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
