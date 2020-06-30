from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BasicForm, EducationForm
from .models import Basic, Education


def cv_home(request):
    # If the user has already entered an entry then get that entry
    if Basic.objects.count() == 1:
        basic = get_object_or_404(Basic, pk=Basic.objects.first().pk)
    # Else we create a blank entry to be
    else:
        basic = Basic()

    if Education.objects.count() > 0:
        education_entries = Education.objects
    else:
        education_entries = []

    return render(request, 'cv/cv_home.html', {'basic': basic, 'education': education_entries})


def cv_edit_basic(request):
    # If the user has already entered an entry then get that entry
    if Basic.objects.count() == 1:
        basic_object = get_object_or_404(Basic, pk=Basic.objects.first().pk)
    # Else we create a blank entry to be
    else:
        basic_object = Basic()
    if request.method == "POST":
        form = BasicForm(request.POST, instance=basic_object)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.last_updated = timezone.now()
            basic.save()
            return redirect('/cv')
    else:
        form = BasicForm(instance=basic_object)
    return render(request, 'cv/cv_edit_basic.html', {'form': form})


def cv_new_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('/cv')
    else:
        form = EducationForm()
    return render(request, 'cv/cv_edit_education.html', {'form': form})


def cv_edit_education(request, pk):
    education_object = get_object_or_404(Education, pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education_object)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('/cv')
    else:
        form = EducationForm(instance=education_object)
    return render(request, 'cv/cv_edit_education.html', {'form': form})


def cv_edit_experience(request):
    return render(request, 'cv/cv_edit_experience.html')


def cv_edit_projects(request):
    return render(request, 'cv/cv_edit_projects.html')


def cv_edit_skills(request):
    return render(request, 'cv/cv_edit_skills.html')
