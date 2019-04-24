from django.conf.urls import url

from GaoKao.view import gk_home_views
from GaoKao.view import gk_user_views
from GaoKao.view import gk_list_views

urlpatterns = [

    url(r'^gkRecommendJson', gk_home_views.JsonGKRecommendView, name="JsonGKRecommendDataView"),
    url(r'^gkCategoryJson', gk_home_views.JsonGKCategoryView, name="JsonGKCategoryView"),
    url(r'^gkNewsJson', gk_home_views.JsonGKNewsView, name="JsonGKNewsView"),


    url(r'^gkListJson', gk_list_views.JsonGKListView, name="JsonGKListView"),


    url(r'^gkUserJson', gk_user_views.JsonUserInfoView, name="JsonGKUserDataView"),
]