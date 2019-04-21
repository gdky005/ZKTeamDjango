from django.conf.urls import url

from GaoKao import views

urlpatterns = [
    url(r'^show', views.show, name="GKDataView"),
    url(r'^index.html', views.GKDataView, name="GKDataView"),
    url(r'^gkJson', views.JsonGKDataView, name="JsonGKDataView"),
]