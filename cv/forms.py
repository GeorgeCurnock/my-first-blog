from django import forms

from .models import Basic, Education, Experience


class BasicForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ('name', 'email', 'phone', 'github', 'linkedin', 'last_updated')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('qualification', 'period', 'institution', 'grade', 'description')


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('title', 'period', 'institution', 'description', 'referee')
