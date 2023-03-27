from django.db.models import Value, F
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import *

from django.contrib.auth.decorators import login_required


# Dashboard Page
@login_required(login_url='users:login')
def dashboard(request):
    logged_in = request.user
    tasks = Task.objects.filter(user_id=logged_in.pk, complete=False).count()
    context = {'tasks': tasks}
    return render(request, 'tasks/dashboard.html', context=context)


# Dashboard Page
@login_required(login_url='users:login')
def user_tasks(request):
    logged_in = request.user
    tasks = Task.objects.filter(user_id=logged_in.pk).values('id', 'header', 'description', 'story_points', 'complete').annotate(user=F('user__username'))
    return render(request, 'tasks/index.html', {'tasks': tasks})


# Get all tasks
@login_required(login_url='users:login')
def index(request):
    tasks = Task.objects.all().values('id', 'header', 'description', 'story_points', 'complete').annotate(user=F('user__username'))
    return render(request, 'tasks/index.html', {'tasks': tasks})


# Create a task
@login_required(login_url='users:login')
def create_task(request):

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/tasks/")

    context = {'form': form,
               'header': 'Creating Task'}

    return render(request, 'tasks/task-form.html', context=context)


# Edit a task
@login_required(login_url='users:login')
def update_task(request, task_id):

    task = Task.objects.get(id=task_id)

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('/tasks/')

    context = {'form': form,
               'header': 'Editing Task'}

    return render(request, 'tasks/task-form.html', context=context)


# Delete a task
@login_required(login_url='users:login')
def delete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    if request.method == 'POST':

        task.delete()

        return redirect('/tasks/')

    context = {'task': task}

    return render(request, 'tasks/delete-task.html', context=context)


# Change a task's status
@login_required(login_url='users:login')
def change_status(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.complete = False if task.complete else True

        task.save()

        return redirect('/tasks/')

    context = {'task': task}

    return render(request, 'tasks/change-task-status.html', context=context)

