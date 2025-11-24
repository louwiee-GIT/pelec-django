from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm

def registeruser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Succesfully! Please Login.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html',{'form':form})


def LoginUSer(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'welcome back, {username}')
                return redirect('dashboard')
            else: 
                messages.error(request, 'Invalid Username or Password.')
        else:
            messages.error(request, 'Invalid Input')
           
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def Logout_user(request):
    logout(request)
    messages.info(request,'You have been logged out')
    return redirect('login')

def dashboard(request):
    return render(render, 'accounts/dashboard.html')


