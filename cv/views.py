from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BasicForm
from .models import Basic


def cv_home(request):
    basic = Basic.objects.first()
    return render(request, 'cv/cv_home.html', {'basic': basic})


def cv_edit_basic(request):
    # If the user has already entered an entry then get that entry
    if Basic.objects.count() == 1:
        basic = get_object_or_404(Basic, pk=Basic.objects.first().pk)
    # Else we create a blank entry to be
    else:
        basic = Basic()
    if request.method == "POST":
        form = BasicForm(request.POST, instance=basic)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_updated = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = BasicForm(instance=basic)
    return render(request, 'cv/cv_edit_basic.html', {'form': form})


def cv_edit_education(request):
    return render(request, 'cv/cv_edit_education.html')


def cv_edit_experience(request):
    return render(request, 'cv/cv_edit_experience.html')


def cv_edit_projects(request):
    return render(request, 'cv/cv_edit_projects.html')


def cv_edit_skills(request):
    return render(request, 'cv/cv_edit_skills.html')

