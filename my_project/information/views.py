from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from information.models import Information


def show_home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        email = request.POST['em']
        username = request.POST['un']
        password = request.POST['pw']

        user = User(first_name=first_name, last_name=last_name, email=email,
                    username=username, password=password)
        user.save()

        return redirect('home')
    else:
        return HttpResponse('Invalid Access')


def login(request):
    pass


def show_about(request):
    # information = Information.objects.all()
    # information = Information.objects.filter(id=2)
    # information = Information.objects.get(pk=2)
    information = Information.objects.filter(section__title='About')
    return render(request, 'about.html', {'information': information})


def show_contacts(request):
    info = Information.objects.filter(section__title='Contacts')
    # info = Information.objects.filter(section_id=2)
    return render(request, 'contacts.html', {'info': info})


def show_policy(request):
    return HttpResponse('This is Policy Page')
