from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Homepage')

def room(request):
    return HttpResponse('ROOM')