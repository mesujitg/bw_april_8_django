from django.db import models
from organizations.models import Organization


class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    requirement = models.TextField()
    salary = models.FloatField()
    deadline = models.DateField()
    status = models.BooleanField(default=True)
    organizations = models.ForeignKey(Organization, on_delete=models.CASCADE)

