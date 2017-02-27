from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.show, name='show1'),
    url(r'^show/', views.show, name="show"),
]
