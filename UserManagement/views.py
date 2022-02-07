from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user(request):
    return HttpResponse("This is a user")

def blank(request):
    return HttpResponse("This is a blank url")