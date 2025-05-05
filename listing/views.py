from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ListModelForm
from django.core.paginator import Paginator
from .models import Lists
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def addlist(request):
    if Lists.objects.filter(user=request.user).count()>=5:
            return render(request,"addlist.html",{"error":"You can add only upto 5 bookmarks "}) 
    
    if request.method=="POST":
        form=ListModelForm(request.POST)
        if form.is_valid():
                bookmark=form.save(commit=False)
                bookmark.user=request.user
                bookmark.save()
                return redirect("home")
    else:
        form=ListModelForm()
    return render(request,"addlist.html",{"form":form})



@login_required(login_url="/login/")
def viewlist(request):
    formData = Lists.objects.filter(user=request.user).order_by("time")
    paginator=Paginator(formData,1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,"viewlist.html",{"page_obj":page_obj})

def search(request):
    if request.method=="GET":
        search=request.GET.get("search"," ")
        if search:
            formData=Lists.objects.filter(user=request.user).filter(Q(title__icontains=search)|Q(url__icontains=search))
            return render(request,"searchlist.html",{"formData":formData})
        else:
            return redirect("viewlist")


def signUp(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserCreationForm()
    return render(request,"signup.html",{"form":form})
        
def logIn(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})


def update(request,pk):
    id=Lists.objects.get(pk=pk)
    if request.method=="POST":
        form=ListModelForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect("viewlist")
    else:
        form=ListModelForm(instance=id)
    return render(request,"updatelist.html",{"form":form})


def delete(request,pk):
    userid=Lists.objects.get(pk=pk)
    if request.method=="POST":
        userid.delete()
        return redirect("viewlist")
    return render(request,"deletelist.html",{"userid":userid})
        


@login_required(login_url="/login")
def logOut(request):
    if request.method=="POST":
        logout(request)
        return redirect("login")
    else:
        user=request.user
    return render(request,"logout.html",{"user":user})



