from django.http import HttpResponse
from django.shortcuts import render


def show_home(request):
    return render(request, 'index.html')


def show_about(request):
    return HttpResponse('This is About Us Page')


def show_contacts(request):
    return HttpResponse('This is Contact Us Page')


def show_policy(request):
    return HttpResponse('This is Policy Page')


# create a new module
# add module to installed_app in settings.py
# add urls for the module in main project's urls.py