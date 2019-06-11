from django.conf.urls import url

from ManHua import views

urlpatterns = [
    url(r'^index.html', views.ManHuaIndex, name="ManHuaIndex"),
]
