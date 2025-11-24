from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def registration(request):
    return HttpResponse('registration')

def newstudent_registration(request):
    return HttpResponse('registration of new students')