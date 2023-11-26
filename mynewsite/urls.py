"""
URL configuration for mynewsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from django.shortcuts import redirect

#from  import views

def button_uwc(request):
    return render(request, 'survey/depression(uwc).html')

def button_ww(request):
    return render(request, 'survey/depression(ww).html')

def depression_uwc(request):
    return render(request, 'survey/depression(uwc).html')

def depression_ww(request):
    return render(request, 'survey/depression(ww).html')

def yes(request):
    return render(request, 'survey/yes.html')

def no(request):
    return render(request, 'survey/no.html')

def confirm(request):
    return render(request, 'survey/confirm.html')

def setup(request):
    return render(request, 'survey/setup.html')

def thank(request):
    return render(request, 'survey/thank.html')

def re(request):
    return redirect('cdc.gov/mentalhealth/learn/index.htm')

def ww_no(request):
    return render(request, 'survey/no.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("survey.urls")),
    path('depression-survey-uwc/', depression_uwc),
    path('depression-survey-ww/', depression_ww),
    path('output-uwc/yes', yes),
    path('output-uwc/no', no),
    path('output/yes/confirm/', confirm),
    path('output-uwc/thank', thank),
    path('setup/', setup),
    path('output-uwc/', button_uwc),
    path('output-ww/', button_ww),
    path('output-ww/no', ww_no),
    path('cdc.gov/mentalhealth/learn/index.htm', re),
]
