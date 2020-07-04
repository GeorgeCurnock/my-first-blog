from django.db import models
from django.utils import timezone

'''
Full name
Email
Phone number
Github Username
LinkedIn Username
'''


class Basic(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=12)
    github = models.CharField(max_length=39)
    linkedin = models.CharField(max_length=60)
    last_updated = models.DateTimeField(default=timezone.now)


'''
Qualification
Period of Study
Institution
Classification/Grade
Description
'''


class Education(models.Model):
    qualification = models.CharField(max_length=42)
    period = models.CharField(max_length=20)
    institution = models.CharField(max_length=80)
    grade = models.CharField(max_length=12)
    description = models.TextField()
