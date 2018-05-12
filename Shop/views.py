from django.shortcuts import render

# Create your views here.
from Shop import models


def shop(request):
    projects = models.ShopInfo.objects.all()
    return render(request, 'index_shop.html')