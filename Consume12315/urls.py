from django.conf.urls import url
from django.conf.urls import handler404, handler500

from Consume12315 import views

urlpatterns = [
    url(r'^index.html', views.Consume12315, name="Consume12315"),
    url(r'^Json', views.Consume12315Json, name="Consume12315"),
    # handler404 = views.page_not_found,

]
