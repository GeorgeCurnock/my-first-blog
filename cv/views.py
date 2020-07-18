from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BasicForm, EducationForm, ExperienceForm, ProjectForm
from .models import Basic, Education, Experience


def cv_home(request):
    # If the user has already entered an entry then get that entry
    if Basic.objects.count() == 1:
        basic = get_object_or_404(Basic, pk=Basic.objects.first().pk)
    # Else we create a blank entry to be
    else:
        basic = Basic()

    education_entries = Education.objects.all()
    experience_entries = Experience.objects.all()

    return render(request, 'cv/cv_home.html',
                  {'basic': basic, 'educationEntries': education_entries, 'experienceEntries': experience_entries})


def cv_edit_basic(request):
    # If the user has already entered an entry then get that entry
    if Basic.objects.count() == 1:
        basic_object = get_object_or_404(Basic, pk=Basic.objects.first().pk)
    # Else we create a blank entry
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
    education_object = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education_object)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('/cv')
    else:
        print("GET method found so creating form with object", pk)
        form = EducationForm(instance=education_object)
    return render(request, 'cv/cv_edit_education.html', {'form': form})


def cv_new_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('/cv')
    else:
        form = ExperienceForm()
    return render(request, 'cv/cv_edit_experience.html', {'form': form})


def cv_edit_experience(request, pk):
    experience_object = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience_object)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('/cv')
    else:
        form = ExperienceForm(instance=experience_object)
    return render(request, 'cv/cv_edit_experience.html', {'form': form})


def cv_new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('/cv')
    else:
        form = ProjectForm()
    return render(request, 'cv/cv_edit_projects.html', {'form': form})


def cv_edit_projects(request, pk):
    project_object = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project_object)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('/cv')
    else:
        form = ProjectForm(instance=project_object)
    return render(request, 'cv/cv_edit_experience.html', {'form': form})


def cv_edit_skills(request):
    return render(request, 'cv/cv_edit_skills.html')
