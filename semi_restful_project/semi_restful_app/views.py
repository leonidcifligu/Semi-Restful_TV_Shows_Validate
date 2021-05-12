from django.shortcuts import render, redirect
from semi_restful_app.models import *
from django.contrib import messages
from .models import Show
  

def index(request):
    return render(request,"add.html")


def create(request):
    errors = Show.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
       for key, value in errors.items():
            messages.error(request, value)
            return redirect("/shows/new")
    
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],)
    return redirect('/shows')


def shows(request):
    context = {
        'shows':Show.objects.all()
    }
    return render(request,'shows.html',context)

def show(request,id):
    context ={
        'show':Show.objects.get(id=id)
    }
    return render(request,'show.html',context)

def edit(request,id):
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request,'edit.html',context)

def update(request,id):
    errors = Show.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
       
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/show/new'+id)
    else:
        shows = Show.objects.get(id=id)
        shows.title=request.POST['title']
        shows.release_date=request.POST['release_date']
        shows.network=request.POST['network']
        shows.description=request.POST['description']
        shows.save()
        messages.success(request, "Show successfully updated")
    return redirect('/shows')

def delete(request,id):
    shows = Show.objects.get(id=id)
    shows.delete()
    return redirect('/shows')