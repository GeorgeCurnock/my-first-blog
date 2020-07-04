from django import forms

from .models import Basic, Education


class BasicForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ('name', 'email', 'phone', 'github', 'linkedin', 'last_updated')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('qualification', 'period', 'institution', 'grade', 'description')
