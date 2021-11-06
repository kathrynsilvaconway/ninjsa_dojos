from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    context = {
        'ninjas': Ninja.objects.all(),
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def processdojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'])
    return redirect('/')

def processninja(request):
    Ninja.objects.create(
        dojo_id=request.POST['dojo'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
        )
    return redirect('/')



# Create your views here.
