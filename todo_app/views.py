from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# First we'll create Login Page
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists !')
            return redirect('signup')
        
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    
    return render(request, 'signup.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user :
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    tasks = Todo.objects.filter(user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')

        if title :
            Todo.objects.create(user = request.user , title=title)
            return redirect('home')
    return render(request, 'home.html', {'tasks' : tasks})

@login_required
def edit_task(request, id):
    task =get_object_or_404(Todo, id=id, user = request.user) #Error handling is importent

    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title :
            task.title = new_title
            task.save()
            return redirect('home')
    return render(request, 'edit.html', {'task': task})

@login_required
def delete_task(request, id):
    del_task = get_object_or_404(Todo, id=id, user= request.user)
    del_task.delete()
    return redirect('home')

@login_required
def toggle_task(request, id):
    task = get_object_or_404(Todo, id=id, user= request.user)
    task.completed = not task.completed
    task.save()
    return redirect('home')




       
    
