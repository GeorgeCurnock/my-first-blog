from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import BasicForm
from .models import Basic


def cv_home(request):
    basic = Basic.objects
    return render(request, 'cv/cv_home.html', {'basic': basic})


def cv_edit_basic(request):
    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_updated = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = BasicForm()
    return render(request, 'cv/cv_edit_basic.html', {'form': form})


def cv_edit_education(request):
    return render(request, 'cv/cv_edit_education.html')


def cv_edit_experience(request):
    return render(request, 'cv/cv_edit_experience.html')


def cv_edit_projects(request):
    return render(request, 'cv/cv_edit_projects.html')


def cv_edit_skills(request):
    return render(request, 'cv/cv_edit_skills.html')

