from django.shortcuts import render,redirect
from .models import Academy

# Create your views here.
def index(request):
    academy = Academy.objects.all()
    context = {'academy': academy}
    return render(request,'index.html',context)

def create(request):
    academy = Academy(name=request.POST['name'], status=request.POST['status'], price=request.POST['price'], nos=request.POST['nos'])
    academy.save()
    return redirect('/')


def edit(request, id):
    academy = Academy.objects.get(id=id)
    context = {'academy': academy}
    return render(request, 'edit.html', context)


def update(request, id):
    academy = Academy.objects.get(id=id)
    academy.name = request.POST['name']
    academy.status = request.POST['status']
    academy.price = request.POST['price']
    academy.nos = request.POST['nos']
    academy.save()
    return redirect('/')


def delete(request, id):
    academy = Academy.objects.get(id=id)
    academy.delete()
    return redirect('/')