from django.shortcuts import render

# Create your views here.
from aoc import models


def githubProjectInfo(request):
    projects = models.ProjectInfo.objects.all()
    render(request, 'aoc_index.html', {"projects": projects})
