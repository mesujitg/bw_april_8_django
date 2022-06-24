from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)
    # section = models.CharField(max_length=255,
    #                            choices=[('About', 'About'),
    #                                     ('Contacts', 'Contacts'),
    #                                     ('Policy', 'Policy')], default='About')
    details = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
