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


import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

# urlpatterns = patterns('',
#     url(r'xadmin/', include(xadmin.site.urls)),
# )

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
    url(r'^aoc/', include('aoc.urls', namespace='aoc', app_name='aoc')),
    url(r'^Consume12315/', include('Consume12315.urls', namespace='Consume12315', app_name='Consume12315')),
    url(r'^JueDiQiuSheng/', include('JueDiQiuSheng.urls', namespace='JueDiQiuSheng', app_name='JueDiQiuSheng')),
    url(r'^Shop/', include('Shop.urls', namespace='Shop', app_name='Shop')),
    url(r'^Subscribe/', include('Subscribe.urls', namespace='Subscribe', app_name='Subscribe')),
    url(r'^WXMoney/', include('WXMoney.urls', namespace='WXMoney', app_name='WXMoney')),
    url(r'^MapPro/', include('MapPro.urls', namespace='MapPro', app_name='MapPro')),
    url(r'^GaoKao/', include('GaoKao.urls', namespace='GaoKao', app_name='GaoKao')),
    url(r'^ManHua/', include('ManHua.urls', namespace='ManHua', app_name='ManHua')),
]
