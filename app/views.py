from django.shortcuts import render,redirect
from .models import Notes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def home(request):
    if request.method=='POST':
        title = request.POST.get('title')
    
        date = request.POST.get('date')
        content = request.POST.get('content')
        Notes.objects.create(user=request.user,title=title,content=content,date=date)
        return redirect('notes_list')
    return render(request,'index.html')

def notes_list(request):
    notes = Notes.objects.filter(user=request.user)
    return render(request,'notes_list.html',{'notes':notes})   
   

def update_notes(request,id):
    a = Notes.objects.get(id=id)
    if request.method == 'POST':
        a.title = request.POST.get('title')
        a.content = request.POST.get('content')
        a.date = request.POST.get('date')
        a.save()
        return redirect('notes_list')
    return render(request,'update.html',{'a':a})

def delete_notes(request,id):
    notes = Notes.objects.filter(id=id)
    notes.delete()
    return redirect('notes_list')   

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('register_page')
    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        User.objects.create_user(username=name,password=password)
        return redirect('login_page')
    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

