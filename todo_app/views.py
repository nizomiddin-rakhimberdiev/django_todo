from django.shortcuts import render, redirect
from .models import Task
from .forms import EditTaskForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title, author=request.user)
        return redirect('home')
    tasks = Task.objects.filter(author=request.user)
    search_query = request.GET.get('qidiruv', '')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.filter(author=request.user)

    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def change_status(request, id):
    task = Task.objects.get(id=id)
    if task.status == 'Pending':
        task.status = 'Done'
    else:
        task.status = 'Pending'
    task.save()
    return redirect('home')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    if task.status == 'Done':
        task.delete()
    return redirect('home')


def edit_task_view(request, id):
    task = Task.objects.get(id=id)
    form = EditTaskForm(instance=task)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'edit_task.html', context)


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')