from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
#from UserManagement.models import UserModel

# Create your views here.

def user(request):
    return HttpResponse("This is a user")

def blank(request):
    return HttpResponse("This is a blank url")

class UserView(DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello")