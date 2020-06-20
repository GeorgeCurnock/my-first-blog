from django.shortcuts import render


def cv_home(request):
    return render(request, 'cv/cv_home.html')
