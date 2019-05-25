import operator
import random
import time


# Create your views here.
from pymysql import Error
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        # https://www.cnblogs.com/sheng-247/articles/7918956.html

        # projects = WXMoneyItemInfo.objects.all().values()  # 取出该表所有的数据

        # data = projects[0]
        # data['startTime'] = str(data['startTime'])
        # data['endTime'] = str(data['endTime'])

        page = request.GET.get("page")
        pageCount = request.GET.get("pageCount")

        if not page or int(page) < 1:
            page = 1

        if not pageCount or int(pageCount) < 1:
            pageCount = 20

        # 取出所有数据（分页的形式）
        # 获取 数据表中的所有记录
        wxMoneyMX = WXMoneyItemInfo.objects.all().values()
        # 生成paginator对象,定义每页显示20条记录
        paginator = Paginator(wxMoneyMX, pageCount)
        # 把当前的页码数转换成整数类型
        currentPage = int(page)
        page = int(page)
        pageCount = int(pageCount)
        number = int((currentPage - 1) * pageCount)  # 每个条数据的编号（防止第二页从第一个开始）

        try:
            newData = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            newData = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        except EmptyPage:
            newData = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容












        # moneyPZ = WXMoneyPZ.objects.all().values()[0]  # 取出该表所有的数据
        #
        # id = request.GET.get("id")
        # name = moneyPZ['name']
        #
        # startTime = moneyPZ['startTime']
        # endTime = moneyPZ['endTime']
        #
        # startMoney = moneyPZ['startMoney']
        # endMoney = moneyPZ['endMoney']
        #
        # spendState = moneyPZ['spendState']
        #
        # startTime = time.mktime(time.strptime(str(startTime), '%Y-%m-%d %H:%M:%S'))
        # endTime = time.mktime(time.strptime(str(endTime), '%Y-%m-%d %H:%M:%S'))
        #
        # projects = []
        #
        # # for data in projects:
        # for i in range(0, 20):
        #     data = {}
        #     newTime = random.randint(startTime, endTime)
        #     newMoney = random.randint(startMoney, endMoney)
        #
        #     newMoney = format(float(newMoney), '0.2f')
        #
        #     data['id'] = i + 1
        #     data['name'] = name
        #     data['newTime'] = newTime
        #     data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(newTime))
        #     data['money'] = newMoney
        #     data['spendState'] = spendState
        #     projects.append(data)
        #
        # # https: // jingyan.baidu.com / article / f3ad7d0ffe8e1409c2345b48.html
        #
        # newData = sorted(newData, key=operator.itemgetter("newTime"), reverse=1)


        for item in newData:
            # item['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['time']))
            item['time'] = str(item['time'])

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
        count = request.GET.get("count")

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
            startTime = int(startTime / 1000)
        if len(str(endTime)) > 10:
            endTime = int(endTime / 1000)

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

        if not count:
            count = 500  #默认生成500条数据

        # 每次生成数据清空之前的表数据
        WXMoneyItemInfo.objects.all().delete()

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

        # return getHttpResponse(0, "ok", data)

        projects = []
        # 生成一组数据
        for i in range(0, count):
            data = {}
            newTime = random.randint(startTime, endTime)
            newMoney = random.randint(startMoney, endMoney)

            newMoney = format(float(newMoney), '0.2f')

            data['id'] = i + 1
            data['name'] = name
            data['newTime'] = newTime
            data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(newTime))
            data['money'] = newMoney
            data['spendState'] = spendState
            projects.append(data)

        # https: // jingyan.baidu.com / article / f3ad7d0ffe8e1409c2345b48.html
        newData = sorted(projects, key=operator.itemgetter("newTime"), reverse=1)

        querysetlist = []
        for item in newData:
            querysetlist.append(WXMoneyItemInfo(name=item['name'], time=item['time'],
                                                spendState=item['spendState'], money=item['money']))
        WXMoneyItemInfo.objects.bulk_create(querysetlist)
        return getHttpResponse(0, "ok", newData)
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
