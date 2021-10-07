from django.shortcuts import redirect, render

from .import models

def index(request):
    if request.POST:
        models.uhuy.objects.create(name=request.POST['name'])

    tasks = models.uhuy.objects.all()
    return render(request, "index.html",{"data" : tasks})