from django.conf.urls import url
from api import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    url(r'^show/', views.show, name="show"),
    url(r'^movie/', views.movie, name="movie"),
    url(r'^json/movie/', views.jsonMovie, name="jsonMovie"),
    url(r'^masterInfo/', views.masterInfo, name="masterInfo"),
    url(r'^masterArticle/', views.masterArticle, name="masterArticle"),
    url(r'^jsonMasterInfo/', views.jsonMasterInfo, name="jsonMasterInfo"),
    url(r'^jsonMasterArticle/', views.jsonMasterArticle, name="jsonMasterArticle"),
    # handler404 = views.page_not_found,

]
