from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
        email = request.POST['em']
        username = request.POST['un']
        password = make_password(request.POST['pw'])

        user = User(first_name=first_name, last_name=last_name, email=email,
                    username=username, password=password, gender=gender, dob=dob,
                    address=address, mobile=mobile)
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
        # username = request.POST['un']
        password = request.POST['pw']

        # job = Job.objects.get(id=jid)
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        # user.username = username
        if request.user.password != password:
            user.password = make_password(password)
        user.save()

        messages.success(request, 'Profile Updated')

    return render(request, 'profile.html')