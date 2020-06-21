from django.shortcuts import render


def cv_home(request):
    return render(request, 'cv/cv_home.html')


def cv_edit_basic(request):
    return render(request, 'cv/cv_edit_basic.html')


def cv_edit_education(request):
    return render(request, 'cv/cv_edit_education.html')


def cv_edit_experience(request):
    return render(request, 'cv/cv_edit_experience.html')


def cv_edit_projects(request):
    return render(request, 'cv/cv_edit_projects.html')


def cv_edit_technologies(request):
    return render(request, 'cv/cv_edit_technologies.html')


def cv_edit_other(request):
    return render(request, 'cv/cv_edit_other.html')
