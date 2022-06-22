from django.http import HttpResponse
from django.shortcuts import render
from information.models import Information


def show_home(request):
    return render(request, 'index.html')


def show_about(request):
    # information = Information.objects.all()
    # information = Information.objects.filter(id=2)
    # information = Information.objects.get(pk=2)
    information = Information.objects.filter(title='About')
    return render(request, 'about.html', {'information': information})


def show_contacts(request):
    pass


def show_policy(request):
    return HttpResponse('This is Policy Page')


# create a new module
# add module to installed_app in settings.py
# add urls for the module in main project's urls.py