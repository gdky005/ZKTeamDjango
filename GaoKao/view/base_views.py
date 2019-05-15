import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from dss.Serializer import serializer
from pymysql import Error


# 用户登录 返回数据体
def loginData(request, data):
    try:
        if request.user.is_authenticated():
            return getHttpResponse(0, "ok", data)

    except Error as e:
        return getHttpResponse(10000, "Error", e)

    return getHttpResponse(10001, "User not login!", "用户没登录，请登录去")


def getPagingData(request, infoData):
    try:
        page = request.GET.get("page")
        pageCount = request.GET.get("pageCount")

        if not page or int(page) < 1:
            page = 1

        if not pageCount or int(pageCount) < 1:
            pageCount = 20

        # 取出所有数据（分页的形式）
        # 获取 数据表中的所有记录
        dataObjects = infoData.objects.all().values()
        # 生成paginator对象,定义每页显示20条记录
        paginator = Paginator(dataObjects, pageCount)
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
            # newData = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
            newData = []

        return getHttpTotalResponse(0, "ok", paginator.count, newData)
    except Error:
        return getHttpResponse(10000, "Error", "")


class ResultResponse(object):

    def __init__(self, code, message, result):
        self.code = code
        self.message = message
        self.result = result

    def __str__(self):
        return '{"code":%s,"message":%s,"result":%s}' % (self.code, self.message, self.result)


class ResultTotalResponse(object):

    def __init__(self, code, message, total, result):
        self.code = code
        self.message = message
        self.total = total
        self.result = result

    def __str__(self):
        return '{"code":%s,"message":%s, "total":%s, "result":%s}' % (self.code, self.message, self.total, self.result)


# 返回 有 total 总数分页的Json结构体
def getHttpTotalResponse(code, message, total, word):
    return getJsonHttpResponse(ResultTotalResponse(code, message, total, word))


# 返回 标准的Json结构体
def getHttpResponse(code, message, word):
    return getJsonHttpResponse(ResultResponse(code, message, word))


# 返回 Json 的通用结构
def getJsonHttpResponse(resultResponse):
    return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                        content_type="application/json;charset=utf-8")
