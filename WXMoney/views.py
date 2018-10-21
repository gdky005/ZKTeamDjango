import operator
import random
import time

from django.shortcuts import render

# Create your views here.
from pymysql import Error
from twisted.python.compat import cmp

from WXMoney.base_views import getHttpResponse

#
# def addData(request):
#     uid = request.GET.get("user_id")
#     # jid = request.GET.get("id")
#     pid = request.GET.get("pid")
#     name = request.GET.get("name")
#     url = request.GET.get("url")
#     number = request.GET.get("number")
#     des = request.GET.get("des")
#
#     if not pid:
#         return getHttpResponse(10000, "Error", "pid not null!")
#
#     if not uid:
#         return getHttpResponse(10000, "Error", "uid not null!")
#
#     try:
#         maxData = 100  # 默认取100条数据
#
#         subInfoObj = SubInfo.objects.get_or_create(pid=pid, name=name, url=url, des=des, new_number=number)[0]
#         userObj = ZKUser.objects.get(id=uid)
#         SubInfo.objects.filter(pid=subInfoObj.pid).first().zk_user.add(userObj)
#
#         return getHttpResponse(0, "ok", subInfoObj)
#     except Exception as e:
#         return getHttpResponse(10000, "Error", "" + str(e))
from WXMoney.models import WXMoneyInfo, WXMoneyItemInfo, WXMoneyPZ


def jsonQueryMoney(request):
    try:
        projects = WXMoneyInfo.objects.all().values()  # 取出该表所有的数据

        qb = projects[0]

        return getHttpResponse(0, "ok", qb)
    except Error:
        return getHttpResponse(10000, "Error", "")


def setQB(request):
    try:
        id = request.GET.get("id")
        name = request.GET.get("name")
        money = request.GET.get("money")

        if not id:
            id = 1
        if not name:
            name = "我的零钱"

        if not money:
            money = '0.00'

        money = format(float(money), '0.2f')

        qbs = WXMoneyInfo.objects.filter(id=id)
        if qbs.__len__() > 0:
            qb = qbs[0]
            qb.money = money
            qb.name = name

            qb.save()

        projects = WXMoneyInfo.objects.all().values()  # 取出该表所有的数据

        data = projects[0]
        return getHttpResponse(0, "ok", data)
    except Error:
        return getHttpResponse(10000, "Error", "")


def jsonQueryLQMX(request):
    try:
        # projects = WXMoneyItemInfo.objects.all().values()  # 取出该表所有的数据

        # data = projects[0]
        # data['startTime'] = str(data['startTime'])
        # data['endTime'] = str(data['endTime'])

        moneyPZ = WXMoneyPZ.objects.all().values()[0]  # 取出该表所有的数据

        id = request.GET.get("id")
        name = moneyPZ['name']

        startTime = moneyPZ['startTime']
        endTime = moneyPZ['endTime']

        startMoney = moneyPZ['startMoney']
        endMoney = moneyPZ['endMoney']

        spendState = moneyPZ['spendState']

        startTime = time.mktime(time.strptime(str(startTime), '%Y-%m-%d %H:%M:%S'))
        endTime = time.mktime(time.strptime(str(endTime), '%Y-%m-%d %H:%M:%S'))

        projects = []

        # for data in projects:
        for i in range(0, 20):
            data = {}
            newTime = random.randint(startTime, endTime)
            newMoney = random.randint(startMoney, endMoney)

            data['id'] = i + 1
            data['name'] = name
            data['newTime'] = newTime
            data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(newTime))
            data['money'] = newMoney
            data['spendState'] = spendState
            projects.append(data)

        newData = sorted(projects, key=operator.itemgetter("newTime"))
        return getHttpResponse(0, "ok", newData)
    except Error:
        return getHttpResponse(10000, "Error", "")


def jsonQueryLQMXPZ(request):
    try:
        projects = WXMoneyPZ.objects.all().values()  # 取出该表所有的数据

        data = projects[0]
        data['startTime'] = str(data['startTime'])
        data['endTime'] = str(data['endTime'])

        return getHttpResponse(0, "ok", data)
    except Error:
        return getHttpResponse(10000, "Error", "")


def setLQMXPZ(request):
    try:
        id = request.GET.get("id")
        name = request.GET.get("name")

        startTime = request.GET.get("startTime")
        endTime = request.GET.get("endTime")

        startMoney = request.GET.get("startMoney")
        endMoney = request.GET.get("endMoney")

        spendState = request.GET.get("spendState")

        if not id:
            id = 1
        if not name:
            name = "扫码支付"

        if not startTime:
            startTime = int(time.time())  # 获取秒级的时间戳
        if not endTime:
            endTime = int(time.time()) + 1000

        startTime = int(startTime)
        endTime = int(endTime)

        if len(str(startTime)) > 10:
            startTime = startTime / 1000
        if len(str(endTime)) > 10:
            endTime = endTime / 1000

        if endTime < startTime:
            endTime = startTime + 1000

        if not startMoney:
            startMoney = 1
        if not endMoney:
            endMoney = 50

        startMoney = int(startMoney)
        endMoney = int(endMoney)
        if endMoney < startMoney:
            endMoney = startMoney + 5

        if not spendState:
            spendState = 1

        pz = WXMoneyPZ.objects.filter(id=id)
        if pz.__len__() > 0:
            qb = pz[0]
            qb.id = id
            qb.name = name

            qb.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
            qb.endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))

            qb.startMoney = startMoney
            qb.endMoney = endMoney

            qb.spendState = spendState

            qb.save()

        projects = WXMoneyPZ.objects.all().values()  # 取出该表所有的数据

        data = projects[0]
        data['startTime'] = str(data['startTime'])
        data['endTime'] = str(data['endTime'])

        return getHttpResponse(0, "ok", data)
    except Error as e:
        return getHttpResponse(10000, "Error", e)

#
# def jsonQueryInfo(request):
#     des = request.GET.get("des")
#
#     if not des:
#         return getHttpResponse(10000, "Error", "des not null!")
#
#     try:
#         # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
#
#         project = SubInfo.objects.filter(des=des).values()
#         return getHttpResponse(0, "ok", project)
#     except Error:
#         return getHttpResponse(10000, "Error", "")
#
#
# def query(request):
#     pid = request.GET.get("pid")
#
#     if not pid:
#         return getHttpResponse(10000, "Error", "pid not null!")
#
#     try:
#         # projects = models.ShopInfo.objects.all().values()[:maxData]  # 取出该表所有的数据
#
#         project = SubInfo.objects.filter(pid=pid).values()
#
#         if project.__len__() > 0:
#             project = project[0]
#         else:
#             project = ''
#
#         data = project
#         return getHttpResponse(0, "ok", data)
#     except Error:
#         return getHttpResponse(10000, "Error", "")
