from django.http import HttpResponse

import django.shortcuts import render


def index(request):
    data = Projects.objects.all()
    # return HttpResponse("Hello CS3001 Class, this is our index page")
    return render(request, "index.html", {"data" : data})