from django import forms

from .models import Basic, Education, Experience, Project, Skill


class BasicForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ('name', 'email', 'phone', 'github', 'linkedin')
        labels = {
            'name':         'Full Name',
            'email':        'Email Address',
            'phone':        'Phone Number',
            'github':       'Github Username',
            'linkedin':     'LinkedIn Username'
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('qualification', 'period', 'institution', 'grade', 'description')
        labels = {
            'qualification':    'Qualification/Certificate',
            'period':           'Period of Study',
            'institution':      'Institution/School',
            'grade':            'Grade',
            'description':      'Description of course'
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('title', 'period', 'institution', 'description', 'referee')
        labels = {
            'title':            'Job Title',
            'period':           'Period of Employment',
            'institution':      'Institution/Company',
            'description':      'Description of work carried out',
            'referee':          'Referee'
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'technologies')
        labels = {
            'title':            'Project Name',
            'description':      'Project Description',
            'technologies':     'Technologies'
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)
