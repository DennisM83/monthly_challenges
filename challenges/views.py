from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hey there!")

def february(request):
    return HttpResponse("February")