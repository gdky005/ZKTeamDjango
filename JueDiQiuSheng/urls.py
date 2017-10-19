from django.conf.urls import url

from JueDiQiuSheng import views

urlpatterns = [
    url(r'^index.html',  views.JDQS, name="JDQS"),
    url(r'^category.html',  views.JDQSCategory, name="JDQS"),
    url(r'^item.html',  views.JDQSItem, name="JDQS"),
    url(r'^content.html',  views.JDQSContent, name="JDQS"),
    url(r'^json',  views.JDQSItemJson, name="JDQS"),
]