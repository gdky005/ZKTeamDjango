from django.conf.urls import url

from ManHua import views

urlpatterns = [
    url(r'^jsonMHCategory', views.JsonMHCategoryView, name="JsonMHCategoryView"),
    url(r'^jsonMHHotData', views.JsonMHHotDataView, name="JsonMHHotDataView"),
    url(r'^jsonMHSelectData', views.JsonMHSelectDataView, name="JsonMHSelectDataView"),
    url(r'^jsonMHDetail', views.JsonMHDetailView, name="JsonMHDetailView"),
    url(r'^jsonMHAllDetailView', views.JsonMHAllDetailView, name="JsonMHAllDetailView"),
    url(r'^jsonMHChapter', views.JsonMHDetailChapterView, name="JsonMHDetailChapterView"),
    url(r'^jsonMHPicList', views.JsonMHChapterPicView, name="JsonMHChapterPicView"),
    url(r'^jsonMHBanner', views.JsonMHBannerView, name="JsonMHBannerView"),
    url(r'^jsonMHKinds', views.JsonMHCategoryForCategoryIdView, name="JsonMHCategoryForCategoryIdView"),
    url(r'^jsonMHAllData', views.JsonMHAllDataView, name="JsonMHAllDataView"),

    # 设置数据源接口
    url(r'^setJsonMHDetailData', views.setMHDetailView, name="setMHDetailView"),
    url(r'^setJsonMHChapterData', views.setJsonMHChapterData, name="setMHDetailView"),
    url(r'^setJsonCategoryForIdData', views.setJsonCategoryForIdData, name="setMHDetailView"),
]
