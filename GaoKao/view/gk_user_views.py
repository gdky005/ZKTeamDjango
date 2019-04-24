from pymysql import Error

from GaoKao.model import GKUserInfo
from GaoKao.view.base_views import getHttpResponse


def JsonGKUserDataView(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        # projects = models.xxx.objects.all()

        # project_info = models.GKUserInfo.objects.values()[:maxData]  # 取出该表所有的数据
        project_info = GKUserInfo.objects.values()
        # projects = list(project_info)

        return getHttpResponse(0, "ok", project_info)
    except Error:
        return getHttpResponse(10000, "Error", "")