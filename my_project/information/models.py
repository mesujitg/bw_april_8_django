from django.db import models


class Information(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)
