from django.conf.urls import url

from ManHua import views

urlpatterns = [
    url(r'^jsonMHCategory', views.JsonMHCategoryView, name="JsonMHCategoryView"),
    url(r'^jsonMHHotData', views.JsonMHHotDataView, name="JsonMHHotDataView"),
    url(r'^jsonMHSelectData', views.JsonMHSelectDataView, name="JsonMHSelectDataView"),
    url(r'^jsonMHDetail', views.JsonMHDetailView, name="JsonMHDetailView"),
    url(r'^jsonMHChapter', views.JsonMHDetailChapterView, name="JsonMHDetailChapterView"),
    url(r'^jsonMHPicList', views.JsonMHChapterPicView, name="JsonMHChapterPicView"),
    url(r'^jsonMHBanner', views.JsonMHBannerView, name="JsonMHBannerView"),
    url(r'^jsonMHKinds', views.JsonMHCategoryForCategoryIdView, name="JsonMHCategoryForCategoryIdView"),
]
