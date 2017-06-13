from django.conf.urls import url
from aoc import views

urlpatterns = [
    url(r'^project/', views.githubProjectInfo, name="project"),
    url(r'^json/project/', views.githubProjectJson, name="projectJson"),
    # url(r'^json/movie/', views.jsonMovie, name="jsonMovie"),

]
