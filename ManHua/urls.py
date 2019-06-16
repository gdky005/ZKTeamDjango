from django.conf.urls import url

from ManHua import views

urlpatterns = [
    url(r'^index.html', views.ManHuaIndex, name="ManHuaIndex"),
    url(r'^jsonMHCategory', views.JsonMHCategoryView, name="JsonMHCategoryView"),
    url(r'^jsonMHHotData', views.JsonMHHotDataView, name="JsonMHHotDataView"),
    url(r'^jsonMHDetail', views.JsonMHDetailView, name="JsonMHDetailView"),
    url(r'^jsonMHChapter', views.JsonMHDetailChapterView, name="JsonMHDetailChapterView"),
    url(r'^jsonMHChapterPic', views.JsonMHChapterPicView, name="JsonMHChapterPicView"),
    url(r'^jsonMHBanner', views.JsonMHBannerView, name="JsonMHBannerView"),
]
