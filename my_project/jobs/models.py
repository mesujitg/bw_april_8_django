from django.db import models


class Job(models.Model):
    status = models.BooleanField(default=True)
