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

def create(request):

    return render(request, "create.html")


def addData(request):
    project_name = request.POST['project_name']
    student_name = request.POST['student_name']
    project_description = request.POST['project_description']

    entry = Projects.objects.create(project_name=project_name, student_name=student_name, project_description=project_description)
    data = Projects.objects.all()
    
    # return HttpResponse("Hello CS3001 Class, this is our index page")
    return render(request, "index.html", {"data" : data})