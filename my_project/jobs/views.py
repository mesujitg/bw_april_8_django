from django.http import HttpResponse
from django.shortcuts import render


def show_jobs(request):
    return HttpResponse('Jobs Page')

