from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^show/', views.show, name="show"),
]
