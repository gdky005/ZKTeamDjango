from django.conf.urls import url
from django.conf.urls import handler404, handler500

from DouYin import views

urlpatterns = [
    url(r'^consume12315_index.html', views.DouYin, name="DouYin"),
    url(r'^video', views.VideoInfo, name="DouYin"),
    url(r'^Json', views.VideoInfoJson, name="DouYin"),
    # handler404 = views.page_not_found,

]
