from django.db import models
from jobs.models import Job
from jobseekers.models import JobSeeker


class Application(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100,
                              choices=[('Submitted', 'Submitted'),
                                       ('On Review', 'On Review'),
                                       ('Selected', 'Selected'),
                                       ('Waiting Listed', 'Waiting Listed'),
                                       ('Rejected', 'Rejected'),
                                       ])

