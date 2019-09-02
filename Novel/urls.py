from django.conf.urls import url

from Novel import views

urlpatterns = [
    # url(r'^index.html', views.MapDataView, name="MapData"),
    url(r'^jsonNovel', views.jsonNovel, name="jsonNovel"),
    url(r'^jsonDetailNovel', views.jsonDetailNovel, name="jsonDetailNovel"),
    url(r'^jsonSearch', views.jsonSearch, name="jsonSearch"),
]
