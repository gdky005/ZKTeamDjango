from django.conf.urls import url

from GaoKao.view import gk_home_views
from GaoKao.view import gk_user_views

urlpatterns = [
    url(r'^gkUserJson', gk_user_views.JsonGKUserDataView, name="JsonGKUserDataView"),
    url(r'^gkRecommendJson', gk_home_views.JsonGKRecommendDataView, name="JsonGKRecommendDataView"),
]