from django.conf.urls import url
from api import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    url(r'^show/', views.show, name="show"),
    # handler404 = views.page_not_found,

]
