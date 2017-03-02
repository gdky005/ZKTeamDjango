from django.shortcuts import render
from api import models


# Create your views here.
def show(request):
    user_list = models.UserInfo.objects.all()  # 取出该表所有的数据

    return render(request, "show.html", {"user_list": user_list})


def home(request):
    return render(request, 'index.html')
