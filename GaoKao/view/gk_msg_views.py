from django.views.decorators.csrf import csrf_exempt
from pymysql import Error

from GaoKao.model import GKMsgInfo
from GaoKao.view.base_views import getHttpResponse, getPagingData


def JsonGKListView(request):
    return getPagingData(request, GKMsgInfo)


@csrf_exempt
def saveMsg(request):
    errorMsg = ""
    try:
        if request.method == 'POST':
            uid = request.POST.get('uid')
            author = request.POST.get('author')
            title = request.POST.get('title')
            summary = request.POST.get('summary')
            des = request.POST.get('des')

            msgInfo = GKMsgInfo()
            msgInfo.uid = uid
            msgInfo.author = author
            msgInfo.title = title
            msgInfo.summary = summary
            msgInfo.des = des
            msgInfo.save()
            projects = msgInfo
            return getHttpResponse(0, "ok", projects)
        else:
            errorMsg = "请使用 POST 请求"
    except Error as e:
        errorMsg = e

    return getHttpResponse(10000, errorMsg, errorMsg)


def msgDetail(request):
    errorMsg = ""
    try:
        if request.method == 'GET':
            msgId = request.GET.get('id')
            projects = GKMsgInfo.objects.filter(id=msgId).values()

            return getHttpResponse(0, "ok", projects[0])
        else:
            errorMsg = "请使用 GET 请求"
    except Error as e:
        errorMsg = e

    return getHttpResponse(10000, errorMsg, errorMsg)
