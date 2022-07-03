from django.db import models
from accounts.models import User


class JobSeeker(models.Model):
    qualification = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    training = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='cvs')
    image = models.ImageField(upload_to='users')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

