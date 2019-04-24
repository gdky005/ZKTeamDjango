from pymysql import Error

from GaoKao.model import GKUserInfo
from GaoKao.view.base_views import getHttpResponse


def JsonUserInfoView(request):
    try:
        project_info = GKUserInfo.objects.values()
        return getHttpResponse(0, "ok", project_info)
    except Error:
        return getHttpResponse(10000, "Error", "")