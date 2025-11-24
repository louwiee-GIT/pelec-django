from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse('courses')

def shift_course(request):
    return HttpResponse('shifting courses here')