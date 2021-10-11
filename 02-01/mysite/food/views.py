from django.shortcuts import redirect, render
from .import models

# Create your views here.
def index (req):
    if req.POST:
        models.Makanan.objects.create(name= req.POST['name'])
        return redirect('/')

    makanan=models.Makanan.objects.all()
    return render (req, 'index.html', {
        'isimakanan': makanan,
    })
