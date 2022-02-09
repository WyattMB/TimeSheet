from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView
from UserManagement.models import Profile
#from UserManagement.models import UserModel

# Create your views here.

class UserDetail(DetailView):
    model = Profile
    template_name = 'templates/user_detail.html'

class HomeView(DetailView):
    model = Profile
    template_name = 'base_timesheet.html'