from django.db import models
from django.utils import timezone


class Basic(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=12)
    github = models.CharField(max_length=39)
    linkedin = models.CharField(max_length=60)
    last_updated = models.DateTimeField(default=timezone.now)



'''
Full name
Email
Phone number
Github Username
LinkedIn Username'''
