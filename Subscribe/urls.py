from django.conf.urls import url
from django.conf.urls import handler404, handler500

from Subscribe import views

urlpatterns = [
    url(r'^show', views.show, name="show"),
    url(r'^jsonShow', views.jsonShow, name="jsonShow"),
    url(r'^add', views.addData, name="addData"),
    url(r'^query', views.query, name="query"),
    url(r'^delete', views.delete, name="delete"),
    # url(r'^login', views.login, name="login"),
    # handler404 = views.page_not_found,

    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.my_login, name='my_login'),
    url(r'^logout/$',views.my_logout, name='my_logout'),

    url(r'^jsonQueryInfo/', views.jsonQueryInfo, name="jsonQueryInfo"),
    url(r'^notifyUser/', views.notifyUser, name="notifyUser"),


    url(r'^jsonLastInfo/', views.jsonLastInfo, name="jsonLastInfo"),
    url(r'^jsonUserInfo/', views.jsonUserInfo, name="jsonUserInfo"),
    url(r'^jsonSubInfo/', views.jsonShow, name="jsonSubInfo"),
    url(r'^jsonFJUpdate/', views.jsonFJUpdate, name="jsonFJUpdate"),
    url(r'^weiXin/', views.weiXin, name="weiXin"),
    url(r'^wxToken/', views.wxToken, name="wxToken"),
    url(r'^wxUsers/', views.wxUsers, name="wxUsers"),
    url(r'^wxUserInfo/', views.wxUserInfo, name="wxUserInfo"),

    url(r'^wxQRcode/', views.wxQRcode, name="wxQRcode"),
    url(r'^wxTemplateMsg/', views.wxTemplateMsg, name="wxTemplateMsg"),
    url(r'^wxAllTemplate/', views.wxAllTemplate, name="wxAllTemplate"),

]
