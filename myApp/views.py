from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import * 

def index(request):
    data = Projects.objects.all()

    for entry in data:
        print(entry.project_name)
    return HttpResponse("Hello, world. the first project is " + entry.project_name)