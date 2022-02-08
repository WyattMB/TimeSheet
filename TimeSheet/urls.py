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
from django.urls import path
from UserManagement import views as umv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', umv.UserView.as_view()), # humm, one can have all the urls listed here but then the list will grow indefinite and also if you want to reuse any of the app in different project then one has to go thro' this list to copy appropriate urls pertaining to the app.
    path('', umv.blank),
]
