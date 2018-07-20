from django.conf.urls import url
from django.conf.urls import handler404, handler500

from Subscribe import views

urlpatterns = [
    url(r'^show', views.shop, name="show"),
    url(r'^jsonShow', views.jsonShow, name="jsonShow"),
    url(r'^add', views.addData, name="addData"),
    url(r'^query', views.query, name="query"),
    url(r'^delete', views.delete, name="delete"),
    # handler404 = views.page_not_found,

]
