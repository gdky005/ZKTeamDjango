from django.conf.urls import url
from aoc import views

urlpatterns = [
    url(r'^show/', views.githubProjectInfo, name="show"),
    # url(r'^json/movie/', views.jsonMovie, name="jsonMovie"),

]
