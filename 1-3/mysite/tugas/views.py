from django.shortcuts import redirect, render

from .import models

def index(request):
    if request.POST:
        input = request.POST['nama']
        models.tugas.objects.create(nama = input)

    data = models.tugas.objects.all()
    print(data)
    return render (request, "index.html",{
        "data":data
    })

def hapus(request, id):
    models.tugas.objects.filter(pk = id).delete()
    return redirect('/')
    
def detail(request, id):
    tasks = models.tugas.objects.filter(id = id).first()
    print (tasks)
    return render(request, "index.html", {
        "Detaildata" : tasks
    })

def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print(input)
        models.tugas.objects.filter(id = id).update(nama=input)
        return redirect('/')

    tasks = models.tugas.objects.filter(id = id).first()
    return render (request, 'edit.html', {
        "detailData" : tasks
    })

def about (request):
    return ("Halaman about")