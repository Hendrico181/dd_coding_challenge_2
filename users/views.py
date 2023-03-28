from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required


# Registering / Creating a user
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/users/my-login/')

    context = {'form': form}

    return render(request, 'users/register.html', context=context)


# Authenticate a user
def my_login(request):

    current_user = request.user
    if current_user:
        if current_user.pk:
            return redirect('/tasks/dashboard/')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)

            return redirect('/tasks/dashboard/')

    context = {'form': form}

    return render(request, 'users/my-login.html', context=context)


# Log out user
@login_required(login_url='users:login')
def my_logout(request):

    auth.logout(request)

    return redirect('/')

