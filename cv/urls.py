from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_home, name='cv_home'),
    path('cv/edit/basic', views.cv_edit_basic, name='cv_edit_basic'),
    path('cv/edit/education', views.cv_edit_education, name='cv_edit_education'),
    path('cv/edit/experience', views.cv_edit_experience, name='cv_edit_experience'),
    path('cv/edit/projects', views.cv_edit_projects, name='cv_edit_projects'),
    path('cv/edit/skills', views.cv_edit_skills, name='cv_edit_skills'),
]