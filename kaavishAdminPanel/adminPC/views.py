from django.shortcuts import render
from .forms import loginForm
from django.db import models
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
# Create your views here.

#login/logout
def userLogin(request):
    if request.method == 'POST':
        print('hello')
        #username = request.POST['username']
        #password = request.POST['password']
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print(user)
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/retryLogin/')
    else:
        print('keli')
        form = loginForm()
    return render(request, 'login.html', {'form':form})
    # , {'form': form})

def retryLogin(request):
    form = loginForm()
    return render(request, 'retryLogin.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/retryLogin/')

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


