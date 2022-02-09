from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, ListView
from UserManagement.models import Profile
#from UserManagement.models import UserModel

# Create your views here.

class UserDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = Profile.pk
        return context

    template_name = 'templates/user_detail.html'

class HomeView(DetailView):
    model = Profile

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pk'] = self.request.user
    #     return context
    def get_object(self):
        return Profile.objects.get(user_id=self.request.user)

    template_name = 'base_timesheet.html'