from django.shortcuts import render

# Create your views here.
from aoc import models


def home(request):
    return render(request, 'aoc_index.html')