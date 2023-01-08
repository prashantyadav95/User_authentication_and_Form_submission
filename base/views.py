from django.shortcuts import render,HttpResponseRedirect
from .forms import Reportform
from .models import Report
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

def user_signup(request):
    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Signupform()
    return render(request, 'base/signup.html',{'form':fm})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request = request, data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname,password = upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Success: You are now logged in.')
                return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'User does not exist!')
            return HttpResponseRedirect('/login/')
    else:
        fm = AuthenticationForm()
    return render(request, 'base/login.html', {'form':fm})


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'base/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def report(request):
    submitted = False
    if request.method == "POST":
        form = Reportform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/report?submitted = True')
    else:
        form = Reportform()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/report.html',{'form':form, 'submitted':submitted})

def home(request):
    return render(request, 'base/home.html')