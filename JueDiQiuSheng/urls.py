from django.conf.urls import url

from JueDiQiuSheng import views

urlpatterns = [
    url(r'^index.html',  views.JDQS, name="JDQS"),
]