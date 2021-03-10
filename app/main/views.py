from django.shortcuts import render,redirect
from .models import Academy

# Create your views here.
def index(request):
    academy = Academy.objects.all()
    context = {'academy': academy}
    return render(request,'index.html',context)

def create(request):
    academy = Academy(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    academy.save()
    return redirect('/')