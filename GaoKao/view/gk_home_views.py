from pymysql import Error

from GaoKao.model.gk_user import GKUserInfo
from GaoKao.model.gk_home import GKRecommendInfo
from GaoKao.view.base_views import getHttpResponse


def JsonGKRecommendDataView(request):
    maxData = 5
    count = request.GET.get("pageCount")
    if count:
        maxData = int(count)

    try:
        project_info = GKRecommendInfo.objects.values()[:maxData]  # 取出该表所有的数据
        projects = list(project_info)

        return getHttpResponse(0, "ok", projects)
    except Error:
        return getHttpResponse(10000, "Error", "")

