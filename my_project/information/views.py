from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from information.models import Information
from jobs.models import Job
from organizations.models import Organization


def show_home(request):
    org = Organization.objects.all()
    jobs = Job.objects.count()
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

        messages.success(request, 'User Registered Successfully.')
        return redirect('home')
    else:
        return HttpResponse('Invalid Access')


def login(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pw']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            return HttpResponse('Wrong credentials')
    else:
        return HttpResponse('Invalid Access')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'You are logged out')
    return redirect('home')


@login_required
def profile(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'Invalid Access')
    #     return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        email = request.POST['em']
        username = request.POST['un']
        password = request.POST['pw']

        # job = Job.objects.get(id=jid)
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.password = password
        user.save()

        messages.success(request, 'Profile Updated')

    return render(request, 'profile.html')


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
