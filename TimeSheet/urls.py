"""TimeSheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import View, ListView, UpdateView, DetailView
from django.views.generic.base import RedirectView
from UserManagement.views import UserDetail, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/user/(?P<pk>\d+)/$', UserDetail.as_view()),
    re_path(r'^login/home/(?P<pk>\d+)/$', HomeView.as_view()),
    path("", RedirectView.as_view(url='/login/')),
    path('registration/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
