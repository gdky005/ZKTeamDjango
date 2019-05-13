from pymysql import Error

from GaoKao.model.gk_school import GKSchool
from GaoKao.model.gk_zy import GKZY
from GaoKao.view.base_views import getHttpResponse


def JsonZYView(request):
    try:
        name = request.GET.get("zy")

        if name:
            project_info = GKZY.objects.filter(name__icontains=name).values()
            return getHttpResponse(0, "ok", project_info)

        return getHttpResponse(10000, "Error", "请输入 keyword")
    except Error:
        return getHttpResponse(10000, "Error", "")