from django.conf.urls import url

from JueDiQiuSheng import views

urlpatterns = [
    url(r'^index.html', views.JDQS, name="JDQS"),
    url(r'^category.html', views.JDQSCategory, name="JDQS"),
    url(r'^item.html', views.JDQSItem, name="JDQS"),
    url(r'^content.html', views.JDQSContent, name="JDQS"),
    url(r'^detail.html', views.JDQSDetail, name="JDQS"),
    url(r'^picCategory.html', views.JDQSPicCategory, name="JDQS"),
    url(r'^picUrl.html', views.JDQSPicUrl, name="JDQS"),

    url(r'^itemJson', views.JDQSItemJson, name="JDQS"),
    url(r'^picCategoryJson', views.JDQSPicCategoryJson, name="JDQS"),
    url(r'^categoryJson', views.JDQSCategoryJson, name="JDQS"),
    url(r'^recommendedJson', views.JDQSCategoryJson, name="JDQS"),
]
