from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import * 

# def index(request):
#     data = Projects.objects.all()

#     for entry in data:
#         print(entry.project_name)
#     return HttpResponse("Hello, world. the first project is " + entry.project_name)




def index(request):
    data = Projects.objects.all()
    # return HttpResponse("Hello CS3001 Class, this is our index page")
    return render(request, "index.html", {"data" : data})