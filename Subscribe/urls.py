from django.conf.urls import url
from django.conf.urls import handler404, handler500

from Subscribe.view import views
from Subscribe.view import wx_views
from Subscribe.view import user_views

urlpatterns = [
    url(r'^show', views.show, name="show"),
    url(r'^jsonShow', views.jsonShow, name="jsonShow"),
    url(r'^add', views.addData, name="addData"),
    url(r'^query', views.query, name="query"),
    url(r'^delete', views.delete, name="delete"),
    # url(r'^login', views.login, name="login"),
    # handler404 = views.page_not_found,

    # 用户登录操作
    url(r'^register/$', user_views.register, name='register'),
    url(r'^login/$', user_views.my_login, name='my_login'),
    url(r'^logout/$', user_views.my_logout, name='my_logout'),

    # json 数据操作
    url(r'^jsonUserInfo/', user_views.jsonUserInfo, name="jsonUserInfo"),
    url(r'^jsonQueryInfo/', views.jsonQueryInfo, name="jsonQueryInfo"),
    url(r'^jsonLastInfo/', views.jsonLastInfo, name="jsonLastInfo"),
    url(r'^jsonSubInfo/', views.jsonShow, name="jsonSubInfo"),
    url(r'^jsonFJUpdate/', views.jsonFJUpdate, name="jsonFJUpdate"),

    # 微信views
    url(r'^weiXin/', wx_views.weiXin, name="weiXin"),
    url(r'^wxToken/', wx_views.wxToken, name="wxToken"),
    url(r'^wxUsers/', wx_views.wxUsers, name="wxUsers"),
    url(r'^wxUserInfo/', wx_views.wxUserInfo, name="wxUserInfo"),
    url(r'^wxQRcode/', wx_views.wxQRcode, name="wxQRcode"),
    url(r'^wxTemplateMsg/', wx_views.wxTemplateMsg, name="wxTemplateMsg"),
    url(r'^wxAllTemplate/', wx_views.wxAllTemplate, name="wxAllTemplate"),

]
