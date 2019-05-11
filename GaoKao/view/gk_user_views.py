from pymysql import Error

from GaoKao.view.base_views import getHttpResponse

from ZKUser.models import ZKUser


def JsonUserInfoView(request):
    try:

        uid = request.GET.get("uid")

        if uid:
            project_info = ZKUser.objects.filter(id=uid).values()
            return getHttpResponse(0, "ok", project_info)

        return getHttpResponse(10000, "Error", "请输入 uid")
    except Error:
        return getHttpResponse(10000, "Error", "")