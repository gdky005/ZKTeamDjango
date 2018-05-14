from django.conf.urls import url
from django.conf.urls import handler404, handler500

from Shop import views

urlpatterns = [
    url(r'^show', views.shop, name="show"),
    url(r'^add', views.addData, name="addData"),
    url(r'^query', views.query, name="query"),
    # handler404 = views.page_not_found,

]
