from django.conf.urls import url
from django.conf.urls import handler404, handler500

from DouYin import views

urlpatterns = [
    url(r'^index.html', views.DouYin, name="DouYin"),
    url(r'^video', views.VideoInfo, name="DouYin"),
    # handler404 = views.page_not_found,

]
