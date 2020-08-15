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

        widgets = {
            'name': forms.TextInput(attrs={'id': 'edit_basic_name_field'}),
            'email': forms.TextInput(attrs={'id': 'edit_email_field'}),
            'phone': forms.TextInput(attrs={'id': 'edit_phone_field'}),
            'github': forms.TextInput(attrs={'id': 'edit_github_field'}),
            'linkedin': forms.TextInput(attrs={'id': 'edit_linkedin_field'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('qualification', 'period', 'institution', 'grade', 'description')
        labels = {
            'qualification':    'Qualification/Certification',
            'period':           'Period of Study',
            'institution':      'Institution/School',
            'grade':            'Classification/Grade',
            'description':      'Description of study'
        }

        widgets = {
            'qualification': forms.TextInput(attrs={'id': 'edit_education_qualification_field'}),
            'period': forms.TextInput(attrs={'id': 'edit_education_period_field'}),
            'institution': forms.TextInput(attrs={'id': 'edit_education_institution_field'}),
            'grade': forms.TextInput(attrs={'id': 'edit_education_grade_field'}),
            'description': forms.TextInput(attrs={'id': 'edit_education_description_field'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('title', 'period', 'institution', 'description', 'referee')
        labels = {
            'title':            'Job Title',
            'period':           'Period of Employment',
            'institution':      'Institution/Company',
            'description':      'Description of work',
            'referee':          'Referee'
        }

        widgets = {
            'title': forms.TextInput(attrs={'id': 'edit_experience_title_field'}),
            'period': forms.TextInput(attrs={'id': 'edit_experience_period_field'}),
            'institution': forms.TextInput(attrs={'id': 'edit_experience_institution_field'}),
            'description': forms.TextInput(attrs={'id': 'edit_experience_description_field'}),
            'referee': forms.TextInput(attrs={'id': 'edit_experience_referee_field'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'technologies')
        labels = {
            'title':            'Project Name',
            'description':      'Project Description',
            'technologies':     'List of technologies used'
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)
        labels = {
            'name': 'Skill Name'
        }
