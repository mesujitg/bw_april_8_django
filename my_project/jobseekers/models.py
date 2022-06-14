from django.db import models


class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    qualification = models.TextField()
    experience = models.TextField()
    training = models.TextField()
    skills = models.TextField()
    cv = models.FileField()
    image = models.ImageField()
