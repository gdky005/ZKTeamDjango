from django.conf.urls import url

from GaoKao.view import gk_home_views
from GaoKao.view import gk_user_views
from GaoKao.view import gk_msg_views
from GaoKao.view import user_views
from GaoKao.view import gk_school_view

from GaoKao.view import gk_lql_view
from GaoKao.view import gk_skx_view
from GaoKao.view import gk_zy_view

urlpatterns = [

    url(r'^gkRecommendJson', gk_home_views.JsonGKRecommendView, name="JsonGKRecommendDataView"),
    url(r'^gkCategoryJson', gk_home_views.JsonGKCategoryView, name="JsonGKCategoryView"),
    url(r'^gkNewsJson', gk_home_views.JsonGKNewsView, name="JsonGKNewsView"),

    url(r'^gkListJson', gk_msg_views.JsonGKListView, name="JsonGKListView"),

    # todo
    url(r'^gkUserJson', gk_user_views.JsonUserInfoView, name="JsonGKUserDataView"),

    # ----------------------------------------------------------------------------------------------------

    # 和 yapi 同步起来
    url(r'^recommend', gk_home_views.JsonGKRecommendView, name="JsonGKRecommendDataView"),
    url(r'^category', gk_home_views.JsonGKCategoryView, name="JsonGKCategoryView"),
    url(r'^newList', gk_home_views.JsonGKNewsView, name="JsonGKNewsView"),

    url(r'^list', gk_msg_views.JsonGKListView, name="JsonGKListView"),
    url(r'^msgList', gk_msg_views.JsonGKListView, name="JsonGKListView"),
    url(r'^saveMsg', gk_msg_views.saveMsg, name="saveMsg"),
    url(r'^msgDetail', gk_msg_views.msgDetail, name="msgDetail"),

    # 用户登录操作
    url(r'^register', user_views.register, name='register'),
    url(r'^login', user_views.my_login, name='my_login'),
    url(r'^logout', user_views.my_logout, name='my_logout'),
    url(r'^userInfo', user_views.jsonUserInfo, name="jsonUserInfo"),

    # 学校相关
    url(r'^school', gk_school_view.JsonSchoolView, name="JsonSchoolView"),
    # 录取率
    url(r'^lql', gk_lql_view.JsonLQLView, name="JsonLQLView"),
    # 省控线
    url(r'^skx', gk_skx_view.JsonSKXView, name="JsonSKXView"),
    # 专业
    url(r'^zy', gk_zy_view.JsonZYView, name="JsonZYView"),
]
