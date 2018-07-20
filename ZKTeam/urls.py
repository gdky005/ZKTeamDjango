"""ZKTeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
    url(r'^aoc/', include('aoc.urls', namespace='aoc', app_name='aoc')),
    url(r'^DouYin/', include('DouYin.urls', namespace='DouYin', app_name='DouYin')),
    url(r'^Consume12315/', include('Consume12315.urls', namespace='Consume12315', app_name='Consume12315')),
    url(r'^JueDiQiuSheng/', include('JueDiQiuSheng.urls', namespace='JueDiQiuSheng', app_name='JueDiQiuSheng')),
    url(r'^Shop/', include('Shop.urls', namespace='Shop', app_name='Shop')),
    url(r'^Subscribe/', include('Subscribe.urls', namespace='Subscribe', app_name='Subscribe')),
]
