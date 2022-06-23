from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job


def show_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def show_single_job(request, jid):
    job = Job.objects.get(id=jid)
    return render(request, 'job-single.html', {'job': job})

