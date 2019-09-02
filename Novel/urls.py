from django.conf.urls import url

from MapPro import views

urlpatterns = [
    url(r'^index.html', views.MapDataView, name="MapData"),
    url(r'^show', views.show, name="show"),
]
