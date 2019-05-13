from pymysql import Error

from GaoKao.model.gk_lql import GKLQL
from GaoKao.view.base_views import getHttpResponse


def JsonLQLView(request):
    try:
        name = request.GET.get("lql")

        if name:
            project_info = GKLQL.objects.filter(name__icontains=name).values()
            return getHttpResponse(0, "ok", project_info)

        return getHttpResponse(10000, "Error", "请输入 keyword")
    except Error:
        return getHttpResponse(10000, "Error", "")