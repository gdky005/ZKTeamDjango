from django.conf.urls import url

from GaoKao.view import gk_home_views
from GaoKao.view import gk_user_views
from GaoKao.view import gk_list_views
from GaoKao.view import user_views

urlpatterns = {

    url(r'^gkRecommendJson', gk_home_views.JsonGKRecommendView, name="JsonGKRecommendDataView"),
    url(r'^gkCategoryJson', gk_home_views.JsonGKCategoryView, name="JsonGKCategoryView"),
    url(r'^gkNewsJson', gk_home_views.JsonGKNewsView, name="JsonGKNewsView"),

    url(r'^gkListJson', gk_list_views.JsonGKListView, name="JsonGKListView"),

    # todo
    url(r'^gkUserJson', gk_user_views.JsonUserInfoView, name="JsonGKUserDataView"),

    # ----------------------------------------------------------------------------------------------------

    # 和 yapi 同步起来
    url(r'^recommend', gk_home_views.JsonGKRecommendView, name="JsonGKRecommendDataView"),
    url(r'^category', gk_home_views.JsonGKCategoryView, name="JsonGKCategoryView"),
    url(r'^newList', gk_home_views.JsonGKNewsView, name="JsonGKNewsView"),

    url(r'^list', gk_list_views.JsonGKListView, name="JsonGKListView"),

    # 用户登录操作
    url(r'^register', user_views.register, name='register'),
    url(r'^login', user_views.my_login, name='my_login'),
    url(r'^logout', user_views.my_logout, name='my_logout'),
    url(r'^jsonUserInfo/', user_views.jsonUserInfo, name="jsonUserInfo"),
}