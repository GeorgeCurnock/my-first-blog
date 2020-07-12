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

    def __str__(self):
        return self.qualification


'''
Job title
Period of employment
Institution/Company
Description of work undertaken
Potential referee
'''


class Experience(models.Model):
    title = models.CharField(max_length=64)
    period = models.CharField(max_length=20)
    institution = models.CharField(max_length=80)
    description = models.TextField()
    referee = models.CharField(max_length=42)

    def __str__(self):
        return self.title


'''
project title
technologies
description
'''


class Technology(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    technologies = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
